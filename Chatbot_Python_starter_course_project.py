"""
    A CHATBOT that can recommend movies, music, games by genre, jokes,
    tarot card with prediction, and also provide the opportunity to play a game
"""

import sys
import random
import pyjokes
from colorama import Fore, init
from art import tprint, art

init()


def print_menu():
    """Chatbot menu output function in the console"""

    print(Fore.RED + "")
    tprint("\nHello, I'm  a  funny  chatbot !!!")
    tprint("I  will  help  you  have  fun.")
    print(Fore.YELLOW + "\n1 - Would you like to play a game?", art("happy"))
    print("2 - Movie Recommendation", art("decorate"))
    print("3 - Music Recommendation", art("boombox2"))
    print("4 - Game Recommendation", art("gun1"))
    print("5 - Jokes for you", art("happy17"))
    print("6 - TAROT card of the day", art("playing cards"))
    print("0 - Finish")



def rock_scissors_paper():
    """Rock paper scissors function"""
    tprint("Rock  Paper  Scissors")

    options = ['rock', 'scissors', 'paper']

    while True:
        robot_choice = random.choice(options)
        user_input = input(Fore.YELLOW + "\nEnter: rock, scissors or paper (or 'stop' to finish): ").strip().lower()

        if user_input == 'stop':
            print("Thanks for playing! See you later", art("cute face6"))
            break
        if user_input not in options:
            print(Fore.RED + "Wrong choice. Try again.", art("sad and confused"))
            continue

        print(Fore.GREEN + art("robot3"), f"The robot chose: {robot_choice}")

        if user_input == robot_choice:
            print(Fore.BLUE + "Draw! Let's do it again", art("love4"))
        elif (
                (user_input == 'rock' and robot_choice == 'scissors') or
                (user_input == 'scissors' and robot_choice == 'paper') or
                (user_input == 'paper' and robot_choice == 'rock')):
            print(Fore.BLUE + "You win!", art("dunno3"))
        else:
            print("I win!", art("rare"))


def guess_the_number():
    """The game Guess the number"""
    tprint("Guess  the  number")

    print("\nHello, this is a game of guessing the number!")

    while True:
        bot_choices = random.randint(1, 10)

        try:
            user_choices = int(input(Fore.YELLOW + "\nEnter a number from 1 to 10, or enter 0 to exit: "))

            if user_choices == 0:
                print("See you later!", art("cute face6"))
                break
            elif 1 <= user_choices <= 10 and user_choices == bot_choices:
                print(Fore.BLUE + "You guessed it right!", art("dunno3"))
            elif 1 <= user_choices <= 10:
                print(Fore.RED + art("robot3"), f"Bot guessed {bot_choices}, you didn't guess, try again.",
                      art("sad and confused"))
            else:
                print("Enter the exact number from 1 to 10!!!", art("sad and confused"))
        except ValueError:
            print(Fore.RED + "You didn't enter a number. Try again.", art("sad and confused"))


def play_game1():
    """Select game function"""

    while True:
        print(Fore.YELLOW + "\nIf you want to play, choose a game.")
        print("\n1 - rock, scissors, paper")
        print("2 - guess the number")
        print("Enter - to finish")

        choice_game = input(Fore.BLUE + "Choose a game: ")

        if choice_game == "1":
            rock_scissors_paper()
        elif choice_game == "2":
            guess_the_number()
        else:
            print(Fore.RED + "Goodbye!", art("cute face6"))
            break


