
scienceFictionStories = ["","The *ADJECTIVE1 replicant ran through the *ADJECTIVE2 market. She glanced back and saw the *ADJECTIVE3 runner turning the corner. Within moments, she pulled out the *OBJECT1 from her belt. With the rain coming down, the *OBJECT1 slipped out of her hands.","The *ADJECTIVE1 crowbar held tightly in his hand, he swung furiously at the *ADJECTIVE2 barricade. Seeing *NAME on the other side surrounded by *NUM combine soldiers, he picked up the pace. Suddenly, an *OBJECT1 came flying at him from across the room."]

def welcome():
    print("Welcome to Mad Libs!")
    genreSelect()

def genreSelect():
    genre = ''
    print("Please select your genre from the list below!")
    print('')
    print('1. Science Fiction')
    print('2. Fantasy')
    x = input()
    if str(x) == '1':
        genre = 'Science Fiction'
    elif str(x) == '2':
        genre = 'Fantasy'
    chooseStory(genre)

def chooseStory(genre):
    print('Please choose your story from below!')
    if genre == 'Science Fiction':
        print("1. Replicant")
        print("2. City 17")
        x = input()
        if str(x) == '1':
            enterInformation(x)

def enterInformation(x):
    print('Please enter an adjective below:')
    userInput = input()
    i = 1
    adj = '*ADJECTIVE' + str(i)
    story = scienceFictionStories[int(x)]
    storySplit = story.split()
    index = storySplit.index(adj)
    storySplit[index] = str(userInput)
    storyJoined = " ".join(storySplit)
    print(storyJoined)

welcome()
