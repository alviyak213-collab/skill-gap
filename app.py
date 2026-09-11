from flask import Flask, render_template, request

from gap import level_names, questions, required_level, skills

app = Flask(__name__, template_folder=".")


def calculate_results(answers):
    skill_scores = {skill: 0 for skill in skills}
    correct_answers = 0
    wrong_questions = []

    for index, question in enumerate(questions):
        selected_answer = answers.get(f"question_{index}")
        if selected_answer == question["answer"]:
            correct_answers += 1
            skill_scores[skills[index // 6]] += 1
        else:
            options = question["options"]
            selected_index = "ABCD".find(selected_answer) if selected_answer else -1
            correct_index = "ABCD".find(question["answer"])
            wrong_questions.append({
                "number": index + 1,
                "category": skills[index // 6],
                "question": question["question"],
                "selected_answer": (
                    options[selected_index] if selected_index >= 0 else "Not answered"
                ),
                "correct_answer": options[correct_index],
            })

    wrong_question_categories = [
        {
            "name": skill,
            "questions": [
                item for item in wrong_questions if item["category"] == skill
            ],
        }
        for skill in skills
        if any(item["category"] == skill for item in wrong_questions)
    ]

    skill_results = []
    for skill in skills:
        score = skill_scores[skill]
        current_level = 3 if score >= 5 else 2 if score >= 3 else 1
        gap = required_level[skill] - current_level
        priority = "HIGH" if gap == 2 else "MEDIUM" if gap == 1 else "NO GAP"
        recommendation = (
            "Basic + Intermediate training recommended" if gap == 2
            else "Intermediate + Advanced training recommended" if gap == 1
            else "No immediate training required"
        )
        skill_results.append({
            "name": skill,
            "score": score,
            "percentage": round((score / 6) * 100),
            "current_level": level_names[current_level],
            "required_level": level_names[required_level[skill]],
            "gap": gap,
            "priority": priority,
            "recommendation": recommendation,
        })

    strongest = max(skill_results, key=lambda skill: skill["score"])
    weakest = min(skill_results, key=lambda skill: skill["score"])
    total_questions = len(questions)

    return {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "wrong_answers": total_questions - correct_answers,
        "percentage": round((correct_answers / total_questions) * 100, 2),
        "skill_results": skill_results,
        "focus_areas": [
            skill for skill in skill_results if skill["percentage"] < 50
        ],
        "wrong_questions": wrong_questions,
        "wrong_question_categories": wrong_question_categories,
        "strongest": strongest,
        "weakest": weakest,
        "high_priority": [
            skill["name"] for skill in skill_results if skill["priority"] == "HIGH"
        ],
    }


@app.route("/", methods=["GET", "POST"])
def home():
    submitted = request.method == "POST"
    answers = request.form if submitted else {}
    results = calculate_results(answers)
    return render_template(
        "index.html",
        questions=questions,
        submitted=submitted,
        **results,
    )


if __name__ == "__main__":
    app.run(debug=True)
