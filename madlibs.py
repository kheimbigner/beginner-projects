"""
Very Beginner Python Project by Kylie Ying
Madlibs using string concatenation

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""
# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# Add missing input statements for all variables used in the madlib
season = input("Season: ")
name = input("Name: ")
place = input("Place: ")
object = input("Object: ")
language = input("Language: ")
terrain = input("Terrain: ")
animal = input("Animal: ")
material = input("Material: ")
scent = input("Scent: ")
verb_ending_s = input("Verb ending in -s: ")
exclamation = input("Exclamation: ")
plural_noun = input("Plural noun: ")
direction = input("Direction: ")
emotion = input("Emotion: ")
unexpected_item = input("Unexpected item: ")

madlib = f"""One sunny {season} a brave explorer named {name} set out on a daring journey through the wilds of  {place}. Armed only with a trusty {object} and an old map scribbled in {language}, they were determined to find the legendary Lost Compass—a magical artifact said to grant perfect direction in life and hiking.

As they trekked through the dense {terrain}, they encountered a mischievous {animal} who offered them a riddle:
Solving the riddle earned them a {adj} key made of {material}, which unlocked a hidden cave behind a waterfall that smelled faintly of {scent}.
Inside the cave, glowing runes lit the walls, and a mysterious voice whispered, "Only the one who {verb_ending_s} with courage shall find the way."
With a deep breath, {name} stepped forward, clutching their {object}, and shouted "{exclamation}!"
Suddenly, the ground shook, and the Lost Compass rose from a pedestal of {plural_noun}, spinning wildly. It pointed toward {direction}, where the final challenge awaited: crossing the Bridge of {emotion}.
Would they make it across? Would the compass lead them to glory—or to a surprise twist involving {unexpected_item} and a singing {animal}?
Only time would tell."""

print(madlib)