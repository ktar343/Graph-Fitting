# -*- coding: utf-8 -*-
"""
Created on Thu Sep  10 2025
@author: ktar343
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# CSV 파일 불러오기 (첫 행에 헤더가 있다고 가정)
data = pd.read_csv("Case1.csv")

x = data["Temp"].values
y = data["Conversion"].values

# 간단한 선형 피팅 (y = a*x + b)
coeffs = np.polyfit(x, y, 1)    # 1차 다항식 피팅
fit_fn = np.poly1d(coeffs)      # 피팅 함수 생성

# 결과 출력
print("피팅 계수 (a, b):", coeffs)

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color="green", label="Conversion")     # 원래 데이터
##plt.plot(x, fit_fn(x), color="red", label="Fit")     # 피팅된 선
plt.xlabel("Temperature",fontsize=14, fontweight="bold")
plt.ylabel("Conversion",fontsize=14, fontweight="bold")
plt.title("Conversion according to Temperature",fontsize=18, fontweight="bold")
plt.legend()
plt.grid(True)
plt.show()
