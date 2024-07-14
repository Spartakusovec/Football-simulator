import random
import requests
from bs4 import BeautifulSoup

POSITION_MAP = {
    0: "GK", 1: "CB", 2: "LB", 3: "RB", 4: "DMF",
    5: "CMF", 8: "AMF", 9: "LWF", 10: "RWF", 12: "CF"
}


def assign_position(i):
    return POSITION_MAP.get(i, "Unknown Position")


def find_player_info(start_index, end_index, position):
    player = []
    player.append(assign_position(position))
    for i in range(start_index, end_index):
        player_name_tag = soup.find_all('td', class_='left')[i].find('a')
        player.append(player_name_tag.text.strip()
                      if player_name_tag else 'Unknown Player')
    if start_index > 2:
        player_rating_tag = soup.find_all('td', class_='selected c0')[1]
    else:
        player_rating_tag = soup.find('td', class_='selected c0')
    player_rating = player_rating_tag.text if player_rating_tag else 'Unknown Rating'
    player.append(int(player_rating) if player_rating.isdigit() else 0)
    return player


def penalties(country1, country2, score1, score2):

    for i in range(5):
        print(f"\n{i+1} round of penalty shootout")
        if random.random() > 0.3:
            print(f"{country1} scores a penalty!")
            score1 += 1
        else:
            # print(f"{country1} misses the penalty!")
            pass

        if random.random() > 0.3:
            print(f"{country2} scores a penalty!")
            score2 += 1
        else:
            # print(f"{country2} misses the penalty!")
            pass

        if score1 > score2 + (4 - i):
            print(f"\n{country1} wins the match on penalties!")
            print(f"and the score is {score1}-{score2}")
            return country1
        elif score2 > score1 + (4 - i):
            print(f"\n{country2} wins the match on penalties!")
            print(f"and the score is {score1}-{score2}")
            return country2

    print("\nSudden death will follow")
    # Additional kicks if necessary
    while score1 == score2:
        if random.random() > 0.3:
            print(f"{country1} scores a penalty!")
            score1 += 1
        else:
            # print(f"{country1} misses the penalty!")
            pass

        if random.random() > 0.3:
            print(f"{country2} scores a penalty!")
            score2 += 1
        else:
            # print(f"{country2} misses the penalty!")
            pass

    if score1 > score2:
        print(f"\n{country1} wins the match on penalties!")
        print(f"and the score is {score1}-{score2}")
        return country1
    else:
        print(f"\n{country2} wins the match on penalties!")
        print(f"and the score is {score1}-{score2}")
        return country2


def calculate_goal_chance(rating):
    base_chance = 0.175  # Default chance to score a goal (17,5 %)
    adjusted_chance = base_chance + (rating / 1000)
    return min(1.0, adjusted_chance)   # Chance can't be higher than 100 %


def calculate_save_chance(rating):
    base_chance = 0.1
    adjusted_chance = base_chance + (rating / 1000)
    return min(1.0, adjusted_chance)


def simulate_individual_match(player1, player2, minute):
    goal_attempt = random.random()
    goal_chance = calculate_goal_chance(player1[-1])
    save_chance = calculate_save_chance(player2[-1])

    if goal_attempt < goal_chance and goal_attempt > save_chance:
        print(f"{player1[1]} shoots and scores in {minute} minute!")
        player_name = player1[1]
        if player_name in player_goals_stats:
            player_goals_stats[player_name] += 1
        else:
            player_goals_stats[player_name] = 1
        return True  # Goal
    else:
        # print(f"{player2[1]} saves the shot from {
        #   player1[1]} in {minute} minute!")
        return False  # Saved shot


def simulate_team_match(team1, team2, extra_time):
    team1_score = 0
    team2_score = 0
    minutes_range = range(1, 91) if extra_time == 0 else range(90, 121)

    for minute in minutes_range:
        action = random.choice(["team1_attack", "team2_attack", "nothing"])

        if action == "team1_attack":
            attacker = random.choice([p for p in team1 if p[0] != "GK"])
            defender = random.choice([p for p in team2 if p[0] == "GK"])
            if simulate_individual_match(attacker, defender, minute):
                team1_score += 1

        elif action == "team2_attack":
            attacker = random.choice([p for p in team2 if p[0] != "GK"])
            defender = random.choice([p for p in team1 if p[0] == "GK"])
            if simulate_individual_match(attacker, defender, minute):
                team2_score += 1

        elif action == "nothing":
            # print(f"Minute {minute + 1}: Nothing happens.")
            pass

    return team1_score, team2_score


