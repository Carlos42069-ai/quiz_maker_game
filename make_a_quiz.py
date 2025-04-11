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
        file.write(f"a) {a}\n")
        file.write(f"b) {b}\n")
        file.write(f"c) {c}\n")
        file.write(f"d) {d}\n")
        file.write(f"Correct Answer is: {correct_answer}\n")\
        file.write("---n") 



#After saving the quiz:
#    - Display a message confirming the question has been saved.
#    - Ask if the user wants to create another question or exit the program.

#If the user chooses to exit:
#    - Display a exiting message.
#    - End the program after.

#End
