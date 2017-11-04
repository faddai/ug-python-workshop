from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_us():
    body = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
    return render_template('about.html', content=body)

@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        message = request.form.get('message')
        data = dict(message=message, name=name, email=email)

        # save the information into a database
        # email information to yourself
        
        return render_template('thank_you.html', data=data)

    return render_template('contact.html')

@app.route('/<name>')
def say_my_name(name):
    return render_template('greetings.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
