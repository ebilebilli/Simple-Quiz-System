from question_info import Quiz, quiz_questions
from answer_check import answer_check
from data_write import quiz_data_writer

point = 0
def test(questions: Quiz): 
    user_name = input('Write your name:').title().strip() 
    point_data = answer_check(questions)
    quiz_data_writer(user_name, point_data)
    print(f'{user_name} point is {point_data}')

    

if __name__ == '__main__':
    test(quiz_questions)