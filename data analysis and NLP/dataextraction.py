import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Load the Excel file
input_file = 'C:\\Users\\DELL\\Downloads\\Input.xlsx'
data = pd.read_excel(input_file)

# Function to extract article title and text
def extract_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming the title is within an <h1> tag
    title = soup.find('h1').get_text()
    
    # Assuming the article text is within a <div> with class 'article-content'
    article_div = soup.find('div', class_='td-post-content tagdiv-type')
    article_text = ""
    if article_div:
        for paragraph in article_div.find_all('p'):
            article_text += paragraph.get_text() + '\n'
    
    return title, article_text

# Create a directory to save the articles if it doesn't exist
if not os.path.exists('articles'):
    os.makedirs('articles')

# Process each URL and save the article text
for index, row in data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    try:
        title, article_text = extract_article(url)
        file_path = os.path.join('articles', f'{url_id}.txt')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(title + '\n\n' + article_text)
        
        print(f'Article {url_id} saved successfully.')
    except Exception as e:
        print(f'Error processing URL_ID {url_id}: {e}')

print('Data extraction completed.')
