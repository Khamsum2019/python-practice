def main():
    grocery()
def grocery():
    GRO = {}
    while True:
        try:
            item = input().strip().upper()
        except (EOFError, KeyboardInterrupt):
            for items in sorted(GRO):
                print(f"{GRO[items]} {items}")
            break   
        if item in GRO:
            GRO[item]     += 1
        else:
            GRO[item] = 1

if __name__ == "__main__":
    main()
