from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the IMDb Top 250 page
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

# Click to switch to the detailed list view
button = driver.find_element(By.ID, 'list-view-option-detailed')
button.click()
time.sleep(3)
soup= BeautifulSoup(driver.page_source,'html.parser')

movie_list=soup.find_all('li',class_='ipc-metadata-list-summary-item')
titles=[]
images=[]
release_years=[]
durations=[]
imdb_ratings=[]
descriptions=[]


for movie in movie_list:
    title=movie.h3.text
    titles.append(title)
    image=movie.img['src']
    images.append(image)
    release_year=movie.find_all('span',class_='sc-5bc66c50-6 OOdsw dli-title-metadata-item')[0].text
    release_years.append(release_year)
    duration=movie.find_all('span',class_='sc-5bc66c50-6 OOdsw dli-title-metadata-item')[0].text
    durations.append(duration)
    imdb_rating=movie.find('span',class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text
    imdb_ratings.append(imdb_rating)
    description=movie.find('div',class_='ipc-html-content-inner-div').text
    descriptions.append(description)

Data=pd.DataFrame({'Titles':titles,'Release Year':release_years,'Duration':durations,'Images':images,'Description':descriptions,'Imdb Rating':imdb_ratings})
Data.to_csv("IMDB Top 250 movies.csv")
