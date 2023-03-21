# this file belongs to assignment  on API's

from flask import Flask
from flask import request

here = Flask(__name__)


@here.route("/")
# def hi():
#     return "Hello , World!"

def comp_deets():
    return '''Company name : ABC Corporation ,
            Location: India ,
            Contact Detail: 999-999-9999'''

@here.route("/welcome")
def padhariye():
    return "Welcome to ABC Corporation"


if __name__ == "__main__":
    here.run(debug =True)
