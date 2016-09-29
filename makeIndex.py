import pandas as pd
from dateutil.parser import parse
from collections import namedtuple
import sys
from fractions import Fraction
from pprint import pprint
stdout = sys.stdout
import numpy as numpy


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

occurances = numpy.zeros((59, 30, 11))
wins = numpy.zeros((59, 30, 11))
losses = numpy.zeros((59, 30, 11))
winp = numpy.zeros((59, 30, 11))
lossp = numpy.zeros((59, 30, 11))

currYear = 1957
for j in range (59):
    currYear = 1957 + j
    sys.stdout = stdout
    print "Calculating year " + str(currYear)

    for i in range (len(teamNames)):
        sys.stdout = stdout
        input = "input/"+teamNames[i]+".csv"
        data = pd.read_csv(input, sep=',',header=None)

        for x in range(len(data)):
    #        sys.stdout = stdout #debug
    #        print x
    #        sys.stdout = f
            if data[0][x] == "Game Date":
               continue
            month, day, yeartmp = data[0][x].split('/')
            year = yeartmp[0:4]

            if int(year) > 1900: #handle variable date formats 1/1/99, 11/11/99, 11/11/1999, 11/11/1999 (1)
                year = int(year)
            elif int(year) > 17:
                year = int('19' + year)
            else:
                year = int('20' + year)
            if (year > currYear):
                break
            if (year < currYear):
                continue
            runs = int(data[13][x])
            outs = float(data[10][x])
            outs = int (outs * 3)
            if outs > 29:
                outs = 29
            if runs > 10:
                runs = 10

            occurances [j][outs][runs] += 1

            if (int(data[6][x]) == 1):
                wins[j][outs][runs] += 1
            elif (int(data[7][x]) == 1):
                losses[j][outs][runs] += 1
    
    output = "indexes/" + str(currYear) + "wins" + ".csv"
    f = file(output, 'w')
    sys.stdout = f
    for i in range (30):
            print wins[j][i][0], ',', wins[j][i][1], ',',wins[j][i][2], ',',wins[j][i][3], ',',wins[j][i][4], ',',wins[j][i][5], ',',wins[j][i][6], ',',wins[j][i][7], ',',wins[j][i][8], ',',wins[j][i][9], ',',wins[j][i][10]

