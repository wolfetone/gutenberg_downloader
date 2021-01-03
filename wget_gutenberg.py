import wget
import os

path = os.path.dirname(__file__)
number_to_download = 25
count = 1

while count < number_to_download:
    count += 1
    try:
        print("\nDowloading file: " + "https://www.gutenberg.org/files/" + str(count) + "/" + str(count) + ".txt")
        print("To: " + path)
        wget.download("https://www.gutenberg.org/files/" + str(count) + "/" + str(count) + ".txt", path)
        print("\n")
    except:
        print("*** File does not exist ***")