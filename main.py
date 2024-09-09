from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/romeo')
def romep():
    return render_template('romeo_and_julet.html')

if __name__ == "__main__":
    app.run(debug=True)