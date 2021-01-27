import json
from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
import re
import pandas as pd

#Looking at Player Stats

def main():
    Soup = EnterName()
    Data = DataGrab(Soup)
    GrabData = Table(Data)
    PlayerStats = ShowData(GrabData)
    print(PlayerStats)
    
    


def EnterName():




    InputFirst = str(input("First Name: "))
    InputLast = str(input("Last Name: "))
    InputFirst = InputFirst.lower()
    InputLast = InputLast.lower()
            
    url = "https://www.nfl.com/players/"+ InputFirst + "-" + InputLast + "/stats/"
           
    page = urlopen(url)
    page_html = page.read()
    page.close()
    pagesoup = soup(page_html, "html.parser")
            

    return pagesoup
    

def DataGrab(Soup):
    
    pagesoup = Soup

    Decide = pagesoup.findAll("div", {"class": "nfl-t-stats__title"})

    DCLEAN = []

    for n in range(len(Decide)):

        Decided = Decide[n]
        Decided = Decided.prettify()
        DClean = re.sub("<.*?>", "", Decided)
        for n in DClean.split():
            DCLEAN.append(n)

    if len(DCLEAN) == 1:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] + "\n Input: "))

    elif len(DCLEAN) == 2:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] +  "\n Input: "))
        
    elif len(DCLEAN) == 3:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + "\n Input: "))
       

    elif len(DCLEAN) == 4:
        
        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + "\n Input: "))

    elif len(DCLEAN) == 5:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + " \n 4 = " + DCLEAN[4] + "\n Input: "))

    elif len(DCLEAN) == 6:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + " \n 4 = " + DCLEAN[4] + " \n 5 = " + DCLEAN[5] + "\n Input: "))

    elif len(DCLEAN) == 7:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + " \n 4 = " + DCLEAN[4] + " \n 5 = " + DCLEAN[5] + " \n 6 = " + DCLEAN[6] + "\n Input: "))

    elif len(DCLEAN) == 8:
        
        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + " \n 4 = " + DCLEAN[4] + " \n 5 = " + DCLEAN[5] + " \n 6 = " + DCLEAN[6] + " \n 7 = " + DCLEAN[7] + "\n Input: "))

    elif len(DCLEAN) == 9:

        Rusrec = int(input("Which stats would you like to view: \n 0 = " + DCLEAN[0] +  " \n 1 = " + DCLEAN[1] + " \n 2 = " + DCLEAN[2] + " \n 3 = " + DCLEAN[3] + " \n 4 = " + DCLEAN[4] + " \n 5 = " + DCLEAN[5] + " \n 6 = " + DCLEAN[6] + " \n 7 = " + DCLEAN[7] + " \n 8 = " + DCLEAN[8] + " \n Input: "))
   

    return DCLEAN, Rusrec, pagesoup


    

