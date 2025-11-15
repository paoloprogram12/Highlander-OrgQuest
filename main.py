from flask import Flask, render_template
from model.club import Club
from model.score import score

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")


@app.route("/")
def home():
    return render_template("index.html")


def main():
    club = Club("chinese club", ["chinese", "language", "liguistic"])
    user_input = ["manderin"]

    print(score(club, user_input))
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
