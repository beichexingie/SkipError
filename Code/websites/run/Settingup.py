import pymysql
from flask import Flask, request
from flask import render_template

db = pymysql.connect(host='localhost',
                     user='root',
                     password='Lydia391213',
                     database='user_auth',
                     port=3306)


app = Flask(__name__)


@app.route("/Register", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        user_name = request.form.get('username')
        pass_word = request.form.get('password')

        with db.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (user_name,pass_word)"
            cursor.execute(sql, (user_name, pass_word))
            db.commit()

        return "用户注册成功！"

    return render_template('Homepage.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5678, debug=True)

# sql = "INSERT INTO users(username, password) VALUES(Username, Password)"

db.close()
