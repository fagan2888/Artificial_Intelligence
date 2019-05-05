import csv
import math


def coorGraph():
    ecef = {}
    R = 3959
    with open('ECEF.txt', 'r') as filein1:
        csvreader = csv.reader(filein1)
        l = []
        for line in csvreader:
            l.append(line)
        for line1 in range(len(l)):
            for line2 in range(len(l)):
                city1 = l[line1][0]
                lat1 = float(l[line1][1].strip())/360
                lon1 = float(l[line1][2].strip())/360
                city2 = l[line2][0]
                lat2 = float(l[line2][1].strip())/360
                lon2 = float(l[line2][2].strip())/360
                x1 = math.cos(lat1) * math.cos(lon1)*R
                y1 = math.cos(lat1) * math.sin(lon1)*R
                z1 = math.sin(lat1)
                x2 = math.cos(lat2) * math.cos(lon2) * R
                y2 = math.cos(lat2) * math.sin(lon2) * R
                z2 = math.sin(lat2)
                codist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
                ecef[city1 + city2] = codist
    return ecef

