#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
#routed at the base URL with /
    @app.route('/')
    # the index()
    def index():
        # the h1 element
        return '<h1>Python Operations with Flask Routing and Views</h1>'
    
    # print_string view
    @app.route('/print/<string:text>')
    def print_string(text):
        print(text)
        return text
    
    # count
    @app.route('/count/<int:num>')
    def count(num):
        nums = '\n'.join([str(i) for i in range(1, num+1)])
        return nums
    
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)
    

