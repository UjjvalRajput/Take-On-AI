# Take On AI

## Introduction
This study is motivated by the need to shed light on how traditional and social media shape public and policy-making perspectives on these technologies. This study contributes to the field of media studies and social data analytics by systematically comparing the portrayal of AI and automation in traditional versus social media. My goal is to identify the subtle differences across these platforms in terms of tone, content, and interaction. By highlighting these differences, the project provides insights into how media forms influence public perceptions and debates surrounding emerging technologies. The findings are intended to assist policymakers, journalists, and technology developers in understanding and navigating the complex media landscape influencing technology adoption and regulation.

### Research Question

How does traditional and social media discourse differ in portraying AI and automation?

### Literature Research

As a background, I will establish the state of discourse in general on traditional and social media platforms. This includes highlighting key themes and comparing the strengths of each platform.

Newspapers, magazines, and television are facets of traditional media characterized by professionalism, credibility, and in-depth analysis. Articles, for example, written by professional journalists and overseen by editors ensure that the information is accurate and reliable (McQuail, 2010). News organizations typically adhere to a set of journalistic standards and ethical guidelines that further enforce accuracy and reliability (Kovach & Rosenstiel, 2014).

We typically rely on traditional media platforms as a primary source of information. They provide a greater general audience with comprehensive coverage and in-depth analyses via expert interviews, investigative reports, and professional commentary (Hamilton, 2004). Longer articles and features in traditional media can provide in-depth nuanced perspectives that go beyond headline news (Boczkowski & Mitchelstein, 2013). If traditional media discourse involving AI and automation is consistent with other topics, we can expect accurate, comprehensive analyses based on reliable, relevant information.

Conversely, discourse on social media platforms like GitHub, Reddit, and Instagram is characterized by user-generated content and engagement that leans toward virality and immediacy. Social media platforms allow a user to share content in real-time, making it a powerful tool for breaking news or live updates (Hermida, 2010). Hermida's research underscores the unique position of social media in the information ecosystem, highlighting its capacity to disseminate information swiftly and broadly, often outpacing traditional news outlets. This real-time nature transforms how news is consumed and shared, amplifying its reach and impact almost instantaneously.

Because social media trivializes the consumption of user-generated content, this content can go viral and reach a wide audience in a short period (Allcott & Gentzkow, 2017). Allcott and Gentzkow's findings emphasize the ease with which misinformation and sensational content can spread on these platforms. Their study suggests that the very structure of social media, which prioritizes engagement and shareability, can inadvertently elevate less reliable information to prominence, leading to widespread dissemination before it can be adequately fact-checked.

An important aspect of social media is its innate interactivity, so because social media fosters community engagement and allows for interactive discussions, engagement is naturally higher regardless of overall sentiment (Boyd, 2014). Boyd's analysis highlights the role of interactivity in enhancing user engagement. By facilitating discussions and interactions, social media platforms create a sense of community and involvement, which drives higher engagement levels. This interactivity means that users are more likely to participate in discussions, share their opinions, and respond to others, creating a dynamic and constantly evolving discourse.

Therefore, if social media discourse involving AI and automation is consistent with other topics, we can typically expect polarizing opinions from a diverse set of actors tending toward, immediate, sensational content over accurate or reliable information (Kaplan & Haenlein, 2010). Kaplan and Haenlein's work indicates that the nature of social media discourse, driven by engagement metrics and the speed of information sharing, often skews toward sensationalism and polarization. This trend suggests that discussions around AI and automation will likely reflect these characteristics, with varied and often conflicting viewpoints being shared rapidly and widely, potentially at the expense of accuracy and depth.

I found two interesting points of comparison between platforms: the tone and framing of the content, as well as public engagement and overall influence. Traditional media tends to deliver AI and automation content in a balanced, cautious tone, framing it within broader contexts such as its economic impact (Brennen, 2018). Social media discourse often tends toward polarizing opinions that could either be in favor of or against AI and automation (Schmidt, 2017) and these polarizing opinions help drive discussions allowing for social media’s overall greater public engagement. The ability to interact directly with stakeholders, policymakers, or software developers is a testament to social media’s truly interactive nature (Flew, 2018). Conversely, public engagement in traditional media is limited in that there is no interaction between the author and the reader, but the influence of traditional media remains significant due to its established reputation and wider reach among general audiences (Boczkowski & Mitchelstein, 2013).

So while traditional media offers depth, reliability, and broad reach, social media provides immediacy, interaction, and diverse perspectives. Both platforms play crucial roles in shaping the public discourse on AI and automation, complementing each other by catering to different aspects of information dissemination and audience engagement.

