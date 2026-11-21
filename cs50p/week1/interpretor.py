def filter(expression):
    leng = (len(expression.split())
    if leng == 3:
        return expression
    else 
        print("limit to 3 strings")

def interpretor(expression):
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        return (x + z)
    elif y == "-":
        return (x - z)
    elif y == "*":
        return (x * z)
    elif y == "/":
        return (x / z)
def main():
    expression = input("Expression: ")
    print(f"{interpretor(expression):.1f}")
main()