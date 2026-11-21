def count_by(x, n):
    result = [] 
    for i in range(n):
        result.append(x*(i+1))
    return result
def main():
    x = int(input("what is x "))
    n = int(input("what is n? "))
    print (count_by(x, n))

if __name__ == "__main__":
    main()
