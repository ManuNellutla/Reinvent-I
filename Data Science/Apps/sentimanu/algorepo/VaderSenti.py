#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    VaderSenti.py
# @Author:      manunellutla
# @Time:        8/16/20 10:30 PM

"""
This simple program calls vader analyzer and returns the score
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_analyzer_polarity_scores(text: str) -> dict:
    """
     This method initialises lexican based vader sentiment analyzer gets polarity scores.
    :param text: 500 or less words of text to be evaluated.
    :return: dictionary of scores
    """
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(text)
    return score

