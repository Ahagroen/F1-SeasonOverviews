import Input
year  = "2019"
team = "red_bull"
DriverList = Input.DriversList(Input.getDriverStandings(year))
teams = []
for i in Input.getConstructorStandings(year)["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]:
    teams.append(i["Constructor"]["constructorId"])


def TeamPerformance(Drivers):
    #Drivers is a list of the drivers for their team and the valid rounds dict found above
    RoundbyRound = {}
    for i in Drivers:
        for j in i:
            if isinstance(j,int):
                if j in RoundbyRound:
                    RoundbyRound[j].append([i["driver"],i[j]])
                else:
                    RoundbyRound[j] = []
                    RoundbyRound[j].append([i["driver"],i[j]])
    RoundbyRound = dict(sorted(RoundbyRound.items()))
    return RoundbyRound

def TeamOverview(team,year):
    teammates = Input.getTeammates(team,DriverList)
    teamOverview = []
    for i in teammates:
        teamOverview.append(Input.getReleventRaces(team,Input.getRaces(i,year),i))
    print(teamOverview)
    #Performance = TeamPerformance(teamOverview)
    #for i in Performance:
    #    print(Performance[i])
    
for i in teams:
    print(i)
    TeamOverview(i,year)

