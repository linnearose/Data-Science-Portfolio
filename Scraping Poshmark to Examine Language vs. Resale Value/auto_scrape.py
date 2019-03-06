from datetime import datetime, timedelta, time
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


while 1:

	# WHERE LINNEA'S CODE STARTS

	url_main = 'https://poshmark.com/category/Women'

	# Create headers to fix 403 status code --> 200
	headers = {'User-agent': 'linnea bot 18'}

	res = requests.get(url_main, headers=headers)
	res.status_code

	# Create BeautifulSoup object
	soup = BeautifulSoup(res.content, 'lxml')

	# Scrape to find URLs
	div = soup.find('div', {'id':'tiles-con'})
	posts = div.find_all('a', {'class':'covershot-con'})

	# Scrape unique part of URL
	urls = []
	for p in range(len(posts)):
		url = posts[p]['href']
		urls.append(url)

	# Create clean URLs
	clean_urls = []
	for u in range(len(urls)):
		full = 'https://poshmark.com' + urls[u]
		clean_urls.append(full)

	print('About to Scrape...')

	# Scraper
	all_posts = []
	for i in clean_urls:
		url = i
		res = requests.get(url)
		soup = BeautifulSoup(res.content, 'lxml')
		content = soup.find('div', {'class':'details'})

		dictionary = {}

		try:
			dictionary['title'] = content.find('h1', {'class':'title'}).text
			dictionary['item_id'] = url[-24:]
			dictionary['price'] = content.find('div', {'class':'price'}).text.split('\xa0')[:2]
			dictionary['description'] = soup.find('div', {'class':'description'}).text
			dictionary['tags'] = [t.text for t in soup.find('div', {'class':'tag-list'})]
			dictionary['status'] = [t.text for t in soup.find('div', {'class':'buy-actions'})][0]
			dictionary['url'] = url
			dictionary['brand'] = content.find('a', {'class':'brand'}).text

		except:
			pass


		all_posts.append(dictionary)


	# Convert list of dictionaries into DataFrame
	print('Putting into DataFrame...')


	df = pd.DataFrame(all_posts)

	# Read in previously saved DataFrame
	df_prev = pd.read_csv('all_posts.csv')

	# Concatenate current df and df_prev
	df = pd.concat([df, df_prev], axis=0)

	# Reset index of newly concatenated df
	df.reset_index(drop=True, inplace=True)

	# Drop 'Unnamed: 0' column
	df.drop(columns=['Unnamed: 0'], inplace=True)

	df.to_csv('all_posts.csv')
	print('DONE - now you wait')
	print(time)


# LINNEA'S CODE ENDS 

	dt = datetime.now() + timedelta(hours=1)
	dt = dt.replace(minute=10)

	while datetime.now() < dt:
		time.sleep(1)
	