#### Hypothesis

Suppose discourse mentioning AI and automation is consistent with the norm on each platform. In that case, I expect traditional media discourse to have an overall neutral tone while framing AI and automation within broader societal contexts. We can expect articles with in-depth analyses of AI advancements in an economic context and a generally positive sentiment when discussing implications on the labor market.

Social media discourse on AI and automation would feature polarizing opinions and a relatively high engagement rate. Due to the nature of GitHub discussions as a community for people already interested in the product, we can expect more positive than negative sentiment in discussion posts. Upon deeper analysis, we should find that more users engage through comments than likes, as a shared interest and forum structure will encourage sharing opinions and foster engagement within the community.

### Methodology

#### Tools and Technologies

- **Python**: Primary programming language for developing AI models and data processing scripts.
- **Jupyter Notebooks**: For interactive coding sessions and sharing insights.
- **NumPy & Pandas**: For data manipulation and analysis.
- **Scikit-Learn**: For feature extraction and topic modeling.
- **Matplotlib & Seaborn**: For data visualization.
- **NLTK**: For natural language processing, including stopwords, WordNetLemmatizer, and SentimentIntensityAnalyzer.
- **TextBlob**: For text processing and sentiment analysis.
- **Re**: For regular expressions and further text cleaning for accuracy regarding top-words.

### Data Collection and Processing

- **GitHub**: Utilized GraphQL to fetch discussion posts from AI-focused repositories, extracting over 1,100 posts.
- **The New York Times**: Accessed via its API, collecting 498 articles related to AI and automation.

## Results

### Sentiment Analysis of GitHub Discussions

- **Positive Sentiment**: Over 630 discussions with a positive sentiment.
- **Neutral Sentiment**: Around 350 discussions with a neutral sentiment.
- **Negative Sentiment**: Fewer than 100 discussions with a negative sentiment.

### Sentiment Analysis of The New York Times Articles

- **Neutral Sentiment**: Many articles with a neutral tone.
- **Positive Sentiment**: Articles with positive sentiments scattered across the dataset.
- **Negative Sentiment**: Negative sentiment articles showing significant variation.

### Temporal Trends

- **GitHub Discussions**: Higher initial interest with gradual decline over time.
- **New York Times Articles**: Consistently low mention rate with occasional peaks.

## Discussion and Conclusion

My research reveals significant differences in how AI and automation are portrayed in traditional versus social media. Traditional media often presents these technologies in a cautious and balanced manner, while social media leans towards sensationalism and polarizing opinions. These findings highlight the need for a nuanced understanding of media influences on public perception and policy-making.

### Limitations and Future Research

- **Scope**: Limited to a few well-known platforms. Future research can explore perspectives from smaller sources.
- **Qualitative Analysis**: Future studies could benefit from qualitative evaluations to understand the context and narrative strategies used in different media platforms.
- **Expansion**: Include a wider range of media sources to understand regional differences and employ advanced computational tools for forecasting patterns in media discourse.

## References

- Allcott, H., & Gentzkow, M. (2017). Social Media and Fake News in the 2016 Election. National Bureau of Economic Research.
- Boczkowski, P. J., & Mitchelstein, E. (2013). The news gap: when the information preferences of the media and the public diverge. The MIT Press.
- Boyd, D. (2014). It’s complicated: the social lives of networked teens. Yale University Press.
- Brennen, J. S., Howard, P. N., & Nielsen, R. K. (2018). An industry-led debate: How UK media cover artificial intelligence. Reuters Institute for the Study of Journalism.
- Flew, T. (2018). Understanding global media. Palgrave Macmillan.
- Hermida, A. (2010). TWITTERING THE NEWS: The emergence of ambient journalism. Journalism Practice, 4(3), 297–308.
- Kaplan, A. M., & Haenlein, M. (2010). Users of the world, unite! The challenges and opportunities of Social Media. Business Horizons, 53(1), 59–68.
- Kovach, B., & Rosenstiel, T. (2001). The elements of journalism: what newspeople should know and the public should expect. Crown Publishers.
- McQuail, D. (2010). McQuail’s mass communication theory (6th ed.). SAGE.
- Schmidt, A. L., Zollo, F., Del Vicario, M., Bessi, A., Scala, A., Caldarelli, G., ... & Quattrociocchi, W. (2017). Anatomy of news consumption on Facebook. Proceedings of the National Academy of Sciences, 114(12), 3035-3039.
