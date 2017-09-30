#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import pandas as pd
import matplotlib.pyplot as plt

result1 = pd.read_csv('result1.csv', header = None, index_col = 0)
result2 = pd.read_csv('result2.csv', header = None, index_col = 0)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection = '3d')
ax1.scatter(result1[1], result1[2], result1[3], c = 'k', marker = 'o')
plt.title("3-D Sobol Sequence with number 32")

result = []
scatternumber = [128, 512, 1024]
for num in scatternumber:
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.scatter(result2[1][:num], result2[2][:num], s = 7, c = 'k')
    plt.grid()
    plt.title("Sobol Sequence until sequence number %d" %num)
    plt.savefig("sobol_2d_%d" %num)
    result.append(fig2)