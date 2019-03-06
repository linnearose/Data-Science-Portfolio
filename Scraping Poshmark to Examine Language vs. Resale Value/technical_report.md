## Technical Report


### Scraping Data
There is no API for obtaining data from poshmark, so I built a custom scraper using BeautifulSoup to obtain the language and price data I needed for my analysis. 

Once I solidified my scraper in a jupyter notebook, I created a .py file that would automatically run every hour from terminal and save the data to a master DataFrame.

### Data Analysis, Cleaning and Processing
There are three notebooks that deal with cleaning and analyzing the raw data from the scrape. Using a tokenizer and lemmatizer, I cleaned both the `title` and `description` columns. 

While conducting EDA, I spent time creating different masks to help filter the data and expose what I will call spam posts. An example of a spam post on Poshmark could be an advertisement for a sale or a promotion of a specific user's account. Instead of a regular post where the title, description and pricing information actually describe an item that is being resold, a spam post will have information unrelated to selling a specific item and completely arbitrary pricing information.


### Modeling
In order to create my initial model, I used the `clean_description` variable to classify each post as being in one of multiple buckets. Each `percent_change_bucket` value represented a range of percentages, which in turn represented the relationship between `original_price` and `new_price` (i.e. the resale price).

I then experimented with both `CountVectorizer()` and `TfidfVectorizer()` to fit and transform each `clean_description`. 

I fed the resulting data into multiple classification models: `LinearSVC()`, `LogisticRegression()` and `DecisionTreeClassifier()`. The decision tree model yielded the highest `accuracy_score` of around 0.396. 


### Summary

The goal of this capstone project was to learn about the relationship between an item's description/title and its resale value. An inital score of almost 40% is a good start, but so far the only takeaway from the models is that there **is** a significant relationship. 

Further linguistic vetting and analysis is needed to isolate the particular language (specific vocabulary, bigrams, etc.) that dictates how much an item should be discounted. In the same vein, I want to be able to discover what language one *should* use to yield a higher return on their sale (`new_price`) compared to the `original_price`. 