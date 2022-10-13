from flask import Flask, redirect, request, render_template

app = Flask("")

user = []
@app.route("/register/", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            user.append({'username': username, 'password':password}) 
            return redirect('/auth')
    return render_template('register.html') 

@app.route("/auth/", methods=['POST', 'GET'])
def auth():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        for i in user:
            if i['username'] == username and i['password'] == password:
                return redirect("/Hello/" + username)
    return render_template("auth.html")

@app.route("/Hello/<username>", methods=['POST', 'GET'])
def hello(username):
    return render_template("hello.html", username = username)

@app.route("/", methods=['POST', 'GET'])
def pusto():
    return redirect('register')

app.run(debug=True)


