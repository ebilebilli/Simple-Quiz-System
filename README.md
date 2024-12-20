
Quiz Application
This program allows users to participate in a quiz by answering questions, earning points for correct answers, and receiving penalties for incorrect ones. It features a scoring system and a punishment mechanism for multiple wrong answers.

Key Features
Dynamic Question Management: Questions are loaded from a Quiz object and presented to the user in a loop.
Answer Validation: User answers are checked against the correct answers provided.
Scoring System:
Each correct answer awards the user 10 points.
After three incorrect answers, the user loses 10 points as a penalty.
Screen Clearing: The console is cleared after each question for a better user experience.
Penalty Mechanism: The program tracks incorrect answers and applies a one-time penalty after three consecutive wrong attempts.
How It Works
The program loads quiz questions from the Quiz object.
Users are prompted with a question and can input their answer.
Correct answers add points to the user's score, while incorrect answers contribute to the penalty system.
After three wrong answers, 10 points are deducted from the total score.
The user's final score is displayed at the end of the quiz.
Code Structure
Modules Used:
question_info: Contains the Quiz class and questions data.
clear_screen: Provides a function to clear the console after each question.
punishment_system: Implements the penalty logic for incorrect answers.
Functions:
answer_check: Handles the quiz flow, validates answers, and updates the score.
punishment: Applies penalties for multiple wrong answers.
Usage
Run the program using Python 3.12 or higher:
bash
Copy code
python quiz_app.py
Enter your name when prompted.
Answer each question by typing your response.
View your final score at the end of the quiz.
Example Interaction
plaintext
Copy code
Question: What is the capital of France?
Write answer: paris
True
If three wrong answers are given:

plaintext
Copy code
You have 3 wrong answers. You lost 10 points.
This program is modular and can be extended to include more questions, features, or advanced scoring mechanisms.