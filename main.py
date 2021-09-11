import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"


passages =  [
{
    "name": "Headquarters",
    "tags": "",
    "id": "1",
    "text": "You are at Space Headquaters. Your objective today is to find the infamous space robber throughout the space city. Where would you like to go? \n\n[[Jupiter Bar]]\n[[Cadet Cafe]]\n[[Astronomy Night Club]]\n[[Moonstar Hotel]]",
    "links": [
    {
        "linkText": "Jupiter Bar",
        "passageName": "Jupiter Bar",
        "original": "[[Jupiter Bar]]"
    },
    {
        "linkText": "Cadet Cafe",
        "passageName": "Cadet Cafe",
        "original": "[[Ct Cafe]]ade"
    },
    {
        "linkText": "Astronomy Night Club",
        "passageName": "Astronomy Night Club",
        "original": "[[Astronomy Night Club]]"
    },
    {
        "linkText": "Moonstar Hotel",
        "passageName": "Moonstar Hotel",
        "original": "[[Moonstar Hotel]]"
    }
    ],
    "hooks": [],
    "cleanText": "You are at Space Headquaters. Your objective today is to find the infamous space robber throughout the space city. Where would you like to go?"
},
{
    "name": "Jupiter Bar",
    "tags": "",
    "id": "2",
    "text": "You are at the Jupiter Bar. The owner of the bar said to you that the space robber stopped by but left a while ago but not sure where. Where would you like to go now?\n\n[[Cadet Cafe]] \n[[Astronomy Night Club]] \n[[Moonstar Hotel]]",
    "links": [
    {
        "linkText": "Cadet Cafe",
        "passageName": "Cadet Cafe",
        "original": "[[Cadet Cafe]]"
    },
    {
        "linkText": "Astronomy Night Club",
        "passageName": "Astronomy Night Club",
        "original": "[[Astronomy Night Club]]"
    },
    {
        "linkText": "Moonstar Hotel",
        "passageName": "Moonstar Hotel",
        "original": "[[Moonstar Hotel]]"
    }
    ],
    "hooks": [],
    "cleanText": "You are at the Jupiter Bar. The owner of the bar said to you that the space robber stopped by but left a while ago but not sure where. Where would you like to go now?"
},
{
    "name": "Cadet Cafe",
    "tags": "",
    "id": "3",
    "text": "You are at the Cadet Cafe. People around the cafe said that they never saw the space robber. But might have not gone too far. Where would you like to go next?\n\n[[Jupiter Bar]] \n[[Astronomy Night Club]] \n[[Moonstar Hotel]]",
    "links": [
    {
        "linkText": "Jupiter Bar",
        "passageName": "Jupiter Bar",
        "original": "[[Jupiter Bar]]"
    },
    {
        "linkText": "Astronomy Night Club",
        "passageName": "Astronomy Night Club",
        "original": "[[Astronomy Night Club]]"
    },
    {
        "linkText": "Moonstar Hotel",
        "passageName": "Moonstar Hotel",
        "original": "[[Moonstar Hotel]]"
    }
    ],
    "hooks": [],
    "cleanText": "You are at the Cadet Cafe. People around the cafe said that they never saw the space robber. But might have not gone too far. Where would you like to go next?"
},
{
    "name": "Astronomy Night Club",
    "tags": "",
    "id": "4",
    "text": "You are at the buzzing Astronomy Night Club! The bouncer said that the space robber was here and pick-pockted a few individuals at the club and ran away through the backdoor. Where would you like to go?\n\n[[Moonstar Hotel]] \n[[Pluto Pizza]]\n[[Earth Arcade]]",
    "links": [
    {
        "linkText": "Moonstar Hotel",
        "passageName": "Moonstar Hotel",
        "original": "[[Moonstar Hotel]]"
    },
    {
        "linkText": "Pluto Pizza",
        "passageName": "Pluto Pizza",
        "original": "[[Pluto Pizza]]"
    },
    {
        "linkText": "Earth Arcade",
        "passageName": "Earth Arcade",
        "original": "[[Earth Arcade]]"
    }
    ],
    "hooks": [],
    "cleanText": "You are at the buzzing Astronomy Night Club! The bouncer said that the space robber was here and pick-pockted a few individuals at the club and ran away through the backdoor. Where would you like to go?"
},
{
    "name": "Moonstar Hotel",
    "tags": "",
    "id": "5",
    "text": "You are at the Moonstar Hotel. The conceirge said they never seen a person like the space robber. Might have to go somewhere else. Where would you like to go?\n\n[[Astronomy Night Club]] \n[[Pluto Pizza]] \n[[Earth Arcade]]",
    "links": [
    {
        "linkText": "Astronomy Night Club",
        "passageName": "Astronomy Night Club",
        "original": "[[Astronomy Night Club]]"
    },
    {
        "linkText": "Pluto Pizza",
        "passageName": "Pluto Pizza",
        "original": "[[Pluto Pizza]]"
    },
    {
        "linkText": "Earth Arcade",
        "passageName": "Earth Arcade",
        "original": "[[Earth Arcade]]"
    }
    ],
    "hooks": [],
    "cleanText": "You are at the Moonstar Hotel. The conceirge said they never seen a person like the space robber. Might have to go somewhere else. Where would you like to go?"
},
{
    "name": "Pluto Pizza",
    "tags": "",
    "id": "6",
    "text": "Sit down and have a pizza! The waiter at Pluto Pizza said he stopped by and had a slice but didn't leave that long ago. You're close! Where would you like to go next?\n\n[[Earth Arcade]] \n[[Saturn Pharamcy]]\n[[Astro Library]]",
    "links": [
    {
        "linkText": "Earth Arcade",
        "passageName": "Earth Arcade",
        "original": "[[Earth Arcade]]"
    },
    {
        "linkText": "Saturn Pharamcy",
        "passageName": "Saturn Pharamcy",
        "original": "[[Saturn Pharamcy]]"
    },
    {
        "linkText": "Astro Library",
        "passageName": "Astro Library",
        "original": "[[Astro Library]]"
    }
    ],
    "hooks": [],
    "cleanText": "Sit down and have a pizza! The waiter at Pluto Pizza said he stopped by and had a slice but didn't leave that long ago. You're close! Where would you like to go next?"
},
{
    "name": "Earth Arcade",
    "tags": "",
    "id": "7",
    "text": "Lots of games you can play at Earth Arcade. The owner said the that the space robber took all their coins and left but not sure where to. Where would you like to go next?\n\n[[Pluto Pizza]] \n[[Saturn Pharamcy]] \n[[Astro Library]]",
    "links": [
    {
        "linkText": "Pluto Pizza",
        "passageName": "Pluto Pizza",
        "original": "[[Pluto Pizza]]"
    },
    {
        "linkText": "Saturn Pharamcy",
        "passageName": "Saturn Pharamcy",
        "original": "[[Saturn Pharamcy]]"
    },
    {
        "linkText": "Astro Library",
        "passageName": "Astro Library",
        "original": "[[Astro Library]]"
    }
    ],
    "hooks": [],
    "cleanText": "Lots of games you can play at Earth Arcade. The owner said the that the space robber took all their coins and left but not sure where to. Where would you like to go next?"
},
{
    "name": "Saturn Pharamcy",
    "tags": "",
    "id": "8",
    "text": "The pharmacist said he stole all their money and left. You might be close on the space robber's tail. Where would you like to go next?\n\n[[Earth Arcade]] \n[[Pluto Pizza]] \n[[Astro Library]] \n[[Rocket Gas Station]]\n[[Houston Headquarters]]",
    "links": [
    {
        "linkText": "Earth Arcade",
        "passageName": "Earth Arcade",
        "original": "[[Earth Arcade]]"
    },
    {
        "linkText": "Pluto Pizza",
        "passageName": "Pluto Pizza",
        "original": "[[Pluto Pizza]]"
    },
    {
        "linkText": "Astro Library",
        "passageName": "Astro Library",
        "original": "[[Astro Library]]"
    },
    {
        "linkText": "Rocket Gas Station",
        "passageName": "Rocket Gas Station",
        "original": "[[Rocket Gas Station]]"
    },
    {
        "linkText": "Houston Headquarters",
        "passageName": "Houston Headquarters",
        "original": "[[Houston Headquarters]]"
    }
    ],
    "hooks": [],
    "cleanText": "The pharmacist said he stole all their money and left. You might be close on the space robber's tail. Where would you like to go next?"
},
{
    "name": "Astro Library",
    "tags": "",
    "id": "9",
    "text": "Welcome to the city's library. But its empty. The space robber must of been here but nowhere in sight. Lets keep going! Where to next?\n\n[[Earth Arcade]] \n[[Pluto Pizza]] \n[[Saturn Pharamcy]] \n[[Rocket Gas Station]]\n[[Houston Headquarters]]",
    "links": [
    {
        "linkText": "Earth Arcade",
        "passageName": "Earth Arcade",
        "original": "[[Earth Arcade]]"
    },
    {
        "linkText": "Pluto Pizza",
        "passageName": "Pluto Pizza",
        "original": "[[Pluto Pizza]]"
    },
    {
        "linkText": "Saturn Pharamcy",
        "passageName": "Saturn Pharamcy",
        "original": "[[Saturn Pharamcy]]"
    },
    {
        "linkText": "Rocket Gas Station",
        "passageName": "Rocket Gas Station",
        "original": "[[Rocket Gas Station]]"
    },
    {
        "linkText": "Houston Headquarters",
        "passageName": "Houston Headquarters",
        "original": "[[Houston Headquarters]]"
    }
    ],
    "hooks": [],
    "cleanText": "Welcome to the city's library. But its empty. The space robber must of been here but nowhere in sight. Lets keep going! Where to next?"
},
{
    "name": "Rocket Gas Station",
    "tags": "",
    "id": "10",
    "text": "The Gas station owner said the robber just left and you can catch him if you're fast enough! GO! \n\n[[Houston Headquarters]]",
    "links": [
    {
        "linkText": "Houston Headquarters",
        "passageName": "Houston Headquarters",
        "original": "[[Houston Headquarters]]"
    }
    ],
    "hooks": [],
    "cleanText": "The Gas station owner said the robber just left and you can catch him if you're fast enough! GO!"
},
{
    "name": "Houston Headquarters",
    "tags": "",
    "id": "11",
    "text": "You found him! With all his stolen goods. Great Job! Think you can find him faster? \n\n[[Headquarters]]",
    "links": [
    {
        "linkText": "Headquarters",
        "passageName": "Headquarters",
        "original": "[[Headquarters]]"
    }
    ],
    "hooks": [],
    "cleanText": "You found him! With all his stolen goods. Great Job! Think you can find him faster?"
}
]



