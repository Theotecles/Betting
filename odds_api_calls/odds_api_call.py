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

book_maker_data = data[0]['bookmakers']
print(book_maker_data[0])
print(book_maker_data[0]['key'])

for num in num_games:

	'''PULL THE START TIMES AND HOME AND AWAY TEAMS FOR EACH GAME'''
	start_times.append(data[num]['commence_time'])
	home_teams.append(data[num]['home_team'])
	away_teams.append(data[num]['away_team'])

	'''CREATE ANOTHER LOOP THAT PULLS ALL OF THE BOOKMAKER DATA FROM THE JSONS'''
	num_book_makers = []
	num_book_makers = range(len(data[num]['bookmakers']))
	book_maker_data = data[num]['bookmakers']

	for num1 in num_book_makers:
		book_maker_keys.append(book_maker_data[num1]['key'])
		book_maker_titles.append(book_maker_data[num1]['title'])
		last_updates.append(book_maker_data[num1]['last_update'])

print(start_times)
print(home_teams)
print(away_teams)
print(book_maker_keys)
print(book_maker_titles)
print(last_updates)
	