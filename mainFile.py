# Module requiredd 
import string
import random


# store all characters in lists
str1 = list(string.ascii_lowercase)
str2 = list(string.ascii_uppercase)
str3 = list(string.digits)
str4 = list(string.punctuation)


# Ask user about the number of characters
UserInput = input("How many characters do you want in your password? :: ")


# check this input is it number? is it more than 8?
while True:

	try:

		characters_number = int(UserInput)

		if characters_number < 8:

			print("Your number should be at least 8.")

			UserInput = input("Please, Enter your number again:: ")

		else:

			break

	except:

		print("Please, Enter numbers only.")

		UserInput = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(str1)
random.shuffle(str2)
random.shuffle(str3)
random.shuffle(str4)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

	result.append(str1[x])
	result.append(str2[x])

for x in range(part2):

	result.append(str3[x])
	result.append(str4[x])


# shuffle result
random.shuffle(result)


# join result
password = "".join(result)
print("Strong Password: ", password)
