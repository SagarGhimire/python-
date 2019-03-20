# Twitter Mining
- Course: Web-Mining
- Midterm Project
- Developer: Sagar Ghimire


## Links
- [Source](https://github.com/44520-w19/wm-project-midterm-SagarGhimire)

## Introduction

I am looking at the Sentiment Analysis of public replies when Apple and Samsung tweets about their products especially their phone products.

Stream of data used in this project is collection of tweets retrived from twitter using tweepy.
The replies of the tweets are collected in specific dates when they offically release their products.


## Data Source

-Twitter : Data is extracted using tweepy module and later done text mining for the statistical purposes. 

## The Challenge

**Getting the replies of the specific tweets**
- Twitter API doesn't provide good source for extracting the replies of the tweets so I have to dig in more to get the replies for that tweet.  
- The second one is parsing the replies. As the replies were in html form so html parsing and unicode parsing has to be done for the analysis purposes.

* Language: Python
* Modules: Beautiful Soup, Vader lexicon

**Chart Visualization:
- Mathplotlib
- Bar graph
