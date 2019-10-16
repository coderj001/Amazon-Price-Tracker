'''
This script is for inserting amazon product links to database.
'''
import time,datetime,os,sqlite3,json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs

class Insert:
    """[class Insert main purpose is to take urls, find data and store it into database.]"""
    
    def __init__(self,url):
        self.url=url
    
    def browser(self):
        # TODO: This is a browser so it will take url and return data.
        # ! url is not checked so try catch should be used to avoid not found error.
        op=Options()
        op.headless=True
        driver=webdriver.Firefox(options=op,executable_path=r'driver/geckodriver')
        driver.get(self.url)
        time.sleep(6)
        t=datetime.datetime.now()
        if not os.path.isdir('./shorts'):
            os.mkdir('shorts')
        png='screenshort-{}.png'.format(t.strftime('%c'))
        driver.save_screenshot('./shorts/{}'.format(png))
        html=driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()
        soup=bs(html,'html.parser')
        p_nm=soup.find('span',{'id':'productTitle'})
        pr=soup.find('span',{'id':'priceblock_ourprice'})
        data={"product_name":p_nm.get_text().replace('\n','').strip(),
                "price":pr.get_text().replace('\u20b9\u00a0','Rs.').strip(),
                "url":self.url,
                "screenshort":'./shorts/{}'.format(png)
                }
        js=json.dumps(data)
        return js

    def databaseEntry(self):
        # TODO: It will get data by calling browser and storing data into database.
        #! Data must be stored carefull into database amazon.db and table links and coloums (product,price,url,screenshort)
        js=self.browser()
        data=json.loads(js)
        con=sqlite3.connect('amazon.db', timeout=10)
        q=con.cursor()
        q.execute('SELECT * FROM links WHERE url=:url',{'url':self.url})
        con.commit()
        rs=q.fetchone()
        if rs == None:
            q.execute('INSERT INTO links VALUES (:product_name,:price,:url,:screenshort)',data)
            print('Data Inserted.')
            con.commit()
        else:
            print('Links is Already In the database.')
        con.close()

    def controller(self):
        # TODO: Task is to compitable other to work together.
        print('Information is Underprocess')
        try:
            self.databaseEntry()
        except Exception as e:
            print('Error: ',e)

