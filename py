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

# @app.route('/products', methods=['GET', 'POST'])
# def products():
#     return  render_template('products.html')

# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#      return  render_template('sign_up.html')
# @app.route('/render-user-creation', methods=['GET', 'POST'])
# def renderusercreation():
#     return  render_template('user-creation.html')

@app.route('/login', methods=['POST'])
def login():
    usr = request.form.get('uname')
    psd = request.form.get('psw')
    print (usr, psd)#jokkjjjjjjjjjjjjjjjjjjjjjj
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname=%s and pword=%s",[usr.strip(),psd.strip()])
    data = cur.fetchall()
    print (data)#jkkkkkkkkkkkkkkkkkkkkkkkkk
    cur.close()
    if len(data) > 0:
     return render_template('products.html',useridx = data[0][2])
    else:
     return render_template('test1.html')
    
@app.route('/sign_up', methods=['POST'])
def signup():
    print ("start")
    usr = request.form.get('uname')
    psw = request.form.get('psw')
    email = request.form.get('email')
    print("c=begore")
    cur = mysql.connection.cursor()
    print("after")
    cur.execute("select * from users where uname=%s",usr.strip())
    data = cur.fetchall()
    print(data)
    print ("here")

    if len(data) == 0:
        cur.execute("insert into users (email,uname,pword) values (%s,%s,%s)",(email,usr,psw))
        mysql.connection.commit()
        cur.close()
        print("now")
        return render_template('login-page.html')
    else:
        cur.close()
        return render_template('test1.html')   


if __name__ == '__main__':
    app.run(debug=True)
