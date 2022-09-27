from calendar import month
import time


user_info = []

print("Welcome to your very own, personalized SmartGym [Sunglaseses Emoji]. \n")
time.sleep(2)

print("I must remark, you purchasing SmartGym already places you amongst the superior rank of individuals in society!  ")
time.sleep(2.5)

name = input("Hi you could call me Jim, what's your name? ") 
#Personal info such as names could be used as motivation, this device is also intended to be a communication tool/coach, hence motivational tools should be at place.
print(f"Username [{name}] is stored to User 1.")
time.sleep(1)

print("Got it, also please fill in your physical details if this isn't too personal.")
while True:
    try: 
        age = int(input("Age: "))
        
    except ValueError:
        print("Please enter a valid age. Eg: 16, 69")
        continue
    break

while True:
    try:
        weight = float(input("Weight(kg): "))
    except ValueError:
        print("Please enter a valid weight. Eg: 16.9, 69")
        continue
    break
while True:
    try:
        height = int(input("Height(cm): "))
    except ValueError:
        print("Please enter a valid weight. Eg: 16.9, 69")
        continue
    break
body_mass_index = float(weight / (height ** 2) * 10000)

answers = ['thank you', 'ok']

while True:
    if body_mass_index < 18.5:
        answer = input(f"Your BMI is {body_mass_index}. Your fleshless soul should gain more weight. Don't worry, SmartGym can help! (Thank you/Ok): ")
        if answer.lower() not in answers:
            print("SmartGym can only accept appreciative answers. Please go back and talk to me respectfully.")
            continue
    if body_mass_index >= 18.5 and body_mass_index < 25:
        answer = input(f"Your BMI is {body_mass_index}. Keep it up! :D, I expect you to live a long life! (Thank you/Ok): ")
        if answer.lower() not in answers:
            print("SmartGym can only accept appreciative answers. Please go back and talk to me respectfully.")
            continue
    if body_mass_index >= 25 and body_mass_index < 30:
        answer = input(f"Your BMI is {body_mass_index}. You are overweight. Don't worry, SmartGym can help you lose some of that belly fat. (Thank you/Ok): ")
        if answer.lower() not in answers:
            print("SmartGym can only accept appreciative answers. Please go back and talk to me respectfully.")
            continue
    if body_mass_index > 30:
        answer= input(f"Your BMI is {body_mass_index}. You are severely overweight. Don't worry, you're already on the right step by using SmartGym! (Thank you/Ok): ")
        if answer.lower() not in answers:
            print("SmartGym can only accept appreciative answers. Please go back and talk to me respectfully.")
            continue
    break

print("Awesome! Transferring user data...")
time.sleep(1.5)
print("\nDone!")

genders =['Male', 'Female']


time.sleep(0.5)

while True:
    gender = input("\nAre you a.. Male/Female/Other : ")
    if gender.lower() == "male":
        answer = input("Hey " +name+ ", whatsup bro! Ready for one heck of a workout? ")

        break
    if gender.lower() == "female":
        answer = input("Hi gorgeous, you sure are looking beautiful today " +name+ " ;D. Let's get your blood rushing shall we? ")
    if gender not in genders:
        print("SmartGym is unable to provide service to other genders :(")
        continue
    break
    
   
 #SmartGym intentionally displays behavior that of a xenophobe. SmartGym is getting cancelled ( I am creative ! >: )
while True:
    try:
         print("Before we begin... remind me what day it is today..")
         time.sleep(0.5)
         day = int(input("Day: "))
         month = int(input("Month: "))
         print(f"Today is {month}/{day}")
    except ValueError:
        print("Please enter an integer value. Eg: Day (1, 2, ... 30/31), Month (1, 2, ... , 12)")
        continue
    except day > 31:
        print("The the extent of my knowledge, this doesn't look like a valid date.")
        continue
    except month > 12:
        print("The the extent of my knowledge, this month does not exist.")
        continue
    break  

goal = input("Why do you work out? (Strength, Sports, Aesthetics, Health) : ")

if goal == "Sports":
    print("Our features for sports will be added soon! In the meantime, you can build your strength instead!")

if goal.lower() == "Strength":
    print("Let's list our current and target numbers for the upcoming month.")
    current_bench = int(input("\nCurrent Bench Press (kg): "))
    target_bench = int(input("Target Bench Press (kg): "))

    current_dead = int(input("\nCurrent Deadlift (kg): "))
    target_dead = int(input("Target Deadlift (kg): "))

    current_squat = int(input("\nCurrent Squat (kg): "))
    target_squat = int(input("Target Squat (kg): "))
    
if int((target_bench - current_bench) or (target2 - current2) or (target3 - current3)) < (7):
    print("Ah,, c'mon you lazy bum, I know you could be stronger than that.")
if int((target1 - current1) or (target2 - current2) or (target3 - current3)) > (7):
    print("Way to go my friend, loving the mindset!")
    
exercise = input("Pick an exercise (Bench/Deadlift/Squat): ")
if exercise.lower() == "bench":
    optimism = "positive"
    
    while optimism == "positive":
        if age > 13:
            current_bench += 5
            print(f"Your lift has been set to {current_bench}, get your stout butt ready here on my countdown.")
            print("\n3...")
            time.sleep(1)
            print("2..")
            time.sleep(1)
            print("1, Take a deep breath!")

            print("Exhale...")
            time.sleep(1)
            print("Rep 1x")
            print("Move your lazy arms you big fat donkey!")
            time.sleep(1.5)
            print("Rep 2x")
            time.sleep(1)
            print("Let's get serious here! LAST REP, you can do it!")
            time.sleep(1.5)

            print("Well done on your first exercise. SmartGym is proud of your effort.")
            print(f"You just lifted {current_bench} kg, 3 times!")

            next_set = input("\n Continue on to the next set? (Y/N): ")
            if next_set.lower() == "y":
                 continue
            if next_set.lower() == "n":
                optimism == "negative"
                break


other_goals = ['Aesthetics', 'Health']

if goal in other_goals:
    print("Looking for your service...")
    time.sleep(0.3)
    print(".")
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    time.sleep(0.3)
    print(f"Unfortunately, SmartGym is unable to provide services for '{goal}' right now. Please notify us at our website so that we could include your need in our next update!")
