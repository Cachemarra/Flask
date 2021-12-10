from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# say_hey function
@app.route('/say_hey/<name>')
def say_hey(name):
    return f'Hey, buddy {name}!'


@app.route('/age/<int:age>')
def show_age(age):
    return f'Your age is: {age} yo'

if __name__ == '__main__':
    app.run()
