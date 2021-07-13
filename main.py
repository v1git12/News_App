import streamlit as st
from GoogleNews import GoogleNews as gn

st.title("News App by Vinayak")
News = gn()
News = gn(period='7d')
newsu = News.search(st.sidebar.text_input('Search Anything:'))
result = News.result()
st.subheader("Today's Headline")
for x in result:
    print("--"*60)
    print("Headline:",x['title'])
    print("Time:",x['date'])
    print("Description:",x['desc'])
    print("Source:",x['link'])
st.write(result)
