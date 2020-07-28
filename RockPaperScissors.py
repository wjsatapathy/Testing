
name_1 = input("Hello Player 1, what's your name? ")
name_2 = input("Hello Player 2, what's your name? ")

print("\nAlright, let's start!")

print("\n...Rock...")
print("...Paper...")
print("...Scissors!\n")

move_1 = (input(name_1 + ", make your move: ")).lower()


while move_1 != "rock" or "paper" or "scissors":
	move_1 = input("Please enter either \"rock,\" \"paper,\" or \"scissors\": ").lower()

	if move_1 == "rock" or "paper" or "scissors":
		break

print("\n*** No cheating! \U0001f600 ****\n" * 10)

move_2 = input(name_2 + ", make your move: ").lower()


while move_2 != "rock" or "paper" or "scissors":
	move_2 = input("Please enter either \"rock,\" \"paper,\" or \"scissors\": ").lower()


if move_1 == move_2:
	print("It's a tie!")

elif move_1 == "rock":
	if move_2 == "paper":
		print("Congratulations! " + name_2 + ", you won!")
	elif move_2 == "scissors":
			print("Congratulations! " + name_1 + ", you won!")

elif move_1 == "paper":
	if move_2 == "rock":
		print("Congratulations! " + name_1 + ", you won!")
	elif move_2 == "scissors":
			print("Congratulations! " + name_2 + ", you won!")

else:
	if move_2 == "rock":
		print("Congratulations! " + name_2 + ", you won!")
	elif move_2 == "paper":
		print("Congratulations! " + name_1 + ", you won!")











