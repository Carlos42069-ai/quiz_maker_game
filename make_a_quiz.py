#Start the program

#Display a welcome message
print("Welcome to the game of quiz creating!")

def creating_a_question():
#Ask the user to give a question and choices:
#    - Ask for the question.
    question = input("Enter your first question: ")
#    - Ask for the options (a, b, c, d).
    option_a = input("Enter your first option: ")
    option_b = input("Enter your second option: ")
    option_c = input("Enter your third option: ")
    option_d = input("Enter your fourth option: ")
                    

#    - Ask for the correct answer (a, b, c, or d).
    correct_answer = input("What is the correct answer in the following choices (a/b/c/d)? ")
    while correct_answer not in ['a', 'b', 'c', 'd']:
        print("The entered input is invalid. Please try again.")
        correct_answer = input("What is the correct answer (a/b/c/d)? ")
    

#    - Save the question, options, and correct answer to a text file (`quiz_questions.txt`).
    with open("quiz_questions.txt", "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"a) {option_a}\n")
        file.write(f"b) {option_b}\n")
        file.write(f"c) {option_c}\n")
        file.write(f"d) {option_d}\n")
        file.write(f"Correct Answer is: {correct_answer}\n")
        file.write("---n") 

#After saving the quiz:
#    - Display a message confirming the question has been saved.
    print("Your quiz has been saved successfully!")

def program():
    print("Welcome to make a quiz program!")

#    - Ask if the user wants to create another question or exit the program.
    while True:
        make = input("\nWould you like to (1) create quiz or (2) exit?: ")
        if make == "1":
            creating_a_question()
            another_question = input("Do you want to create another question? (yes/no): ")
            if another_question != "yes":
                print("Thanks for using the make a quiz program!")
                break
            
#If the user chooses to exit:
        elif make == "2":
#    - Display a exiting message.
            print("Thank you for creating the quizzes!")
            break
        else:
            print("Please enter between choices 1 and 2.")
#    - End the program after.
program()
#End
