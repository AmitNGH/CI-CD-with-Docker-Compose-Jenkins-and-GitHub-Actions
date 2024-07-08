from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    body_template = ('<html>'
                     '   <head>'
                     '           <title>Scores Game</title>'
                     '   </head>'
                     '   <body>'
                     '           <h1>The score is <div id="score">{SCORE}</div></h1>'
                     '   G</body>'
                     '</html>')
    return body_template

app.run(debug=True)