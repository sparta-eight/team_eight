from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.wrgvto4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/comment", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.eight.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/comment/delete", methods=["POST"])
def guestbook_delete():
    name_receive = request.form['name_give']
    db.eight.delete_one({'name':name_receive})
    return jsonify({'msg': '삭제 완료!'})

@app.route("/comment", methods=["GET"])
def guestbook_get():
    all_comments = list(db.eight.find({},{'_id':False}))
    return jsonify({'result': all_comments})

@app.route('/team1')
def team1():
    return render_template('team1.html')

@app.route('/team2')
def team2():
    return render_template('team2.html')

@app.route('/team3')
def team3():
    return render_template('team3.html')

@app.route('/team4')
def team4():
    return render_template('team4.html')

if __name__ == '__main__':
    app.run()