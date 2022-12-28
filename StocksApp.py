import yfinance as yf
import streamlit as st
import datetime
import pandas as pd


st.set_page_config(page_title="Stocks",page_icon="📈")
st.title('Welcome to Stock Comparer!')


with st.container():
    st.header('How to Use ?')
    st.write("Choose your preferred Input Method by selecting the appropriate radio button. Choose 'Select' to choose "
             "from a pre-made list, or choose 'Type' to enter the name of any stock. The program will display the "
             "current Stock Price along with a delta comparing Yesterday's Price. Alter the slider to change the "
             "History Length of the Comparison Graph.")

with st.container():
    st.write('---')
    st.header('Select from Options below')
    selection = st.radio(label='Input Method', options=['Select', 'Type'])
    if selection == 'Type':
        tickername1 = st.text_input('Enter Name of Stock 1', value='AAPL')
        tickername1 = tickername1.strip().upper()
        test1 = tickername1
        tickername2 = st.text_input('Enter Name of Stock 2', value='AMZN')
        tickername2 = tickername2.strip().upper()
        test2 = tickername2
        tickername3 = st.text_input('Enter Name of Stock 3', value='GOOGL')
        tickername3 = tickername3.strip().upper()
        test3 = tickername3

    else:
        tickername1 = st.selectbox('Select Stock 1',
                                   ['AAPL', 'AMZN', 'TSLA', 'META', 'MSFT', 'NVDA', 'AMD', 'INTC', 'GOOGL'])
        tickername2 = st.selectbox('Select Stock 2',
                                   ['AMZN', 'TSLA', 'AAPL', 'GOOGL', 'META', 'MSFT', 'NVDA', 'AMD', 'INTC'])
        tickername3 = st.selectbox('Select Stock 3',
                                   ['GOOGL', 'AAPL', 'AMZN', 'TSLA', 'META', 'MSFT', 'NVDA', 'AMD', 'INTC'])

    back = st.select_slider('Select History Length for Graph (in years)', options=[1,2,3,4,5,6,7,8,9,10,11,12], value=6)


with st.container():
    today = datetime.date.today()
    d = today.day
    m = today.month
    y = today.year

    tickerdata1 = yf.Ticker(tickername1)
    todaytickerDF1 = tickerdata1.history(period='1min')
    try:
        todayprice1 = round(todaytickerDF1['Close'][0], 2)
    except(IndexError):
        st.error(f'{test1} does not exist, defaulting to AAPL !')
        tickername1 = 'AAPL'
        tickerdata1 = yf.Ticker(tickername1)
        todaytickerDF1 = tickerdata1.history(period='1min')
    else:
        pass
    todayprice1 = round(todaytickerDF1['Close'][0],2)
    todaytickerDF10 = tickerdata1.history(period='1d',start=f"{y}-{m}-{d-2}", end=f"{y}-{m}-{d-1}")
    try:
        todayprice10 = round(todaytickerDF10['Close'][0], 2)
    except IndexError:
        todayprice10 = todayprice1
    else:
        todayprice10 = round(todaytickerDF10['Close'][0], 2)
    tickerDF1 = tickerdata1.history(period='1d', start=f"{y - back}-{m}-{d}", end=f"{y}-{m}-{d}")


    tickerdata2 = yf.Ticker(tickername2)
    todaytickerDF2 = tickerdata2.history(period='1min')
    try:
        todayprice2 = round(todaytickerDF2['Close'][0], 2)
    except(IndexError):
        st.error(f'{test2} does not exist, defaulting to AMZN !')
        tickername2 = 'AMZN'
        tickerdata2 = yf.Ticker(tickername2)
        todaytickerDF2 = tickerdata2.history(period='1min')
    else:
        pass
    todayprice2 = round(todaytickerDF2['Close'][0],2)
    todaytickerDF20 = tickerdata2.history(period='1d',start=f"{y}-{m}-{d-2}", end=f"{y}-{m}-{d-1}")
    try:
        todayprice20 = round(todaytickerDF20['Close'][0], 2)
    except IndexError:
        todayprice20 = todayprice2
    else:
        todayprice20 = round(todaytickerDF20['Close'][0], 2)
    tickerDF2 = tickerdata2.history(period='1d', start=f"{y - back}-{m}-{d}", end=f"{y}-{m}-{d}")


    tickerdata3 = yf.Ticker(tickername3)
    todaytickerDF3 = tickerdata3.history(period='1min')
    try:
        todayprice3 = round(todaytickerDF3['Close'][0], 2)
    except(IndexError):
        st.error(f'{test3} does not exist, defaulting to GGOGL !')
        tickername3 = 'GOOGL'
        tickerdata3 = yf.Ticker(tickername3)
        todaytickerDF3 = tickerdata3.history(period='1min')
    else:
        pass
    todayprice3 = round(todaytickerDF3['Close'][0],2)
    todaytickerDF30 = tickerdata3.history(period='1d',start=f"{y}-{m}-{d-2}", end=f"{y}-{m}-{d-1}")
    try:
        todayprice30 = round(todaytickerDF30['Close'][0], 2)
    except IndexError:
        todayprice30 = todayprice3
    else:
        todayprice30 = round(todaytickerDF30['Close'][0], 2)
    tickerDF3 = tickerdata3.history(period='1d', start=f"{y - back}-{m}-{d}", end=f"{y}-{m}-{d}")


    data = [tickerDF1.Close, tickerDF2.Close, tickerDF3.Close]
    data = pd.DataFrame(data)
    data = data.transpose()
    data.columns = [f'{tickername1}', f'{tickername2} ', f'{tickername3}  ']


col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label=f'{tickername1}', value=f"{todayprice1} USD", delta=f'{round(todayprice1-todayprice10,2)} USD')
with col2:
    st.metric(label=f'{tickername2}', value=f"{todayprice2} USD", delta=f'{round(todayprice2-todayprice20,2)} USD')
with col3:
    st.metric(label=f'{tickername3}', value=f"{todayprice3} USD", delta=f'{round(todayprice3-todayprice30,2)} USD')

with st.container():
    st.line_chart(data=data)


with st.container():
    st.caption("Made by Rohit")
    st.markdown("[![Foo](https://cdn-icons-png.flaticon.com/24/25/25231.png)](https://github.com/ItsNotRohit02)")



