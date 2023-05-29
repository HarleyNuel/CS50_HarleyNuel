def interpreter():
    expression = input("Enter an arithmetic expression (in the format x y z): ")

    x, operator, z = expression.split()
    x = int(x)
    z = int(z)

    result = None

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    if result is not None:
        formatted_result = "{:.1f}".format(result)
        print("Result:", formatted_result)

interpreter()