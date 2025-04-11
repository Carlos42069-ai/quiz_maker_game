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
        print("The entered input is invali. Please try again.")
        correct_answer = input("What is the correct answer (a/b/c/d)? ")
    

#    - Save the question, options, and correct answer to a text file (`questions.txt`).
    

#After saving the quiz:
#    - Display a message confirming the question has been saved.
#    - Ask if the user wants to create another question or exit the program.

#If the user chooses to exit:
#    - Display a exiting message.
#    - End the program after.

#End
