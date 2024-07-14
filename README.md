# Football-simulator ⚽
Football simulator for semifinal and final 

This is my first major python project. The data for this simulator is downloaded from the internet database pesdb.net, I chose this site because I play efootball and this site contains player ratings from this game and the ratings are objective.

### TODO list 📝
- 📊 Player stats
- ⚽ Match results with goals, not just who is the winner
- 🏆 Announcement of the best player of the tournament, considering defensive players as well
- 🛠️ The possibility to create your own team
- 🔄 Adjust player's form based on their real-world performance
# 0.2.1 🚀

In this version, I completely redesigned the penalty shootout, also players now have a 70% chance of scoring a goal, a success rate similar to the real world.
Fixed a bug where score in extra time would be set to 0:0

# 0.2.0 🌟

Changed the way the program works, chances on winning is now calculated on comparing random players against goalkeeper. Also there are now penalties, but I'm not really happy with it, i wanted to implement it so bad so I used a lot of copilots help, definitely will change it in following updates, but for now it's fine. 
One bigger feature is the the program saves players statistics.

### Features in this version:

- Simulator now doesn't compare team overall rating, but instead starts a game and tracks it"s statistics
- 📈 Player statistics
- 🥅 Penalties after extra time

### New bugs 🐞:

- Penalties are weird and I wanna rework them
- Since overall rating influences chance to score a goal, defenders have same chance of scoring a goal as attackers

### Bugs:

- Fixed formation 433, some teams don't play this way and therefore this may lower their rating
- I didn't handle exceptions.
- if a team is missing a player for a certain position, the program will crash, ideally a replacement should be found for that player for example in another position LB -> RB, etc..
- and much more.

## Version 0.1.1 🛠️
I removed one fucntion that was redundant and made the code cleaner.
## Version 0.1.0 🏁
I wanted to finish this project before the start of the final match of the EURO, that's why it contains only basic features, on the other hand, the code is quite modular and adding new features shouldn't be that difficult.
### Features in this version:
- 🏅 Semi-final and final simulation
- 🌐 Web scraping of data from pesdb.net
- 🎲 Element of randomness in the coefficient calculation
### Bugs:
- Fixed formation 433, some teams don't play this way and therefore this may lower their rating
- I didn't handle exceptions.
- if a team is missing a player for a certain position, the program will crash, ideally a replacement should be found for that player for example in another position LB -> RB, etc..
- and much more. 
