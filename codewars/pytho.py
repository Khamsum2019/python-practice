def to_camel_case(text):
    camel_str =''
    capitalize_next = False
    for char in text:
        if (char == '-' or char == '_'):
           capitalize_next = True
        else:
            if capitalize_next:
                camel_str += char.upper()
                capitalize_next = False
            else:
                camel_str += char
    return camel_str
def main():
    py = input("input string: ")
    out = to_camel_case(py)
    print(out)
main()