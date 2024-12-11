

# Setting up essential imports 

import requests
import pandas as pd
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import base64


# Reading the file passed via command-line arguments 
# and converting it into a DataFrame

file = sys.argv[1]
folder = os.path.splitext(os.path.basename(file))[0]
os.makedirs(folder, exist_ok=True)
try: 
    df = pd.read_csv(file, encoding='utf-8') 
except UnicodeDecodeError: 
    try: 
        df = pd.read_csv(file, encoding='ISO-8859-1') 
    except UnicodeDecodeError: 
        df = pd.read_csv(file, encoding='windows-1252')


# Generating Summary Statistics and converting them 
# into markdown table format

desc = df.describe().round(2)
desc = desc.map(lambda x: int(x) if not np.isnan(x) else x)
summary_mdt = desc.to_markdown(index=True)


# Creating three figures to illustrate data insights

# Figure-1: Histogram

df.hist(bins=100, figsize=(14, 14))
plt.savefig(f'./{folder}/histogram.png')
plt.close()

# Figure-2: Box Plot

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 14))
fig.suptitle('Box Plots of Variables', fontsize=16)
axes = axes.flatten()
variables = df.select_dtypes(include=['number']).columns.tolist()

for ax, var in zip(axes, variables):
    sns.boxplot(data=df[var], ax=ax)
    ax.set_title(f'Box Plot of {var.capitalize()}', fontsize=14)
    ax.set_xlabel(var.capitalize(), fontsize=12)

for i in range(len(variables), len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig(f'./{folder}/box_plot.png')

# Figure-3: Correlation Heatmap

fig, ax = plt.subplots(figsize=(14, 14)) 
sns.heatmap(df.loc[:,variables].corr(), annot=True, fmt=".2f")
plt.tight_layout()
plt.savefig(f'./{folder}/corr_hmap.png')


# Consulting LLM for insights
 
# Defining a helper function for sending requests
def send_llm_request(messages):
    """
    Sends a request to the LLM and retrieves the main content.

    Args:
        messages (list): Messages to send.

    Returns:
        str: The response from the LLM.
    """
    API_KEY = os.environ["AIPROXY_TOKEN"]
    model = "gpt-4o-mini"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages
    }

    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    r = requests.post(url, headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

# Determining the domain of the data

messages = [
    {"role": "system", "content": "Determine the domain based on column names in the data in only one word"},
    {"role": "user", "content": str(df.columns)}
]
domain = send_llm_request(messages)

# Converting images to base64

with open(f"./{folder}/box_plot.png", "rb") as image_file: 
    box_plot_enc = base64.b64encode(image_file.read()).decode("utf-8")

with open(f"./{folder}/corr_hmap.png", "rb") as image_file: 
    corr_hmap_enc = base64.b64encode(image_file.read()).decode("utf-8")

with open(f"./{folder}/histogram.png", "rb") as image_file: 
    histogram_enc = base64.b64encode(image_file.read()).decode("utf-8")

# Helper to build LLM request messages

def build_msgs(text, img):
    """
    Constructs the 'messages' parameter for LLM requests.

    Args:
        text (str): The message prompt.
        img (str): Base64 encoded image.

    Returns:
        list: Messages for the LLM request.
    """
    return [{
        "role": "user",
        "content": [
            {"type": "text", "text": text},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}", "detail": "low"}}
        ]
    }]

# LLM analyses

histogram_ana_llm = send_llm_request(build_msgs("Analyze histograms in a story-like manner.", histogram_enc))
corr_hmap_ana_llm = send_llm_request(build_msgs("Analyze the correlation heatmap.", corr_hmap_enc))
box_plot_ana_llm = send_llm_request(build_msgs("Analyze the box plots.", box_plot_enc))


# Writing the README file

content = f"""
# Data Analysis Project 
Welcome to the data analysis project! Here's an overview of your dataset:

## Domain
Your data relates to **{domain}**.

## Key Statistics
{summary_mdt}

## Visualizations
### Correlation Heatmap
![Figure](./corr_hmap.png)
{corr_hmap_ana_llm}

### Histograms
![Figure](./histogram.png)
{histogram_ana_llm}

### Box Plots
![Figure](./box_plot.png)
{box_plot_ana_llm}
"""

with open(f'./{folder}/README.md', 'w') as file:
    file.write(content)