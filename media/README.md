
# Data Analysis Project 
Hey! Hope you are doing fine. Hmm... You've got some interesting data I see.  
Let's begin this journey with first identifying what your data is like.  
So, you have got 100 rows and 500 columns in your data and as I can  
see this data is related to Reviews. Below are some key statistics  
about the data you provided  

## Key Statistics
|       |   overall |   quality |   repeatability |
|:------|----------:|----------:|----------------:|
| count |      2652 |      2652 |            2652 |
| mean  |         3 |         3 |               1 |
| std   |         0 |         0 |               0 |
| min   |         1 |         1 |               1 |
| 25%   |         3 |         3 |               1 |
| 50%   |         3 |         3 |               1 |
| 75%   |         3 |         4 |               2 |
| max   |         5 |         5 |               3 |  
  
Let's move a little deeper and see what wonders the data is yet to reveal.
  
## Visualizing Data
Let's see how numerical columns correlate with each other  
  
![Figure](./corr_hmap.png)

  
Once upon a time in a land of data, three important friends gathered to see how they influenced each other: Overall, Quality, and Repeatability. They decided to create a heatmap to visualize their connections.

As they looked at the map, Overall beamed with pride, shining at the top of the grid with a perfect score of 1.00 next to itself. This indicated that Overall was quite confident in its own existence, but it also had strong ties to Quality, boasting a significant correlation of 0.83. This suggests that when Overall improved, Quality was likely to follow closely behind, working hand in hand towards excellence.

However, when it came to Repeatability, Overall was a bit more reserved, showing a moderate connection with a correlation of 0.51. This indicated that while there was some relationship, it wasn’t as strong, hinting that improvements in Overall might not always guarantee consistent Repeatability.

Quality and Repeatability, on the other hand, had a more subdued interaction. Their correlation stood at a modest 0.31, revealing that while they were friends, their relationship wasn’t as tightly knit. This hinted that enhancing Quality didn’t necessarily mean Repeatability would also flourish. 

As they stepped back to assess their relationships, they realized that the journey of improvement would require understanding their bonds deeply. Quality and Repeatability needed to nurture their friendship if they all wanted to thrive in harmony. Thus, the friends left determined to work together, excited to strengthen their connections and foster a future of collaboration. 

Now in the second figure we'll see numerical columns spread themselves.  
  
![Figure](./histogram.png)

  
Once upon a time in the land of data analysis, a curious analyst sought to unravel the secrets hidden within a dataset. The analyst decided to gaze into the realms of three important attributes: **overall**, **quality**, and **repeatability**.

In the first window, the histogram of **overall** ratings stood tall, its peaks revealing a clear penchant for scores clustered around 1.5 and 2.5, with a few brave souls at the edges. This suggested that while many submissions gathered around these central values, there was a noticeable tapering off as the ratings approached the extremes. Perhaps the majority of participants found themselves in the realms of mediocrity, with only a handful achieving excellence.

Next, the analyst turned to the **quality** score, where a vast majority of entries clustered around the value of 4, almost like a thriving community praising the chosen few. The spike here indicated a consistent adherence to high standards, suggesting that many contributors had successfully met or exceeded expectations. However, the few that lingered at the lower end hinted at a small fraction struggling to attain those quality benchmarks.

Finally, the histogram of **repeatability** painted a stark contrast. Most of the entries gathered around 1.75, but as the analyst peered closer, they noticed the presence of a slender tail stretching towards higher repeatability scores. This puzzling inconsistency suggested that while many results lacked reliability, a smaller group demonstrated strong repeatability, hinting at deeper insights waiting to be discovered.

As the analyst finished their exploration, they realized that the tales of these histograms painted a vivid picture of both challenges and triumphs in the dataset. It became evident that understanding these distributions was key to fostering improvement and ensuring quality in future endeavors. And so, the journey of data exploration continued, with questions leading to further insights and discoveries.

Lastly, we'll see some mischievous datapoints that don't follow the trend (Outliers!).  
  
![Figure](./box_plot.png)

  
In the land of data analysis, we find ourselves surrounded by three intriguing box plots, each telling a unique story about their respective variables: Overall, Quality, and Repeatability.

First, let’s venture into the realm of **Overall**. Here, we see a median that sits comfortably at around 3.5. However, the whiskers tell a tale of limited range, with the highest value barely reaching 4.5. Despite a solitary outlier lurking at the lower end, this plot reveals a generally stable landscape, indicating that most of our data points are clustered centrally. 

Next, we explore the domain of **Quality**, where the story unfolds with a median of around 3.6. Unlike the Overall plot, this one is more varied, showcasing a range that stretches from just above 2 to around 5. The presence of several outliers at both ends adds color to this narrative, hinting that while most quality assessments hover around the median, some experiences deviate significantly, both positively and negatively.

Finally, we arrive at the kingdom of **Repeatability**. This plot stands out with a median hovering near 1.5 and a stark range that extends to nearly 3—but with a substantial drop into the deeper waters of low values. This indicates a somewhat lower consistency in Repeatability compared to the other domains. The pronounced spread suggests that while some instances achieve high repeatability, many do not, resulting in a more tumultuous journey through this variable landscape.

In summary, these box plots guide us through a rich tapestry of data, each weaving a different narrative about central tendencies, variability, and the occasional outlier. The Overall and Quality variables show moderate stability, while Repeatability’s variability raises questions about consistency that warrant further exploration.

