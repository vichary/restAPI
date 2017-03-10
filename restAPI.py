#!flask/bin/python
from flask import Flask, request, jsonify
import sqlite3

#
# Create a database called MYRESTAPI.DB and create two tables
#
db = sqlite3.connect("MYRESTAPI.DB", check_same_thread = False)

db.execute('''create table if not exists users(user_id integer primary key autoincrement,
                                                username text, fname text, lname text);''')
db.execute('''create table if not exists addresses(addr_id integer primary key autoincrement,
                                                address text);''')
app = Flask(__name__)

#
# GET and POST methods
# if method is GET, respond with all the user details
# i.e., http://localhost:5000/users
# if method is POST, take input as params from uri
# e.g., http://localhost:500/users?uname=vichary&fname=vishwa&lname=chary&addr=jpnagar,Bangalore,KA
# all the methods are tested with postman 
#
@app.route('/users', methods=['GET','POST'])
def get_all_users():
    if request.method == 'GET':
        try:
            cursor1 = db.execute('select * from users')
            cursor2 = db.execute('select * from addresses')
            users = []
            
            for user,addr in zip(cursor1,cursor2):
                uname,fn,ln,addr = user[1],user[2],user[3],str(addr[1])
                userinfo = dict(zip(("username","fname","lname","address"),(uname,fn,ln,addr.split(','))))
                users.append(userinfo)
                
            return jsonify({'users': users})
        except Exception as e:
            return str(e)
    
    elif request.method == 'POST':
        uname = request.args.get('uname')
        fname = request.args.get('fname')
        lname = request.args.get('lname')
        addr = str(request.args.get('addr'))
               
        try:
            db.execute('insert into users(username,fname,lname) values (?,?,?)', (uname,fname,lname))
            db.execute('insert into addresses(address) values (?)', (addr,))
            db.commit()
            #db.close()
        except Exception as e:
            return str(e)
        else:
            return "200 ok"       

        
        
#
# GET method for specified user
# e.g., http://localhost:5000/user/vichary
#
@app.route('/user/<uname>', methods=['GET'])
def get_user(uname):
    try:
        cursor = db.execute('select * from users where username=?',(uname,))
        uid,uname,fn,ln = cursor.fetchone()    
        addr = db.execute('select address from addresses where addr_id=?', (int(uid),)).fetchone()[0]
        userinfo = dict(zip(("username","fname","lname","address"),(uname,fn,ln,addr.split(','))))

        return jsonify({'user': userinfo})
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
