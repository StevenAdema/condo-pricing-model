import time

class Redfin:
    def __init__(self, driver, location):
        self.url = 'https://www.redfin.ca/on/ottawa/filter/'
        self.driver = driver
        self.location = location

    def search_listings(self, filters):
        '''
        :param filters: a list of filters
        :return:
        '''
        filtered_url = self.url + ','.join(filters) + ',' + self.location
        print(filtered_url)
        self.driver.get(filtered_url)

    def get_listings(self):
        elements = self.driver.find_elements_by_xpath("//a[@href]")
        listing_links = []
        for i in elements:
            listing_links.append(i.get_attribute('href'))
        
        listing_links = [i for i in listing_links if 'home' in i]
        listing_links = list(dict.fromkeys(listing_links))

        print(listing_links)



