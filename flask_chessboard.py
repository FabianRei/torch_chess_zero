from flask import Flask, render_template, request, jsonify
import time
from state import get_random_move

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def chess():
    if request.method == 'POST':
        position = request.form
        print(position['fen'])
        # This should return a smart move at some point
        random_move = get_random_move(position['fen'])
        #time.sleep(3)
        return jsonify(code=0, msg='Success!!', move=random_move)

    else:
        return render_template("chess.html", fun="Only random moves.. Yet")


if __name__ == "__main__":
    app.run(debug=True)
