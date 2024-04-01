#Hint System

def qAndA():
    print("\n\n\nWelcome to Night Among The Tree's Q&A System!")
    print("Here you can get some questions you might have")
    print("about the game answered.")
    print("But I encourage you to explore the game first before")
    print("looking at these!")
    hints1()

def hints1():
    print("\n\n\n")
    print("Please enter the number of the question you want an")
    print("answer to, such as '1'.\n")
    print("This first page is for early game questions.\n")
    print("1. Where should I go first?")
    print("2. How can I get into the gift shop?")
    print("3. How can I navigate the woods?")
    print("4. Where can I find a gift for Ms. Ravenlock?")
    print("5. Can I climb the rockslide?")
    print("6. How can I beat the game?")
    print("Enter 'n' to go to the next set of questions.")
    print("Enter 'e' to return to the title screen.")
    i = input("\nI would like to... ")
    if i == '1':
        print("\nGo to the factory first. Make sure to check out the")
        print("outside area and grab the gloves before turning on the power.")
        x = input("\nPress enter when ready.")
    elif i == '2':
        print("\nYou need to turn on the power first.")
        print("This can be done in the factory.")
        x = input("\nPress enter when ready.")
    elif i == '3':
        print("\nThe woods are very tricky to navigate.")
        print("However, any time you enter them you will start at the same location,")
        print("regardless of where you entered from.")
        print("However, beware! If you go into the woods without the compass you are already dead.")
        x = input("\nPress enter when ready.")
    elif i == '4':
        print("\nThe gift for Ms. Ravenlock is located outside the factory.")
        x = input("\nPress enter when ready.")
    elif i == '5':
        print("\nYou cannot climb the rockslide until late in the game.")
        print("I recommend focusing on other areas before then.")
        x = input("\nPress enter when ready.")
    elif i == '6':
        print("\nThere are two good endings to the game.")
        print("First, you can escape the monster among the trees.")
        print("To do this you need quite a few items, so I do not recommend trying this")
        print("until you feel adequately prepared.")
        print("Question 13 will list the items you need if you want to know though!")
        x = input("\nPress enter when ready.")
    elif i == 'n':
        hints2()
    elif i == 'e':
        return
    else:
        pass
    hints1()


def hints2():
    print("\n\n\n")
    print("Please enter the number of the question you want an")
    print("answer to, such as '1'.\n")
    print("This second page is for middle game questions.\n")
    print("7. What is the 'bus pass'?")
    print("8. Where is the cabin?/How can I survive the cabin?")
    print("9. What items do I need from the cabin?")
    print("10. How can I access the gift shop backroom?")
    print("11. What are the key areas in the woods and how do I reach them?")
    print("12. How can I reach the item stuck in a tree near the campfire?")
    print("Enter 'n' to go to the next set of questions.")
    print("Enter 'b' to go to the previous page.")
    i = input("\nI would like to... ")
    if i == '7':
        print("\nThe notebook you find in the gift shop can be used as your bus pass.")
        x = input("\nPress enter when ready.")
    elif i == '8':
        print("\nYou can reach the cabin by sleeping on the bus bench. Once you're in the cabin,")
        print("be polite and wait to see what they want. Then eat the slop, but only one bite.")
        print("Say thank you, or say nothing, just don't eat another spoonful.")
        print("You then will be able to move about the cabin! But be cautious...")
        x = input("\nPress enter when ready.")
    elif i == '9':
        print("\nYou need the rope, the whistle, and a hook from the cabin.")
        print("First, go into the connecting room and slowly take the hook.")
        print("Then get the rope and whistle from the pile of items.")
        print("After this, escape the cabin by going through the window.")
        print("However, beware! If you go to the cabin without the compass you are already dead.")
        print("Oh, and try the rockslide again after you get these items...")
        x = input("\nPress enter when ready.")
    elif i == '10':
        print("\nYou cannot access the gift shop backroom until late in the game.")
        print("I recommend focusing on other areas before then.")
        x = input("\nPress enter when ready.")
    elif i == '11':
        print("\nFollow these paths after entering the woods to reach the key areas.")
        print("However, beware! If you go into the woods without the compass you are already dead.")
        print("Campfire: Forward, forward.")
        print("Cave: Right, left left. (Go left, not right in the cave.)")
        print("Journal page location: left, left, left.")
        print("Dog: forward, right, left, right, backward.")
        x = input("\nPress enter when ready.")
    elif i == '12':
        print("\nYou need the softball from the cabin.")
        print("However, you cannot win if you don't get the whistle and rope, so seeing this journal")
        print("entry does ultimately result in a game over.")
        print("If you do escape the cabin after getting the softball, go forward, forward in the woods.")
        x = input("\nPress enter when ready.")
    elif i == 'n':
        hints3()
    elif i == 'b':
        return
    else:
        pass
    hints2()


