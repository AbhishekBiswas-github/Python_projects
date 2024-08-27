logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# Intro
print(logo)

# alphabet lisr
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(original_text, shift_amount, encode_decode):
  cipher_text = ""

  # change the direction of shifting by multiply by -1
  if encode_decode == 'decode':
    shift_amount *= -1

  # looping through the original user message
  for letter in original_text:
    # skip any number or spaces or special character
    if letter not in alphabet_list:
      cipher_text += letter
    else:
      shifted_index = alphabet_list.index(letter) + shift_amount
      shifted_index %= len(alphabet_list)
      cipher_text += alphabet_list[shifted_index]
    
  print(f"Here is your {encode_decode}d message: {cipher_text} ")

want_to_continue = 'yes'

# while loop for continue encoding and decoding
while want_to_continue == 'yes':
  # ask user whether to encode message or decode the message
  direction = input("Do you want to encrypt you message or decrypt your message.\nEnter encode for encrypt or decode for decrypt: ").lower()
  # user message
  text = input("Enter your message: ").lower()
  # number of position to be shifted
  shift = int(input("Enter shift amount: "))

  caeser(original_text=text, shift_amount=shift, encode_decode=direction)

  want_to_continue = input("\nType 'yes' if you want to go again. Otherwise type 'no: ").lower()

print("Goodbye")
