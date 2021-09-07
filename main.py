import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

space = {
  "uuid": "BE2DD242-8821-4C6D-B17F-6EA2D6AC58E8",
  "name": "the detective",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630965447127,
  "passages": [
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
}

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in space:
		for passage in space["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
  if "name" in current_location and "cleanText" in current_location:
			print("Moves: {}, Score: {}".format(moves, score))
			print("You are at the " + str(current_location["name"]))
			print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Headquarters"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")