def hints3():
    print("\n\n\n")
    print("Please enter the number of the question you want an")
    print("answer to, such as '1'.\n")
    print("This last page is for end game questions.\n")
    print("13. What items do I need to beat the monster among the trees?")
    print("14. How can I get the compass?")
    print("15. How can I get the key needed for the trapdoor?")
    print("16. What is the answer to the time puzzle?")
    print("17. How can I get the key for the manager's desk?")
    print("18. What is the creator's favorite ending and how do I reach it?")
    print("Enter 'b' to go to the previous page.")
    i = input("\nI would like to... ")
    if i == '13':
        print("\nYou first need to veer right, and then run at the wolves.")
        print("Then you will be safe if you have...")
        print("1. Fully befriended the dog. (the game will tell you when you do!)")
        print("2. Made the grappling hook by taking the rope and hook to the rockslide.")
        print("3. Gotten the compass.")
        print("4. Kept the electricity on.")
        print("...and input all the prompts in a timely manner!")
        print("Additionally, if you have the camera and film you can take a picture of the monster,")
        print("unlocking a secret ending.")
        print("Or if you got the diamond from the cave: this too unlocks a secret ending.")
        print("And of course, if you have both, this unlocks an even more secret ending!")
        x = input("\nPress enter when ready.")
    elif i == '14':
        print("\nTo get the compass, perhaps the most valuable item in the game,")
        print("you must first find The Midnight Bus by waiting for the real bus.")
        print("You must then present the notebook you got from the gift shop as your bus pass.")
        print("Talk to the driver until you can input a unique sentence.")
        print("Type in the next line exactly as it appears:")
        print("I want to come back")
        print("And then you will get the bus compass! You can go into and come back from the woods")
        print("as you please.")
        print("Also, the time spent in the woods will reset every time you leave, so don't worry about")
        print("running into the monster among the trees too much.")
        x = input("\nPress enter when ready.")
    elif i == '15':
        print("\nThe key to the trapdoor will be given to you by Ms. Ravenlock.")
        print("Just follow the rules and she will give it to you.")
        x = input("\nPress enter when ready.")
    elif i == '16':
        print("\nThis is a really fun puzzle, but if you really want to know type 'imaloser'")
        l = input("I would like to... ")
        if l.lower() == "imaloser":
            print("\nThe answer is 1849562. Also totally lame as to not solve it on your own.")
            x = input("\nPress enter when ready.")
        else:
            print("\nAwesome choice!!!")
            x = input("\nPress enter when ready.")
    elif i == '17':
        print("\nThe dog has the key to the manager's desk.")
        print("Visit the dog with the whistle and the plushie and you can get it.")
        x = input("\nPress enter when ready.")
    elif i == '18':
        print("\nMy favorite ending is ending #4!")
        print("In the cabin, wait until you can roam around.")
        print("Then go to the connecting room.")
        print("Choose to stand still, and then choose to take the item the figure offers to you.")
        x = input("\nPress enter when ready.")
    elif i == 'b':
        return
    else:
        pass
    hints3()


if __name__ == "__main__":
    qAndA()
