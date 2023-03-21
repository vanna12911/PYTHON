# code is from lab , supports global API's 
# here , To access your flask application open new tab in and paste the url:

#   https://{your_url}.pwskills.app:5000/



from flask import Flask
from flask import request

# here we created an object variable
app = Flask(__name__)

@app.route("/")          # 5000 is default port number over here
def hello_world():
    return "Hello, World!"

@app.route("/vella")
def vella():
    return "kaisan ba re Recursion"

@app.route("/gm")
def good_morning():
    return "Good morning , BMI=26.9 kg/m^2"

@app.route("/test", defaults = {'params':'default'})
def test_func():
    a=5*6
    return f"The output of the function comes out to be {a}"

#whenever we search something on google,it accepts keyword as input in url and at the backend ,
# it process the function requewt and serves us output at the client side

@app.route("/input_url")                                     
def input_data():                                    # accpeting input via url
    data =request.args.get("x")
    return "the input for this url is {}".format(data)        #https://black-painter-sdfyc.pwskills.app:5000/input_url?x=pista



# How do you specify a URL parameter with a default value in Flask?

#nt @app.route('/', defaults={'param': 'default'})


if __name__=="__main__":
    
    app.run(host="0.0.0.0")
