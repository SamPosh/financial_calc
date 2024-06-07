from jugaad_data.nse import NSELive
import pandas as pd
import matplotlib.pyplot as plt

def _get_stock_live(nse_live,stock_name='ASHOKLEY'):
    q = nse_live.stock_quote(stock_name)
    # print(q['priceInfo'])
    qprice = q['priceInfo']
    data = {"price": qprice['lastPrice'] , 
            "52W_High": qprice['weekHighLow']['max'],
            "52W_Low": qprice['weekHighLow']['min'],
            "Today_High": qprice['intraDayHighLow']['max'],
            "Today_min": qprice['intraDayHighLow']['min'],
            "previousClose": qprice["previousClose"],
            "name": stock_name}
    return data

# Create the bar graph
def _plot_stocks(tickers, highs, lows, todays_prices):
    fig, ax = plt.subplots(figsize=(15, 8))

    bar_width = 0.2
    x = range(len(tickers))
# Plotting each bar
    high_bars = ax.bar([p - bar_width for p in x], highs, width=bar_width, label='52-week High', align='center')
    today_bars = ax.bar(x, todays_prices, width=bar_width, label="Today's Price", align='center')
    low_bars = ax.bar([p + bar_width for p in x], lows, width=bar_width, label='52-week Low', align='center')

# Adding labels and title
    ax.set_xticks(x)
    ax.set_xticklabels(tickers,rotation=45, ha='right')
    ax.set_xlabel('Stock Tickers')
    ax.set_ylabel('Price')
    ax.set_title('52-week High, Low, and Today\'s Price for Stocks')
    ax.legend()

# Annotate bars with values
    for bars in [high_bars, today_bars, low_bars]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=60)
            
    # plt.subplots_adjust(hspace=0.5)  # Increase the vertical space
# Adjust layout to prevent clipping of tick-labels
    plt.tight_layout()

# Display the plot
    plt.show()

def _get_stock_prices(stock_list):
    highs = []
    lows = []
    todays_prices = []
    stock_info = {}
    nse_live = NSELive()
    # Fetch data for each ticker
    for stock in stock_list:
        d= _get_stock_live(nse_live,stock)
        
        # 52-week high, low, and today's price
        high = d['52W_High']
        low = d['52W_Low']
        today = d['price']
        
        highs.append(high)
        lows.append(low)
        todays_prices.append(today)
    stock_info['52_week_high'] = highs
    stock_info['52_week_low'] = lows
    stock_info['today_price'] = todays_prices
    return stock_info

def plot_stocks(stock_list):
    stock_info = _get_stock_prices(stock_list)
    _plot_stocks(stock_list, stock_info['52_week_high'], stock_info['52_week_low'], stock_info['today_price'])
    return stock_info

stock_list = ['IDFCFIRSTB','ASHOKLEY','CPSEETF','TATASTEEL','PSUBNKBEES','IOC','ITBEES','TATAGOLD']
# Create lists to hold the data
stock_info = plot_stocks(stock_list)
# print(stock_info)
stock_list = ['TATAMOTORS','CANBK','EXIDEIND','ARE&M','ORIENTELEC']
stock_info = plot_stocks(stock_list)
