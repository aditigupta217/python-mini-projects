import random;

subjects = ["shrukhan khan", "virat kholi ", "Nikita", "Aditi", "Mummy and Baba", "Moo"]

sports_actions = ["plays", "play cricket", " play games"]

politic_actions = ["rules in ", "is a prime minister", "is cm of maharasahtra"]

environments_actions = ["is cause pollution", "eats a fish"]

film_actions = ["is making a new film", "is a famous actor"]

actions = ["eats","dance in", "wins","do party ", "watch reels" , "drives a car", "play with lolo"]

place = ["in market", " in shopping mall","at India gate"," in hall ", "at manalli", "in hotel", "in bathroom"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(place)
    sports_action = random.choice(sports_actions)
    politics_actions = random.choice(politic_actions)
    film_action = random.choice(film_actions)
    environment_actions = random.choice(environments_actions)


    inputt = input("\n Do you want a headline on a specific topic ?(yes/no):").strip().lower()

    if inputt == 'yes':
         inputtt = input("\n On which topic you want the headline (sports , politics , environment , films ): ").strip().lower()
         if inputtt == 'sports' :
            headline = f"BREAKING NEWS : {subject} {sports_action} {places}"
            print("\n"+headline)
         elif inputtt == 'politics' :
             headline = f"BREAKING NEWS : {subject} {politics_actions} {places}"
             print("\n"+headline)
         elif inputtt == 'environment' :
             headline = f"BREAKING NEWS : {subject} {environment_actions} {places}"
             print("\n"+headline)
         else :
             headline = f"BREAKING NEWS : {subject} {film_action} {places}"
             print("\n"+headline)
         
    else :
         headlines = f"BREAKING NEWS : {subject} {action} {places}"
         print("\n"+headlines)
    
    user_input = input("\n Do you want another headline (yes/no)? : ").strip().lower()
    if user_input == 'no' :
        break

print("Thank you for using fake headline generator!!")

