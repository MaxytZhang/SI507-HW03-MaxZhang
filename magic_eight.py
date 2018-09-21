import random


def ask_question():
    question = input("What is your question?: ")
    while question[-1] != "?" and question != "quit":
        question = input("I’m sorry, I can only answer questions.\nWhat is your question?: ")
    return question


def get_answer():
    answer_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    num = random.randint(0, 19)
    answer = answer_list[num]
    a = 10
    return answer


while ask_question() != "quit":
    print(get_answer())

