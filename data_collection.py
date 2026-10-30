from nba_api.stats.endpoints import leaguegamelog

# Download 2024-25 season
print("Downloading 2024-25 NBA data...")

games_2024 = leaguegamelog.LeagueGameLog(
    season="2024-25",
    season_type_all_star="Regular Season"
)

df_2024 = games_2024.get_data_frames()[0]

df_2024.to_excel("nba_2024_25_raw.xlsx", index=False)

print("2024-25 data saved!")
print("Number of rows:", len(df_2024))


# Download 2025-26 season
print("\nDownloading 2025-26 NBA data...")

games_2025 = leaguegamelog.LeagueGameLog(
    season="2025-26",
    season_type_all_star="Regular Season"
)

df_2025 = games_2025.get_data_frames()[0]

df_2025.to_excel("nba_2025_26_raw.xlsx", index=False)

print("2025-26 data saved!")
print("Number of rows:", len(df_2025))