#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    HypothesisTesting.py
# @Author:      manunellutla
# @Time:        8/1/20 6:17 PM

import numpy as np
import scipy.stats as stats
import pandas as pd


def interpret_results(s, p, n1, n2):
    print(f"\nT-test results: \n Statistic (T-value) = {s} and P-value = {p}")
    # interpretting results:
    print("\nInterpretation of the Test: ")
    print(f"  {n1} has Lower mean than  {n2}" if s < 0 else f" {n1} mean is higher than {n2}")
    # Null hypothesis Ho is both means are same.
    alpha = 0.05
    print("  Ho is rejected" if p < alpha else "  Ho is kept (failed to reject)")


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
print(f" \nfull population mean is : {population_ages.mean()} \nsample population mean is = {sample_ages.mean()} ")

# ttest for 1 sample - A t-test is a type of inferential statistic used to determine if there is a significant
# difference between the means of two groups, which may be related in certain features
statistic, p = stats.ttest_1samp(a=sample_ages, popmean=population_ages.mean())
interpret_results(statistic, p, "Sample", "Population")

print("\n")
print('-' * 25)
print(".... 2 Sample T-Test .... ")
print('-' * 25)
np.random.seed(12)
Sample3_ages = stats.poisson.rvs(loc=18, mu=26, size=40)
Sample4_ages = stats.poisson.rvs(loc=18, mu=19, size=25)
sample2_ages = np.concatenate((Sample3_ages, Sample4_ages))
print(f" \nSample1 ages mean is : {population_ages.mean()} \nSample2 population mean is = {sample_ages.mean()} ")

statistic, p = stats.ttest_ind(a=sample_ages, b=sample2_ages, equal_var=True)
interpret_results(statistic, p, "Sample1", "Sample2")

print("\n")
print('-' * 25)
print(".... Paired Random Test .... ")
print('-' * 25)
np.random.seed(12)
before = stats.norm.rvs(scale=30, loc=250, size=100)
after = before + stats.norm.rvs(scale=5, loc=-1.25, size=100)
weight_df = pd.DataFrame({"weight_before": before,
                          "weight_after": after,
                          "weight_change": after - before})
print("\nPair-test results: \n")
print(weight_df.describe())

statistic, p = stats.ttest_rel(a=before, b=after)
interpret_results(statistic, p, "Before", "After")

print("\n")
print('-' * 25)
print(".... KS 2 sample test .... ")
print('-' * 25)

statistic, p = stats.ks_2samp(sample_ages, sample2_ages)
interpret_results(statistic, p, "Sample1", "Sample2")