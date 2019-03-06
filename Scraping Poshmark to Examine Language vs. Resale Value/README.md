## Problem Statement
This project uses a classification model with NLP to predict the resale value of women's goods on poshmark.com. 

In today's world, selling used goods online is not only normal, but increasingly popular. Poshmark.com is an online tool specifically designed for selling and buying used designer or vintage apparel and accessories. 

When sellers use this convenient tool, they are prompted to create their *own*, unique title and description for each post. Other information, like `category`, is required to an extent, but these are predetermined discrete fields. 

By scraping Poshmark for relevant language data, I determined morpheme frequencies and their effect on illustrating the relationship between language and resale value.   


## Data Dictionary

1. title - raw text data from post titles
2. price - raw string of original and new prices
3. description - raw text data from post descriptions
4. item_id - unique id for each post
5. brand - designer brand (if applicable - vintage items may be null for this feature)
6. status - 'buy now'; available for purchase; not having been sold yet
7. url - unique url for each items information page
8. original_price - original price paid for the item
9. new_price - new price of the item
10. tags - raw string of item tags
11. tag_1, tag_2, tag_3 - each level of category tags (all posts have tag_1='women')
12. tag_2 dummy columns - dummy variables indicating tag category for each post
13. percent_change - percentage off of the original price --> new price
14. percent_change_bucket - buckets for percent_change
15. category_id - each number reprenting a different bucket