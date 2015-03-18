#!/usr/bin/python
from tabulate import tabulate
import pprint
import operator 
import json

file = open('ncaa.json', 'rb')
b12 = json.load(file)
file.close()

#b12 = [ 
#  { 'team': 'Iowa State', 'games': 31, 'record': [ 23, 8 ], 'pf': 2449, 'pa': 2155 }, 
#  { 'team': 'West Virginia', 'games': 32, 'record': [ 23, 9 ], 'pf': 2366, 'pa': 2139 }, 
#  { 'team': 'Oklahoma', 'games': 31, 'record': [ 22, 9 ], 'pf': 2237, 'pa': 1941 }, 
#  { 'team': 'Kansas', 'games': 32, 'record': [ 25, 7 ], 'pf': 2293, 'pa': 2077 }, 
#
#  KU without loss to Kentucky makes no difference.
#
#  { 'team': 'Kansas', 'games': 31, 'record': [ 25, 6 ], 'pf': 2253, 'pa': 2005 }, 
#  { 'team': 'Baylor', 'games': 32, 'record': [ 24, 8 ], 'pf': 2241, 'pa': 1929 }, 
#  { 'team': 'Texas Christian', 'games': 33, 'record': [ 18, 15 ], 'pf': 2249, 'pa': 2058 }, 
#  { 'team': 'Texas', 'games': 33, 'record': [ 20, 13 ], 'pf': 2242, 'pa': 1993 }, 
#  { 'team': 'Oklahoma State', 'games': 31, 'record': [ 18, 13 ], 'pf': 2087, 'pa': 1932 }, 
#  { 'team': 'Kansas State', 'games': 31, 'record': [ 15, 17 ], 'pf': 2016, 'pa': 2042 }, 
#  { 'team': 'Texas Tech', 'games': 32, 'record': [ 13, 19 ], 'pf': 1949, 'pa': 2059 } ]

#b12 = [
#  { 'team': 'Golden State', 'games': 63, 'record': [ 51, 12 ], 'pf': 6902, 'pa': 6259 } ]

b12_expected_results = []
exp = 8.25
#exp = 16.5

for school in b12['ncaa']:
  if int(school['games']) > 0:
#    print school
    pf = school['pf']
    pa = school['pa']

    py_expectation = pf ** exp / (( pf ** exp ) + ( pa ** exp ))
    expected_wins = py_expectation * school['games']
    expected_losses = ( 1 - py_expectation ) * school['games']
    wins = int(round(expected_wins))
    losses = int(round(expected_losses))
    expected_record = [ wins, losses ]

    b12_expected_results.append( { 'team': school['team'], 'expected_record': expected_record } )
#
#
#  if expected_wins > school['record'][0]:
#    print school['team'] + " is under-valued by " + str(expected_wins - school['record'][0])  + " games."
#    print "Expected wins: " + str(expected_wins)
#  else:
#    print school['team'] + " is over-valued by " + str(school['record'][0] - expected_wins)  + " games."
#    print "Expected wins: " + str(expected_wins)


#pp = pprint.PrettyPrinter() 
#pp.pprint(sorted(b12, key=lambda k: k['record'], reverse=True))
#pp.pprint(sorted(b12_expected_results, key=lambda k: k['expected_wins'], reverse=True))

print "\n"
print "\n"
b12_expected_results.sort(key=lambda k: (-k['expected_record'][0], k['expected_record'][1]))
#b12_expected_results.sort(key=lambda k: k['expected_record'][1])
print tabulate(b12_expected_results, headers="keys")
print "\n"
b12['ncaa'].sort(key=lambda k: (-k['record'][0], k['record'][1]))
#b12['ncaa'].sort(key=lambda k: k['record'][1])

print tabulate(b12['ncaa'], headers="keys")
