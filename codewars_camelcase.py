import re
def main():
    text = input("Text: ")
    print(camel_case(text))

def camel_case(text):
    arr = re.split(r'_|-', text)
    for i in range(1, len(arr)):    
        arr[i] = arr[i][:1].upper() + arr[i][1:]
    return ''.join(arr)
    
if __name__ == "__main__":
    main()
    