def movie_recommendation2():
    """A function that returns a random movie by genre"""
    tprint("Movie  Recommendation")

    genre_film = input(Fore.YELLOW + "\nEnter genre (Comedy, Action, Fantasy, Drama, Horror): ").lower().strip()

    film_dict = {
        "horror": ["Get Out (2017)", "The Shining (1980)", "Hereditary (2018)", "A Quiet Place (2018)",
                   "The Exorcist (1973)", "Halloween (1978), Us (2019)", "The Texas Chain Saw Massacre (1974)",
                   "Psycho (1960)", "The Babadook (2014)"],
        "comedy": ["Some Like It Hot (1959)", "Dr. Strangelove or: How I Learned to Stop Worrying and "
                                              "Love the Bomb (1964)", "Monty Python and the Holy Grail (1975)",
                   "Airplane! (1980)",
                   "Blazing Saddles (1974)", "When Harry Met Sally... (1989)", "Caddyshack (1980)", "Life of Brian "
                                                                                                    "(1979)",
                   "Shaun of the Dead (2004)", "Anchorman: The Legend of Ron Burgundy (2004)"],
        "action": ["Die Hard (1988)", "Mad Max: Fury Road (2015)", "The Matrix (1999)", "Terminator 2: "
                                                                                        "Judgment Day (1991)",
                   "John Wick (2014)", "Casino Royale (2006)", "Mission:Impossible – Fallout"
                                                               "(2018)", "Raiders of the Lost Ark (1981)",
                   "The Dark Knight (2008)", "Kill Bill: Volume 1 (2003)"],
        "fantasy": ["The Lord of the Rings: The Fellowship of the Ring (2001)", "Pan's Labyrinth (2006)",
                    "Harry Potter and the Prisoner of Azkaban (2004)", "The Princess Bride (1987)",
                    "Star Wars: Episode "
                    "V - The Empire Strikes Back (1980)", "Spirited Away (2001)", "The Wizard of Oz (1939)", "The Dark "
                                                                                                             "Crystal (1982)",
                    "Labyrinth (1986)", "Big Fish (2003)"],
        "drama": ["The Shawshank Redemption (1994)", "Forrest Gump (1994)", "Schindler's List (1993)",
                  "The Godfather (1972)", "12 Angry Men (1957)", "Pulp Fiction (1994)", "Fight Club (1999)",
                  "Goodfellas (1990)", "The Green Mile (1999)", "American History X (1998)"]
    }

    if genre_film in film_dict:
        film = random.choice(film_dict[genre_film])
        print(f"\nThe {genre_film} movie recommendation is: {film}", art("cute face6"))
    else:
        print("This genre is not on the list.", art("sad and confused"))

    input(Fore.RED + "\nPress enter to continue...")


def music_recommendation3():
    """A function that returns a random music"""
    tprint("Music  Recommendation")

    music_list = [
        "Hey Jude - The Beatles", "Bohemian Rhapsody - Queen", "Smells Like Teen Spirit - Nirvana",
        "Like a Rolling Stone - Bob Dylan", "What's Going On - Marvin Gaye", "Imagine - John Lennon",
        "Billie Jean - Michael Jackson", "One - U2", "I Will Always Love You - Whitney Houston", "Hotel California - "
                                                                                                 "Eagles",
        "Hallelujah - Leonard Cohen", "Lose Yourself - Eminem", "Mr. Brightside - The Killers", "Wonderwall "
                                                                                                "- Oasis",
        "Don't Stop Believin' - Journey", "...Baby One More Time - Britney Spears",
        "Single Ladies (Put a Ring on It) - Beyoncé", "All of Me - John Legend", "Rolling in the Deep - Adele",
        "Despacito - Luis Fonsi feat. Daddy Yankee", "Bad Guy - Billie Eilish", "Blinding Lights - The Weeknd",
        "Old Town Road - Lil Nas X ft. Billy Ray Cyrus", "The Box - Roddy Ricch", "God's Plan - Drake",
        "Uptown Funk - Mark Ronson ft. Bruno Mars", "Thinking Out Loud - Ed Sheeran", "Happy - Pharrell Williams",
        "Get Lucky - Daft Punk ft. Pharrell Williams", "Can't Hold Us - Macklemore & Ryan Lewis ft. Ray Dalton",
        "Radioactive - Imagine Dragons", "Shake It Off - Taylor Swift", "Let It Go - Idina Menzel",
        "Shallow - Lady Gaga & Bradley Cooper", "The Sound of Silence - Simon & Garfunkel",
        "My Heart Will Go On - Celine Dion", "I Wanna Dance with Somebody - Whitney Houston",
        "Sweet Child o'Mine - Guns N'Roses", "Sweet Dreams (Are Made of This) - Eurythmics",
        "Livin'on a Prayer - Bon Jovi", "Bohemian Like You - The Dandy Warhols", "Everlong - Foo Fighters",
        "Take on Me - a-ha, Nothing Else Matters - Metallica", "Creep - Radiohead", "Yesterday - The Beatles",
        "Stand by Me - Ben E. King", "Dancing Queen - ABBA", "Good Vibrations - The Beach Boys",
        "All You Need Is Love - The Beatles"
    ]

    music = random.choice(music_list)
    print(Fore.YELLOW + f"\nYou can listen today: {music}", art("cute face6"))

    input(Fore.RED + "\nPress enter to continue...")


