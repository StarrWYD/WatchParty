import requests, os, json, time, datetime
evpath = ''
playlist = []
playdict = {}
prtplaylist = []
def cc():
  os.system('clear || cls')
def evseldirec():
    global evpath
    cc()
    print('Would you like to see avalible events or input event url?\n1. Input URL\n2. See Avalible Events')
    direc = input('')
    if direc == '1':
        cc()
        evsel = input('What is the fortnite tracker event url?\n')
        if '?window=' not in evsel:
            r = requests.get('https://fortnitetracker.com/api/v3/events/' + evsel.split('events/')[1]).json()
            r = requests.get('https://fortnitetracker.com/api/v3/events/' + evsel.split('events/')[1] + '/' + r['event']['activeWindowId']).json()
            title = r['event']['titleLine1'] + ' ' + r['event']['titleLine2'] + ' ' + wd['name']
            title = title.lower()
            title = title.title()
            cc()
            print('Is ' + title + ' the correct event?\n1. Yes\n2. No')
            direc = input('')
            if direc == '1':
                r = requests.get('https://fortnitetracker.com/api/v3/events/' + evsel.split('events/')[1]).json()
                evpath = evsel.split('events/')[1] + '/' + r['event']['activeWindowId']
                main()
            if direc == '2':
                cc()
                print('Sending you back in \n3')
                time.sleep(1)
                cc()
                print('Sending you back in \n3\n2')
                time.sleep(1)
                cc()
                print('Sending you back in \n3\n2\n1')
                time.sleep(1)
                evseldirec()
        if '?window=' in evsel:
            r = requests.get('https://fortnitetracker.com/api/v3/events/' + evsel.split('events/')[1]).json()
            title = r['event']['titleLine1'] + ' ' + r['event']['titleLine2'] + ' ' + r['eventWindow']['name']
            title = title.lower()
            title = title.title()
            cc()
            print('Is ' + title + ' the correct event?\n1. Yes\n2. No')
            direc = input('')
            if direc == '1':
                evpath = evsel.split('/events/')[1].replace('?window=', '/')
                main()
            if direc == '2':
                cc()
                print('Sending you back in \n3')
                time.sleep(1)
                cc()
                print('Sending you back in \n3\n2')
                time.sleep(1)
                cc()
                print('Sending you back in \n3\n2\n1')
                time.sleep(1)
                evseldirec()
    if direc == '2':
        evselsee()
