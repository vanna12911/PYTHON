# this file invovles all the integration with web browser on web pages and api testing with postman as well
from flask import Flask, request , render_template , jsonify

App = Flask(__name__)

@App.route("/")
def home_page():
    return render_template('index.html')

# this method is going to work for the web page on browser  
# @app.route('/math', methods = ['POST'])
# def math_op():
#     if(request.method == 'POST'):
#         ops = request.from['operation']
#         num1 =int(request.form['num1'])
#         num2 =int(request.form['num2'])
#         if ops== 'add':
#             r=  num1+num2
#             result = "the sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        

#         if ops== 'subtract':
#             r=  num1-num2
#             result = "the subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
#         if ops== 'multiply':
#             r=  num1*num2
#             result = "the multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
#         if ops== 'divide':
#             r=  num1/num2
#             result = "the divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
#         return render_template('results.html' , result = result)


# this methos is going to work for the api testing and not for the webpage on the browser
@App.route('/postman_action', methods = ['POST'])
def math_op():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 =int(request.json['num1'])
        num2 =int(request.json['num2'])
        if ops== 'add':
            r=  num1+num2
            result = "the sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        

        if ops== 'subtract':
            r=  num1-num2
            result = "the subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if ops== 'multiply':
            r=  num1*num2
            result = "the multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if ops== 'divide':
            r=  num1/num2
            result = "the divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        return jsonify(result)



if __name__=="__main__":
    App.run(host="0.0.0.0")