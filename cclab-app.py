print("Hello")from flask import Flask
app = Flask(__name__)

@app.route('/sid', methods=['GET'])
def sid():
    return "Hello Siddhardh"

@app.route('/hai', methods=['GET'])
def hai():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
