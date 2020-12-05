from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
	if(request.method == 'POST'):
			username = request.form['username']
			password = request.form['password']
			if(username == 'admin' and password == '123'):
				return render_template("admin.html")
			else:
				return render_template("index.html")
	else:
		return render_template("index.html")

@app.route("/logout")
def logout():
	return render_template("index.html")


if(__name__ == "__main__"):
	app.run(debug=True)