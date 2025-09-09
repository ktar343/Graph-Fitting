# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 2025

G(T,P,n) 자유에너지를 임의 난수 데이터로 3D 그래프 표시
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D 그리기 위해 필요

# ------------------------------
# 1. 난수 데이터 생성
# ------------------------------
num_points = 100

T = np.random.uniform(300, 1000, num_points)   # 온도(K)
P = np.random.uniform(1, 100, num_points)      # 압력(bar)
n = np.random.uniform(0.1, 10, num_points)     # 몰수(mol)

# 예시로 G 값을 임의 함수로 정의 (실제 계산식 아님)
# G = a*T + b*P - c*n + 임의 노이즈
G = 5*T + 2*P - 10*n + np.random.normal(0, 50, num_points)

# ------------------------------
# 2. 3D 그래프 그리기
# ------------------------------
fig = plt.figure(figsize=(10, 7)) #그래프의 크기를 정의하는 것
ax = fig.add_subplot(111, projection='3d')

# 3D 산점도
sc = ax.scatter(T, P, n, c=G, cmap='plasma', s=50)
   # 그래프의 색깔을 변화 --> cmap='viridis, plasma, 
# 축 라벨
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Pressure (bar)')
ax.set_zlabel('Moles (mol)')
ax.set_title('G(T, P, n) - Random Data Example')

# 컬러바 추가 (G 값 시각화)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Gibbs Free Energy (kJ)')

plt.show()
