
"""
  !!! This code filters condition-score combinations within a user-defined score range while excluding specific keywords to refine trade signal analysis.
  """



import pandas as pd

def get_score_range():
    min_score = float(input("Minimum skor yüzdesini girin: "))
    max_score = float(input("Maksimum skor yüzdesini girin: "))
    return min_score, max_score

def filter_scores_by_range(min_score, max_score):
    try:
        df = pd.read_csv("condition_combinations_scores.csv")

        exclude_keywords = ["TREND", "STRONG_SIGNAL", "CYPHER_PATTERN"]
        filtered_df = df[
            (df["Score %"] >= min_score) & 
            (df["Score %"] <= max_score) & 
            ~df["Sağlanan Şartlar"].str.contains('|'.join(exclude_keywords), na=False)
        ]

        print("\nBu aralıktaki skorlar ve ilgili koşullar:")
        print(filtered_df.to_string(index=False))
    except Exception as e:
        print(f"Hata: {e}")

selection = input("1 - Skor aralığı + şart görmek\n2 - Koşulları tek tek seçerek devam etmek\nSeçiminiz (1/2): ")

if selection == "1":
    min_score, max_score = get_score_range()
    print(f"Skor aralığınız: {min_score} - {max_score}")
    filter_scores_by_range(min_score, max_score)
else:
    print("Bu seçenek henüz uygulanmadı.")
