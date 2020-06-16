import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests

def scrape_mars():
    url = 'https://mars.nasa.gov'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

#Find the Feature articles title and description
    news_title = soup.find('h1', class_='media_feature_title').text
    news_p = soup.find('div', class_='description').text 

    # print(news_title)
    # print(news_p)

#Set up the Chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

#Use splinter to navigate to the correct page
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')

#Use BeautifulSoup to get the image url
    response = requests.get(browser.url)
    soup = bs(response.text, 'html.parser')

    featured_image_url = soup.find('figure', class_='lede').    find('a')['href']
    mars_image_url = 'https://www.jpl.nasa.gov' + featured_image_url
    # print('https://www.jpl.nasa.gov/' + featured_image_url)
    browser.quit()

#Setting up BeautifulSoup
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

#Print the latest tweet
    tweet = soup.find('div', class_='css-901oao r-1adg3ll r-1b2b6em r-q4m81j').    find('span', class_='css-901oao css-16my406').text

    # print(tweet)

#Getting the first table
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_table = tables[0]

#Create and save the HTML file
    mars_html = mars_table.to_html()
    mars_html.replace('\n', '')
    mars_table.to_html('mars_table.html')

#Set up the Chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

# Navigate to all pages and grab the image we need
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")

    cerberus_image_url = soup.find("li").find("a")["href"]
    cerberus_image_title = soup.find("h2", class_="title").text
    # print(cerberus_image_url)
    # print(cerberus_image_title)

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")
    schiaparelli_image_url = soup.find("li").find("a")["href"]
    schiaparelli_image_title = soup.find("h2", class_="title").text
    # return schiaparelli_image_url)
    # return schiaparelli_image_title)

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")

    syrtis_image_url = soup.find("li").find("a")["href"]
    syrtis_image_title = soup.find("h2", class_="title").text
    # return syrtis_image_url
    # return syrtis_image_title

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")
    browser.click_link_by_partial_text("Open")

    response = requests.get(browser.url)
    soup = bs(response.text, "html.parser")

    valles_image_url = soup.find("li").find("a")["href"]
    valles_image_title = soup.find("h2", class_="title").text
    # return valles_image_url
    # return valles_image_title

#save the info as a dictionary
    # hemisphere_image_urls = [
    #     {"title": "Cerberus Hemi", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg" },
    #     {"title": "Schiaparelli Hemi", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    #     {"title": "Syrtis Major Hemi", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    #     {"title": "Valles Marineris", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    # ]
    browser.quit()

    mars_dict = {
        'Title': news_title,
        'Paragraph': news_p,
        'Featured_Images': mars_image_url,
        'Tweet': tweet,
        'cerb_title': cerberus_image_title,
        'cerb_url': cerberus_image_url,
        'schiaparelli_title': schiaparelli_image_title,
        'schiaparelli_url': schiaparelli_image_url,
        'syrtis_title': syrtis_image_title,
        'syrtis_url': syrtis_image_url,
        'valles_title': valles_image_title,
        'valles_url': valles_image_url
    }

    return mars_dict