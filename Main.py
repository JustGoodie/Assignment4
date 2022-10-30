from flask import Flask, request, session, redirect, url_for, render_template, flash
import requests
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash

headers = {
 "X-RapidAPI-Key": "79e45bf277msh84f2840e7a48c1dp1fed2bjsnd23c661c5706",
 "X-RapidAPI-Host": "spec-it.p.rapidapi.com"
}

app = Flask(__name__)
app.secret_key = "bkvdsfkbvsfudbhsdfbhuo"

conn = psycopg2.connect(database="PyProject_db", user="postgres", password="123", host="127.0.0.1", port="5432")


@app.route('/', methods=["POST", "GET"])
def index():
    if 'loggedin' in session:
        if request.method == 'POST':
            game = request.form["gname"]
            specs = request.form["specs"]
            return redirect(url_for("game", game=game, specs=specs))
        else:
            return render_template('index.html')

    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cur.fetchone()

        if account:
            password_rs = account['password']
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['username'] = account['username']
                return redirect(url_for('index'))
            else:
                flash('Incorrect username/password')
        else:
            flash('Incorrect username/password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        repass = request.form['repass']

        if password == repass:

            _hashed_password = generate_password_hash(password)

            cur.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cur.fetchone()

            if account:
                flash('Account already exists!')
            else:

                cur.execute("INSERT INTO users (fullname, username, password) VALUES (%s,%s,%s) RETURNING *", (fullname, username, _hashed_password))
                account = cur.fetchone()
                conn.commit()
                session['loggedin'] = True
                session['username'] = account['username']
                return redirect(url_for('index'))

        else:
            flash('Passwords do not match')
    elif request.method == 'POST':

      flash('Please fill out the form!')

    return render_template('register.html')


@app.route('/Error')
def error():
    return render_template('Error.html')


@app.route("/Game", methods=["POST", "GET"])
def game():
    gameid = request.args.get('game')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.args.get('specs') == "recommended":
        cur.execute("SELECT G_NAME, CPU, RAM, GPU, DX, OS, Store, Net FROM Recommended WHERE G_NAME = %s", (gameid,))
        data = cur.fetchall()
    else:
        cur.execute("SELECT G_NAME, CPU, RAM, GPU, DX, OS, Store, Net FROM minimal WHERE G_NAME = %s", (gameid,))
        data = cur.fetchall()
    if len(data):
        return render_template('Game.html', Game=data[0])
    else:
        url = "https://spec-it.p.rapidapi.com/"+(((gameid.replace(":", "")).replace("’", "")).replace("'", "")).replace(" ", "-")

        response = requests.request("GET", url, headers=headers)

        try:
            rCPU=response.json()["recommended"]["CPU:"]
        except:
            rCPU="No requirements"
        try:
            rRAM=response.json()["recommended"]["RAM:"]
        except:
            rRAM="No requirements"
        try:
            rGPU=response.json()["recommended"]["GPU:"]
        except:
            rGPU="No requirements"
        try:
            rDX=response.json()["recommended"]["DX:"]
        except:
            rDX="No requirements"
        try:
            rOS=response.json()["recommended"]["OS:"]
        except:
            rOS="No requirements"
        try:
            rSTO=response.json()["recommended"]["STO:"]
        except:
            rSTO="No requirements"
        try:
            rNET=response.json()["recommended"]["NET:"]
        except:
            rNET="No requirements"
        try:
            mCPU=response.json()["minimum"]["CPU:"]
        except:
            mCPU=rCPU
        try:
            mRAM=response.json()["minimum"]["RAM:"]
        except:
            mRAM=rRAM
        try:
            mGPU=response.json()["minimum"]["GPU:"]
        except:
            mGPU=rGPU
        try:
            mDX=response.json()["minimum"]["DX:"]
        except:
            mDX=rDX
        try:
            mOS=response.json()["minimum"]["OS:"]
        except:
            mOS=rOS
        try:
            mSTO=response.json()["minimum"]["STO:"]
        except:
            mSTO=rSTO
        try:
            mNET=response.json()["minimum"]["NET:"]
        except:
            mNET=rNET

        if rCPU == rRAM and rRAM == rGPU and rGPU == rDX and rDX == rOS and rOS == rSTO and rSTO == rNET:

            return redirect(url_for("error"))

        else:

            cur.execute("INSERT INTO Recommended (G_NAME, CPU, RAM, GPU, DX, OS, Store, Net) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (gameid, rCPU, rRAM, rGPU, rDX, rOS, rSTO, rNET))
            cur.execute("INSERT INTO minimal (G_NAME, CPU, RAM, GPU, DX, OS, Store, Net) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (gameid, mCPU, mRAM, mGPU, mDX, mOS, mSTO, mNET))
            conn.commit()
            if request.args.get('specs') == "recommended":
                cur.execute("SELECT G_NAME, CPU, RAM, GPU, DX, OS, Store, Net FROM Recommended WHERE G_NAME = %s", (gameid,))
                data = cur.fetchall()
                cur.close()
            else:
                cur.execute("SELECT G_NAME, CPU, RAM, GPU, DX, OS, Store, Net FROM minimal WHERE G_NAME = %s", (gameid,))
                data = cur.fetchall()
                cur.close()
            return render_template('Game.html', Game=data[0])


@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('username', None)

   return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
