#1) Coffee Shop:
import random
def coffeeShop():
    
    order_num = random.randint(1, 10)
    '''while wondering to use a while loop or for loop to keep in track
    of the order number, I chose just to randomly generate the order number for
    this time'''
    
    print("\nWelcome to our coffee shop")
    name = input("What is your name? ")
    order = input("What would you like to order? ")

    print("Here is your receipt ")
    print("Name: {}, Order: {}, Order Number: {}".format(name,order,order_num))
    

#2) Palindrome:
def palindrome(string):
<<<<<<< HEAD
    if string == str(string[::-1]):
=======
    opposite_str = str(string[::-1])
    if string == opposite_str:
>>>>>>> 5c3cf4e04c081ed5e67fdc272fefbcc40626a550
        print("True")
    else:
        print("False")
    

def main():
    coffeeShop()
    word = input("\nEnter word to check palindrome: ")
    palindrome(word)
    
if __name__ == "__main__":
    main()
