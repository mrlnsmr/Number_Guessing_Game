import random 

#top of range
top_of_range = input("Select your top range: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

#random number
random_number = random.randint(0, top_of_range)
guesses = 0

#guess
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right! Congratulations!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

#evaluation
if guesses == 1:
    print("You got it in" ,guesses, "guess!")
else:
    print("You got it in" , guesses , "guesses!")

if guesses > 20:
    print("You have to work on this!")
elif guesses > 10:
    print("Next time you got it in less guesses!")
elif guesses > 1: 
    print("Wow pretty good!")
else:
    print("You´re a genius!")