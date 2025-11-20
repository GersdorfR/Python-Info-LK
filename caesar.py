alphabet_klein=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_gross=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def verschieBER(text, ber):
    nachricht = ""
    for i in range(len(text)): 
        if text[i] in alphabet_klein:
            nachricht += alphabet_klein[(alphabet_klein.index(text[i])+ber)%26]
        elif text[i] in alphabet_gross:
            nachricht += alphabet_gross[(alphabet_gross.index(text[i])+ber)%26]
        else: nachricht += text[i]
    return nachricht

def entschieBER(nachricht, ber): 
    return verschieBER(nachricht, -1*ber)




def wiesoner(text, pw):
    nachricht = ""
    pw=pw.lower()
    z=0
    for i in range(len(text)): 
        if text[i] in alphabet_klein: 
            nachricht += alphabet_klein[(alphabet_klein.index(text[i])+alphabet_klein.index((pw[z%len(pw)])))%26]
        elif text[i] in alphabet_gross:
            nachricht += alphabet_gross[(alphabet_gross.index(text[i])+alphabet_klein.index((pw[z%len(pw)])))%26]
        else: 
            nachricht += text[i]
            z-=1
        z+=1
    return nachricht