#my attempt *********************************


response = ""
curr_location = "headquarters"
moves = 0
valid_passages = {
                "headquarters" : ["jupiter bar","cadet cafe","astronomy night club","moonstar hotel","houston headquarters"],
                "jupiter bar" : ["cadet cafe", "astronomy night club", "moonstar hotel"],
                "cadet cafe" : ["jupiter bar", "astronomy night club", "moonstar hotel"],
                "astronomy night club" : ["moonstar hotel","pluto pizza","earth arcade"],
                "moonstar hotel" : ["astronomy night club","pluto pizza","earth arcade"],
                "pluto pizza" : ["earth arcade","saturn pharamcy","astro library"],
                "earth arcade" : ["pluto pizza","saturn pharamcy","astro library"],
                "saturn pharamcy" : ["earth arcade","pluto pizza","astro library","rocket gas station","houston headquarters"],
                "astro library" : ["earth arcade","pluto pizza","saturn pharamcy","rocket gas station","houston headquarters"],
                "rocket gas station" : ["houston headquarters"],
                "houston headquarters": []
                }

passages_welcome ={
    "headquarters" : "You are at Space Headquaters. Your objective today is to find the infamous space robber throughout the space city. Aim for the lowest amount of moves and score",
    "jupiter bar" : "You are at the Jupiter Bar. The owner of the bar said to you that the space robber stopped by but left a while ago but not sure where.",
    "cadet cafe" : "You are at the Cadet Cafe. People around the cafe said that they never saw the space robber.",
    "astronomy night club" : "You are at the buzzing Astronomy Night Club! The bouncer said that the space robber was here and pick-pockted a few individuals at the club and ran away through the backdoor.",
    "moonstar hotel" : "You are at the Moonstar Hotel. The conceirge said they never seen a person like the space robber. Might have to go somewhere else.", 
    "pluto pizza" : "Sit down and have a pizza! The waiter at Pluto Pizza said he stopped by and had a slice but didn't leave that long ago.", 
    "earth arcade" : "Lots of games you can play at Earth Arcade. The owner said the that the space robber took all their coins and left but not sure where to.", 
    "saturn pharamcy" : "The pharmacist said he stole all their money and left. You might be close on the space robber's tail.", 
    "astro library" : "Welcome to the city's library. But its empty. The space robber must of been here but nowhere in sight.", 
    "rocket gas station" : "The Gas station owner said the robber just left and you can catch him if you're fast enough! GO!.", 
    "houston headquarters" : "You found him! With all his stolen goods. Great Job! Think you can find him faster?", 
 }

