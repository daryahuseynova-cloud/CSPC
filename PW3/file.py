import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
 

if not os.path.exists("heart.csv"):
    cols = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
            "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
    raw = pd.read_csv("processed_cleveland.data", header=None,
                      names=cols, na_values="?")
    raw["target"] = (raw["target"] > 0).astype(int)  # 0 = healthy, 1 = disease
    raw.to_csv("heart.csv", index=False)

#--------Task 1 
df = pd.read_csv("heart.csv")
 
print("Shape (rows, columns):", df.shape)
print("\nFirst rows:")
print(df.head())
 
#Isolate the four continuous columns
cols = ["age", "chol", "trestbps", "thalach"]
continuous = df[cols]
print("\nContinuous columns:")
print(continuous.head())
print("\nSummary statistics:")
print(continuous.describe())

#----------Task 2

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

ax1.hist(df["age"], bins=25);       ax1.set_title("age")
ax2.hist(df["chol"], bins=25);      ax2.set_title("chol")
ax3.hist(df["trestbps"], bins=25);  ax3.set_title("trestbps")
ax4.hist(df["thalach"], bins=25);   ax4.set_title("thalach")

plt.tight_layout()
plt.savefig("PW3_histograms.png")
plt.show()

#----------Task3

#A)

fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, figsize=(10, 8))

stats.probplot(df["age"], dist="norm", plot=ax5);      ax5.set_title("Q-Q plot: age")
stats.probplot(df["chol"], dist="norm", plot=ax6);     ax6.set_title("Q-Q plot: chol")
stats.probplot(df["trestbps"], dist="norm", plot=ax7); ax7.set_title("Q-Q plot: trestbps")
stats.probplot(df["thalach"], dist="norm", plot=ax8);  ax8.set_title("Q-Q plot: thalach")

plt.tight_layout()
plt.savefig("PW3_qqplots.png")
plt.show()

#B)
for c in cols:
    W, p = stats.shapiro(df[c])
    if p < 0.05:
        verdict = "NOT normal"  
    else:
        verdict = "normal OK"
    print(f"{c:10s} W = {W:.4f}  p = {p:.4g}  -> {verdict}")