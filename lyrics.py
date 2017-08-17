#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import sys
import getopt

def getLyrics(artist, title):
    lyricsTitle = artist + ' - ' + title # do this before we convert artist and title to fit to azlyrics
    artist = artist.lower().replace(" ", "").replace('\'', '').replace('(', '').replace(')', '')
    title = title.lower().replace(" ", "").replace('\'', '').replace('(', '').replace(')', '')
    try:
    		# azlyrics always uses this format: .../<artist>/<title>...
        html = urllib2.urlopen('http://azlyrics.com/lyrics/' + artist + '/' + title + '.html')
        soup = BeautifulSoup(html.read(), 'html.parser')
        lyrics = soup.find("div", attrs={"class": None, "id": None})
        displayLyrics(lyricsTitle, lyrics.getText().strip())
    except urllib2.URLError:
        print('Sorry, we could not find these lyrics :-(')

def displayLyrics(lyricsTitle, lyrics):
    print(lyricsTitle + '\n')
    print(lyrics + '\n')

def helpAndExit():
    print('Usage: lyrics -a [--artist] <artist> -t [--title] <title>')
    sys.exit()

def main(argv):
    if len(argv) != 4:
        helpAndExit()
    try:
        opts, args = getopt.getopt(argv, 'a:t:', ['artist=','title='])
        for opt, arg in opts:
            if opt in ("-a", "--artist"):
                artist = arg.strip()
            elif opt in ("-t", "--title"):
                title = arg.strip()
            else:
                helpAndExit()
        # everything is fine -> get the lyrics
        getLyrics(artist, title)
    except getopt.GetoptError:
        helpAndExit()

if __name__ == "__main__":
    main(sys.argv[1:])
