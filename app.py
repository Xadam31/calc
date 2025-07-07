from flask import Flask, render_template, request

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            q = request.form.get("type")
            if q == "two":
                num1 = float(request.form["num1"])
                num2 = float(request.form["num2"])
                op = request.form["op1"]

                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        error = "Cannot divide by zero."
                    else:
                        result = num1 / num2
                else:
                    error = "Invalid operator."
                
                if result is not None and error is None:
                    entry = f"{num1} {op} {num2} = {result}"
                    history.append(entry)

            elif q == "three":
                num1 = float(request.form["num1"])
                num2 = float(request.form["num2"])
                num3 = float(request.form["num3"])
                op1 = request.form["op1"]
                op2 = request.form.get("op2")

                # One or two operators?
                if op2:
                    # Two operators
                    if op1 == "+":
                        temp = num1 + num2
                    elif op1 == "-":
                        temp = num1 - num2
                    elif op1 == "*":
                        temp = num1 * num2
                    elif op1 == "/":
                        if num2 == 0:
                            error = "Cannot divide by zero."
                            return render_template("index.html", error=error, history=history)
                        temp = num1 / num2

                    if op2 == "+":
                        result = temp + num3
                    elif op2 == "-":
                        result = temp - num3
                    elif op2 == "*":
                        result = temp * num3
                    elif op2 == "/":
                        if num3 == 0:
                            error = "Cannot divide by zero."
                            return render_template("index.html", error=error, history=history)
                        result = temp / num3
                    else:
                        error = "Invalid second operator"
                    
                    if result is not None and error is None:
                        entry = f"{num1} {op1} {num2} {op2} {num3} = {result}"
                        history.append(entry)
                else:
                    # One operator applied to all three
                    if op1 == "+":
                        result = num1 + num2 + num3
                    elif op1 == "-":
                        result = num1 - num2 - num3
                    elif op1 == "*":
                        result = num1 * num2 * num3
                    elif op1 == "/":
                        if num2 == 0 or num3 == 0:
                            error = "Cannot divide by zero."
                        else:
                            result = num1 / num2 / num3
                    else:
                        error = "Invalid operator"

                    if result is not None and error is None:
                        entry = f"{num1} {op1} {num2} {num3} = {result}"
                        history.append(entry)

        except Exception as e:
            error = "Error: " + str(e)

    return render_template("index.html", result=result, error=error, history=history)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/patch.notes")
def patch_notes():
    return render_template("patch.html")


if __name__ == "__main__":
    app.run(debug=True)
