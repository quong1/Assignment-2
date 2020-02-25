from urllib.request import urlopen, hashlib
import time

timeStart = time.time()
#User enter hash
hashsha1 = input("Please enter the hash:")
#Open files of common password
password = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
# Split the passwords by line and stores them into arrays
array = password.split()


#Function for normal Hash
def guess1(x):
    # Count the number tries it takes to crack the password
    count = 1
    for x in array:
        hashedGuess = hashlib.sha1(bytes(x, 'utf-8')).hexdigest()
    #Compare with the given hash value
        if hashedGuess == hashsha1:
            print("Found Hash")
            print("Number of tries:", count)
            print("The password is ", x)
            break;
        count+=1
    return x

#Functions for salted hash
def guess2(y,z):
    concat = y
    mainHash = z
    count = 1
    for x in array:
        saltHash = concat + x
        hashedGuess = hashlib.sha1(bytes(saltHash, 'utf-8')).hexdigest()
        if hashedGuess == mainHash:
            print("\tNumber of Attempts: " + count)
            print("\tMatch Word: " + y + x + "\n")
            break;
        count += 1
    return x

if " " in hashsha1:
    arr1 = hashsha1.split()
    salt = guess1(arr1[0])
    guess2(salt, arr1[1])
else:
    guess1(hashsha1)

timeEnd = time.time()
print ("Total running time: "+ str(timeEnd - timeStart))
