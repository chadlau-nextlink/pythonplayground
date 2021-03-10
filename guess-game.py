secret_word = "peter"
guess = ""
guess_num = 0
guess_limit = 3
cant_guess = False

while secret_word != guess and not(cant_guess):
    if guess_num < guess_limit:
        guess = input("Try the secret word: ")
        guess_num +=1
    else:
        cant_guess = True
        
if cant_guess:
    print ("You guess too many times")
else:
    print ("You win")    

