import sys
from flask import render_template, request, Flask

app = Flask(__name__)
 
@app.route("/", methods=['GET'])
def mainpage():
    name = request.args.get('name')
    msg = request.args.get('message')
    if name is None or msg is None:
        return '<h1>Rekruto! Будем дружить?</h1>'
    return '<h1>{}! {}!</h1>'.format(name, msg)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=8000)
