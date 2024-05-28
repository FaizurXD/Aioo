from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Has Been Started"

def start_flask():
    app.run(debug=True)

if __name__ == '__main__':
    start_flask()
