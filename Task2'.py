#Task2: breaking the encryption (Caesar Cipher) using frequency analysis

def encrypt(integer, string):

  ccipher = ''

  #doing a shift for each letter:
  for char in string:

    if char == ' ': 
      ccipher = ccipher + char
    elif char.isupper():
      ccipher = ccipher + chr( ( ( ord(char) + integer - 65 ) % 26 ) + 65 )
    elif char.islower():
      ccipher = ccipher + chr( ( ( ord(char) + integer - 97) % 26 ) + 97 )

  return ccipher

def freqAnalysis(ccipher):

  frequency = {}

  for char in ccipher:
    if char in frequency: frequency[char] += 1
    else: frequency[char] = 1

  return frequency

def breakEncryption(frequency):

    original = ''
    allValues = frequency.values()
    max1 = max(allValues) #whitespace is the first max

    if( list( frequency.keys() )[ list( frequency.values() ).index(max1) ] == ' ') :

      max2 = 0 #finding the second max value 
      for value in frequency.values():
        if( value > max2 and value < max1 ): max2 = value
      max1 = max2
  
    key = list( frequency.keys() )[ list( frequency.values() ).index(max1) ]

    rotation = ord(key.upper()) - ord('E') #E is the most frequently used letter
    rotation = (rotation + 26) % 26

    return rotation

def decrypt(integer, string):
  
  ccipher = ''
    
  #doing a shift for each letter:
  for char in string:

    if char == ' ': 
      ccipher = ccipher + char
    elif char.isupper():
      ccipher = ccipher + chr( ( ( ord(char) + ( 26 - integer ) - 65 ) % 26 ) + 65 )
    elif char.islower():
      ccipher = ccipher + chr( ( ( ord(char) + ( 26 - integer ) - 97) % 26 ) + 97 )

  return ccipher

def menu2():

  print("         Welcome to Encryption breaking system!         ")
  rotation = int(input("Choose the rotation factor for symmetric encryption (indicate integer number): "))
  phrase = input("Please enter your phrase: ")

  ccipher = encrypt(rotation, phrase)

  frequency = freqAnalysis(ccipher)
  key = breakEncryption(frequency)
  original = decrypt(key, ccipher)

  print(key)
  print("The encrypted string: ", ccipher)
  print("The decrypted string: ", original)

menu2()