def evselsee():
    global evpath
    cc()
    rglist = ['1. EU', '2. NAE', '3. NAW', '4. OCE', '5. ME', '6. ASIA', '7. BR']
    print('What region do you want to look at?\n' + '\n'.join(rglist))
    rg = input('')
    rg = rglist[(int(rg) - 1)].split('. ')[1]
    r = json.loads(requests.get('https://fortnitetracker.com/events?region=' + rg).text.split('var imp_calendar =')[1].split(';</')[0])
    evdict = {}
    evlist = []
    evwindowdict = {}
    a = 0
    while a < len(r):
        ev = r[a]
        wds = ev['customData']['windows']
        if len(wds) != 1:
            b = 0
            while b < len(wds):
                wd = wds[b]
                title = ev['customData']['title']
                wdtitle = title + ' ' + wd['name']
                wdtitle = wdtitle.upper()
                if title in evlist:
                    evdict[title].append(wdtitle)
                    evwindowdict[wdtitle] = wd['eventId'] + '/' + wd['eventWindowId']
                if title not in evlist:
                    evlist.append(title)
                    evdict[title] = [wdtitle]
                    evwindowdict[wdtitle] = wd['eventId'] + '/' + wd['eventWindowId']
                b = b + 1
        if len(wds) == 1:
            wd = wds[0]
            title = ev['customData']['title']
            wdtitle = title + ' ' + wd['name']
            wdtitle = wdtitle.upper()
            if title in evlist:
                evdict[title].append(wdtitle)
                evwindowdict[wdtitle] = wd['eventId'] + '/' + wd['eventWindowId']
            if title not in evlist:
                evlist.append(title)
                evdict[title] = [wdtitle]
                evwindowdict[wdtitle] = wd['eventId'] + '/' + wd['eventWindowId']
        a = a + 1
    a = 0
    prtevlist = []
    while a < len(evlist):
        prtevlist.append(str(a + 1) + '. ' + evlist[a])
        a = a + 1
    longlist = [evlist[0]]
    a = 0
    while a < len(prtevlist):
        if len(longlist[0]) < len(prtevlist[a]):
            longlist = [prtevlist[a]]
        a = a + 1
    a = 0
    bs = '-'*len(longlist[0])
    bs = bs + '--'
    cc()
    print('Which event would you like to look at?\n' + bs + '\n' + '\n'.join(prtevlist) + '\n' + bs)
    evlook = input('')
    livelist = []
    upcominglist = []
    endedlist = []
    evlooklist = evdict[evlist[int(evlook) - 1]]
    a = 0
    while a < len(evlooklist):
        r = requests.get('https://fortnitetracker.com/api/v3/events/' + evwindowdict[evlooklist[a]]).json()['eventWindow']
        bt = r['beginTime'].split('+')[0]
        et = r['endTime'].split('+')[0]
        ct = str(datetime.datetime.utcnow()).replace(' ', 'T').split('.')[0]
        datelist = [bt, et, ct]
        datelist.sort()
        if datelist == [ct, bt, et]:
            upcominglist.append(str(a + 1) + '. ' + evlooklist[a])
        if datelist == [bt, ct, et]:
            livelist.append(str(a + 1) + '. ' + evlooklist[a])
        if datelist == [bt, et, ct]:
            endedlist.append(str(a + 1) + '. ' + evlooklist[a])
        a = a + 1
    longlist = [evlooklist[0]]
    a = 0
    while a < len(evlooklist):
        if len(longlist[0]) < len(evlooklist[a]):
            longlist = [evlooklist[a]]
        a = a + 1
    bs = '-'*(len(longlist[0]) + 3) + '--'
    a = 0
    endedlist2 = []
    livelist2 = []
    upcominglist2 = []
    while a < len(endedlist):
        endedlist2.append(endedlist[a] + bs[len(endedlist[a]):].replace('-', ' ') + '|')
        a = a + 1
    a = 0
    while a < len(upcominglist):
        upcominglist2.append(upcominglist[a] + bs[len(upcominglist[a]):].replace('-', ' ') + '|')
        a = a + 1
    a = 0
    while a < len(livelist):
        livelist2.append(livelist[a] + bs[len(livelist[a]):].replace('-', ' ') + '|')
        a = a + 1
    livelist = livelist2
    upcominglist = upcominglist2
    endedlist = endedlist2
    if len(livelist) == 0:
        livelist.append(bs.replace('-', ' ') + '|')
    if len(endedlist) == 0:
        endedlist.append(bs.replace('-', ' ') + '|')
    if len(upcominglist) == 0:
        upcominglist.append(bs.replace('-', ' ') + '|')
    cc()
    print('Live Sessions\n' + bs + '\n' + '\n'.join(livelist) + '\n' + bs + '\nEnded Sessions\n' + bs + '\n' + '\n'.join(endedlist) + '\n' + bs + '\nUpcoming Sessions\n' + bs + '\n' + '\n'.join(upcominglist) + '\n' + bs)
    direc = input('Which number event would you like to look at?\n')
    evpath = evwindowdict[evlooklist[int(direc) - 1]]
    main()
def main():
    global playlist
    global playdict
    global prtplaylist
    cc()
    print('You have ' + str(len(playlist)) + ' in your WatchParty, what would you like to do?\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\n1. Add a player\n2. Remove a player\n3. Reset WatchParty\n4. Load from URL\n5. WatchParty\n6. Change Event')
    direc = input('')
    if direc == '1':
        add()
    if direc == '2':
        dele()
    if direc == '3':
        res()
    if direc == '4':
        load()
    if direc == '5':
        wp()
    if direc == '6':
        evseldirec()
def add():
    global prtplaylist
    global playlist
    global playdict
    a = 0
    if len(playlist) == 10:
        cc()
        print('You have reached the max amount of players, sending you back in \n3')
        time.sleep(1)
        cc()
        print('You have reached the max amount of players, sending you back in \n3\n2')
        time.sleep(1)
        cc()
        print('You have reached the max amount of players, sending you back in \n3\n2\n1')
        time.sleep(1)
        main()
    cc()
    print('You have ' + str(len(playlist)) + ' in your WatchParty\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\nWhat is the epic name of the player you would like to add?')
    epic = input('')
    pnm = requests.get('https://fortnitetracker.com/api/v0/profiles/find?platformUserHandle=' + epic).json()['platformUserHandle']
    pid = requests.get('https://fortnitetracker.com/api/v0/profiles/find?platformUserHandle=' + epic).json()['platformUserId']
    playdict[pnm] = pid
    playlist.append(pnm)
    prtplaylist.append(str(len(prtplaylist) + 1) + '. ' + pnm)
    cc()
    print('You now have ' + str(len(playlist)) + ' in your WatchParty\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\nWould you like to add another?\n1. Yes\n2. No')
    direc = input('')
    if direc == '1':
        add()
    if direc == '2':
        main()
