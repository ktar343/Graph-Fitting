# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 19:02:54 2025

@author: ktar343
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# CSV 파일 불러오기 
data = pd.read_csv("XRD.csv")

x = data["2theta"].values
y = data["intensity"].values

# 간단한 선형 피팅 (y = a*x + b)
coeffs = np.polyfit(x, y, 1)    # 1차 다항식 피팅
fit_fn = np.poly1d(coeffs)      # 피팅 함수 생성

# 결과 출력
print("피팅 계수 (a, b):", coeffs)

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(x, y, color="black", label="N_0.65 C_0.25 M_0.1")     # 원래 데이터
##plt.plot(x, fit_fn(x), color="red", label="Fit")     # 피팅된 선
plt.xlim(10, 90)
plt.xlabel("2theta",fontsize=14, fontweight="bold")
plt.ylabel("Intensity (A.U)",fontsize=14, fontweight="bold")
plt.title("XRD peak of NCM cathode",fontsize=18, fontweight="bold")
plt.legend()
plt.grid(True)
plt.show()