import pandas as pd
import os

# INGEST STAGE

data_path = "../data/StudentsPerformance.csv"
df = pd.read_csv(data_path)

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# PREPROCESS STAGE

df = df.dropna()

# overall average score
df["overall_avg"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

print("\nAfter preprocessing:")
print(df.head())

# ANALYSIS STAGE

import matplotlib.pyplot as plt

# V1 — Gender boxplots (math vs reading)

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Separate data by gender
female = df[df["gender"] == "female"]
male = df[df["gender"] == "male"]

# Prepare data for boxplot
data = [
    female["math score"],
    male["math score"],
    female["reading score"],
    male["reading score"]
]

# Create boxplot
ax.boxplot(data)

# Set x-axis labels
ax.set_xticklabels([
    "Female Math",
    "Male Math",
    "Female Reading",
    "Male Reading"
])

ax.set_title("Math and Reading Scores by Gender")
ax.set_ylabel("Score")

plt.xticks(rotation=30)
plt.tight_layout()

# Save figure
plt.savefig("../reports/V1_gender_boxplot.png")

plt.close()

# V2 — Test preparation impact on math score

# Calculate mean math score by test preparation course
math_means = df.groupby("test preparation course")["math score"].mean()

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Create bar chart
math_means.plot(kind="bar", ax=ax)

plt.title("Mean Math Score by Test Preparation Course")
plt.xlabel("Test Preparation Course")
plt.ylabel("Mean Math Score")

plt.xticks(rotation=0)
plt.tight_layout()

# Save figure
plt.savefig("../reports/V2_testprep_math.png")

plt.close()

# V3 — Lunch type and average overall performance

# Calculate mean overall average by lunch type
lunch_means = df.groupby("lunch")["overall_avg"].mean()

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Create bar chart
lunch_means.plot(kind="bar", ax=ax)

plt.title("Mean Overall Score by Lunch Type")
plt.xlabel("Lunch Type")
plt.ylabel("Mean Overall Score")

plt.xticks(rotation=0)
plt.tight_layout()

# Save figure
plt.savefig("../reports/V3_lunch_overall.png")

plt.close()

# V4 — Correlation heatmap for three subjects

import numpy as np

# Select subject scores
subjects = df[["math score", "reading score", "writing score"]]

# Compute correlation matrix
corr_matrix = subjects.corr()

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Create heatmap
cax = ax.imshow(corr_matrix, cmap="coolwarm")

# Add color bar
plt.colorbar(cax)

# Set axis ticks
ax.set_xticks(np.arange(len(corr_matrix.columns)))
ax.set_yticks(np.arange(len(corr_matrix.columns)))

ax.set_xticklabels(corr_matrix.columns)
ax.set_yticklabels(corr_matrix.columns)

# Rotate x labels
plt.xticks(rotation=45)

# Annotate correlation values
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        ax.text(j, i,
                f"{corr_matrix.iloc[i, j]:.2f}",
                ha="center",
                va="center",
                color="black")

plt.title("Correlation Heatmap of Subject Scores")
plt.tight_layout()

# Save figure
plt.savefig("../reports/V4_correlation_heatmap.png")

plt.close()

# V5 — Math vs Reading with trend lines by test preparation

# Separate groups
completed = df[df["test preparation course"] == "completed"]
none = df[df["test preparation course"] == "none"]

# Count sample sizes
n_completed = len(completed)
n_none = len(none)

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Scatter points
ax.scatter(completed["reading score"],
           completed["math score"],
           alpha=0.6,
           label=f"Completed (n={n_completed})")

ax.scatter(none["reading score"],
           none["math score"],
           alpha=0.6,
           label=f"None (n={n_none})")

# Fit regression lines
coef_completed = np.polyfit(completed["reading score"],
                            completed["math score"], 1)

coef_none = np.polyfit(none["reading score"],
                       none["math score"], 1)

x_vals = np.linspace(df["reading score"].min(),
                     df["reading score"].max(), 100)

y_completed = coef_completed[0] * x_vals + coef_completed[1]
y_none = coef_none[0] * x_vals + coef_none[1]

# Plot regression lines
ax.plot(x_vals, y_completed)
ax.plot(x_vals, y_none)

plt.title("Math vs Reading by Test Preparation Course")
plt.xlabel("Reading Score")
plt.ylabel("Math Score")
plt.legend()

plt.tight_layout()

# Save figure
plt.savefig("../reports/V5_math_reading_scatter.png")

plt.close()