#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Sentiv2.py
# @Author:      manunellutla
# @Time:        8/16/20 10:25 PM

"""
 This program takes a text input from web and does sentiment analysis on it.
 This is my version 2.0 attempt with multiple feature updates.
"""

# required packaes
import streamlit as st
import os
from algorepo import VaderSenti, txtblb

# global variables
builddir = os.path.dirname(os.path.abspath(__file__))
remote_css = 'https://fonts.googleapis.com/icon?family=Material+Icons'


def loadcss():
    """
    method to load required css
    :return: none
    """
    # Read in local css file
    with open(builddir + '/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # Remote Css link
    st.markdown(f'<link href="{remote_css}" rel="stylesheet">', unsafe_allow_html=True)


def loadui():
    # title
    st.title(f'Manu\'s Sentimental Analysis App')

    st.write('This is just a fun app to check the sentiment of a given text. You will be able to choose an algorithm')


def loadselect():
    opts = ('Vader Sentiment', 'TextBlob Sentiment', 'CNN Sentiment', 'RNN Sentiment', 'All')
    option_selected = st.selectbox("Select and algorithm below:", opts)
    return option_selected


def donlp(alg, txt):
    score = "Algorithm under construction"
    if alg == "Vader Sentiment":
        score = VaderSenti.sentiment_analyzer_polarity_scores(txt)
    elif alg == "TextBlob Sentiment":
        score = txtblb.formatted_textblob_score(txt)

    return score


def dispresults(alg, res):
    lines = '''
    <div class="result">
    <table>
     <tr><th>Algorithm</th><th>Score</th><th>Result></tr>
     <tr><td>%s</td><td>%s</td><td>%s</d>
    </table>   
    </div>
    ''' % (alg, res, "later")
    if res != "":
        st.markdown(lines, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write('Result in json format:')
        st.json(res)


if __name__ == '__main__':
    # st.write(os.path.dirname(os.path.abspath(__file__)))
    loadcss()
    loadui()
    selected = loadselect()

    input_text = st.text_area("Enter Text Below:", "Enter Text", height=40, max_chars=500)
    button_clicked = st.button("Check")


    if input_text != "Enter Text":
        result = donlp(selected, input_text)
        st.write('Results Below:')
        dispresults(selected, result)
        #st.write(f'Result :`%s`' % result)
        #st.json(result)
