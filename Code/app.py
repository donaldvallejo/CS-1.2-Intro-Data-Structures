from flask import Flask, render_template
from sampling import sampling, weight, select_words
from frequency import histogram, frequency
app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('index.html')


    if __name__ == '__main__':
        app.run(debug=True)