# -----------------------------------------
# IPL Data Analysis Project
# Author: Subhank Suyal
# -----------------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load Dataset
# ---------------------------

df = pd.read_csv("ipl_matches_data.csv")

print("\nFirst 5 rows of dataset:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows count:")
print(df.duplicated().sum())

# ---------------------------
# Analysis 1: Toss Decision
# ---------------------------

plt.figure(figsize=(6,4))
df['toss_decision'].value_counts().plot(kind='bar')
plt.title("Toss Decision Distribution")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ---------------------------
# Analysis 2: Toss Impact
# ---------------------------

toss_win = df[df['toss_winner'] == df['match_winner']]
percentage = (len(toss_win) / len(df)) * 100

print("\nToss winner also won:", round(percentage, 2), "% matches")

# ---------------------------
# Analysis 3: Defending vs Chasing
# ---------------------------

runs_win = (df['win_by_runs'] > 0).sum()
wickets_win = (df['win_by_wickets'] > 0).sum()

print("\nWins by defending (runs):", runs_win)
print("Wins by chasing (wickets):", wickets_win)

# ---------------------------
# Analysis 4: Matches Per Season
# ---------------------------

plt.figure(figsize=(10,5))
season_counts = df['season'].value_counts().sort_index()

season_counts.plot(kind='bar')
plt.title("Number of Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ---------------------------
# Conclusion
# ---------------------------

print("\nProject Conclusion:")
print("- Toss gives slight advantage (~51%)")
print("- Chasing teams win slightly more matches")
print("- IPL remains competitive overall")