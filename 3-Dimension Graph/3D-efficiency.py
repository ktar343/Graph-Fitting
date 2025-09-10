import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

path = "3di.csv"  # 파일명이 다르면 바꿔주세요
df_raw = pd.read_csv(path)

# --- 1) 컬럼 자동 매핑 (대소문자 무시, 유사명 허용) ---
cols = {c.lower().strip(): c for c in df_raw.columns}

def pick(*cands):
    for c in cands:
        if c in cols:
            return cols[c]
    return None

col_T = pick("temperature","temp","t")
col_P = pick("pressure","p")
col_M = pick("flow","moles","mol","n","flowrate","flow_rate","flow rate")
col_E = pick("efficiency","eff","g","z","value","c")

print("Columns in CSV:", list(df_raw.columns))
print("Guessed mapping:", {"T": col_T, "P": col_P, "M": col_M, "E": col_E})

# --- 2) 값에서 단위/문자 제거 후 숫자화 ---
def to_num_clean(s):
    # 문자열이면 단위/기호 제거 ("300 K", "1 bar", "85%") → "300", "1", "85"
    if pd.isna(s):
        return np.nan
    if isinstance(s, str):
        s2 = re.sub(r"[^\d\.\-eE+]", "", s)  # 숫자, 부호, 소수점, 지수표기만 남김
        return pd.to_numeric(s2, errors="coerce")
    return pd.to_numeric(s, errors="coerce")

need = [col_T, col_P, col_M, col_E]
if any(v is None for v in need):
    raise ValueError("필수 컬럼명을 찾지 못했습니다. CSV의 실제 헤더명을 확인해주세요.")

df = df_raw.copy()
for c in need:
    df[c] = df[c].map(to_num_clean)

d = df[[col_T, col_P, col_M, col_E]].dropna()
print("Rows after cleaning & dropna:", len(d), "/", len(df))
print(d.describe())

# --- 3) 3D 산점도 ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(d[col_T], d[col_P], d[col_M], c=d[col_E], cmap="viridis", s=40)

ax.set_xlabel(col_T, fontsize=12, fontweight="bold")
ax.set_ylabel(col_P, fontsize=12, fontweight="bold")
ax.set_zlabel(col_M, fontsize=12, fontweight="bold")
ax.set_title("Efficiency practice", fontsize=16, fontweight="bold")

cbar = plt.colorbar(sc, ax=ax)
cbar.set_label(col_E)

plt.tight_layout()
plt.show()
