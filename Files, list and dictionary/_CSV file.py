
Ime = str(input("Ime: "))
Starost = int(input("Starost: "))
Spol = str(input("Spol: "))
person_id = 0

with open("_person.csv", "a") as person_list:
    person_list.write(f"{Ime}; {Starost}; {Spol}\n")

while True:
    Add = str(input("Add person: "))
    if Add.lower() != "no" or Add.lower() != "n":
        with open("_person.csv", "a") as person_list:
            person_list.write(f"{Ime}; {Starost}; {Spol}\n")
    else:
        break

#Kak bi z loopom naredil, da če nekdo vpiše Yes ali Y lahko vnese novega uporabnika? Torej program odpre novo datoteko. in v njo zapiše spremenljivke.
# Nato te program vpraša, če želiš dodati novo osebo in če rečeš y ali yes bo ponudil nove inpute + index zapisa.






