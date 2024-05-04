from bs4 import BeautifulSoup
from urllib.request import urlopen
import cloudscraper
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class Download:
    def __init__(self,url):
        self.url = url

    def facebook(self):
        data = {
                'URLz': self.url,
                }        
        try:       
            scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
            response = scraper.post('https://fdown.net/download.php',  data=data)
            download_soup = BeautifulSoup(response.text,"html.parser")
            downlaod_hdlink = download_soup.find("a",id="hdlink" )
            downlaod_sdlink = download_soup.find("a",id="sdlink" )
            downlaod_imgs = download_soup.find_all("img",class_="lib-img-show")
            downlaod_description = download_soup.find_all("div",class_='lib-row lib-desc')
            try:
                img = downlaod_imgs[0]["src"] if downlaod_imgs else None
            except :
                img = downlaod_imgs[0]["data-cfsrc"] if downlaod_imgs else None
            res={
                        'hdlink':downlaod_hdlink['href'] if downlaod_hdlink else None,
                        'sdlink':downlaod_sdlink["href"] if downlaod_sdlink else None,
                        'fb_img':img,
                        'description': downlaod_description[0].text.strip() if downlaod_description else None,
                        'duration': downlaod_description[1].text.strip() if downlaod_description else None,
                        'status_code': 200,
            }
        except Exception as e:
            res={
            'status_code': 302,
            'message': "Uh-Oh! This video might be private and not public ",
                }  
        return res
    
    def youtube(self):
        return "download link from youtube"
    def instagram(self):
        print('instahh')
        print(self.url)
            
                
        res={
            'status_code': 200,
            'message': "hhh",
                } 
        return res
    
    def tiktok(self):
        return "download link from tiktok"