from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Xin chào từ Flask CI/CD!"

if __name__ == "__main__":
    app.run(debug=True)