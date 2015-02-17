from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def user_input():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def calc_answer():
    number1 = int(request.form['number1'])
    operator = request.form['operator'].lower()
    number2 = int(request.form['number2'])

    answer = math_operations(number1, number2, operator)
    operator = operator_lookup(operator)

    return render_template('index.html', number1=number1,
                           operator=operator, number2=number2, answer=answer)

def math_operations(number1, number2, operator):
    if operator == 'plus':
        return number1 + number2
    elif operator == 'minus':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    elif operator == 'divide':
        return number1 / number2

def operator_lookup(operator):
    operator_dict = {'plus': '+',
               'minus': '-',
               'multiply':'*',
               'divide': '/'}
    return operator_dict.get(operator)

if __name__ == "__main__":
    app.run(debug=False)