def dele():
    global prtplaylist
    global playdict
    global playlist
    a = 0
    if len(playlist) == 0:
        cc()
        print('You have reached the min amount of players, sending you back in \n3')
        time.sleep(1)
        cc()
        print('You have reached the min amount of players, sending you back in \n3\n2')
        time.sleep(1)
        cc()
        print('You have reached the min amount of players, sending you back in \n3\n2\n1')
        time.sleep(1)
        main()
    cc()
    print('You have ' + str(len(playlist)) + ' in your WatchParty\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\nWhich number player would you like to delete?')
    playnum = input('')
    del playdict[playlist[(int(playnum) - 1)]]
    del playlist[(int(playnum) - 1)]
    prtplaylist = []
    a = 0
    while a < len(playlist):
        prtplaylist.append(str(a + 1) + '. ' + playlist[a])
        a = a + 1
    cc()
    print('You have ' + str(len(playlist)) + ' in your WatchParty\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\nWould you like to delete another?\n1. Yes\n2. No')
    direc = input('')
    if direc == '1':
        dele()
    if direc == '2':
        main()
def res():
    global prtplaylist
    global playdict
    global playlist
    playlist = []
    playdict = {}
    prtplaylist = []
    main()
def load():
    global prtplaylist
    global playdict
    global playlist
    if len(playlist) == 10:
        cc()
        print('You have reached the max amount of players, sending you back in \n3')
        time.sleep(1)
        cc()
        print('You have reached the max amount of players, sending you back in \n3\n2')
        time.sleep(1)
        cc()
        print('You have reached the max amount of players, sending you back in \n3\n2\n1')
        time.sleep(1)
        main()
    cc()
    print('You have ' + str(len(playlist)) + ' in your WatchParty\n------------------\n' + '\n'.join(prtplaylist) + '\n------------------\nWhat is the WatchParty URL?')
    wpurl = input('')
    wpurl = wpurl.split('watch#')[1].split(',')
    a = 0
    metaid = requests.get('https://fortnitetracker.com/events/' + evpath + '/watch').text.split('metaEventId: ')[1].split(',')[0]
    nplist = []
    npdict = {}
    while a < len(wpurl):
        obj = requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + wpurl[a]).json()
        lst = eval(str(obj['accountNames'].keys()).split('(')[1].split(')')[0])
        lst.sort()
        pnm = requests.get('https://fortnitetracker.com/api/v0/profiles/find?platformUserId=' + lst[0]).json()['platformUserHandle']
        pid = requests.get('https://fortnitetracker.com/api/v0/profiles/find?platformUserId=' + lst[0]).json()['platformUserId']
        nplist.append(pnm)
        npdict[pnm] = pid
        a = a + 1
    nplist2 = []
    for i in nplist:
        if i not in nplist2:
            nplist2.append(i)
    a = 0
    nplist = nplist2
    while a < len(nplist):
        if len(playlist) == 10:
            cc()
            print('You have reached the max amount of players, sending you back in \n3')
            time.sleep(1)
            cc()
            print('You have reached the max amount of players, sending you back in \n3\n2')
            time.sleep(1)
            cc()
            print('You have reached the max amount of players, sending you back in \n3\n2\n1')
            time.sleep(1)
            main()
        prtplaylist.append(str(len(prtplaylist) + 1) + '. ' + nplist[a])
        playlist.append(nplist[a])
        playdict[nplist[a]] = npdict[nplist[a]]
        a = a + 1
    main()
