"""
Project: Quiz Application
Author: Mocherla Kasthuri
Description: A simple multiple-choice quiz that calculates the user's score.
"""

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Hyderabad"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI and data science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 364", "B. 365", "C. 366", "D. 367"],
        "answer": "C"
    }
]

score = 0

print("=== Python Quiz ===")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Your Answer: ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

print("\n===== Quiz Finished =====")
print(f"Your Score: {score}/{len(questions)}")
