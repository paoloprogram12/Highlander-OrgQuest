from flask import Flask, render_template, request, jsonify
from model.club import Club, read_club_data
from model.score import score
import json

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")

club_list = read_club_data("data.json")


@app.route("/scores", methods=["POST"])
def scores():
    data = json.loads(request.data.decode("utf-8"))
    output = []
    for club in club_list:
        club_score = score(club, data)
        output.append(
            {
                "name": club.name,
                "score": club_score.item(),
                "labels": club.labels,
            }
        )

    return jsonify(output), 200


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


def main():
    club = Club("chinese club", ["chinese", "language", "liguistic"])
    user_input = ["manderin"]

    print(score(club, user_input))
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
