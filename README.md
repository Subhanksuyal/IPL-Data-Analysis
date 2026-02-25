🏏 IPL Data Analysis using Python

This project analyzes 1169 IPL matches to explore match trends and understand whether the toss significantly impacts match outcomes.

The analysis is performed using Python, Pandas, and Matplotlib.

📌 Project Overview

This project focuses on:

Toss decision distribution

Impact of toss on match results

Defending vs chasing success comparison

Season-wise match growth analysis

📊 Dataset Information

Total Matches: 1169

Total Columns: 23

No duplicate records found

Logical missing values handled appropriately

Key Columns Used:

season

toss_winner

toss_decision

match_winner

win_by_runs

win_by_wickets

player_of_match

venue and city

🔍 Key Findings

Toss winner won approximately 51.58% of matches

Teams chasing won 615 matches

Teams defending won 531 matches

Fielding is the preferred toss decision

IPL remains highly competitive despite toss influence

📈 Visualizations Included

Toss Decision Distribution (Bar Chart)

Number of Matches Per Season (Bar Chart)

🛠 Tools Used

Python

Pandas

Matplotlib

📂 Project Structure
IPL-Data-Analysis/
│
├── ipl_analysis.py
├── ipl_matches_data.csv
└── README.md
▶ How to Run the Project

Install required libraries:

pip install pandas matplotlib

Run the script:

python ipl_analysis.py

The script will:

Display dataset information

Perform statistical analysis

Generate visualizations

Print final conclusions

📌 Conclusion

The toss provides only a slight statistical advantage (~51%), indicating that overall team performance plays a larger role in match outcomes. Chasing appears slightly more favorable, but IPL remains competitively balanced.

👨‍💻 Author

Subhank Suyal
BSc Data Science Student
