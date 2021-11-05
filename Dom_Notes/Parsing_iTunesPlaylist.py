import matplotlib

def findDuplicates(fileName):
    print('Finding duplicate tracks in %s...' % fileName)
    # read in a Playlist
    plist = plistlib.readPlist(fileName)
    # get tracks from the Tracks dictionary
    tracks = plist['tracks']
    # create a track name dictionary
    trackNames = {}
    # iterate through the Tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # look for existing entrie
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track length to the nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
                else:
                    # add dictionary entry as tuple (duration, count)
                    trackNames[name] = (duration, 1)
        except:
            # ignore
            pass

# UNFINISHED - Not sinking in!!!!! :'(
