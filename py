from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'web_ise'


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return  render_template('loginpage.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    return  render_template('products.html')
@app.route('/login', methods=['POST'])
def login():
    usr = request.form.get('uname')
    psd = request.form.get('pword')
    cur = mysql.connection.cursor()
    cur.execute("select * from users )
    data = cur.fetchall()
    cur.close()
    return data
    if len(data) > 0:
     return render_template('products.html',useridx = data[0][2])
    else:
     return render_template('test1.html')

if __name__ == '__main__':
    app.run(debug=True)
