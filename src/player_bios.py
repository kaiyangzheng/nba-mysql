import requests 
from settings import Settings 
from models import PlayerBio

settings = Settings()
settings.db.create_tables([PlayerBio], safe=True)

header_data  = {
    'User-Agent': 'Some User Agent',
    'x-nba-stats-origin': 'stats',
    'Referer': 'https://stats.nba.com/',
}

# endpoints
def player_bio_url(season_id, per_mode):
    return  'http://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode={}&Period=0&PlayerExperience=&PlayerPosition=&Season={}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='.format(per_mode, season_id)

# Extract json
def extract_data(url):
    r = requests.get(url, headers=header_data)
    resp = r.json()
    return resp

per_mode = 'Totals'
season_list = [
    '1996-97',
    '1997-98',
    '1998-99',
    '1999-00',
    '2000-01',
    '2001-02',
    '2002-03',
    '2003-04',
    '2004-05',
    '2005-06',
    '2006-07',
    '2007-08',
    '2008-09',
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20',
    '2020-21',
    '2021-22'
]

# create player in db
def create_player(row, season_id):
    player = PlayerBio(
        season_id=season_id,
        player_id=row[0],
        player_name=row[1],
        team_id=row[2],
        team_abbreviation=row[3],
        age=row[4],
        player_height=row[5],
        player_height_inches=row[6],
        player_weight=row[7],
        college=row[8],
        country=row[9],
        draft_year=row[10],
        draft_round=row[11],
        draft_number=row[12],
        gp=row[13],
        pts=row[14],
        reb=row[15],
        ast=row[16],
        net_rating=row[17],
        oreb_pct=row[18],
        dreb_pct=row[19],
        usg_pct=row[20],
        ts_pct=row[21],
        ast_pct=row[22]
    )
    return player 

def main():
    for i, season_id in enumerate(season_list):
        print(f"Processing season {season_id}")
        response = extract_data(player_bio_url(season_id, per_mode))
        player_info = response['resultSets'][0]['rowSet']
        for row in player_info:
            try:
                player = PlayerBio.get(PlayerBio.player_id == row[0], PlayerBio.season_id == season_id)
                # update last season by deleting and creating new record
                if i == len(season_list) - 1:
                    player.delete_instance()
                    player = create_player(row, season_id)
                    player.save()
            except:
                # ccreate new record
                player = create_player(row, season_id)
                player.save()

    print("Done inserting player bios!")

if __name__ == '__main__':
    main()