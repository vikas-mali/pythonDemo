from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Handle the form data (e.g., save to a database)

    return f'Registration successful for {name} with email {email}.'

if __name__ == '__main__':
    app.run(debug=True)
