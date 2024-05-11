# Module 2 : 從前述 SQL database 中，取出 股票資料，繪製 K線 及價量圖。

from sqlalchemy import text
# visual
import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd
#time
import datetime as datetime

def plot_stock_data(engine, sql_name, sid):
    # Retrieve data from SQL
    conn = engine.connect()
    query = text(f"SELECT * FROM {sql_name} WHERE sid = '{sid}'")
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    df = df.drop(columns="index")
    df.set_index('日期')
    
    df['成交股數'] = df['成交股數'].str.replace(",","")
    df['成交金額'] = df['成交金額'].str.replace(",","")
    df['成交筆數'] = df['成交筆數'].str.replace(",","")

    # Plotting K-line and Price-Volume graphs
    # 繪製 Ｋ線
    fig = plt.figure(figsize=(24, 15))
    ax = fig.add_axes([0,0.2,1,0.5])
    ax2 = fig.add_axes([0,0,1,0.2],sharex = ax)

    ax2.set_xticks(range(0, len(df['日期']), 20))
    ax2.set_xticklabels(df['日期'][::20])
    
    plt.title(f"stock ID {sid}", fontsize=18)
    mpf.candlestick2_ochl(ax,
                          df['開盤價'].astype(float),
                          df['收盤價'].astype(float),
                          df['最高價'].astype(float),
                          df['最低價'].astype(float),
                          width=0.6, colorup='r', colordown='g', alpha=0.75)

    mpf.volume_overlay(ax2, 
                       df['開盤價'].astype(float),
                       df['收盤價'].astype(float),
                       df['成交股數'].astype(float),
                       colorup='r', colordown='g', width=0.5, alpha=0.8)
    
    plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 