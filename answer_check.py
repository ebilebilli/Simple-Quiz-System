from question_info import Quiz
from clear_screen import clear_screen

def answer_check(questions: Quiz):
    point = 0
    minus_point = 0
    minus_touch = False

    for x in questions:
        print(x.question)
        user_answer = input('Write answer: ').title().strip()

        if user_answer in x.correct_answer:
            print(True)
            point += 10
        else:
            print(False)
            minus_point += 1
            if minus_point == 3 and minus_touch is False :
                point -= 10
                minus_touch = True
                print('You have 3 wrong answer.You lost 10 point')

    clear_screen()
    return point


