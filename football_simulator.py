import random
import requests
from bs4 import BeautifulSoup


def find_player_info():
    # Find the <td> element with class 'left' containing the player's name
    i = 0
    player = []
    for i in range(0, 3):
        player_name_tag = soup.find_all('td', class_='left')[i].find('a')
        player.append(player_name_tag.text.strip()
                      if player_name_tag else 'Unknown Player')
        i = +1
    player_rating_tag = soup.find('td', class_='selected c0')
    player_rating = player_rating_tag.text if player_rating_tag else 'Unknown Rating'
    player.append(int(player_rating))

    return player


# This function retrieves names and ratings of players playing as center-backs.
def find_player_info2():
    i = 3
    player = []
    for i in range(3, 6):
        player_name_tag = soup.find_all('td', class_='left')[i].find('a')
        player.append(player_name_tag.text.strip()
                      if player_name_tag else 'Unknown Player')
        i = +1
    player_rating_tag = soup.find_all('td', class_='selected c0')[1]
    player_rating = player_rating_tag.text if player_rating_tag else 'Unknown Rating'
    player.append(int(player_rating))

    return player


# Simulates a semifinal match between two countries and determines the finalist.
def semifinal(country1, country2, sum_country1, sum_country2):
    while True:
        if sum_country1 > sum_country2:
            final_team = country1
            print(f"{country1} beats {country2} and advances to final!")
            break
        elif sum_country1 < sum_country2:
            final_team = country2
            print(f"{country2} beats {country1} and advances to final!")
            break
        else:
            sum_country1 = round(
                sum_rating_by_country[country1]*random.uniform(0.9, 1.10))
            sum_country2 = round(
                sum_rating_by_country[country2]*random.uniform(0.9, 1.10))
    return final_team


# Simulates the final match and declares the winner based on their ratings.
def final(final_team1, final_team2, sum_finalist1, sum_finalist2):
    while True:
        if sum_finalist1 > sum_finalist2:
            print(f"\nWinner is {final_team1}!")
            break
        elif sum_finalist1 < sum_finalist2:
            print(f"\nWinner is {final_team2}!")
            break
        else:
            sum_finalist1 = round(
                sum_rating_by_country[final_team1] * random.uniform(0.85, 1.25))
            sum_finalist2 = round(
                sum_rating_by_country[final_team2] * random.uniform(0.85, 1.25))


countries = ['England', 'Spain', 'Netherlands', 'France']
players = []

for teams in countries:  # Iterates through countries to fetch web pages for player information from different national teams
    for i in [0, 1, 2, 3, 4, 5, 8, 9, 10, 12]:
        url = f"https://pesdb.net/efootball/?nationality={teams}&pos={i}"
        response = requests.get(url)
        if ((response.status_code == 200) and (i == 1)):
            soup = BeautifulSoup(response.content, 'html.parser')
            player_info = find_player_info()
            players.append(player_info)
            player_info = find_player_info2()
            players.append(player_info)

        elif response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # append the players info to new list
            player_info = find_player_info()
            players.append(player_info)

        else:
            print(f"Failed to retrieve the page. Status code: {
                response.status_code}")

players_by_country = {}

for player in players:
    name, team, country, rating = player
    if country not in players_by_country:
        players_by_country[country] = []
    players_by_country[country].append(player)


for country, players_list in players_by_country.items():
    print(f"Players from {country}:")
    for player in players_list:
        print(player)
    print()

sum_rating_by_country = {}

# Calculates the total player ratings for each country based on fetched data.
for country, players_list in players_by_country.items():
    sum_rating = sum(player[3] for player in players_list)
    sum_rating_by_country[country] = sum_rating

# SHows the total player ratings for each country.
for country, summary in sum_rating_by_country.items():
    print(f"{country}: {summary}")

# Generates random countries for the semifinal matches.
random_country = random.sample(list(sum_rating_by_country.keys()), 4)
country1, country2, country3, country4 = random_country


sum_country1 = round(
    sum_rating_by_country[country1]*random.uniform(0.9, 1.10))
sum_country2 = round(
    sum_rating_by_country[country2]*random.uniform(0.9, 1.10))
sum_country3 = round(
    sum_rating_by_country[country3]*random.uniform(0.9, 1.10))
sum_country4 = round(
    sum_rating_by_country[country4]*random.uniform(0.9, 1.10))
# show the total player ratings for each country after modifying them.
print(f"\nCountry 1: {country1} - Sum rating after modifying: {sum_country1}")
print(f"Country 2: {country2} - Sum rating after modifying: {sum_country2}")
print(f"Country 3: {country3} - Sum rating after modifying: {sum_country3}")
print(f"Country 4: {country4} - Sum rating after modifying: {sum_country4}")

print(f"\n1. Semifinal: {country1} vs {country2}")
final_team1 = semifinal(country1, country2, sum_country1, sum_country2)
print(f"\n2. Semifinal: {country1} vs {country2}")
final_team2 = semifinal(country3, country4, sum_country3, sum_country4)

sum_finalist1 = round(
    sum_rating_by_country[final_team1] * random.uniform(0.85, 1.05))
sum_finalist2 = round(
    sum_rating_by_country[final_team2] * random.uniform(0.85, 1.05))

print(f"\nFinal: {final_team1} vs {final_team2}")
print(f"{final_team1} - Sum rating after another modifying: {sum_finalist1}")
print(f"{final_team2} - Sum rating after another modifying: {sum_finalist2}")

final(final_team1, final_team2, sum_finalist1, sum_finalist2)
