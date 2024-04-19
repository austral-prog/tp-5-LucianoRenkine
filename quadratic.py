# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    if (b**2-4*a*c)>=0:
        raiz_1 = (b*-1 + (b**2-4*a*c)**0.5)/2*a
        raiz_2 = (b*-1 - (b**2-4*a*c)**0.5)/2*a
        if raiz_1 != raiz_2:
            return f"({raiz_1}, {raiz_2})"
        else:
            return f"({raiz_1})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y = a*(x**2) + b*x + c
    return y

def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        function = f"f(x) = {a} * X^2 + {b} * X + {c}"
        return function
    elif a == 0 and b != 0 and c != 0:
        function = f"f(x) = {b} * X + {c}"
        return function
    elif a == 0 and b == 0:
        function = f"f(x) = {c}"
        return function
    elif a != 0 and b == 0 and c != 0:
        function = f"f(x) = {a} * X^2 + {c}"
        return function
    elif a != 0 and b == 0 and c == 0:
        function = f"f(x) = {a} * X^2"
        return function
    elif a != 0 and b != 0 and c == 0:
        function = f"f(x) = {a} * X^2 + {b} * X"
        return function
    elif a == 0 and b != 0 and c == 0:
        function = f"f(x) = {b} * X + {c}"
        return function
    elif a == 0 and b == 0 and c == 0:
        funtion = "f(x) = 0"
        return function

def derivation(a, b, c):
    if a == 0 and b == 0:
        derivative = f"f'(x) = 0"
        return derivative
    elif a == 0 and b != 0:
        derivative = f"f'(x) = {b}"
        return derivative
    elif a != 0 and b == 0:
        derivative = f"f'(x) = {2*a} * X"
        return derivative
    else:
        derivative = f"f'(x) = {2*a} * X + {b}"
        return derivative
