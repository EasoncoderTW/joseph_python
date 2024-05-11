# Module 3 : 再從 股票的收盤價 (Close) 歷史資料，訂出策略，選取適當的 「移動均線 (Moving
# Averages)」(例如：5日-10日、10日-30日、20日-60日、…) 繪製移動均線曲線 於 K
# 線圖中。 之後，撰寫程式 找出「黃金交叉」和「死亡交叉」日期，並標示於 K線圖
# 中。

from sqlalchemy import text
# visual
import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd
#time
import datetime as datetime

# Module 3: Moving Averages and Identifying Golden/Death Cross
def plot_stock_data_with_moving_averages(engine, sql_name, sid, short_window, long_window):
    conn = engine.connect()
    query = f"SELECT * FROM {sql_name} WHERE sid = '{sid}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    df = df.drop(columns="index")
    df.set_index('日期')
    
    df['short_ma'] = df['收盤價'].rolling(window=short_window).mean()
    df['long_ma'] = df['收盤價'].rolling(window=long_window).mean()
    
    # Identifying Golden Cross and Death Cross
    golden_crosses = df[(df['short_ma'] > df['long_ma']) & (df['short_ma'].shift(1) <= df['long_ma'].shift(1))]
    death_crosses = df[(df['short_ma'] < df['long_ma']) & (df['short_ma'].shift(1) >= df['long_ma'].shift(1))]
    
    df['成交股數'] = df['成交股數'].str.replace(",","")
    df['成交金額'] = df['成交金額'].str.replace(",","")
    df['成交筆數'] = df['成交筆數'].str.replace(",","")

    # Plotting K-line and Price-Volume graphs
    # 繪製 Ｋ線
    fig = plt.figure(figsize=(24, 15))
    ax = fig.add_axes([0,0.2,1,0.5])
    ax2 = fig.add_axes([0,0,1,0.2],sharex = ax)

    ax.set_xticks(range(0, len(df['日期']), 20))
    ax.set_xticklabels(df['日期'][::20])
    
    plt.title(f"stock ID {sid}", fontsize=18)
    
    # 繪製 均線
    ax.plot(df['日期'], df['short_ma'].to_numpy(), label=f'{short_window}-Day MA')
    ax.plot(df['日期'], df['long_ma'].to_numpy(), label=f'{long_window}-Day MA')
    ax.scatter(golden_crosses['日期'], golden_crosses['short_ma'], color='gold', label='Golden Cross', marker='^')
    ax.scatter(death_crosses['日期'], death_crosses['short_ma'], color='black', label='Death Cross', marker='v')
    
    mpf.candlestick2_ochl(ax,
                          df['開盤價'].astype(float),
                          df['收盤價'].astype(float),
                          df['最高價'].astype(float),
                          df['最低價'].astype(float),
                          width=0.6, colorup='r', colordown='g', alpha=0.75)
    
    ax2.set_xticks(range(0, len(df['日期']), 20))
    ax2.set_xticklabels(df['日期'][::20])
    
    mpf.volume_overlay(ax2, 
                       df['開盤價'].astype(float),
                       df['收盤價'].astype(float),
                       df['成交股數'].astype(float),
                       colorup='r', colordown='g', width=0.5, alpha=0.8)
    
    plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 
    ax.legend()