def semifinal(country1, country2, team1, team2):
    score1, score2 = simulate_team_match(team1, team2, 0)
    while True:
        if score1 > score2:
            final_team = country1
            print(f"\n{country1} beats {country2} with a score of {
                score1}-{score2} and advances to the final!")
            return final_team
        elif score1 < score2:
            final_team = country2
            print(f"\n{country2} beats {country1} with a score of {
                score2}-{score1} and advances to the final!")
            return final_team
        else:
            print(f"\nThe match ends in a draw. Extra time will be played.")
            et_score1, et_score2 = simulate_team_match(team1, team2, 1)
            score1 += et_score1
            score2 += et_score2
            if score1 > score2:
                final_team = country1
                print(f"\n{country1} beats {country2} with a score of {
                    score1}-{score2} and advances to the final!")
                return final_team
            elif score1 < score2:
                final_team = country2
                print(f"\n{country2} beats {country1} with a score of {
                    score2}-{score1} and advances to the final!")
                return final_team
            else:
                break
    print(
        f"\nThe match ends in a draw after extra time with a score of {country1} {score1} - {score2} {country2}. Penalties will be played.")
    final_team = penalties(country1, country2, score1, score2)
    return final_team


def final(final_team1, final_team2, team1, team2):
    score1, score2 = simulate_team_match(team1, team2, 0)
    while True:
        if score1 > score2:
            winner = final_team1
            print(f"\n{final_team1} wins the final against {
                final_team2} with a score of {score1}-{score2}!")
            return winner
        elif score1 < score2:
            winner = final_team2
            print(f"\n{final_team2} wins the final against {
                final_team1} with a score of {score2}-{score1}!")
            return winner
        else:
            print("The match ends in a draw. Extra time will be played.")
            score1, score2 = simulate_team_match(team1, team2, 1)
            if score1 > score2:
                winner = final_team1
                print(f"{final_team1} wins the final against {
                    final_team2} with a score of {score1}-{score2}!")
                return winner
            elif score1 < score2:
                winner = final_team2
                print(f"{final_team2} wins the final against {
                    final_team1} with a score of {score2}-{score1}!")
                return winner
            else:
                break
    print("\nThe match ends in a draw after extra time. Penalties will be played.")
    winner = penalties(final_team1, final_team2, score1, score2)
    print(f"{winner} wins the TITLE!")


def print_player_statistics(player_stats):
    # Sort the player statistics by the number of goals scored
    sorted_players = sorted(player_stats.items(),
                            key=lambda x: x[1], reverse=True)
    print("\nPlayer Statistics:")
    for player_name, goals_scored in sorted_players:
        print(f"{player_name}: {goals_scored} goals")


player_goals_stats = {}
countries = ['England', 'Spain', 'Netherlands', 'France']
players = []

for teams in countries:  # Iterates through countries to fetch web pages for player information from different national teams
    for position_assign in [0, 1, 2, 3, 4, 5, 8, 9, 10, 12]:
        url = f"https://pesdb.net/efootball/?nationality={
            teams}&pos={position_assign}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            if position_assign == 1:
                players.append(find_player_info(0, 3, position_assign))
                players.append(find_player_info(3, 6, position_assign))
            else:
                players.append(find_player_info(0, 3, position_assign))
        except requests.HTTPError as e:
            print(f"Failed to retrieve the page. Status code: {
                  response.status_code}. Error: {e}")

players_by_country = {}

for player in players:
    position, name, team, country, rating = player
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
    sum_rating = sum(player[-1] for player in players_list)
    sum_rating_by_country[country] = sum_rating

# Shows the total player ratings for each country.
for country, summary in sum_rating_by_country.items():
    print(f"{country}: {summary}")

# Generates random countries for the semifinal matches.
random_country = random.sample(list(sum_rating_by_country.keys()), 4)
country1, country2, country3, country4 = random_country

sum_country1 = round(
    sum_rating_by_country[country1] * random.uniform(0.9, 1.10))
sum_country2 = round(
    sum_rating_by_country[country2] * random.uniform(0.9, 1.10))
sum_country3 = round(
    sum_rating_by_country[country3] * random.uniform(0.9, 1.10))
sum_country4 = round(
    sum_rating_by_country[country4] * random.uniform(0.9, 1.10))

team1 = players_by_country[country1]
team2 = players_by_country[country2]
team3 = players_by_country[country3]
team4 = players_by_country[country4]

print(f"\n1. Semifinal: {country1} vs {country2}")
final_team1 = semifinal(country1, country2, team1, team2)
print(f"\n2. Semifinal: {country3} vs {country4}")
final_team2 = semifinal(country3, country4, team3, team4)

print(f"\nFinal: {final_team1} vs {final_team2}")
winner = final(final_team1, final_team2,
               players_by_country[final_team1], players_by_country[final_team2])

print_player_statistics(player_goals_stats)
