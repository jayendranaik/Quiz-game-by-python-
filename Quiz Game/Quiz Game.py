# MINI PROJECT OF PYTHON NO. 1) QUIZ GAME
# Namaste🙏 My name is JAYENDRA and this is my mini project of python which is quiz game 
# I recently learned the basics of Python, and I used the for loop and if else statement to create this wonderful and entertaining project.


print("\033[1m✨✨✨✨✨ Welcome to the Ultimate Tech Quiz Adventure! ✨✨✨✨✨\033[1m")

questions = ("Question 1: What does CPU stand for in a computer?",
             "Question 2: Which company developed the Windows operating system?",
             "Question 3: What does HTML stand for in the context of web development?",
             "Question 4: In the context of mobile phones, what does 'iOS' stand for?",
             "Question 5: Which programming language is used to create applications for Android?",
             "Question 6: What is the primary function of RAM in a computer?",
             "Question 7: Which search engine is known for its colorful logo and is the most widely used globally?",
             "Question 8: What is the purpose of a firewall in computer security?",
             "Question 9: Which programming language is often used for building dynamic websites and web applications?",
             "Question 10: What does the acronym 'URL' stand for in the context of web addresses?")

options = (("A) Central Processing Unit", "B) Computer Processing Unit", "C) Central Processor Unit", "D) Central Printed Unit"),
           ("A) Apple", "B) Microsoft", "C) Google", "D) Linux"),
           ("A) HyperText Markup Language", "B) HyperText Modeling Language",
            "C) High-Level Text Language", "D) HyperTransfer Markup Language"),
           ("A) Internet Operating System", "B) International Operating System",
            "C) iPhone Operating System", "D) Interactive Operating System"),
           ("A) Swift", "B) Java", "C) C#", "D) Python"),
           ("A) Storing long-term data", "B) Providing power to the computer",
            "C) Running applications and storing temporary data", "D) Managing network connections"),
           ("A) Bing", "B) Yahoo", "C) Google", "D) DuckDuckGo"),
           ("A) Protecting against physical damage", "B) Filtering network traffic to prevent unauthorized access",
            "C) Enhancing display quality", "D) Improving internet speed"),
           ("A) Java", "B) Python", "C) JavaScript", "D) C++"),
           ("A) Universal Resource Locator", "B) Uniform Resource Locator", "C) Unique Resource Locator", "D) Universal Rendering Locator"))

correct_answers = ("A", "B", "A", "C", "B", "C", "C", "B", "C", "B")

user_ans = []
score = 0
question_num = 0

for question in questions:
    print("                                                               ")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print("                                                               ")
    print("\033[1m" + question + "\033[0m")
    for option in options[question_num]:
        print(option)

    guess = input("Enter you option (A,B,C,D): ").upper()
    user_ans.append(guess)
    if guess == correct_answers[question_num]:
        score += 1
        print("🎉✔--CORRECT!--✔🎉")
    else:
        print("❌INCORRECT❌")
        print(f"The correct answer is {correct_answers[question_num]}")
    question_num += 1

print()
print()
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
print("\033[1m---------------RESULT------------------\033[1m")
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score} %")
print()
print("CORRECT ANSWERS: ", end=" ")
for answer in correct_answers:
    print(answer, end=" ")
print()

print("YOUR ANSWERS:    ", end=" ")
for your_answer in user_ans:
    print(your_answer, end=" ")
print()
print()