def game_recommendation4():
    """A function that returns a random game by genre"""
    tprint("Game  Recommendation")

    genre_game = input(
        "\nEnter genre (RPG, Action, Strategy, Platformer, Racing,"
        " Adventure, Horror, Shooter, Simulation, Fighting, Sports): "
    ).lower().strip()

    game_dict = {
        "horror": ["Resident Evil 2 (Remake)", "Silent Hill 2", "Dead Space", "Amnesia: The Dark Descent",
                   "Alien: Isolation", "Outlast", "The Last of Us", "P.T.", "Resident Evil 7: Biohazard", "BioShock"],
        "rpg": ["The Witcher 3: Wild Hunt", "Elden Ring", "Persona 5 Royal", "Mass Effect 2", "Fallout: New Vegas",
                "Divinity: Original Sin II", "Skyrim", "Disco Elysium", "Planescape: Torment", "Final Fantasy VII"],
        "action": ["Grand Theft Auto V", "God of War (2018)", "The Last of Us", "Red Dead Redemption 2",
                   "Sekiro: Shadows Die Twice", "Metal Gear Solid V: The Phantom Pain", "Devil May Cry 5",
                   "Uncharted 4: A Thief's End", "Doom Eternal", "Bloodborne"],
        "strategy": ["StarCraft II: Wings of Liberty", "Civilization VI", "XCOM 2", "Warcraft III: Reign of Chaos",
                     "Age of Empires II", "Total War: Warhammer II", "Crusader Kings III", "Stellaris",
                     "Command & Conquer: Red Alert 2", "Factorio"],
        "adventure": ["The Legend of Zelda: Breath of the Wild", "Red Dead Redemption 2", "Uncharted 4: A Thief's End",
                      "God of War (2018)", "The Witcher 3: Wild Hunt", "Tomb Raider (2013)", "A Way Out",
                      "Detroit: Become Human", "Life is Strange", "Firewatch"],
        "shooter": ["DOOM Eternal", "Half-Life 2", "Halo 3", "Call of Duty 4: Modern Warfare", "Titanfall 2",
                    "Overwatch", "Valorant", "Apex Legends", "Gears of War 2", "Battlefield 1"],
        "simulation": ["The Sims 4", "Microsoft Flight Simulator", "Stardew Valley", "Cities: Skylines",
                       "Euro Truck Simulator 2", "Planet Coaster", "Kerbal Space Program", "Factorio", "RimWorld",
                       "SimCity 4"],
        "platformer": ["Super Mario Odyssey", "Celeste", "Hollow Knight", "Ori and the Will of the Wisps",
                       "Shovel Knight", "Cuphead", "Rayman Legends", "A Hat in Time",
                       "Donkey Kong Country: Tropical Freeze", "Psychonauts 2"],
        "fighting": ["Street Fighter V", "Tekken 7", "Mortal Kombat 11", "Super Smash Bros. Ultimate",
                     "Dragon Ball FighterZ", "Guilty Gear Strive", "Killer Instinct", "Soulcalibur VI",
                     "BlazBlue: Central Fiction", "Injustice 2"],
        "racing": ["Forza Horizon 5", "Mario Kart 8 Deluxe", "Gran Turismo 7", "Need for Speed Heat", "F1 22",
                   "Forza Motorsport", "Burnout Paradise Remastered", "DiRT Rally 2.0", "Wipeout Omega Collection",
                   "Assetto Corsa Competizione"],
        "sports": ["FIFA 23", "NBA 2K23", "Madden NFL 23", "EA Sports FC 24", "MLB The Show 23", "F1 23",
                   "PGA Tour 2K23", "NHL 23", "eFootball 2023", "Rocket League"]

    }

    if genre_game in game_dict:
        game = random.choice(game_dict[genre_game])
        print(Fore.YELLOW + f"\nThe {genre_game} game recommendation is: {game}", art("cute face6"))
    else:
        print("This genre is not on the list.", art("sad and confused"))

    input(Fore.RED + "\nPress enter to continue...")


