def main(): 
    # Prompt the user for input in main 
    user_input = input("Enter text: ") 
    # Pass user_input into convert(), then print the returned result \
    print(convert(user_input)) 
def convert(text): 
    # Chain both replacements together on the input text 
    formatted_text = text.replace(":(", "🙁").replace(":)", "🙂") 
    return formatted_text
main()