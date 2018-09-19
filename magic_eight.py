def ask_question():
    question = input("What is your question?: ")
    while question[-1] != "?" and question != "quit":
        question = input("I’m sorry, I can only answer questions.\nWhat is your question?: ")

    return question

while ask_question() != "quit":
    if ask_question() == "quit":
        break
