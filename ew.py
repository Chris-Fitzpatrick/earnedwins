import pandas as pd
from dateutil.parser import parse
from collections import namedtuple
import sys
from fractions import Fraction
from pprint import pprint
stdout = sys.stdout


perfList = []
seasonList = []
careerList = []
allTimeSeasons = []

teamNames = []
teamNames.append("Angels")
teamNames.append("Astros")
teamNames.append("Athletics")
teamNames.append("Jays")
teamNames.append("Braves")
teamNames.append("Brewers")
teamNames.append("Cardinals")
teamNames.append("Cubs")
teamNames.append("Diamondbacks")
teamNames.append("Dodgers")
teamNames.append("Giants")
teamNames.append("Indians")
teamNames.append("Mariners")
teamNames.append("Marlins")
teamNames.append("Mets")
teamNames.append("Nationals")
teamNames.append("Orioles")
teamNames.append("Padres")
teamNames.append("Phillies")
teamNames.append("Pirates")
teamNames.append("Rangers")
teamNames.append("Rays")
teamNames.append("Red_Sox")
teamNames.append("Reds")
teamNames.append("Rockies")
teamNames.append("Royals")
teamNames.append("Tigers")
teamNames.append("Twins")
teamNames.append("White_Sox")
teamNames.append("Yankees")

#make the win and loss percentage arrays
w, h = 12, 30
winp = [[0 for x in range(w)] for y in range(h)]
lossp = [[0 for x in range(w)] for y in range(h)]

#set the values
winData = pd.read_csv('winpercentage.csv', header=None)
lossData = pd.read_csv('losspercentage.csv', header=None)
lossp = lossData.values
winp = winData.values


class perf:
    def __init__(self, month, day, year, name, w, l, ip, er, team, ew, el):
        self.month = month
        self.day = day
        self.year = year
        self.name = name
        self.ip = ip
        self.er = er
        self.w = w
        self.l = l
        self.team = team
        self.ew = ew
        self.el = el

    def printcsv(self):
        decision = 'N'
        if self.w == 1:
            decision = 'W' 
        elif self.l == 1:
            decision = 'L'
        print self.name, ',', self.team, ',', self.year, ',', round(float(self.ip),2), ',', self.er, ',', decision, ',', round(float(self.ew),2), ',', round(float(self.el),2)
        #, ',' self.year, ',', self.ip, ',', self.er, ',', self.w, '-', self.l, ',', str(self.ew), "-" , str(self.el), ',' self.w - self.ew


class season:

    seasonPerfs = []
    def __init__(self, perf):
        self.name = perf.name
        self.year = perf.year
        self.team = perf.team
        self.er = perf.er
        self.w = perf.w
        self.l = perf.l
        self.ew = perf.ew
        self.el = perf.el
        self.ip = perf.ip
        self.seasonPerfs.append(perf)
        self.gs = 1
        self.var = int(perf.w) - float(perf.ew)

    def addPerf (self, performance):
        self.er += performance.er
        self.w += performance.w
        self.l += performance.l
        self.ew += performance.ew
        self.el += performance.el
        self.ip += performance.ip
        self.seasonPerfs.append(performance)
        self.gs += 1
        self.var += int(performance.w) - float(performance.ew)

    def printcsv(self):
        #output = "output/" + self.team + ".csv"
        #f = file(output, 'w')
        #sys.stdout = f
        if (float(self.ip) == 0):
            era = 99
        elif (int(self.er) == 0):
            era = 0
        else:
            era = round (int(self.er)/(float(self.ip) / 9), 2)
        print self.name, ',', self.team, ',', self.year, ',', self.gs, ',', round(float(self.ip),2), ',', era, ',', round(float(self.ew/self.gs), 2), ',', self.w, ',', self.l, ',', round(float(self.ew), 2), ',', round(float(self.el),2), ',', round(self.var + self.el - self.l, 2)

