# encoding=utf-8
from flask import Flask, request, render_template
import re
import random
app = Flask(__name__)


def ss(text):

    # 106年律師民法第一大題第二題
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(text)
    if match:
        pass
    else:
        return "輸入錯誤"

    # 字數統計(隨機分)
    random_score = 0
    mark = 25
    word_count = len(text)
    if 10 <= word_count/mark <= 80:
        random_score = random.randint(5, 25)
    else:
        random_score = 5

    # 法律用語分
    basic_words = ["管見", "通說", "學說", "本件", "本案", "實務", "本文",
                   "見解", "惟", "然", "或有附言者", "予以", "亦同", "依據", '按', '故', '是']
    basic_score = 0
    for i in range(len(basic_words)):
        a = text.find(basic_words[i])
        if a != -1:
            basic_score += 3

    if basic_score > 25:
        basic_score = 25
    elif basic_score == 0:
        basic_score = -20

    # 題目關鍵字分
    key_words = ['191', '227', '184']
    key_word2 = ['所有人', '契約', '附隨義務', '保護照顧義務', '可歸責', '不完全給付',
                 '開啟', '交通', '交往', '交易安全', '不作為', '不真正連帶', '損害賠償']
    keyword_score = 0
    code_score = 0
    part2_score = 0
    for i in range(len(key_words)):
        a = text.find(key_words[i])
        if a != -1:
            code_score += 6
    for i in range(len(key_word2)):
        a = text.find(key_word2[i])
        if a != -1:
            keyword_score += 4

    if code_score == 0 and keyword_score == 0:
        part2_score = -30
    elif code_score == 0:
        keyword_score = 0
    else:
        print('he')

    part2_score = keyword_score+code_score
    if part2_score > 40:
        part2_score = 40

    total = (random_score+basic_score+part2_score+10)*0.8/4  # 本題滿分25
    if total <0:
        total=0
    return total


@app.route('/')
def login():

    return render_template('start.html')


@app.route('/login', methods=['POST'])
def hello():
    if request.method == 'POST':
        Score = ss(request.form['Answer'])
        Score = str(Score)
        return render_template('result.html', Score=Score)


if __name__ == '__main__':
    app.debug = True
    app.run()


'''from flask import Flask, request, render_template, redirect, url_for
from flask import flash

app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')

def login_check(username, password):
    """登入帳號密碼檢核"""
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run()'''


'''@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('login.html')

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.debug = True
    app.run()'''

###############################
'''@app.route('/para/<user>')
def index(user):
    return render_template('abc.html', user_template=user)

if __name__ == '__main__':
    app.debut = True
    app.run()'''
