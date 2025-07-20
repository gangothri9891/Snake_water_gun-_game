from flask import Flask, render_template, request
import random

app = Flask(__name__)

CHOICES = ['Snake', 'Water', 'Gun']

def check(computer, user):
    if computer == user:
        return "Draw"
    elif (computer == 'Snake' and user == 'Water') or \
         (computer == 'Water' and user == 'Gun') or \
         (computer == 'Gun' and user == 'Snake'):
        return "Computer Wins"
    else:
        return "You Win"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(CHOICES)
        result = check(computer_choice, user_choice)
        return render_template("index.html", user=user_choice,
                               computer=computer_choice,
                               result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)