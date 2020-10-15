import requests
from  bs4 import BeautifulSoup
import time
import csv

#building the scraper as a class
class zillowscraper:
    #got the url, headers and parameters from the browser developer tools
    results = []
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'zguid=23|%2427d01781-c31c-4664-ba82-269ce14920f9; zjs_user_id=null; _ga=GA1.2.2132743643.1601557857; zjs_anonymous_id=%2227d01781-c31c-4664-ba82-269ce14920f9%22; _gcl_au=1.1.50288752.1601557858; _pxvid=8aba3e33-03e7-11eb-a177-0242ac12000a; _fbp=fb.1.1601557858859.274892253; _pin_unauth=dWlkPU4yTmlaR1U1WVRRdFlqY3lZUzAwWXpobExUbG1ZVGN0TW1NNE5UVXdOakl4WW1Oaw; zgsession=1|e4250fe3-cd46-45dd-b3d9-76d658a36328; _gid=GA1.2.85461898.1602587184; KruxPixel=true; DoubleClickSession=true; __gads=ID=ef1ea1b6150c628c:T=1602587194:S=ALNI_MZN1YDLxFJWStz-QHSiPv3ghvhaQw; KruxAddition=true; ki_s=; g_state={"i_p":1602677293479,"i_l":2}; ki_r=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%3D; JSESSIONID=623194410702460E4DAC51BE155FB954; ki_t=1602587192404%3B1602587192404%3B1602600401897%3B1%3B79; search=6|1605195242699%7Cregion%3Dca%26rect%3D50.62214%252C-68.327143%252C23.705962%252C-125.374896%26disp%3Dmap%26mdm%3Dauto%26type%3Dcondo%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26rs%3D0%26ah%3D0%09%0912447%09%09%09%09%09%09; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_bsco=1; _px3=1960617ebef7d6dc7930ce59abce0c5a5584a64ff3a5c7894cfe08cea17a417a:XOXwa87rdffSt3WH+jzien6Z7YdAOke3NHtESrvqNImKTGO/g08vUNnOCeSVKA5W3IIGsLDtpSzI5VZUtugehg==:1000:Uf+Cz/N1yux+tmcEqfOtJRcN5hVN6acXmtkKTc5MHUAgIWFRX+0pnqk3+YgLyhMDE9qgfqyYMtCQS+PpGLeGY4BpPnUZo7IdGZcKxXwGMO0eXorC1GT87amoogfjH+LvnGHAIuQjDwlCQPYWFz+52wqTzm9yFmxTsChZifeoO1Y=; _uetsid=269cdbf00d4411eb9c7afb71665c7281; _uetvid=1c5465edaf877802ddfdf3f3020b2879; AWSALB=edDkxwjHG5f5H6QkkolNPrax08w0B2psZXbJ6IxY0KZco/6YTckNPGvCtXK8DKhQ3Jecfqz9N7e+qJ2zS19FhuTGTHqtM+DhpuSf4YKRqSXsQ4fkliWlG0O6XExg; AWSALBCORS=edDkxwjHG5f5H6QkkolNPrax08w0B2psZXbJ6IxY0KZco/6YTckNPGvCtXK8DKhQ3Jecfqz9N7e+qJ2zS19FhuTGTHqtM+DhpuSf4YKRqSXsQ4fkliWlG0O6XExg',
    'referer': 'https://www.google.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    
    #set requests to the website that contains the data to be scraped
    def fetch(self, url, params):
        response = requests.get(url, headers=self.headers, params=params)
        return(response)
    
    #parse the data from the HTML script using BeautifulSoup
    def parse(self, response):
        content = BeautifulSoup(response)
        deck = content.find('ul', {'class': 'photo-cards photo-cards_wow photo-cards_short'})
        for card in deck.contents:
            script = card.find('script', {'type': 'application/ld+json'})
            if script:
                self.results.append({
                    'price': card.find('div', {'class': 'list-card-price'}).text,
                    'bedrooms': card.find('ul', {'class': 'list-card-details'}).contents[0].text,
                    'bathrooms': card.find('ul', {'class': 'list-card-details'}).contents[1].text,
                    'floorsize': card.find('ul', {'class': 'list-card-details'}).contents[2].text,
                    'address': card.find('address', {'class': 'list-card-addr'}).text
                })
    
    #write the data contained in the 'results' variable in a csv file
    def to_csv(self):
        with open('zillow.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys(), lineterminator = '\n')
            writer.writeheader
            for row in self.results:
                writer.writerow(row)
    
    #run the scraper and use a delay between pages
    def run(self):
        url = 'https://www.zillow.com/ca/condos/'
        for page in range (1,21):
            params ={
            'searchQueryState': '{"pagination":{"currentPage":%s},"mapBounds":{"west":-124.482044,"east":-114.131252,"south":32.528832,"north":42.009517},"regionSelection":[{"regionId":9,"regionType":2}],"isMapVisible":false,"filterState":{"apa":{"value":false},"mf":{"value":false},"ah":{"value":true},"sort":{"value":"globalrelevanceex"},"sf":{"value":false},"land":{"value":false},"tow":{"value":false},"manu":{"value":false}},"isListVisible":true}' %page
            }
            res = self.fetch(url, params)
            self.parse(res.text)
            print(res)
            time.sleep(3)
        self.to_csv()

if __name__ == "__main__":
    scraper = zillowscraper()
    scraper.run()