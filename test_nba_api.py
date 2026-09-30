from nba_api.stats.endpoints import leaguegamelog

print("Downloading 2025-26 NBA data...")

games = leaguegamelog.LeagueGameLog(
    season="2025-26",
    season_type_all_star="Regular Season"
)

df = games.get_data_frames()[0]

print("\nNumber of rows:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 10 rows:")
print(df.head(10))

# Save as Excel
df.to_excel("nba_2025_26_raw.xlsx", index=False)

print("\nExcel file saved successfully!")