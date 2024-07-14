from openpyxl import Workbook
import pandas as pd
import time
import logging
from datetime import datetime
from urllib.request import urlretrieve
import os
import re
from dateutil.relativedelta import relativedelta
log = logging.getLogger('robotlog')

def download_image(url, image_name):
    log.info("download_image execution started")
    if not os.path.exists('output'):
        os.makedirs('output')
    image_path = os.path.join('output', image_name)
    urlretrieve(url, image_path)
    log.info("download_image execution ended")


def get_occurrences(text, search_phrase):
    return text.lower().count(search_phrase.lower())


def write_data_to_excel(data):
    log.info("write_data_to_excel execution started")
    headers = ['Title', 'Date', 'Description', 'Picture filename', 'Search phrases count',
               'Title or description contains currency']
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, 'output.xlsx')
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    log.info("write_data_to_excel execution ended, excel created at: "+ output_path)


class customDate:
    def __init__(self, date: str):
        self.date = date

    def format_1(self):
        str_format_1 = self.date.strftime('%b. %d, %Y')
        return str_format_1
    
    def format_2(self):
        str_format_2 = self.date.strftime('%B %d, %Y')
        return str_format_2
    


def compare_dates(number: int, date: str):

    """Dates can be of the followin type (from newest to oldest by appearance)
    * seconds ago
    1 minute ago
    * minutes ago
    1 hour ago
    * hours ago
    June 25, 2024
    Jan. 1, 1985
    """
    log.info("compare_dates execution started")
    current_date_aux = datetime.now().date()
    today = customDate(current_date_aux)
    days_in_month = 30 #we take this as average days in month

    if 'seconds' in date or 'minute' in date or 'minutes' in date or 'hour' in date or 'hours' in date:
        #make the date the same as today date (we use arbitrary format)
        date_correct_format = datetime.strptime(today.format_2(), '%B %d, %Y').date()
    elif '.' in date:
        #make the date a datetime with correct format (with .)
        date_correct_format = datetime.strptime(date, '%b. %d, %Y').date()
    else:
        #make the date a datetime with correct format (without .)
        date_correct_format = datetime.strptime(date, '%B %d, %Y').date()

    #print('date_correct_format = '+ str(date_correct_format))
    
    #calculate the date difference (the result will always be negative...eg -30)
    date_difference = date_correct_format - datetime.strptime(today.format_2(), '%B %d, %Y').date()
    str_date_difference = str(date_difference).split(' ')[0]

    #check if date difference is 0
    if '0:00:00' in str_date_difference:
        return False

    #check if we signal stop or not
    if number == 0:
        number = 1

    #print('days in the past to search for = ', number * days_in_month ,' and abs =  ', abs(int(str_date_difference)))
    #check if we reached the desired period of time
    if number * days_in_month <= abs(int(str_date_difference)):
        return True #stop execution on main
    else:
        return False #doesn't stop execution on main
    
    
#print(compare_dates (1, 'July 13, 2024'))
