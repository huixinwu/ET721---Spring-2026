"""
student's full name
Nov 12, 2025
lab 12, APIs (Soccer Edition)
"""

import pandas as pd
print(pd.__version__)


# ------------------------------
# 3. External API data
# ------------------------------
# a. download match results CSV
import requests

url = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"

print("\nDownloading external data...")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete")
else:
    print("Download failed")

# b. load dataframe
matches = pd.read_csv(file_name)
print("\nMatch results:")
print(matches.head())

# c. filter Arsenal matches
arsenal_matches = matches[
    (matches["HomeTeam"] == "Arsenal") |
    (matches["AwayTeam"] == "Arsenal")
]

# home vs away
arsenal_home = arsenal_matches[arsenal_matches["HomeTeam"] == "Arsenal"]
arsenal_away = arsenal_matches[arsenal_matches["AwayTeam"] == "Arsenal"]

# d. calculate averages
home_avg_goals = arsenal_home["FTHG"].mean()
away_avg_goals = arsenal_away["FTAG"].mean()

print(f"\nArsenal home average goals: {home_avg_goals:.2f}")
print(f"Arsenal away average goals: {away_avg_goals:.2f}")

# ------------------------------
# 4. Visualization
# ------------------------------
import matplotlib.pyplot as plt

labels = ["Home Goals", "Away Goals"]
values = [home_avg_goals, away_avg_goals]

plt.figure(figsize=(6, 4))
plt.bar(labels, values)
plt.title("Arsenal Average Goals: Home vs Away")
plt.ylabel("Goals per Match")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

input("Press Enter to close...")