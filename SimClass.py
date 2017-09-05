#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:51:28 2017

@author: park-wanbae
"""
import numpy as np
import PayoffClass

class MarketVariable:
    def __init__(self, s, r, q, sigma):
        self.s = s
        self.r = r
        self.q = q
        self.sigma = sigma
        
class Option:
    def __init__(self, t, k, optionType):
        #Call: 1, Put: -1
        optType = {'Call':1, 'Put':-1}
        
        self.t = t
        self.k = k
        self.optionType = optType.optionType
    
    def npv(self):
        pass
    
    def setPricingMethod(self, prcmethod):
        method = {'Analytic':0, 'MonteCarlo':1, 'BinomialTree':2}
        self.pricingMethod = method[prcmethod]
        
    def setMarketVariable(self, mktVar):
        self.marketVariable = mktVar

class CallOption(Option):
    def __init__(self, t, k):
        self.t = t
        self.k = k
        self.optionType = 1
    
    def npv(self):
        if self.pricingMethod == 0:     #if Analytic
            pass
        elif self.pricingMethod == 1:   #if MCS
            payoff = calcPayoff_MCS(self.marketVariable, self.t, 100000, 100,
                                    self.k, PayoffClass.callPayoff)[-1]
            return np.exp(-self.marketVariable.r * self.t) * (payoff.mean())
        else:                           #Tree
            pass
    
def generatePath(mktVar, t, n, m):
    #n: sample 개수, m: path 개수
    dt = t / m
    path = np.zeros([m, n])
    path[0] = mktVar.s
    
    for i in range(len(path) - 1):
        z = np.random.randn(1, n)
        path[i+1] = path[i] * np.exp((mktVar.r - mktVar.q - 0.5 * mktVar.sigma ** 2) * dt +\
                                        mktVar.sigma * z * np.sqrt(dt))
    
    return path

def calcPayoff_MCS(mktVar, t, n, m, k, payoffFunc):
    path = generatePath(mktVar, t, n, m)
    return payoffFunc(path, k)

if __name__ == '__main__':
    mktVar = MarketVariable(250, 0.02, 0.01, 0.2)
    call = CallOption(0.1, 250)
    call.setMarketVariable(mktVar)
    call.setPricingMethod('MonteCarlo')
    print(call.npv())