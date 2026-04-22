# For reference purposes only

while True:
    matchingQuestion = [q for q in questions if q["category"] == category]

    if not matchingQuestion:
        quiz_active = False
        print(f"No questions available for {category}.")
        break

    question = random.choice(matchingQuestion)

    if isinstance(question["text"], list):
        text = " ".join(question["text"])
    else:
        text = question["text"]
    print(f"\n--- {category} Question ---")

    if question["question_num"] >= 6:
        print("\n" + text)
    else:
        print("\n" + text)
        print("Choices:", ", ".join(question["choices"]))

    answer = input("Enter your answer: ")

    if answer.lower() == question["answer"].lower():
        print(f"Paithon: Correct! You earned {reward} Primogems ദ്ദി(｡•̀,<)~✩‧₊\n")
        data[0]["primogems"] += reward
        save_data()
    else:
        print(f"Paithon: Wrong! (╥﹏╥) The correct answer is {question['answer']}.\n")

    question["answered"] = True
