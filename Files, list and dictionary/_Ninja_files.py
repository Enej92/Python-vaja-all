#1 način: ninja_file = open("ninja.txt", "r")

#1 način: contents = ninja_file.read()
#1 način: print(contents)

#1 način: ninja_file.close()

#With clause
with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    print(contents)


# for loop reading lines? To je kao isto kot with clause? Če prav razumem lahko s for loopom printam tudi posamezno vrstico? Kak?
with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines()

    for line in ninja_lines:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file")

