"""
    HW 10: Music Recommender+
    Max Shi
    11/13/2018
    I pledge my honor that I have abided by the Stevens Honor System
"""

SAMPLE_FILE_CONTENT = ['dave:alanis Morrisset, Khaled, Michael Jackson','sue:Kate Bush,Nirvana,Michael Jackson']
SAMPLE_DATA = [['Dave', 'Sue'],[['alanis morrisset', 'khaled', 'michael jackson'], ['kate bush', 'nirvana', 'michael jackson']],1]

from cs115 import filter


def loadFiles():
    """Load file from musicrecplus.txt and return data"""
    filenames = []
    fileartists = []
    try:
        input_file = open("musicrecplus.txt",'r')
        #input_file = SAMPLE_FILE_CONTENT
        for line in input_file:
            name, artists = line.split(':')
            artists = artists.split(',')
            for i in range(len(artists)):
                artists[i] = artists[i].strip().lower()
            artists.sort()
            fileartists += [artists]
            filenames += [name.strip()]
        input_file.close()
    except IOError:
        pass
    return [filenames, fileartists]


def getIntersection(listA, listB):
    """Get the intersection between two lists sorted with python built in sort()"""
    #print("list A: "+str(listA))
    #print("list B: "+str(listB))
    if listA == [] or listB == []: return []
    else:
        if listA[0] == listB[0]: 
            return [listA[0]]+getIntersection(listA[1:],listB[1:])
        elif listA[0]<listB[0]: 
            return getIntersection(listA[1:],listB)
        else: 
            return getIntersection(listA, listB[1:])

def getNameIndex(names):
    """Get the index of the user given username, or append one if the user is new"""
    userIndex = -1
    userName = input("Please input your name:")
    userName = userName.title()
    if userName in names:
        userIndex = names.index(userName)
    else: 
        userIndex = len(names)
        names += [userName]
    #print(userIndex)
    return userIndex

'''
DICTIONARY DEFINED FUNCTIONS
data = [list of names, list of artists, current user index]
All functions below with parameter (data) use this format
'''
def setPreferences(data):
    """Prompts the user to input their preferences and overrides the old ones and returns True to continue program"""
    userInput = "filler"
    userIndex = data[2]
    userArtists = []
    while(userInput):
        userInput = input("Enter an artist that you like (Enter to finish):")
        userInput = userInput.strip().lower()
        if(userInput != ""):
            userArtists += [userInput]
    userArtists.sort()
    if(userIndex == len(data[1])):
        data[1] += [userArtists]
    else: data[1][userIndex] = userArtists
    #print(userArtists)
    return True
def getRecommendations(data):
    """Gets artist recommendations from public users and returns True to continue program"""
    #print(data)
    recommendations = []
    userArtists = data[1][data[2]]
    mostCommonCount = 2
    for index in range(len(data[1])):
        if(data[0][index][-1] != '$'):
            artists = data[1][index]
            if not (userArtists == artists):
                common = getIntersection(userArtists, artists)
                #print("common " + str(common))
                if(len(common)>mostCommonCount):
                    recommendations = []
                    mostCommonCount = len(common)
                    for entry in artists:
                        if not(entry in userArtists):
                            recommendations += [entry]
                elif(len(common) == mostCommonCount):
                    for entry in artists:
                        if (entry not in userArtists) and (entry not in recommendations):
                            recommendations += [entry]
    if len(recommendations)==0:
        print("No recommendations available at this time")
    else:
        for entry in recommendations:
            print(entry)
    return True
def getPopular(data):
    """Prints the most popular artist(s) and returns True to continue program"""
    popularity = {}
    maxOccurrences = 0
    for index in range(len(data[1])):
        if(data[0][index][-1] != '$'):
            userList = data[1][index]
            for entry in userList:
                if entry in popularity:
                    popularity[entry] += 1
                    num = popularity[entry]
                    if(num > maxOccurrences): maxOccurrences = num
                else: 
                    popularity[entry] = 1
                    if(1>maxOccurrences): maxOccurrences = 1
    mostPopular = filter(lambda entry: popularity[entry] == maxOccurrences, popularity.keys())
    if (mostPopular == []): print("Sorry, no artists found.")
    else: 
        for entry in mostPopular:
            print(entry)
    return True
def getHowPopular(data):
    """Prints how popular the most popular artist is and returns True to continue program"""
    popularity = {}
    maxOccurrences = 0
    for index in range(len(data[1])):
        if(data[0][index][-1] != '$'):
            userList = data[1][index]
            for entry in userList:
                if entry in popularity:
                    popularity[entry] += 1
                    num = popularity[entry]
                    if(num > maxOccurrences): maxOccurrences = num
                else: 
                    popularity[entry] = 1
                    if(1>maxOccurrences): maxOccurrences = 1
        print(maxOccurrences if maxOccurrences>0 else "Sorry, no artists found.")
    return True
def getMostUser(data):
    """Prints the public user who likes the most music and returns True to continue program""" 
    maxEntries = 0
    usernames = []
    for index in range(len(data[1])):
        if(data[0][index][-1] != '$'):
            numEntries = len(data[1][index])
            #print(str(numEntries)+" : "+str(maxEntries))
            if(numEntries>maxEntries): 
                usernames = [data[0][index]]
                maxEntries = numEntries
            elif(numEntries == maxEntries): usernames += [data[0][index]]
    if(usernames != []):
        usernames.sort()
        for name in usernames:
            print(name)
    else: print("Sorry, no user found.")
    return True
def quitProg(data):
    """Save data and return false to quit program"""
    recFile = open("musicrecplus.txt",'w')
    for index in range(len(data[0])):
        line = str(data[0][index])+" : "+str(data[1][index])[1:-1].replace('\'','')+'\n'
        #print(data[1][index])
        recFile.write(line) 
    return False

def menuInput():
    """Get user input from main menu"""
    menu = \
    '''Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
'''
    return input(menu)

#dictionary defined commands
userPossibleChoices = { \
    'e':setPreferences, \
    'r':getRecommendations, \
    'p':getPopular, \
    'h':getHowPopular, \
    'm':getMostUser, \
    'q':quitProg  \
    }
    


def main():
    """main function for music recommender"""
    #load data
    data = loadFiles()
    filenames = data[0]
    fileartists = data[1]
    
    #get user index
    userIndex = getNameIndex(filenames)
    totalData = [filenames, fileartists, userIndex]
    #new user initialization
    if(userIndex == len(fileartists)):
        setPreferences(totalData)

    #begin program functionality
    continueProg = True
    while(continueProg):
        userChoice = menuInput()
        if userChoice in userPossibleChoices:
            continueProg = userPossibleChoices[userChoice](totalData)
        else:
            print("Invalid command, try again.")
"""
loadFiles()
printData()
main()
"""
if __name__ == "__main__":
    main()
    


