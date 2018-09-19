import random
def ask_question():
    answer = input("What is your question?: ")
    return answer


ask_question()

def get_answer():
    answer_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    num = random.randint(0, 19)
    answer = answer_list[num]
    return answer

print(get_answer())