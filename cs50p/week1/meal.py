def main():
    time_str = input("what time is it?")
    time = convert(time_str)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >=18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.strip().split(":")
    h = float(hours)
    m = float(minutes)
    return h + m/60
main()