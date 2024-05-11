# Module 1 : 下載 TSMC 台股證交所股票: 2020/01 ~ 2024/04，儲存至 SQL database 。

import bs4 as bs  #  beautifulsoup 4
import urllib
import urllib.request
import json
import pandas as pd
import time
from sqlalchemy import create_engine

# Module 1: Download TSMC Stock Data and Store in SQL Database
def get_stock_data(year, month, sid): # get a month in once scype
    base_url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={:d}{:02d}01&stockNo={:s}"
    target_url = base_url.format(year,month,sid)
    # get data and parsing (剖析)
    webpage_history = urllib.request.urlopen(target_url)
    web_html = bs.BeautifulSoup(webpage_history, 'html.parser')
    stock = json.loads(web_html.text)  #  讀取 JSON 資料 -> 轉換成 dictionary
    stock_info = list(stock.values())  #  轉換成 list 格式
    stock_price = pd.DataFrame(stock_info[4]) # 使用pandas創建dataframe(資料表格)
    stock_price.columns = stock_info[3] # 將 data frame 資料加上 column name
    return stock_price # 傳回 dataframe

def get_stock_datas(start_year,start_month,stop_year,stop_month,sid): # include stoped month
    year = start_year
    month = start_month
    
    df_list = [] # prepare empty list to store dataframes of each month
    while True:
        # download
        print("[Downloading] year = {:d}, month = {:2d}".format(year, month))
        df = get_stock_data(year,month, sid) # get a month of data
        df_list.append(df) # append into list
        # check if abort
        if (year == stop_year and month == stop_month):
            break
        # if not abort, then increase one month
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        # delay a little time
        #time.sleep(0.1) # 5 sec 

    
    fused_df = pd.concat(df_list, ignore_index=True, axis=0) # ignore_index (忽略原有的index)
    fused_df["sid"] = sid
    return fused_df # return dataframe


def store_to_sql(df,name):
    # create a referrence for sql library 
    engine = create_engine('sqlite://', echo = False) 
    df.to_sql(name, con = engine) 
    return engine