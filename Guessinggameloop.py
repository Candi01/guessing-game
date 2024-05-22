#set the secret
secret_number= 9 
guess_count=0  
guess_limit = 3  # assumes this is the number of conditions the user has made
while guess_count < guess guess_limit: # i is the number of gueses the user had. our loop will be allowed to beb excuted 4 time being  (0, 1, 2 and 3
     guess = int(input("Guess"))
     guess_count += 1
     if guess == secret_number
        print ("you won!")
        break
     else: 
         print("sorry you failed!")