passages_scores = {
     "headquarters" : 0,
     "jupiter bar" : 1,
     "cadet cafe" :1,
     "astronomy night club" : 1, 
    "moonstar hotel" : 1,
    "pluto pizza" : 1,
    "earth arcade" : 1,
    "saturn pharamcy" : 1,
    "astro library" : 1,
    "rocket gas station" : 1,
    "houston headquarters" : 1,
 }

#inputs
def get_input():

  response = input("What do you want to do? ")
  response = response.lower().strip()
  return response

print("You are at the Headquarters")
score = 0
while True:
    response = get_input()
    if response == "QUIT":
        break
    #if place exists and place is reachable
    if (response in valid_passages) and response in valid_passages[curr_location]:
        curr_location = response
        moves += 1
        #move limit reached
        if moves > 5:
            print("You are at your move limit. Start from the beginning. ")
            score, moves = 0, 0
            curr_location = 'headquarters'
        score += passages_scores[curr_location]
        print(f'Moved to {curr_location}')
        print(f'Moves : {moves}')
        print(f'Score: {score}')
        print(f'{passages_welcome[curr_location]}\n')

        #if houstan reached, prompt 'play again' or 'quit'
        if curr_location == "houston headquarters":
            response = input("Found robber, play again or quit? ")
            response = response.lower().strip()
            #prompt options after game
            while True:
                if response == "play again":
                    curr_location = "headquarters"
                    print("You are playing again")
                    break
                elif response == "quit":
                    break
                else:
                    print("Invalid input!!")
                    response = input("What you wanna do? ")
                    response = response.lower().strip()
    #place is not reachable
    elif (response in valid_passages) and response not in valid_passages[curr_location]:
        print(f'You cannot reach {response} from {curr_location}')
        
    #place does not exist/invalid response
    else:
        print(f'This is an in-valid place!!: {response}')