class career:

    careerSeasons = [] 
    def __init__(self, season):
        self.name = season.name
        self.er = season.er
        self.w = season.w
        self.l = season.l
        self.ew = season.ew
        self.el = season.el
        self.ip = season.ip
        self.careerSeasons.append(season)
        self.gs = season.gs
        self.var = season.var
        self.firstSeason = season.year
        self.lastSeason = season.year

    def addSeason (self, season):
        self.er += season.er
        self.w += season.w
        self.l += season.l
        self.ew += season.ew
        self.el += season.el
        self.ip += season.ip
        if (season.year > self.lastSeason):
            self.lastSeason = season.year
        if (season.year < self.firstSeason):
            self.firstSeason = season.year
        self.careerSeasons.append(season)
        self.gs += season.gs
        self.var += int(season.w) - float(season.ew)

    def printcsv(self):
        
        if (float(self.ip) == 0):
            era = 99
        elif (int(self.er) == 0):
            era = 0
        else:
            era = round (int(self.er)/(float(self.ip) / 9), 2)
        var = round(self.var + self.el - self.l, 2)
        print self.name, ',', str(self.firstSeason) + '-' + str(self.lastSeason), ',', self.gs, ',', int(self.ip), ',', era, ',', round(self.ew/self.gs, 2), ',', self.w, '-', self.l, ',', round(self.ew, 2), '-', round(self.el, 2), ',', round(self.w - self.ew + self.el - self.l, 2) , ',', self.ew, ',', self.el


def addToSeason(performance):
    if len(seasonList) == 0:
        currSeason = season(performance)
        seasonList.append(currSeason)
        return
    for x in range(len(seasonList)):
        if seasonList[x].name == performance.name and seasonList[x].year == performance.year:
            seasonList[x].addPerf(performance)
            return

    currSeason = season(performance)
    seasonList.append(currSeason)

def addToCareer(season):

    if len(careerList) == 0:
        currCareer = career(season)
        careerList.append(currCareer)
        return

    for x in range(len(careerList)):
        if careerList[x].name == season.name:
            careerList[x].addSeason(season)
            return

    currCareer = career(season)
    careerList.append(currCareer)
#    seasonList = []




for i in range (len(teamNames)):
    sys.stdout = stdout
    print "Changing teams to: " + teamNames[i]
    input = "input/"+teamNames[i]+".csv"
    data = pd.read_csv(input, sep=',',header=None)
    seasonList = []
    lastyear = 1

    for x in range(len(data)):
#        sys.stdout = stdout #debug
#        print x
#        sys.stdout = f
        if data[0][x] == "Game Date":
           continue
        month, day, yeartmp = data[0][x].split('/')
        year = yeartmp[0:4]

        if int(year) > 1900: #handle date formats 1/1/99, 11/11/99, 11/11/1999, 11/11/1999 (1)
            year = int(year)
        elif int(year) > 17:
            year = int('19' + year)
        else:
            year = int('20' + year)
        
        #update the output when the year or team changes
        if int(lastyear) != int(year):
            output = "output/performances/"+teamNames[i]+"/" + str(year)+".csv"
            f = file(output, 'w')
            sys.stdout = f
            print "Name, Team, Year, IP, ER, Decision, Earned Wins, Earned Losses"
        
        runs = int(data[13][x])
        outs = float(data[10][x])
        outs = int (outs * 3)
        lastyear = int(year)
        if outs > 29:
            outs = 29
        if runs > 11:
            runs = 11
        ew = winp[outs][runs]
        el = lossp[outs][runs]
        
        #create the performance
        currPerf = perf (month, day, year, data[1][x], int(data[6][x]), int(data[7][x]), float(data[10][x]), runs, teamNames[i], ew, el)
        currPerf.printcsv()
        perfList.append(currPerf)
        addToSeason(currPerf)
    
    output = "output/"+teamNames[i]+".csv"
    f = file(output, 'w')
    sys.stdout = f
    print "Name, Team, Year, Games Started, IP, ERA, EWA, Record, Earned Record, Support/Luck"
    for x in range (len(seasonList)):
        seasonList[x].printcsv()
        allTimeSeasons.append(seasonList[x])

    for x in range (len(seasonList)):
        addToCareer(seasonList[x])


output = "EWSeason.csv"
f = file(output, 'w')
sys.stdout = f
print "Name, Team, Year, Starts, IP, ERA, EWA, W, L, EW, EL, Support/Luck"
for x in range (len(allTimeSeasons)):
    allTimeSeasons[x].printcsv()


output = "CareerEWList.csv"
f = file(output, 'w')
sys.stdout = f
print "Name, Years, Starts, IP, ERA, EWA, W-L, EW-EL, Support/Luck, EW, EL"
for x in range (len(careerList)):
    careerList[x].printcsv()
