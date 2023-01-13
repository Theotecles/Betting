#IMPORT NEEDED PACKAGES
import requests
from datetime import datetime
import pyodbc
import pandas as pd

# PULL THE ODDS DATA USING THE ODDS API
url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=12e82279ea3ede7d35d97bfbc173feca&regions=us&markets=h2h,spreads&oddsFormat=american'
r = requests.get(url)
data = r.json()

# WRITE A LOOP THAT WILL PULL THE NECESSARY DATA FROM THE ODDS
# CREATE AN EMPTY LIST
num_games = []
num_games = range(len(data))

start_times = []
home_teams = []
away_teams = []
book_maker_keys = []
book_maker_titles = []
last_updates = []
betting_keys = []
h2h_outcomes = []
spread_outcomes = []

book_maker_data = data[0]['bookmakers']
odds_data = book_maker_data[0]['markets']
print(odds_data[1])
print(len(odds_data))

for num in num_games:

	'''PULL THE START TIMES AND HOME AND AWAY TEAMS FOR EACH GAME'''
	start_time = data[num]['commence_time']
	home_team = data[num]['home_team']
	away_team = data[num]['away_team']

	'''CREATE ANOTHER LOOP THAT PULLS ALL OF THE BOOKMAKER DATA FROM THE JSONS'''
	num_book_makers = []
	num_book_makers = range(len(data[num]['bookmakers']))
	book_maker_data = data[num]['bookmakers']

	for num1 in num_book_makers:
		
		start_times.append(start_time)
		home_teams.append(home_team)
		away_teams.append(away_team)
		book_maker_keys.append(book_maker_data[num1]['key'])
		book_maker_titles.append(book_maker_data[num1]['title'])
		last_updates.append(book_maker_data[num1]['last_update'])
		odds = book_maker_data[0]['markets']

		for num2 in num_betkeys
		betting_keys.append(odds[0]['key'])
		betting_keys.append(odds[1]['key'])
		h2h_outcomes.append(odds[0]['outcomes'])
		spread_outcomes.append(odds[1]['outcomes'])



print(len(start_times))
print(len(home_teams))
print(len(away_teams))
print(len(book_maker_keys))
print(len(book_maker_titles))
print(len(last_updates))
print(len(betting_keys))
print(len(h2h_outcomes))
print(len(spread_outcomes))
