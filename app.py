import random
import sys # import sys module

def random_quote():
    quotes = [
        "\nThe only way to do great work is to love what you do. -Steve Jobs\n",
        "\nSuccess is not the key to happiness. Happiness is the key to success. -Albert Schweitzer\n",
        "\nIn the middle of difficulty lies opportunity. -Albert Einstein\n",
        "\nBelieve you can and you're halfway there. -Theodore Roosevelt\n",
        "\nYour time is limited, so don't waste it living someone else's life. Don't be trapped by dogma, which is living with the results of other people's thinking. -Steve Jobs\n",
        "\nThe way to get started is to quit talking and begin doing. -Walt Disney\n",
        "\nThe future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt\n",
        "\nIf you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey\n",
        "\nIf you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron\n",
        "\nYou must be the change you wish to see in the world. -Mahatma Gandhi\n",
        "\nDo one thing every day that scares you. -Eleanor Roosevelt\n",
        "\nSuccess is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill\n",
        "\nIf you can dream it, you can do it. -Walt Disney\n",
        "\nThe best way to find out if you can trust somebody is to trust them. - Ernest Hemingway\n",
        "\nThe most important thing is to enjoy your life - to be happy - it's all that matters. - Steve Jobs\n",
    ]
    quote = random.choice(quotes)
    print(quote)
    

# Start a while loop with True condition
while True:
    # Call the random_quote function
    random_quote()
    
    # Ask the user if they want to quit or continue
    choice = input("Do you want to quit (Q) or continue (C)? ")
    
    # If the user enters Q or q, quit the program
    if choice == "Q" or choice == "q":
        print("\nGoodbye!\n")
        sys.exit() # terminate the program
        
    # If the user enters C or c, continue the loop
    elif choice == "C" or choice == "c":
        print("\nLet's go on!\n")
        continue # resume the next iteration
        
    # If the user enters anything else, print an error message and repeat the loop
    else:
        print("Invalid input! Please enter Q or C.")
        