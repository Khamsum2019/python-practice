def camel_to_snake(camel_str):
    snake_str = ''
    for char in camel_str:
        if char.isupper():
            snake_str = snake_str + '_' + char.lower()
        else:
            snake_str = snake_str + char
    return snake_str 
def main():
    snake_str = camel_to_snake(input("camelCase: "))
    print(f"snake_case: {snake_str}")
main()