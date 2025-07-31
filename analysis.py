import pandas as pd
import matplotlib.pyplot as plt

# --- Top Goal Scorers ---

player_goals = {
    "Emma Muchnick": 34,
    "Caroline Trinkaus": 32,
    "Emma Ward": 30,
    "Alexa Vogelman": 21,
    "Mileena Cotter": 21,
    "Gracie Britton": 20
}

plt.figure(figsize=(8, 5))
plt.bar(player_goals.keys(), player_goals.values(), color='skyblue')
plt.xticks(rotation=30, ha='right')
plt.title("Top Goal Scorers - SU Women's Lacrosse 2025")
plt.ylabel("Goals")
plt.tight_layout()
plt.savefig("figures/top_scorers.png")
plt.close()

# --- Win Distribution Pie Chart ---

win_distribution = {"Home Wins": 5, "Away Wins": 4, "Neutral Wins": 1, "Losses": 9}
plt.figure(figsize=(6, 6))
plt.pie(win_distribution.values(), labels=win_distribution.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Win Distribution by Location")
plt.savefig("figures/win_distribution.png")
plt.close()

# --- Game-by-Game Goals ---

# You can replace this with your own CSV file if needed
games = [
    "2/07", "2/15", "2/18", "2/22", "2/25", "3/01", "3/07", "3/10", "3/15",
    "3/19", "3/23", "3/29", "4/02", "4/05", "4/12", "4/17", "4/22", "5/09", "5/11"
]
goals_scored = [21, 15, 18, 8, 8, 8, 14, 13, 17, 14, 12, 13, 10, 18, 11, 2, 10, 15, 8]
goals_against = [9, 9, 10, 16, 12, 9, 13, 14, 11, 12, 11, 12, 13, 6, 14, 17, 15, 9, 9]

plt.figure(figsize=(10, 5))
plt.plot(games, goals_scored, marker='o', label='Goals Scored', color='green')
plt.plot(games, goals_against, marker='x', label='Goals Against', color='red')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.title("Game-by-Game Goals: Syracuse 2025")
plt.ylabel("Goals")
plt.tight_layout()
plt.savefig("figures/goals_per_game.png")
plt.close()