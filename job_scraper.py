from bs4 import BeautifulSoup
import requests
import pandas as pd

# Show every row
pd.set_option('display.max_rows', None)

# Show every column
pd.set_option('display.max_columns', None)

# Prevent cell contents from being cut off
pd.set_option('display.max_colwidth', None)

#getting url
url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

#scraping the data needed
job_titles = soup.find_all('h2', class_='title is-5' )
job_table_titles = [title.text for title in job_titles]
company = soup.find_all('h3', class_='subtitle is-6 company' )
company_name = [title.text for title in company]
location = soup.find_all('p', class_='location' )
location_name = [title.text.strip() for title in location]
job_details = soup.find_all('a', class_='card-footer-item', href= lambda href: href!= "https://www.realpython.com" )
job_detail_page_url = [link['href'] for link in job_details]
# putting the data in a data frame
df = pd.DataFrame({'Job Title': job_table_titles,
                  
                  'Company Name' : company_name,
                   'Location' : location_name,
                   'Job detail page URL' : job_detail_page_url
                  
                  })
print(df)
#exporting to a csv file
df.to_csv('fakepythonjobs_data')
