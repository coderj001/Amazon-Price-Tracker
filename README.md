
# Amazon-Price-Tracker

## About

> The amazon price tracker use python selenium to crawl webpage and track price info.
> And stored into the database which will updated by user preference.
> Mail info should be inserted to recive mail notification.
> Database will stored in local folder so user will get full access.

## Installation

* Download the Amazon-Price-Tracker form https://github.com/coderj001/Amazon-Price-Tracker
* Python and pip should be installed on your system.
* Open the terminal or command prompt and move Amazon-Price-Tracker directory.
* Use the command pip install -r requirement.txt, all the necessary modules will be installed.
* Then run by command python main.py or python3 main.py

## Usage

* On running main.py, you will get 
      Amazon Price Trace
    Note:
        python main.py url http://www.amazon.in/7gyyf6ft/0-ji/9yui-9
        python main.py update
        python main.py show
        python main.py  email
* use command python main.py url http://www.amazon.in/7gyyf6ft/0-ji/9yui-9 to store you product data inserted.Please use full url of the product webpage and product only limited to amazon.in 
* Use commamd python main.py update to update your database.
* Use command python main.py show to show stored database.
* Use command python main.py email to change email info.
