import random;

subjects = ["shrukhan khan", "virat kholi ", "Nikita", "Aditi", "Mummy and Baba", "Moo"]

sports_actions = ["plays", "play cricket", " play games"]

actions = ["eats","dance in", "wins","do party ", "watch reels" , "drives a car", "play with lolo"]

place = ["in market", " in shopping mall","at India gate"," in hall ", "at manalli", "in hotel", "in bathroom"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(place)
    sports_action = random.choice(sports_actions)

    inputt = input("\n Do you want to any specific sports news ?(yes/no):").strip().lower()

    if inputt == 'yes':
         headline = f"BREAKING NEWS : {subject} {sports_action} {places}"
         print("\n"+headline)
    else :
         headlines = f"BREAKING NEWS : {subject} {action} {places}"
         print("\n"+headlines)
    
    user_input = input("\n Do you want another headline (yes/no)? : ").strip().lower()
    if user_input == 'no' :
        break

print("Thank you for using fake headline generator!!")

