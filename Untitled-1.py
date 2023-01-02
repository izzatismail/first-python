print("Hello World! My First Python")

# To define function in Python, use def, then indent the rest of the code
def get_choices():
    # To get input from user
    player_choice = input("Enter a choice (rock, paper, scissors): ") 
    computer_choice = "Paper"
    
     # Dictionary is similar to HashMap in Java
    choices_dictionary = {"Player": player_choice, "Computer": computer_choice}
    return choices_dictionary

choices = get_choices()
print(choices)