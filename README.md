## Overview

The optimization process involved filtering and analyzing different condition combinations based on their **Score %**, which represents the strength of the buy signal. The main objectives were:

- Identifying the most **frequent score range** where potential buy signals occur.
- Filtering out conditions containing **irrelevant or misleading signals** (e.g., "TREND", "STRONG_SIGNAL").
- Selecting conditions with the **highest number of fulfilled criteria**.
- Prioritizing conditions with **the highest Score %**.

## Creating Conditions csv
```python
weights = [
    1.4,  # RSI_DIVERGENCE_S
    0.7,  # MACD_VOLUME_S
    1.2,  # EMA_CONDITION_S
    0.4,  # NEAR_LOWER_CHANNEL_S
    1.0,  # FIBONACCI_SUPPORT_S
    0.4,  # PRICE_PREDICTION_TAHMIN_S
    1.4,  # SUPER_TREND_S
    0.3,  # FORECAST_S
    1.6,  # STRONG_SIGNAL_S
    1.2,  # TREND_KIRILDI_4H_S
    1.5   # CYPHER_PATTERN_WEIGHT
]
condition_names = [
    "RSI_DIVERGENCE",
    "MACD_VOLUME",
    "EMA_CONDITION",
    "NEAR_LOWER_CHANNEL",
    "FIBONACCI_SUPPORT",
    "PRICE_PREDICTION_TAHMIN",
    "SUPER_TREND",
    "FORECAST",
    "STRONG_SIGNAL",
    "TREND_KIRILDI_4H",
    "CYPHER_PATTERN"
]

detailed_results = []

for r in range(1, len(weights) + 1):
    for combo in combinations(enumerate(weights), r):
        selected_indices = [index for index, _ in combo]  # Seçilen şartların indeksleri
        selected_weights = [w for _, w in combo]  # Seçilen ağırlıklar
        
        weighted_score = sum(selected_weights)
        
        # Eğer 9. şart (STRONG_SIGNAL) sağlanıyorsa +2 ekleniyor
        if 8 in selected_indices:
            weighted_score += 2.0

        score_percentage = (weighted_score / max_possible_score) * 100

        # Şartların isimlerini alalım
        selected_condition_names = [condition_names[i] for i in selected_indices]

        # Sonucu listeye ekleyelim
        detailed_results.append({
            "Sağlanan Şartlar": ", ".join(selected_condition_names),
            "Score %": round(score_percentage, 2)
        })

df_detailed_results = pd.DataFrame(detailed_results).sort_values(by="Score %", ascending=False).reset_index(drop=True)

csv_filename = "condition_combinations_scores.csv"
df_detailed_results.to_csv(csv_filename, index=False)



```


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
