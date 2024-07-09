from Score import get_score
from flask import Flask
from Utils import BAD_RETURN_CODE

app = Flask(__name__)


def run_score_main():
    app.run(debug=True, use_reloader=False)


@app.route('/')
def score_server():
    try:
        current_score = get_score()
    except:
        body_content = f"<h1><div id=\"score\" style=\"color:red\">{BAD_RETURN_CODE}</div></h1>"
    else:
        body_content = f" <h1>The score is <div id=\"score\">{current_score}</div></h1>"

    body_template = ("<html>"
                     "   <head>"
                     "           <title>Scores Game</title>"
                     "   </head>"
                     "   <body>"
                     f"      {body_content}"
                     "   </body>"
                     "</html>")

    return body_template


if __name__ == "__main__":
    run_score_main()
