names = []
with open("Input/Names/invited_names.txt") as file:
    for line in file:
        names.append(line.strip())

for i in range(0, len(names)):
        with open("Input/Letters/starting_letter.txt", mode = "r") as file:
            text = file.read()
            f = open(f"Output/ReadyToSend/letter_to_{names[i]}.txt", "w")
            f.write(text.replace("[name]", names[i]))
            f.close()





