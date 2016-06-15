#Let's format the string to output a float with two decimal places.
def main(readersname, amt):
    print("Hello, %s, your total pages read are %0.2f." % (readersname, amt)) 

if __name__ == '__main__': 
    main('Chad', 50)
