#!/usr/bin/env python

from lxml import etree as ET
import os, sys, urllib
import time
import pymongo

client = pymongo.MongoClient()
db = client.songs

FILE_TYPE = "xml"
CALL_SIGN = sys.argv[1].upper()
BASE_DIR = "/usr/local/share/stations/" + CALL_SIGN.lower() + "/playlists/"

if not os.path.exists(BASE_DIR):
  os.makedirs(BASE_DIR)

URL = ("http://playerservices.streamtheworld.com/public/nowplaying?mountName=%s") % (CALL_SIGN)

urllib.urlretrieve(URL, BASE_DIR + CALL_SIGN + "." + FILE_TYPE)
content = BASE_DIR + CALL_SIGN + "." + FILE_TYPE

c = db[CALL_SIGN.lower()]

tree = ET.parse(content)
root = tree.getroot()

#node = root.findall("./nowplaying-info/property")
node = root.findall("./nowplaying-info")

songs = []

for prop in node:
  song_dict = {}
  if prop.attrib['type'] == "track":
    for p in prop:
      n = str(p.attrib['name'])

      if n == "track_artist_name":
        song_dict.update({ 'artist': p.text })
      elif n == "cue_time_duration":
          song_dict.update({ 'duration': p.text.encode('ascii', 'ignore') })
      elif n == "cue_title":
          song_dict.update({ 'title': p.text.encode('ascii', 'ignore') })
      elif n == "cue_nowplaying_url":
          song_dict.update({ 'url': p.text.encode('ascii', 'ignore') })
      song_dict.update({ 'date': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float(prop.attrib['timestamp']))) })
      song_dict.update({ '_id': prop.attrib['timestamp'] })

    songs.append(song_dict)
    c.update({'_id': song_dict['_id']}, song_dict, upsert=True)

for song in songs:
  print song