def Table(Data):

    DCLEAN = Data[0]

    Rusrec = Data[1]

    pagesoup = Data[2]
   

    Table = pagesoup.findAll("table", {"class":"d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]], debug: true}"})

    if DCLEAN[Rusrec] == "Rushing":

        Number = DCLEAN[Rusrec]

        Rushing = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = Rushing.prettify()

        Raw = re.sub("<.*?>", "", Raw)
        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)




            

        Year = []
        Team = []
        Yards = []
        Games = []
        Att = []
        Avg = []
        Lng = []
        TD =[]
        FirstDowns = []
        FirstPer = []
        TwentyPlus =[]
        FourtyPlus =[]
        Fumbled = []

        for n in range(14):
            for ele in range(n, len(Polished), 14):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Att.append(Polished[ele])
                elif n == 5:
                    Yards.append(Polished[ele])
                elif n == 6:
                    Avg.append(Polished[ele])
                elif n == 7:
                    Lng.append(Polished[ele])
                elif n ==8:
                    TD.append(Polished[ele])
                elif n == 9:
                    FirstDowns.append(Polished[ele])
                elif n == 10:
                    FirstPer.append(Polished[ele])
                elif n == 11:
                    TwentyPlus.append(Polished[ele])
                elif n == 12:
                    FourtyPlus.append(Polished[ele])
                elif n == 13:
                    Fumbled.append(Polished[ele])
                else:
                    print("N/A")
            





        m = len(Team)/2
        TeamProper =[]

        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)


        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Attempts": Att, "Yards" : Yards, "AVG" : Avg,  "Long": Lng, "TouchDowns": TD, "FirstDown%": FirstPer, "TwentyYardRuns": TwentyPlus, "FourtyYardRuns": FourtyPlus, "Fumbles": Fumbled}

    elif DCLEAN[Rusrec] == "Receiving":

        Receiving = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = Receiving.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        




            

        Year = []
        Team = []
        Yards = []
        Games = []
        Rec = []
        Avg = []
        Lng = []
        TD =[]
        FirstDowns = []
        FirstPer = []
        TwentyPlus =[]
        FourtyPlus =[]

        for n in range(13):
            for ele in range(n, len(Polished), 13):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Rec.append(Polished[ele])
                elif n == 5:
                    Yards.append(Polished[ele])
                elif n == 6:
                    Avg.append(Polished[ele])
                elif n == 7:
                    Lng.append(Polished[ele])
                elif n ==8:
                    TD.append(Polished[ele])
                elif n == 9:
                    FirstDowns.append(Polished[ele])
                elif n == 10:
                    FirstPer.append(Polished[ele])
                elif n == 11:
                    TwentyPlus.append(Polished[ele])
                elif n == 12:
                    FourtyPlus.append(Polished[ele])
                else:
                    print("N/A")

        m = len(Team)/2
        TeamProper =[]

        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)

        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Receptions": Rec, "Yards" : Yards, "AVG" : Avg,  "Long": Lng, "TouchDowns": TD, "FirstDown": FirstDowns, "FirstDown%": FirstPer, "TwentyYardRuns": TwentyPlus, "FourtyYardRuns": FourtyPlus}

        
    elif DCLEAN[Rusrec] == "Fumbles":

        Fumbles = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = Fumbles.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        Year = []
        Team = []
        Fum = []
        Games = []
        Lost = []
        FF = []
        OwnFR = []
        OppFR =[]
        TD = []

        for n in range(10):
            for ele in range(n, len(Polished), 10):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Fum.append(Polished[ele])
                elif n == 5:
                    Lost.append(Polished[ele])
                elif n == 6:
                    FF.append(Polished[ele])
                elif n == 7:
                    OwnFR.append(Polished[ele])
                elif n == 8:
                    OppFR.append(Polished[ele])
                elif n == 9:
                    TD.append(Polished[ele])
                else:
                    print("N/A")

        m = len(Team)/2
        TeamProper =[]

        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)

        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Attempts": Att, "Fumbles": Fum, "Lost" : Lost,  "Forced Fum": FF, "Own FR": OwnFR, "Opp FR": OppFR , "TD": TD}


    elif DCLEAN[Rusrec] == "Defense":

        Defense = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = Defense.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        Year = []
        Team = []
        Solo = []
        Total = []
        Games = []
        AST = []
        SCK = []
        SFTY = []
        PDEF =[]
        INT = []
        TDS = []
        YDS = []
        AVG = []
        LNG = []

        for n in range(15):
            for ele in range(n, len(Polished), 15):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Total.append(Polished[ele])
                elif n == 5:
                    Solo.append(Polished[ele])
                elif n == 6:
                    AST.append(Polished[ele])
                elif n == 7:
                    SCK.append(Polished[ele])
                elif n ==8:
                    SFTY.append(Polished[ele])
                elif n == 9:
                    PDEF.append(Polished[ele])
                elif n == 10:
                    INT.append(Polished[ele])
                elif n == 11:
                    TDS.append(Polished[ele])
                elif n == 12:
                    YDS.append(Polished[ele])
                elif n == 13:
                    AVG.append(Polished[ele])
                elif n == 14:
                    LNG.append(Polished[ele])
                else:
                    print("N/A")

        m = len(Team)/2
        TeamProper =[]

        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)

        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Total": Total, "Solo": Solo, "Assist" : AST,  "Sack": SCK, "Safety": SFTY, "Pass Def": PDEF , "INT": INT, "TDS": TD, "Yards": YDS, "AVG": AVG, "Long": LNG}


    elif DCLEAN[Rusrec] == "Passing":

        Passing = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = Passing.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        Year = []
        Team = []
        Att = []
        Comp = []
        PCT = []
        YDS = []
        AVG = []
        LNG = []
        TD =[]
        INT = []
        FIRST = []
        FIRSTPER = []
        Twenty = []
        SCK = []
        SCKY = []
        RATE = []
        Games = []
        
        for n in range(18):
            for ele in range(n, len(Polished), 18):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Att.append(Polished[ele])
                elif n == 5:
                    Comp.append(Polished[ele])
                elif n == 6:
                    PCT.append(Polished[ele])
                elif n == 7:
                    YDS.append(Polished[ele])
                elif n ==8:
                    AVG.append(Polished[ele])
                elif n == 9:
                    LNG.append(Polished[ele])
                elif n == 10:
                    TD.append(Polished[ele])
                elif n == 11:
                    INT.append(Polished[ele])
                elif n == 12:
                    FIRST.append(Polished[ele])
                elif n == 13:
                    FIRSTPER.append(Polished[ele])
                elif n == 14:
                    Twenty.append(Polished[ele])
                elif n == 15:
                    SCK.append(Polished[ele])
                elif n == 16:
                    SCKY.append(Polished[ele])
                elif n == 17:
                    RATE.append(Polished[ele])
                else:
                    print("N/A")

        m = len(Team)/2
        TeamProper =[]

        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)

        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Attempts": Att, "Completions": Comp, "Percentage" : PCT,  "Yards": YDS, "LNG": LNG, "TD": TD, "INT": INT, "FIRST": FIRST, "First Down Percentage": FIRSTPER, "Twenty Plus": Twenty, "Sack": SCK, "SCKY": SCKY, "Rate": RATE }

    elif DCLEAN[Rusrec] ==  "Kick Return":

        KickRet = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = KickRet.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        Year = []
        Team = []
        Ret = []
        Games = []
        YDS = []
        AVG = []
        LNG = []
        TD =[]
        Twenty = []
        Fourty = []
        FC = []
        Fum = []

        for n in range(13):
            for ele in range(n, len(Polished), 13):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Ret.append(Polished[ele])
                elif n == 5:
                    YDS.append(Polished[ele])
                elif n == 6:
                    AVG.append(Polished[ele])
                elif n == 7:
                    LNG.append(Polished[ele])
                elif n ==8:
                    TD.append(Polished[ele])
                elif n == 9:
                    Twenty.append(Polished[ele])
                elif n == 10:
                    Fourty.append(Polished[ele])
                elif n == 11:
                    FC.append(Polished[ele])
                elif n == 12:
                    Fum.append(Polished[ele])
                else:
                    print("N/A")


        
        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)

        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Ret Yards": Ret, "Yards": YDS, "Average" : AVG, "LNG": LNG, "TD": TD, "Twenty Plus": Twenty, "Fourty Plus": Fourty, "Fair Catch": FC, "Fumbles": FUM }

    elif DCLEAN[Rusrec] == "Punt Return":

        PuntRet = Table[Rusrec].tbody

        Classy = "class"

        Class = Table[Rusrec].td[Classy]

        Class = Class[0]

        Gen = Classy + '="' + Class + '">'

        Raw = PuntRet.prettify()

        Raw = re.sub("<.*?>", "", Raw)

        Polished = []

        for n in Raw.split():
            Polished.append(n)

        Third = ['Patriots', 'Jets', 'Chargers', 'Rams', 'Chiefs', 'Saints', 'Raiders', 'Giants', 'Chargers', '49ers', 'Buccaneers', 'Team']

        Popped = []

        for word in range(len(Polished)):
            Word = Polished[word]
            for n in Third:
                if Word == n:
                    Popped.append(word)

        for n in range(len(Popped)):
            Polished.pop(Popped[n]-n)

        Year = []
        Team = []
        Ret = []
        Games = []
        YDS = []
        AVG = []
        LNG = []
        TD =[]
        Twenty = []
        Fourty = []
        FC = []
        Fum = []

        for n in range(13):
            for ele in range(n, len(Polished), 15):
                if n == 0:
                    Year.append(Polished[ele])
                elif n == 1:
                    Team.append(Polished[ele])
                elif n == 2:
                    Team.append(Polished[ele])
                elif n == 3:
                    Games.append(Polished[ele])
                elif n == 4:
                    Ret.append(Polished[ele])
                elif n == 5:
                    YDS.append(Polished[ele])
                elif n == 6:
                    AVG.append(Polished[ele])
                elif n == 7:
                    LNG.append(Polished[ele])
                elif n ==8:
                    TD.append(Polished[ele])
                elif n == 9:
                    Twenty.append(Polished[ele])
                elif n == 10:
                    Fourty.append(Polished[ele])
                elif n == 11:
                    FC.append(Polished[ele])
                elif n == 12:
                    Fum.append(Polished[ele])
                else:
                    print("N/A")


        
        for n in range(int(m)):
                Half = int(m)
                First, Last = Team[n], Team[Half + n]
                Teams = First + " " + Last
                TeamProper.append(Teams)


        Data = {"Year": Year, "Team": TeamProper, "Games": Games, "Ret Yards": Ret, "Yards": YDS, "Average" : AVG, "LNG": LNG, "TD": TD, "Twenty Plus": Twenty, "Fourty Plus": Fourty, "Fair Catch": FC, "Fumbles": FUM }

    return Data



def ShowData(Data):

    Data = Data

    Data = pd.DataFrame(Data)

    return Data



main()    
    

    


    


    

    
    







        
    
    
    
    