def jokes_for_you5():
    """The function returns a random joke."""
    tprint("Jokes  for  you")

    print(Fore.YELLOW + f"\n{pyjokes.get_joke()}", art("cute face6"))
    input(Fore.RED + "\nPress enter to continue...")


def tarot_cards6():
    """The function returns a random tarot card with prediction."""
    tprint("T A R O T")

    tarot_dict = {
        "The Fool": "Embrace new beginnings and have faith in your journey.",
        "The Magician": "Manifest your desires with focused intention and skill.",
        "The High Priestess": "Trust your intuition and listen to your inner voice.",
        "The Empress": "Nourish your creative energy and enjoy life's beauty.",
        "The Emperor": "Take charge and establish order with calm confidence.",
        "The Hierophant": "Seek wisdom from a trusted mentor or spiritual tradition.",
        "The Lovers": "Make a choice that aligns with your heart's true desire.",
        "The Chariot": "Move forward with determination and controlled power.",
        "Strength": "Show compassion and inner courage to overcome challenges.",
        "The Hermit": "Find quiet time for reflection and self-discovery.",
        "Wheel of Fortune": "Embrace the cycles of life and trust in positive change.",
        "Justice": "Seek balance and be fair in all your decisions.",
        "The Hanged Man": "Gain a new perspective by pausing and letting go.",
        "Death": "Allow transformation to happen, releasing the old.",
        "Temperance": "Find harmony and balance in every aspect of your life.",
        "The Devil": "Acknowledge your shadows, then liberate yourself from them.",
        "The Tower": "See sudden change as an opportunity for profound growth.",
        "The Star": "Embrace hope and healing; the universe is on your side.",
        "The Moon": "Explore your dreams and uncover hidden truths.",
        "The Sun": "Experience joy, success, and radiate warmth to others.",
        "Judgement": "Heed the call to awaken and find a new purpose.",
        "The World": "Celebrate your achievements and feel a sense of completion."

    }

    tarot_card = random.choice(list(tarot_dict.keys()))
    tarot_prediction = tarot_dict[tarot_card]
    print(f"\nYour tarot card for today {tarot_card} so your prediction is: {tarot_prediction}", art("cute face6"))

    input(Fore.RED + "\nPress enter to continue...")


def chat_bot():
    while True:
        print_menu()
        choice = input(Fore.BLUE + "\nEnter option number: ")

        if choice == "1":
            play_game1()
        elif choice == "2":
            movie_recommendation2()
        elif choice == "3":
            music_recommendation3()
        elif choice == "4":
            game_recommendation4()
        elif choice == "5":
            jokes_for_you5()
        elif choice == "6":
            tarot_cards6()
        elif choice == "0":
            print(Fore.RED + "")
            tprint("\nThank you for visiting!")
            tprint("See you later!")
            break
        else:
            print("Wrong choice. Try again.", art("sad and confused"))


chat_bot()
