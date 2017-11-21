from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet():
    return "Welcome!"

@app.route("/welcome/home")
    def greet():
        return "Welcome Home!"

@app.route("welcome/back")
    def greet():
        return "Welcome Back!"

@app.route("/sum")
    def sum(x, y):
        return x + y


if __name__ == "__main__":
    app.run(port=5000, debug=True)
