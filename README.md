# NBA SQL Database
## Description
Reads and stores NBA data in a MySQL database.
## Database Tables
|Table|Description|
|-----|-----------|
|[PlayerBio](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/models/PlayerBio.py)|Stores basic bio information for a player|
|[PlayerGeneralTraditionalPerGame](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/models/PlayerGeneralTraditionalPerGame.py)|Stores per game traditional statistics for a player|
|[PlayerGeneralTraditionalTotals](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/models/PlayerGeneralTraditionalTotals.py)|Stores traditional statistic totals for a player|
## Use
1. Install Python >= 3.10
2. Install dependencies with ```pip install -r requirements.txt```
3. Install MySQL and start a local server
4. Create a .env file in /src and fill in the parameters DB_NAME, DB_HOST, DB_USER, and DB_PASSWORD
5. To generate data for PlayerBio table, run [player_bios.py](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/player_bios.py)
6. To generate data for PlayerGeneralTraditionalPerGame, run [player_general_traditional_per_game.py](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/player_general_traditional_per_game.py)
7. To generate data for PlayerGeneralTraditionalTotals, run [player_general_traditional_totals.py](https://github.com/kaiyangzheng/nba-mysql/blob/main/src/player_general_traditional_totals.py)