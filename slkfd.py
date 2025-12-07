import pandas as pd

# Veriyi yükle
df = pd.read_parquet("data_with_all_columns.parquet")

# Sadece popularity_score_old sütununu al
df_popularity = df[['popularity_score_old']].copy()

# Yeni dosya olarak kaydet
df_popularity.to_parquet("popularity_score_old.parquet", index=False)

# Kontrol
print(" Yeni dosya oluşturuldu: popularity_score_old.parquet")
print(f"Shape: {df_popularity.shape}")
print(f"\nİlk 5 satır:")
print(df_popularity.head())