def deep(n):

    if n == "42":
        print("yes")
    elif n == "forty-two":
        print("yes")
    elif n == "forty two":
        print("yes")
    else:
        print("incorrect")
def main():
    query = input("what is the answer to the ultimate question of life, the universe, and everything?")
    deep(query)

main()