import pygame
from termcolor import colored # Module used to give color to the text
# Function to play the audio
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

# Initialize pygame
pygame.init()

# Main game loop
while True:
    play_audio("C:/Users/Shantanu/OneDrive/Desktop/MiniprojectTreasureHunt/welcome_sound.mp3")
    print(colored("* Welcome to Treasure Hunt Game! * ","red"))

    name = input("* Enter your name: ")
    print(f"Hello, {name}, Welcome to the treasure hunt game")
    print(colored('''You are on a quest to find the ancestral treasure
You've reached an island by sailing on a boat with the assistance of the half of the map you obtained''',"magenta"))
    print(colored('Now you want to find the key and the remaining half map which will help you to find the treasure','magenta'))
    print(colored("Best of luck for your treasure hunt journey","light_yellow"))
    print("You observe two paths; One leading to the"+colored(" forest ","green") +"and the other heading towards a"+ colored(" desert ","light_red"))

    location1 = input("Enter the location where you want to go: ")

    if (location1 == 'desert' or location1 == 'Desert'):
        print("You have arrived at the desert. You walked for a few miles and after some time\nTo your right, you spot a camel, and to your left, there's a pond of water.")
        location2 = input("Enter the location where you want to go: ")

        if (location2 == 'camel' or location2 == 'Camel'):
            print(colored('''You have reached the camel. You encounter a stranger who is the owner of the camel")
            You engaged in conversation with him, and accidentally revealed your quest for treasure and then he asked you for the treasure location but you didn't give him any information")
            However, he kills you because you didn't give him the information about the treasure''',"magenta"))
            print("Game Over!")

        elif (location2 == 'pond' or location2 == 'Pond'):
            print('* You kept on walking for hours, but that pond of water was just a mirage in the desert')
            print("You died due to dehydration\nGame Over")

        else:
            print('Invalid input')

    elif (location1 == 'forest' or location1 == 'Forest'):
        print("* You have arrived at the forest. There are two paths: one leads to "+colored('River',"blue") +" and the other heads to "+colored('forest track',"light_green"))
        path = input("Choose your Path: ")
        if (path == "River" or path == "river"):
            print("You tried to cross the River. Unfortunately, you were eaten by an alligator\nGame Over")
        elif (path == "Forest track" or path == "forest track"):
            print("There are two paths, one is on the 'Right' side, and the other is on the 'Left'")
            path_2 = input("Choose the further Path: ")
            if (path_2 == "Left" or path_2 == "left"):
                print("You lost your way, GAME OVER")
            elif (path_2 == "Right" or path_2 == "right"):
                print(colored("Congrats !🥳 you are close to the Treasure .Since you found the 'KEY' ","light_cyan"))
                from treasurekey import treasure_key
                
                print("There are 3 Caves in front of you, choose any one")
                cave = int(input("Enter the cave number you want to go ahead: "))
                if cave == 1:
                    print("You save the Village at the end of the Cave. You visited there and were killed by the Villagers\nGAME OVER")
                elif cave == 2:
                    print(colored(" You followed the map and finally got the TREASURE.\nCongratulations! 🥳 You won the GAME ","light_magenta"))
                    from tressurebox import tresure_hunt
                    
                elif cave == 3:
                    print("You were killed by a LION\nGAME OVER")
                else:
                    print("Invalid input")

    else:
        print("Invalid input")

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.lower() != "yes":
        print(f"Thanks for playing. Goodbye !{name}")
        break  # Exit the game loop

# Quit pygame when the game is over
pygame.quit()
