yes = ["Yes","Y", "yes", "y"]
no = ["No", "N", "no", "n"]
raw_text = str(input ("Please input text you want to code: "))
coded_text = raw_text
def replacing(coded_text, raw_text):
    print("Code looked like this on the beggining: ",raw_text)
    if (coded_text != raw_text):
        print("Thats how text looked before performing: ",coded_text)
    x = input("Please type in letter you want to replace: ")
    y = input("Please type in letter you want it replaced with: ")
    proceed = input("Proceed? (Y/N)")
    if proceed in yes:
        coded_text = coded_text.replace(x,y)
    elif proceed in no:
        print('Nothing will be done to the code')
        exit()
    coded_text = coded_text.replace(x,y)
    print("\n Code looks like this after performing",coded_text)
    again = input("Do you want to continue? (Y/N)")
    if again in yes:
        replacing(coded_text, raw_text)
    if again in no:
        exit()
replacing(coded_text, raw_text)