def wp():
    global prtplaylist
    global playdict
    global playlist
    global evpath
    spc = '          '
    grank = '    '
    gepc = '                                                    '
    gwns = '    '
    gmchs = '              '
    gpts = '      '
    metaid = requests.get('https://fortnitetracker.com/events/' + evpath + '/watch').text.split('metaEventId: ')[1].split(',')[0]
    a = 0
    header = 'Rank' + spc + 'Points' + spc + 'Matches Played' + spc + 'Wins' + spc + 'Epic Names'
    lb = '------------------------------------------------------------------------------------------------------------------------'
    strlist = []
    strdict = {}
    while a < len(playlist):
        obj = requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + playdict[playlist[a]]).json()
        if obj == {'error': 'Could not find this players team.'}:
            bs = 'NO DATA        '
            strlist.append(10000 + a)
            strdict[10000 + a] = '                   ' + 'NO DATA        ' + playlist[a]
        else:
            b = 0
            plslist = []
            lst = eval(str(obj['accountNames'].values()).split('(')[1].split(')')[0])
            while b < len(obj['accountNames']):
                plslist.append(lst[b])
                b = b + 1
            plslist.sort()
            pls = ', '.join(plslist)
            rank = obj['rank']['rank']
            wns = obj['rank']['wins']
            mchs = obj['rank']['matchesPlayed']
            pts = obj['rank']['pointsEarned']
            strlist.append(rank)
            strdict[rank] = str(rank) + grank[len(str(rank)):] + spc + str(pts) + gpts[len(str(pts)):] + spc + str(mchs) + gmchs[len(str(mchs)):] + spc + str(wns) + gwns[len(str(wns)):] + spc + pls + gepc[len(pls):]
        a = a + 1
    a = 0
    strlist.sort()
    wplist = []
    while a < len(strlist):
        wplist.append(strdict[strlist[a]])
        a = a + 1
    cc()
    print(header + '\n' + lb + '\n' + ('\n' + lb + '\n').join(wplist) + '\n' + lb + '\n' + 'What would you like to do?\n1. Refresh Data\n2. Return\n3. View Team Match History\n4. Check to see if team is in match')
    direc = input('')
    if direc == '1':
        wp()
    if direc == '2':
        main()
    if direc == '3':
        tmh()
    if direc == '4':
        tml()
def tmh():
    global prtplaylist
    global playdict
    global playlist
    global evpath
    metaid = requests.get('https://fortnitetracker.com/events/' + evpath + '/watch').text.split('metaEventId: ')[1].split(',')[0]
    a = 0
    tmplaylist = []
    while a < len(playdict):
        pls = eval(str(requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + playdict[playlist[a]]).json()['accountNames'].values()).split('(')[1].split(')')[0])
        pls.sort()
        pls = ', '.join(pls)
        tmplaylist.append(str(len(tmplaylist) + 1) + '. ' + pls)
        a = a + 1
    longlist = [tmplaylist[0]]
    a = 0
    while a < len(tmplaylist):
        if len(longlist[0]) < len(tmplaylist[a]):
            longlist = [tmplaylist[a]]
        a = a + 1
    bs = '-'*len(longlist[0]) + '--'
    cc()
    print(bs + '\n' + '\n'.join(tmplaylist) + '\n' + bs + '\nWhich team would you like to view?')
    tmlook = input('')
    mh = requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + playdict[playlist[int(tmlook) - 1]]).json()['sessions']
    mh.reverse()
    a = 0
    gmdata = []
    ptsbs = '             '
    killsbs = '     '
    plcbs = '         '
    spc = '   '
    gnbs = '  '
    bs = '-'*39
    bs2 = '--|------------------------------------|'
    hd = 'GN' + '|' + spc + 'Kills' + spc + 'Placement' + spc + 'Points Earned'
    lb = '-'*39
    while a < len(mh):
        gm = mh[a]
        plc = str(gm['placement'])
        kills = str(gm['eliminations'])
        pts = str(gm['points'])
        gn = str(a + 1)
        gmdata.append(gn + gnbs[len(gn):] + '|' + spc + kills + killsbs[len(kills):] + spc + plc + plcbs[len(plc):] + spc + pts + ptsbs[len(pts):] + '|')
        if (a + 1) != len(mh):
            gmdata.append(bs2)
        a = a + 1
    cc()
    print(tmplaylist[int(tmlook)-1][3:] + '\n' + lb + '\n' + 'GN|   Kills   Placement   Points Earned|' + '\n' + bs2 + '\n' + '\n'.join(gmdata) + '\n' + lb + '\nWhat would you like to do?\n1. Refresh Data\n2. Change Teams\n3. Return to WatchParty')
    direc = input('')
    if direc == '1':
        tmh2(tmplaylist, tmlook)
    if direc == '2':
        tmh()
    if direc == '3':
        wp()
