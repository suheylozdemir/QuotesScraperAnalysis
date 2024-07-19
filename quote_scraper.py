import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sqlalchemy import create_engine
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def scrape_quotes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    quotes = []
    authors = []
    
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        
        quotes.append(text)
        authors.append(author)
    
    data = {'Quote': quotes, 'Author': authors}
    df = pd.DataFrame(data)
    return df

def analyze_and_visualize(df):
    if df.empty:
        st.write("No data available to analyze.")
        return
    
    author_counts = df['Author'].value_counts().head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=author_counts.index, y=author_counts.values, palette='viridis')
    plt.title('Top 10 Authors by Number of Quotes')
    plt.xlabel('Author')
    plt.ylabel('Number of Quotes')
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    text = ' '.join(df['Quote'])
    stop_words = set(stopwords.words('english'))
    wordcloud = WordCloud(stopwords=stop_words, background_color='white', width=800, height=400).generate(text)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Quotes')
    st.pyplot(plt.gcf())

def save_to_database(df, db_name='quotes.db', table_name='quotes'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)

st.title("Quotes Scraping and Analysis")

st.write("""
## Scrape Quotes from Quotes to Scrape
Click the button below to scrape quotes from the Quotes to Scrape website, analyze the data, and save it to a database.
""")

if st.button("Scrape and Analyze"):
    df = scrape_quotes()
    st.write("### Scraped Data")
    st.write(df)
    st.write("### Analysis and Visualization")
    analyze_and_visualize(df)
    save_to_database(df)
    st.write("Data saved to database.")