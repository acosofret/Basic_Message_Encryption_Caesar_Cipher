# Put all the letters in the alphabet into a list:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ask user to select what they want to do: encode or decode a message:
function_required = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# # The user may enter a word different that "encode" or "decode". We add a condition to verify this and to ask again in case input is not valid:
function_capability = ["encode", "decode"]
if function_required not in function_capability:
	print("Please enter a valid choice.\nType in 'encode' (to encrypt a message) or 'decode' (to decrypt a message).\nAny other input is invalid.")
	function_required = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Ask the user to input the message to be encrypted or decrypted:
message = input("Type your message:\n").lower()
# Ask the user to insert a key number. This will be the number by which each letter in the message is shifted
key = int(input("Type the key number:\n"))
# There are 26 letters in the alphabet. That means that if the user enters 26 (or a multiple of 26) as the key number, -
# # - the encrypted message will come out exactly the same as the original message (Because the program will shift -
# # # - letters, but will end up to the same letter as the original.
# We cover this scenario in the code below (Letting the user know that and why they should use a different key number):
if key % 26 == 0:
	print("ATTENTION: The key number 26 (or any multiple of 26) will generate an encrypted/decrypted message that is identical to the original.\nPlease chose a different key number. ")
	key = int(input("Type the key number:\n"))

# Define a function for the encryption functionality:
def encrypt(message, shift):
	output_text = ""
	# # There will be cases when the key number will be higher than the number of cases in the alphabet.
	# #  This scenario will generate an out-of-range error.
	# # So, we add a condition that covers this scenario:
	if shift > len(alphabet):
		shift = shift % len(alphabet)
		# # logic behind this condition is that whatever the required key will be, the program will go thru the -
		# # - alphabet as many times as necessary and the remainder will be the count at which the key will stop -
		# # - on the last iteration (after starting again from "a"
	for letter in message:
		# # The "letter" will actually refer to every single character in the input text, including spaces, commas, etc.
		# # Since letters as " ", "," , ".", etc. won't be found in the alphabet list the program will generate an error.
		# # Hence why we have to add a conditional statement -
		# # - to cover any other character than the letters in the "alphabet" list.
		# # So we say that if letter is in the alphabet, do the key, otherwise keep the letter in the input:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			new_index = letter_index + shift
			# # Again, we may end up in a situation where new index is a higher number that the no. of letters.
			# # So, we add the same condition we added for the key input at the start of the function
			if new_index > len(alphabet):
				new_index = new_index % len(alphabet)
			output_text += alphabet[new_index]
		else:
			output_text += letter
	print(f"The encoded text is: '{output_text}'.")


# Define a function for the decryption functionality:
def decrypt(message, shift):
	output_text = ""
	# # There will be cases when the key number will be higher than the number of cases in the alphabet.
	# #  This scenario will generate an out-of-range error.
	# # So, we add a condition that covers this scenario:
	if shift > len(alphabet):
		shift = shift % len(alphabet)
		# # logic behind this condition is that whatever the required key will be, the program will go thru the -
		# # - alphabet as many times as necessary and the remainder will be the count at which the key will stop -
		# # - on the last iteration (after starting again from "a"
	for letter in message:
		# # The "letter" will actually refer to every single character in the input text, including spaces, commas, etc.
		# # Since letters as " ", "," , ".", etc. won't be found in the alphabet list the program will generate an error.
		# # Hence why we have to add a conditional statement -
		# # - to cover any other character than the letters in the "alphabet" list.
		# # So we say that if letter is in the alphabet, do the key, otherwise keep the letter in the input:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			new_index = letter_index - shift
			# # Again, we may end up in a situation where new index is a higher number that the no. of letters.
			# # So, we add the same condition we added for the key input at the start of the function
			if new_index < 0:
				new_index = len(alphabet) + new_index
			output_text += alphabet[new_index]
		else:
			output_text += letter
	print(f"The encoded text is: '{output_text}'.")


# Define a function to ask the program for the right functionality:
def run_program(function_required):
	if function_required == "encode":
		encrypt(message, key)
	elif function_required == "decode":
		decrypt(message, key)

# Run the program and ask user if they want to encrypt or decrypt another message:
run_program(function_required)
repetition = False
repeat = input("Do you want to encrypt/decrypt another message?\nPlease type in 'yes' or 'no': ").lower()
while repeat == "yes":
	# # We ask for inputs again (just copy the code lines from original input requests):
	function_required = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	function_capability = ["encode", "decode"]
	if function_required not in function_capability:
		print(
			"Please enter a valid choice.\nType in 'encode' (to encrypt a message) or 'decode' (to decrypt a message).\nAny other input is invalid.")
		function_required = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	message = input("Type your message:\n").lower()
	# Ask the user to insert a key number. This will be the number by which each letter in the message is shifted
	key = int(input("Type the key number:\n"))
	if key % 26 == 0:
		print(
			"ATTENTION: The key number 26 (or any multiple of 26) will generate an encrypted/decrypted message that is identical to the original.\nPlease chose a different key number. ")
		key = int(input("Type the key number:\n"))
	# # And the run the program again:
	run_program(function_required)
	repeat = input("Do you want to encrypt/decrypt another message?\nPlease type in 'yes' or 'no': ").lower()

print("Thanks for using our program !\n Have a great rest of the day !")
exit()

# # ***bug: We get an error for Type your message: <civilization> & Type the key number: <85> (but works for 84, 86 or other numbers I try
# # ***bug: We get errors for Type your message: <Ana are mere.> & Type the key number: <100>
# # ***bug: We get error if user input anything else other than an integer number as key number. We can easily -
# # # - add a condition to check that and repeat the input request if necessary.
# # *functionality: to be added to encrypt or decrypt numbers as well
