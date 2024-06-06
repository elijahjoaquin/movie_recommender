from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import re


GENRE_XPATHS = {
    "action": '//*[@id="accordion-item-genreAccordion"]/div/section/button[1]',
    "adventure": '//*[@id="accordion-item-genreAccordion"]/div/section/button[2]',
    "animation": '//*[@id="accordion-item-genreAccordion"]/div/section/button[3]',
    "comedy": '//*[@id="accordion-item-genreAccordion"]/div/section/button[5]',
    "drama": '//*[@id="accordion-item-genreAccordion"]/div/section/button[8]',
    "horror": '//*[@id="accordion-item-genreAccordion"]/div/section/button[14]',
    "musical": '//*[@id="accordion-item-genreAccordion"]/div/section/button[16]',
    "romance": '//*[@id="accordion-item-genreAccordion"]/div/section/button[20]',
    "sci-fi": '//*[@id="accordion-item-genreAccordion"]/div/section/button[21]',
    "sport": '//*[@id="accordion-item-genreAccordion"]/div/section/button[23]',
    "war": '//*[@id="accordion-item-genreAccordion"]/div/section/button[26]'
}

def get_movies_by_genre(genre):
    # Setup Selenium WebDriver for Edge
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    driver = webdriver.Edge(options=options)

    try:
        driver.maximize_window()
        url = 'https://www.imdb.com/search/title/'
        driver.get(url)

        # Wait for the page to load
        time.sleep(1)
        
        select_title_type = driver.find_element(By.XPATH, '//*[@id="titleTypeAccordion"]/div[1]/label/span[1]/div')
        select_title_type.click()
        time.sleep(1)
        
        select_movie_filter = driver.find_element(By.XPATH, '//*[@id="accordion-item-titleTypeAccordion"]/div/section/button[1]')
        select_movie_filter.click()
        time.sleep(1)        
        
        navigate_genre = driver.find_element(By.XPATH, '//*[@id="genreAccordion"]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", navigate_genre)
        time.sleep(2) 
        navigate_genre.click()
        time.sleep(1)
        
        if genre in GENRE_XPATHS:
            select_genre = driver.find_element(By.XPATH, GENRE_XPATHS[genre])
            select_genre.click()
            time.sleep(2)
        else:
            print("Genre not found")
            return None
        
        see_results = driver.find_element(By.CSS_SELECTOR, 'button.ipc-btn.ipc-btn--single-padding.ipc-btn--center-align-content.ipc-btn--default-height.ipc-btn--core-accent1.ipc-btn--theme-base.sc-e3ac1175-4.ceNEEH') 
        see_results.click()
        time.sleep(2)
        
        movies = driver.find_elements(By.CSS_SELECTOR, 'div.ipc-metadata-list-summary-item__c')
        
        random_movie = random.choice(movies)

        title = random_movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
        title = re.sub(r'^\d+\.\s*', '', title)
        synopsis = random_movie.find_element(By.CSS_SELECTOR, 'div.ipc-html-content-inner-div').text
        year = random_movie.find_element(By.CSS_SELECTOR, 'span.sc-b189961a-8.kLaxqf.dli-title-metadata-item').text
        poster = random_movie.find_element(By.CSS_SELECTOR, 'img.ipc-image').get_attribute('src')

        print(f"""
              Title: {title} 
              Synopsis: {synopsis}
              Year: {year}
              """)
        return {
            'title': title,
            'synopsis': synopsis,
            'year': year,
            'poster': poster
        }
        
    finally:
        # Close the WebDriver
        driver.quit()


