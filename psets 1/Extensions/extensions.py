def get_media_type(filename):
    lowercase_filename = filename.lower()

    if lowercase_filename.endswith(".gif"):
        return "image/gif"
    elif lowercase_filename.endswith(".jpg") or lowercase_filename.endswith(".jpeg"):
        return "image/jpeg"
    elif lowercase_filename.endswith(".png"):
        return "image/png"
    elif lowercase_filename.endswith(".pdf"):
        return "application/pdf"
    elif lowercase_filename.endswith(".txt"):
        return "text/plain"
    elif lowercase_filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def extensions():
    filename = input("Please enter the name of the file: ")

    media_type = get_media_type(filename)
    print("Media type:", media_type)

extensions()