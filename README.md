# 🏏 IPL Data Analysis (Python + Power BI Dashboard)

This project analyzes 1169 IPL matches to explore match trends, understand toss impact, and visualize team performance using Python and Power BI.

The project combines statistical analysis with an interactive dashboard to provide meaningful insights into IPL match outcomes.

---

# 📌 Project Overview

This project focuses on:

- Toss decision distribution
- Impact of toss on match results
- Defending vs chasing success comparison
- Season-wise match growth analysis
- Team performance analysis
- Venue and city analysis

---

# 📊 Power BI Dashboard

An interactive dashboard was built using Power BI to visualize IPL match insights.

## Dashboard Features

- Matches won by each team
- Toss decision distribution
- Matches per season trend
- Win type analysis (runs vs wickets)
- Top venues and cities
- Interactive season filter
- KPI card showing total matches

The dashboard allows users to explore trends and compare team performance dynamically.

---

# 📊 Dashboard Preview

![Dashboard Preview](dashboard.png)

---

# 📊 Dataset Information

- Total Matches: 1169  
- Total Columns: 23  
- No duplicate records found  
- Missing values handled appropriately  

## Key Columns Used

- season  
- toss_winner  
- toss_decision  
- match_winner  
- win_by_runs  
- win_by_wickets  
- player_of_match  
- venue  
- city  

---

# 🔍 Key Findings

- Toss winner won approximately 51.58% of matches  
- Teams chasing won 615 matches  
- Teams defending won 531 matches  
- Fielding is the preferred toss decision  
- IPL remains highly competitive despite toss influence  

---

# 📈 Visualizations Included (Python)

- Toss Decision Distribution  
- Matches per Season  
- Toss Impact Analysis  

---

# 🛠 Tools Used

- Python  
- Pandas  
- Matplotlib  
- Power BI  
- Data Visualization  

---

# ▶ How to Run the Python Analysis

Install required libraries:

```bash
pip install pandas matplotlib
```

Run the script:

```bash
python ipl_analysis.py
```

The script will:

- Load and clean dataset  
- Perform statistical analysis  
- Generate visualizations  
- Display insights  

---

# 📂 Project Structure

```
IPL-Data-Analysis/
│
├── IPL-Data-Analysis-Dashboard.pbix
├── dashboard.png
├── ipl_analysis.py
├── ipl_matches_data.csv
└── README.md
```

---

# 📌 Conclusion

The toss provides only a slight statistical advantage (~51%), indicating that overall team performance plays a larger role in match outcomes. Chasing appears slightly more favorable, but IPL remains competitively balanced.

The Power BI dashboard enhances this analysis by providing interactive visual insights and allows deeper exploration of team and match trends.

---

# 👨‍💻 Author

**Subhank Suyal**  
BSc Data Science Student  
Aspiring Data Analyst  

---

# ⭐ If you found this project useful, consider giving it a star!
