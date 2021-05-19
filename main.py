from selenium import webdriver
import yaml
import time
from redfin_scraper import Redfin
import pickle


def main():
    # get credentials
    with open('config/config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    # variables
    driver = get_driver(cfg)
    location = cfg['location']
    filters = cfg['filters']

    reddy = Redfin(driver, location)
    reddy.search_listings(filters)
    time.sleep(2)
    reddy.get_listings()


def get_driver(cfg):
    # Method to get driver
    path = cfg['chrome_driver_path']
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.redfin.ca/on/ottawa/')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    return driver


if __name__ == '__main__':
    main()