print("Thanks for playing!")








# # ----------------------------------------------------------------
# def find_current_location(location_label):
#   if "passages" in space:
#     for passage in space["passages"]:
#       if location_label == passage["name"]:
#         return passage
#   return {}

# # ----------------------------------------------------------------

# def render(current_location, score, moves):
#   if "name" in current_location and "cleanText" in current_location:
#       print("Moves: {}, Score: {}".format(moves, score))
#       print("You are at the " + str(current_location["name"]))
#       print(current_location["cleanText"] + "\n")

# #inputs
# def get_input():
#   response = input("What do you want to do? ")
#   response = response.strip()
#   print(f'response: {response}')
#   return response

# def update(current_location, location_label, response):
#   if response == "":
#     return location_label
#   #curr_location is empty dictionary
#   if "links" in current_location:
#     for link in current_location["links"]:
#       if link["linkText"] == response:
#         return link["passageName"]
#   print("I don't understand what you are trying to do. Try again.")
#   return location_label


# # ----------------------------------------------------------------

# location_label = "Headquarters"
# current_location = {}
# response = ""
# score = 0
# moves = 0

# while True:
#   if response == "QUIT":
#     break
#   response = get_input()
#   moves += 1
#   location_label = update(current_location, location_label, response)
#   current_location = find_current_location(location_label)
#   if "score" in current_location:
#     score = score + current_location["score"]
#   render(current_location, score, moves)



# print("Thanks for playing!")