

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 
 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(text , shift):
    encode_text=""
    for i in text:
        char=i
        if char in alphabet:
            position = alphabet.index(i)
            new_position= position + shift
            encode_text += alphabet[new_position]
        else:
            encode_text += char
            
    print(f"Encoded Text is  {encode_text} ")
    return encode_text

def decode(encodedtext , shift):
    decode_text= ""
    for i in encodedtext:
        char =i
        if char in alphabet:
            dposition = alphabet.index(i)
            new_position= dposition - shift
            decode_text += alphabet[new_position]
        else:
            decode_text += char
    print(f"Decoded text is {decode_text}")




direction = input("Type 'encode'to encrypt , type 'decode' to decrypt:\n ").lower()
text =input("Enter your messege\n").lower()
shift=int(input("Enter number of shifts\n"))
if shift >26:
    shift = shift % 26
want_con ="y"
while want_con == "y" or want_con == "Y" :

    if direction == "encode":
        encoded_text=encode(text=text,shift=shift)
    if direction == "decode":
        decode(encodedtext=encoded_text,shift=shift)
    want_con=input("Want to continue Press Y to Yes or N to No\n")
    if want_con=="y" or want_con=="Y":
        direction = input("Type 'encode'to encrypt , type 'decode' to decrypt:\n ").lower()
        text =input("Enter your messege\n").lower()
        shift=int(input("Enter number of shifts\n"))
        if shift >26:
            shift = shift % 26
    else:
        print("Turning off.....")