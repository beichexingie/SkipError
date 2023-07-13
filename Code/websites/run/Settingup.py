import pymysql
from flask import Flask, request


db = pymysql.connect(host='localhost',
                     user='root',
                     password='Lydia391213',
                     database='user_auth',
                     port=3306)

cursor = db.cursor()


app = Flask(__name__)

info = ["a", "b"]


@app.route("/", methods=['POST', 'GET'])
def submit_form():
    user_name = request.form.get('username')
    pass_word = request.form.get('password')
    info[0] = user_name
    info[1] = pass_word
    return "用户注册成功！"


if __name__ == '__main__':
    app.run(host='localhost', port=3306, debug=True)


Username = info[0]
Password = info[1]

sql = "INSERT INTO users(username, password) VALUES('apple','567890')"

cursor.execute(sql)
db.commit()
db.close()
