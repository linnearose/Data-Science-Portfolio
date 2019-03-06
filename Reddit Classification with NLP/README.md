## Problem Statement

How can we use language data scraped from reddit to predict a given post’s subreddit?


## Executive Summary

The goal of the reddit API project was to collect, clean, analyze and model language data to be able to classify posts and their subreddits. To do this, we used different NLP functions to wrangle the language data (in this case, the title) from each reddit post. Once we had clean data, ridden of stop words (“function” words), extraneous morphemes and unnecessary characters, like numbers or emoji, we ran the data through our models. 

In this case I opted to try a random trees model and compare it to a logistic regression model. Initially, I took data from r/aww and r/datascience to compare, but it proved TOO easy to differentiate between the two subreddits since the subject matter and vocabulary was completely different and made for simple binary classification. 

Then, I switched over to collecting data from r/cats and r/dogs, while keeping my r/aww data, to give myself more of a challenging comparison. In the end, a random trees model was far superior for modeling the data. Whether I was doing a binary or three-way classification, random trees reliably created a model on the train data that wasn’t wildly overfit on the test data. 

For future dives into this topic, I would love to get a better handle on the Lemmatizer and PorterStemmer tools to be able to do more linguistic analysis on words and their roots. In addition it would be interesting to see if n-grams have a significant effect on the data in this specific classification problem. Since we're using post titles on what I would consider a relatively informal platform, sentence structure might not be as helpful in determining the true meaning of each word, and in turn not do much to increase how effective the model is.
