alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function_required = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
key = int(input("Type the key number:\n"))

def encrypt(message, shift):
	# # There will be cases when the key number will be higher than the number of cases in the alphabet.
	# #  This scenario will generate an out-of-range error.
	# # So, we add a condition that covers this scenario:
	if shift > len(alphabet):
		shift = shift % len(alphabet)
		# # logic behind this condition is that whatever the required key will be, the program will go thru the -
		# # - alphabet as many times as necessary and the remainder will be the count at which the key will stop -
		# # - on the last iteration (after starting again from "a"
	output_text = ""
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

if function_required == "encode":
	encrypt(message, key)

# # ***bug: I get an error for word civilization and key 85 (but works for 84, 86 or other numbers I try
