from flask import Flask
from flask import request

app = Flask(__name__)

# these API'S in vs code are local and not global api so cant be used in another system where as those in laba are global.
@app.route("/")
def test_func():
    return "All good , working well and fine"

@app.route("/test")
def test2():
    return "thats how I call my test function"


if __name__ =="__main__":
    
    app.run(debug=True)






