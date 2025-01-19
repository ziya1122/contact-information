from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contactform.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    return f"<h1>Details Submitted:</h1><p>Name: {name}</p><p>Email: {email}</p><p>Phone: {phone}</p>"

if __name__ == "__main__":
    app.run(debug=True)