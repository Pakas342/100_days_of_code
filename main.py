#TODO: Create a letter using starting_letter.txt
with open(file="./Input/Letters/starting_letter.txt") as starting_letter:
    starting_text = starting_letter.read()
print(starting_text)
with open(file="./Input/Names/invited_names.txt") as invited_friends:
    friends = invited_friends.read()
    list_of_friends = friends.split()
for friend in list_of_friends:
    new_letter = starting_text.replace("[name]", f"{friend}")
    with open(file=f"./Output/ReadyToSend/{friend}_letter.txt", mode="w") as txt_letter:
        txt_letter.write(new_letter)


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp