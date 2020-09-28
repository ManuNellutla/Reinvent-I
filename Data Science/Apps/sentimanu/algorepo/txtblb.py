#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    txtblb.py
# @Author:      manunellutla
# @Time:        8/16/20 10:48 PM

"""
This program uses textblob based sentiment analysis
"""

from textblob import TextBlob


def sentiment_analyzer_polarity_scores(text: str):
    """

    :param text:
    :return:
    """
    score = TextBlob(text).sentiment.polarity
    #print(score)
    return score


def formatted_textblob_score(text: str):
    """

    :param text:
    :return:
    """
    score = sentiment_analyzer_polarity_scores(text)

    if score > 0.05:
        return {'Pos': score}
    elif score < -0.05:
        return {'Neg': score}
    else:
        return {'Neu': score}

if __name__ == '__main__':
    print(formatted_textblob_score("I am not too bad"))
    print(formatted_textblob_score("I am extremely happy"))
    print(formatted_textblob_score("I am very sad"))
    print(formatted_textblob_score("i am indian"))
