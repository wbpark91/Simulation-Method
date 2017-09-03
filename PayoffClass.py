#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:28:57 2017

@author: park-wanbae
"""
import numpy as np

def callPayoff(s, k):
    return np.where(s[-1] > k, s[-1] - k, 0)

def putPayoff(s, k):
    return np.where(s[-1] > k, 0, k - s[-1])

def callPayoff_DG(s, k):
    return np.where(s[-1] > k, 1, 0)

def putPayoff_DG(s, k):
    return np.where(s[-1] > k, 0, 1)

if __name__ == '__main__':
    path = np.exp(np.random.randn(1, 100)) * 100
    print(callPayoff_DG(path, 100))
    print(putPayoff_DG(path, 100))