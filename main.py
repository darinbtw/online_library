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
if __name__ == "__main__":
    app.run(debug=True)