def main():
    x = fuel()
    print(x)
def fuel():
    while True:
        try:
            guage = input("Fraction: ")
            x, y = guage.split("/")
            x, y = int(x), int(y)
            if x > y or x < 0:
                continue
            percent = round(x / y * 100)
            if percent >= 99:
                return "F"
            elif percent <= 1:
                return "E"
            else:
                return f"{percent}%"
        except (ValueError, ZeroDivisionError):
            pass
if __name__ == "__main__":
    main()