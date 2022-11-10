import json
import random
import datetime


current_time: datetime = datetime.datetime.now()
print(current_time)
username = input(str("Enter Username: "))
Name = input(str("Enter your first name: "))
Surname = input(str("Enter your last name: "))

secret = random.randint(1, 30)
print("Psst, secret je: "+ str(secret))
attempts = 0

with open("secret_nm_score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print(f"Top scores: {str(score_list)}")

    # razvrščanje

    new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

    for score_dict in new_score_list:
        score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(score_dict.get("user_name"),
                                                                                             str(score_dict.get("attempts")),
                                                                                             score_dict.get("date"),
                                                                                             score_dict.get("secret_number"),
                                                                                             score_dict.get("wrong_guesses"))
        print(score_text)

    wrong_guesses = []
while True:

    guess = int(input("Ugani številko: "))
    attempts += 1 #Kak deluje attempts +=1

    if guess == secret:
        score_list.append({"user_name": username, "first_name": Name, "last_name": Surname, "attempts": attempts, "date":str(datetime.datetime.now()), "secret_number": secret, "wrong_guesses": wrong_guesses})
        with open("secret_nm_score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print(f"Bravo! Številka je {secret}")
        print(f"Število poizkusov: {attempts}")


        break
    elif guess > secret:
        print ("Poizkusi nekaj manjšega")
    elif guess < secret:
        print ("Poizkusi nekaj večjega")

        wrong_guesses.append(guess)