#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
from pprint import pprint

url = 'http://www.sports-reference.com/cbb/seasons/2015-school-stats.html'

def build_request(url):
  user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
  headers = { 'User-Agent' : user_agent }
  req = urllib2.Request(url, '', headers)
  response = urllib2.urlopen(req)
  html = response.read()

  return html

def get_soup(url):
  html = build_request(url)

  return BeautifulSoup(html)


soup = get_soup(url)

stats = []
rows = soup.find(id='basic_school_stats').find('tbody').find_all('tr')
for row in rows:
  print row['class']
  if len(row['class']) == 1:
    cells = row.find_all('td')
#  rank = int(cells[0].get_text().encode('ascii', 'ignore'))
    school = cells[1].get_text().encode('ascii', 'ignore')
    games = int(cells[2].get_text().encode('ascii', 'ignore'))
    wins = int(cells[3].get_text().encode('ascii', 'ignore'))
    losses = int(cells[4].get_text().encode('ascii', 'ignore'))
    wl_percent = float(cells[5].get_text().encode('ascii', 'ignore'))
    srs = float(cells[6].get_text().encode('ascii', 'ignore'))
    sos = float(cells[7].get_text().encode('ascii', 'ignore'))
    conf_wins = int(cells[8].get_text().encode('ascii', 'ignore'))
    conf_losses = int(cells[9].get_text().encode('ascii', 'ignore'))
    home_wins = int(cells[10].get_text().encode('ascii', 'ignore'))
    home_losses = int(cells[11].get_text().encode('ascii', 'ignore'))
    away_wins = int(cells[12].get_text().encode('ascii', 'ignore'))
    away_losses = int(cells[13].get_text().encode('ascii', 'ignore'))
    team_points = int(cells[14].get_text().encode('ascii', 'ignore'))
    opp_points = int(cells[15].get_text().encode('ascii', 'ignore'))
    fg = int(cells[17].get_text().encode('ascii', 'ignore'))
    fga = int(cells[18].get_text().encode('ascii', 'ignore'))
    fg_percent = float(cells[19].get_text().encode('ascii', 'ignore'))
    threept = int(cells[20].get_text().encode('ascii', 'ignore'))
    threepta = int(cells[21].get_text().encode('ascii', 'ignore'))
    threept_percent = float(cells[22].get_text().encode('ascii', 'ignore'))
    ft = int(cells[23].get_text().encode('ascii', 'ignore'))
    fta = int(cells[24].get_text().encode('ascii', 'ignore'))
    ft_percent = float(cells[25].get_text().encode('ascii', 'ignore'))
    off_reb = int(cells[26].get_text().encode('ascii', 'ignore'))
    tot_reb = int(cells[27].get_text().encode('ascii', 'ignore'))
    ast = int(cells[28].get_text().encode('ascii', 'ignore'))
    stl = int(cells[29].get_text().encode('ascii', 'ignore'))
    blk = int(cells[30].get_text().encode('ascii', 'ignore'))
    tov = int(cells[31].get_text().encode('ascii', 'ignore'))
    pf = int(cells[32].get_text().encode('ascii', 'ignore'))

    team_stats = dict([
      ('school', school), ('games', games), ('wins', wins),
      ('losses', losses), ('wl%', wl_percent), ('srs', srs),
      ('sos', sos), ('conf_wins', conf_wins), ('conf_losses', conf_losses),
      ('home_wins', home_wins), ('home_losses', home_losses), 
      ('away_wins', away_wins), ('away_losses', away_losses),
      ('team_points', team_points), ('opp_points', opp_points),
      ('fg', fg), ('fga', fga), ('fg%', fg_percent), ('3p', threept),
      ('3pa', threepta), ('3p%', threept_percent), ('ft', ft), 
      ('fta', fta), ('ft%', ft_percent), ('off_reb', off_reb), 
      ('tot_reb', tot_reb), ('ast', ast), ('stl', stl), ('blk', blk),
      ('tov', tov), ('pf', pf)])

               
    stats.append(team_stats)

pprint(stats)

print len(stats)
