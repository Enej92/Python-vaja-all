import random

secret = random.randint(1, 30)
print("Psst, secret je: "+ str(secret))
attempts = 0

with open("../Conditions and loops/score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print(f"Top score: {str(best_score)}")

while True:
    guess = int(input("Ugani številko: "))
    attempts += 1 #Kak deluje attempts +=1

    if guess == secret:
        print(f"Bravo! Številka je {secret}")
        print(f"Število poizkusov: {attempts}")
        if attempts < best_score:
            with open("../Conditions and loops/score.txt", "w") as score_file:
                score_file.write(str(attempts))

        break
    elif guess > secret:
        print ("Poizkusi nekaj manjšega")
    elif guess < secret:
        print ("Poizkusi nekaj večjega")
