## Overview

The optimization process involved filtering and analyzing different condition combinations based on their **Score %**, which represents the strength of the buy signal. The main objectives were:

- Identifying the most **frequent score range** where potential buy signals occur.
- Filtering out conditions containing **irrelevant or misleading signals** (e.g., "TREND", "STRONG_SIGNAL").
- Selecting conditions with the **highest number of fulfilled criteria**.
- Prioritizing conditions with **the highest Score %**.

## Filtering Conditions

A filtering mechanism was implemented to extract **the most relevant buy conditions** within a specific score range:

```python
import pandas as pd

df = pd.read_csv("condition_combinations_scores.csv")
```


```python
min_score = 30
max_score = 40
exclude_keywords = ["TREND", "STRONG_SIGNAL", "CYPHER_PATTERN"]

filtered_df = df[
    (df["Score %"] >= min_score) & 
    (df["Score %"] <= max_score) & 
    ~df["Sağlanan Şartlar"].str.contains('|'.join(exclude_keywords), na=False)
]
```

- **min_score / max_score**: Defines the **score range** for filtering.
- **exclude_keywords**: Removes conditions with **irrelevant indicators**.
- **filtered_df**: The resulting dataset containing the optimized buy conditions.

## Statistical Analysis

To determine the **most common score range**, a **histogram** was used to visualize the distribution of scores across all condition combinations:

```python
import matplotlib.pyplot as plt

plt.hist(df["Score %"], bins=20, edgecolor="black")
plt.xlabel("Score %")
plt.ylabel("Frequency")
plt.title("Distribution of Score % Across Conditions")
plt.show()
```

This allowed the identification of the **score range with the highest frequency**, helping refine the **buy strategy thresholds**.
