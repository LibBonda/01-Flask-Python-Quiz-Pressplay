from flask import Flask, render_template, request
from waitress import serve


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    playing = request.form.get("playing")
    if playing.lower() != "yes":
        return "Quiz not started. Come back when you're ready!"

    score = 0
    questions = [
        ("What does CPU stand for?", "central processing unit"),
        ("What's the national currency of Mexico?", "peso"),
        ("What's the capital city of South Africa?", "pretoria"),
        ("What does AI stand for?", "artificial intelligence"),
        ("What's the speed of sound in metres per second?", "343"),
        ("On which continent is San Marino?", "europe"),
        ("Which item of clothing did Albert Einstein never wear?", "socks"),
        ("Hydrogen and oxygen are the two chemical components of ...?", "water"),
        ("What does RAM stand for?", "random access memory"),
        ("What is cheese made from?", "milk")
    ]

    for question, answer in questions:
        # Get user's answer from the form data
        user_answer = request.form.get(question)
        if user_answer.lower() == answer:
            score += 1

    result_message = f"You got {score} questions correct!\n"
    result_message += f"You got {(score/len(questions)) * 100}%.\n"
    
    return result_message



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)



        #    serve(app, host="0.0.0.0", port=8000, debug=True)
        #     #  app.run(debug=True)