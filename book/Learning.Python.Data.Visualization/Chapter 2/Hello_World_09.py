#Here we use string formatting to better construct our strings.
def main(readersname, amt):
    print("Hello, %s, you have read %i" % (readersname, amt)) 

if __name__ == '__main__': 
    main('Chad', 35)
