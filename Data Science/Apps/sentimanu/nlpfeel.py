#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    nlpfeel.py
# @Author:      manunellutla
# @Time:        8/16/20 9:14 AM

#using Streamlit io

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def sentiment_analyzer_scores(text):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(text)
    return score


local_css("/Users/manunellutla/PycharmProjects/Reinvent-I/Data Science/Apps/sentimanu/style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.title(f'Manu\'s Sentimental Analysis')
st.write('Using **Vader sentimental analysis algorithm** and **stremlitio** front end')
#selected = st.text_input("Enter Text Below:", "Enter Text")
input_text = st.text_area("Enter Text Below:", "Enter Text", height=40, max_chars=500)

score = sentiment_analyzer_scores(input_text)

button_clicked = st.button("Check")

if input_text != "Enter Text":
    st.write('Result: `%s`' % score)
    st.write('Overall:')
    if score['compound'] > 0.05 :
        st.markdown(f'<i class="material-icons yellow md-48">sentiment_very_satisfied</i>', unsafe_allow_html=True)
        st.balloons()
    elif score['compound'] < -0.05 :
        st.markdown(f'<i class="material-icons red md-48">sentiment_very_dissatisfied</i>', unsafe_allow_html=True)
    else:
        st.markdown(f'<i class="material-icons green md-48">sentiment_satisfied</i>', unsafe_allow_html=True)

