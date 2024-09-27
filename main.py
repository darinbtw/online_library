from flask import Flask,render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect('books.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS name_books(
    name TEXT,
    authors TEXT 
    )
    ''')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/books')
def books():
    db = sqlite3.connect()
    cur = db.cursor()
    cur.execute('SELECT * FROM name_books')
    books_data = cur.fetchall()
    db.close()
    return render_template('books.html', books=books_data)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    db = sqlite3.connect('books.db')
    cur = db.cursor()
    cur.execute('''SELECT * FROM name_books
                WHERE name LIKE ? OR authors LIKE ?
                ''', ('%' + query + '%', '%' + query + '%'))
    search_result = cur.fetchall()
    db.close()
    return render_template('books.html', query=query, books=search_result)

@app.route('/romeo')
def romep():
    return render_template('romeo_and_julet.html')

@app.route('/sinok')
def sinok():
    return render_template('sinok.html')

@app.route('/three_musketera')
def three_musketera():
    return render_template('tri_musketera.html')

@app.route('/Sherlock')
def sherlock():
    return render_template('sherlock.html')

@app.route('/Na_zapade')
def Na_zapade():
    return render_template('Na_zapade.html')

@app.route('/Triumfalnaya')
def Triumfalnaya():
    return render_template('Triumfalnaya.html')

@app.route('/dubroski')
def dubroski():
    return render_template('dubroski.html')

@app.route('/mertvye')
def mertvye():
    return render_template('mertvye.html')

if __name__ == "__main__":
    app.run(debug=True)