def tmh2(tmplaylist, tmlook):
    global prtplaylist
    global playdict
    global playlist
    global evpath
    mh = requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + playdict[playlist[int(tmlook) - 1]]).json()['sessions']
    mh.reverse()
    a = 0
    gmdata = []
    ptsbs = '             '
    killsbs = '     '
    plcbs = '         '
    spc = '   '
    gnbs = '  '
    bs = '-'*39
    bs2 = '--|------------------------------------|'
    hd = 'GN' + '|' + spc + 'Kills' + spc + 'Placement' + spc + 'Points Earned'
    lb = '-'*39
    while a < len(mh):
        gm = mh[a]
        plc = str(gm['placement'])
        kills = str(gm['eliminations'])
        pts = str(gm['points'])
        gn = str(a + 1)
        gmdata.append(gn + gnbs[len(gn):] + '|' + spc + kills + killsbs[len(kills):] + spc + plc + plcbs[len(plc):] + spc + pts + ptsbs[len(pts):] + '|')
        if (a + 1) != len(mh):
            gmdata.append(bs2)
        a = a + 1
    cc()
    print(tmplaylist[int(tmlook)-1][3:] + '\n' + lb + '\n' + 'GN|   Kills   Placement   Points Earned|' + '\n' + bs2 + '\n' + '\n'.join(gmdata) + '\n' + lb + '\nWhat would you like to do?\n1. Refresh Data\n2. Change Teams\n3. Return to WatchParty')
    direc = input('')
    if direc == '1':
        tmh2(tmplaylist, tmlook)
    if direc == '2':
        tmh()
    if direc == '3':
        wp()
def tml():
    global prtplaylist
    global playdict
    global playlist
    global evpath
    metaid = requests.get('https://fortnitetracker.com/events/' + evpath + '/watch').text.split('metaEventId: ')[1].split(',')[0]
    a = 0
    tmplaylist = []
    while a < len(playdict):
        pls = eval(str(requests.get('https://fortnitetracker.com/api/v0/events/watch/' + metaid + '/' + playdict[playlist[a]]).json()['accountNames'].values()).split('(')[1].split(')')[0])
        pls.sort()
        pls = ', '.join(pls)
        tmplaylist.append(str(len(tmplaylist) + 1) + '. ' + pls)
        a = a + 1
    longlist = [tmplaylist[0]]
    a = 0
    while a < len(tmplaylist):
        if len(longlist[0]) < len(tmplaylist[a]):
            longlist = [tmplaylist[a]]
        a = a + 1
    bs = '-'*len(longlist[0]) + '--'
    cc()
    print(bs + '\n' + '\n'.join(tmplaylist) + '\n' + bs + '\nWhich team would you like to view?')
    tmlook = input('')
    pnm = playlist[int(tmlook) - 1]
    pid = playdict[playlist[int(tmlook) - 1]]
    ldb = requests.get('https://fortnitetracker.com/api/v3/events/' + evpath + '?q=' + pnm).json()['leaderboard']['entries']
    obj = []
    a = 0
    while a < len(ldb):
        tm = ldb[a]
        if pid in str(tm):
            obj.append(tm)
        a = a + 1
    obj = obj[0]
    if 'liveSessionId' not in obj:
        cc()
        print('The player ' + pnm + ' is not in a live match\n1. Refresh Data\n2. Change Player\n3. Return to WatchParty')
        direc = input('')
        if direc == '1':
            tml2(pnm, pid)
        if direc == '2':
            tml()
        if direc == '3':
            wp()
    cc()
    print(pnm + ' Live Session ID: ' + obj['liveSessionId'] + '\n1. Change Player\n2. Return to WatchParty')
    direc = input('')
    if direc == '1':
        tml()
    if direc == '2':
        wp()
def tml2(pnm, pid):
    global prtplaylist
    global playdict
    global playlist
    global evpath
    ldb = requests.get('https://fortnitetracker.com/api/v3/events/' + evpath + '?q=' + pnm).json()['leaderboard']['entries']
    obj = []
    a = 0
    while a < len(ldb):
        tm = ldb[a]
        if pid in str(tm):
            obj.append(tm)
        a = a + 1
    obj = obj[0]
    if 'liveSessionId' not in obj:
        cc()
        print('The player ' + pnm + ' is not in a live match\n1. Refresh Data\n2. Change Player\n3. Return to WatchParty')
        direc = input('')
        if direc == '1':
            tml2(pnm, pid)
        if direc == '2':
            tml()
        if direc == '3':
            wp()
    cc()
    print(pnm + ' Live Session ID: ' + obj['liveSessionId'] + '\n1. Change Player\n2. Return to WatchParty')
    direc = input('')
    if direc == '1':
        tml()
    if direc == '2':
        wp()
evseldirec()
