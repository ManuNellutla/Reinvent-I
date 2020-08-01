#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    HypothesisTesting.py
# @Author:      manunellutla
# @Time:        8/1/20 6:17 PM

import numpy as np
import scipy.stats as stats

np.random.seed(6)

# generate
# poisson distributed random variates.
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))
Sample1_ages1 = stats.poisson.rvs(loc=18, mu=30, size=30)
Sample2_ages2 = stats.poisson.rvs(loc=18, mu=10, size=20)

sample_ages = np.concatenate((Sample1_ages1, Sample2_ages2))
print('-' * 25)
print(".... 1 Sample T-Test .... ")
print('-' * 25)
print(f" \nfull population mean is : {population_ages.mean()} \nsample populaiton mean is = {sample_ages.mean()} ")

# ttest for 1 sample - A t-test is a type of inferential statistic used to determine if there is a significant
# difference between the means of two groups, which may be related in certain features
statistic, p = stats.ttest_1samp(a=sample_ages, popmean=population_ages.mean())
print(f"\nT-test results: \n Statistic (T-value) = {statistic} and P-value = {p}")

# interpretting results:
print("\nInterpretation of the Test: ")
print("  Sample has Lower mean than  population" if statistic < 0 else "  Sample mean is higher than population")
# Null hypothesis Ho is both means are same.
alpha = 0.05
print("  Ho is rejected" if p < alpha else "  Ho is kept (failed to reject)")


