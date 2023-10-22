# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names_file = "Input/Names/invited_names.txt"
with open(invited_names_file) as file:
    invited_names = file.readlines()

starting_letter_file = "Input/Letters/starting_letter.txt"
with open(starting_letter_file) as file:
    starting_letter = file.read()

for name in invited_names:
    name = name.strip()
    output_letter_file = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(output_letter_file, mode="w") as file:
        output_letter = starting_letter.replace("[name]", name)
        file.write(output_letter)
