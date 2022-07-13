import requests
from settings import Settings
from models import PlayerGeneralTraditionalTotals

settings = Settings()
settings.db.create_tables([PlayerGeneralTraditionalTotals], safe=True)

header_data  = {
    'User-Agent': 'Some User Agent',
    'x-nba-stats-origin': 'stats',
    'Referer': 'https://stats.nba.com/',
}

# endpoints
def player_stats_url(season, per_mode):
    return "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode={1}&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={0}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=".format(
        season, per_mode)

# Extract json
def extract_data(url):
    r = requests.get(url, headers=header_data)                  # Call the GET endpoint
    resp = r.json()                                             # Convert the response to a json object
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
    player = PlayerGeneralTraditionalTotals(
            season_id=season_id,
            player_id=row[0],
            player_name=row[1],
            team_id=row[3],
            team_abbreviation=row[4],
            age=row[5],
            gp=row[6],
            w=row[7],
            l=row[8 ],
            w_pct=row[9],
            min=row[10],
            fgm=row[11],
            fga=row[12],
            fg_pct=row[13],
            fg3m=row[14],
            fg3a=row[15],
            fg3_pct=row[16],
            ftm=row[17],
            fta=row[18],
            ft_pct=row[19],
            oreb=row[20],
            dreb=row[21],
            reb=row[22],
            ast=row[23],
            tov=row[24],
            stl=row[25],
            blk=row[26],
            blka=row[27],
            pf=row[28],
            pfd=row[29],
            pts=row[30],
            plus_minus=row[31],
            nba_fantasy_pts=row[32],
            dd2=row[33],
            td3=row[34],
            gp_rank=row[36],
            w_rank=row[37],
            l_rank=row[38],
            w_pct_rank=row[39],
            min_rank=row[40],
            fgm_rank=row[41],
            fga_rank=row[42],
            fg_pct_rank=row[43],
            fg3m_rank=row[44],
            fg3a_rank=row[45],
            fg3_pct_rank=row[46],
            ftm_rank=row[47],
            fta_rank=row[48],
            ft_pct_rank=row[49],
            oreb_rank=row[50],
            dreb_rank=row[51],
            reb_rank=row[52],
            ast_rank=row[53],
            tov_rank=row[54],
            stl_rank=row[55],
            blk_rank=row[56],
            blka_rank=row[57],
            pf_rank=row[58],
            pfd_rank=row[59],
            pts_rank=row[60],
            plus_minus_rank=row[61],
            nba_fantasy_pts_rank=row[62],
            dd2_rank=row[63],
            td3_rank=row[64],
            cfid=row[66],
            cfparams=row[67]
        )
    return player

def main():
    for i, season_id in enumerate(season_list):
        print(f"Processing season {season_id}")
        response = extract_data(player_stats_url(season_id, per_mode))
        player_info = response['resultSets'][0]['rowSet']
        for row in player_info:
            try:
                player = PlayerGeneralTraditionalTotals.get(PlayerGeneralTraditionalTotals.player_id == row[0], PlayerGeneralTraditionalTotals.season_id == season_id)
                # update last season by deleting and creating new record
                if i == len(season_list) - 1:
                    player.delete_instance()
                    player = create_player(row, season_id)
                    player.save()
            except:
                # ccreate new record
                player = create_player(row, season_id)
                player.save()

    print("Done inserting player general traditional totals!")

if __name__ == '__main__':
    main()