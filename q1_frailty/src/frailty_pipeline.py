import pandas as pd

# INGEST stage
df = pd.read_csv("../data/frailty_raw.csv")

print(df)

# unit standardization
df["Height_m"] = df["Height_in"] * 0.0254
df["Weight_kg"] = df["Weight_lb"] * 0.45359237

print(df.head())

# FEATURE ENGINEERING
# BMI
df["BMI"] = (df["Weight_kg"] / (df["Height_m"] ** 2)).round(2)
# AgeGroup
def age_group(age):
    if age < 30:
        return "<30"
    elif 30 <= age <= 45:
        return "30-45"
    elif 46 <= age <= 60:
        return "46-60"
    else:
        return ">60"

df["AgeGroup"] = df["Age_yr"].apply(age_group)

print(df.head())

# ENCODING
# frailty binary
df["Frailty_binary"] = df["Frailty"].map({"Y": 1, "N": 0}).astype("int8")

age_dummies = pd.get_dummies(df["AgeGroup"], prefix="AgeGroup")

df = pd.concat([df, age_dummies], axis=1)

print(df.head())

# ANALYZE & REPORT
numeric_cols = df.select_dtypes(include="number")

summary = numeric_cols.agg(["mean", "median", "std"])

# Grip ↔ Frailty correlation
corr_value = df["Grip_kg"].corr(df["Frailty_binary"])

report_path = "../reports/findings.md"
with open(report_path, "w") as f:
    f.write("# Q1 Findings\n\n")
    f.write("## Summary statistics (mean, median, std) for numeric columns\n")
    f.write(summary.to_markdown())
    f.write("\n\n")
    f.write(f"## Correlation between Grip strength and Frailty_binary: {corr_value:.2f}\n")

print("EDA report saved to:", report_path)