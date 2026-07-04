name = input("Enter your name: ").upper()

print("Welcome!", name, "to the General Knowledge Quiz...")
print("Note: Type 'exit' anytime to quit the quiz.\n")

total = 0

# Question 1
print("1. What is the capital of Pakistan?")
ans = input("Answer here: ").lower().strip()

if ans == "exit":
    print("Thank you for playing!")
    print("Your Final Score:", total, "/5")
    exit()

if ans == "islamabad":
    total += 1

# Question 2
print("\n2. Who was the founder of Pakistan?")
ans = input("Answer here: ").lower().strip()

if ans == "exit":
    print("Thank you for playing!")
    print("Your Final Score:", total, "/5")
    exit()

if ans == "muhammad ali jinnah" or ans == "quaid e azam":
    total += 1

# Question 3
print("\n3. How many provinces are there in Pakistan?")
ans = input("Answer here: ").strip()

if ans.lower() == "exit":
    print("Thank you for playing!")
    print("Your Final Score:", total, "/5")
    exit()

if ans == "4":
    total += 1

# Question 4
print("\n4. In which city is the Badshahi Mosque located?")
ans = input("Answer here: ").lower().strip()

if ans == "exit":
    print("Thank you for playing!")
    print("Your Final Score:", total, "/5")
    exit()

if ans == "lahore":
    total += 1

# Question 5
print("\n5. Which province of Pakistan has the largest population?")
ans = input("Answer here: ").lower().strip()

if ans == "exit":
    print("Thank you for playing!")
    print("Your Final Score:", total, "/5")
    exit()

if ans == "punjab":
    total += 1

print("\nQuiz Completed!")
print("Your Final Score:", total, "/5")

if total == 5:
    print("Excellent! You got all answers correct.")
elif total >= 3:
    print("Good Job!")
else:
    print("Keep Learning and Try Again!")