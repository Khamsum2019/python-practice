def extensions(filename):
    filename = filename.lower().strip()
    if filename.endswith(".gif"): 
        print("image/gif")    
    elif filename.endswith(".jpg", ".jpeg"): 
        print("image/jpeg")
    elif filename.endswith(".png"): 
        print("image/png")
    elif filename.endswith(".pdf"): 
        print("application/pdf")
    elif filename.endswith(".zip"):
        print("application/zip")
    elif filename.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")
    
def main():
    filename = input("File name: ")
    extensions(filename)
main()