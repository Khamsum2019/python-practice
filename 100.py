def age_hun(age):
    age = (100 - age) + 2026
    return age
def main():
    name = input("Enter name: ")
    num = int(input("Enter age: "))
    age = age_hun(num)
    print(f"{name} will turn 100 in the year {age}")
main()