#ROT-13
import os
out=1
#--------------------------------------------------------------------------------------------------------------#
a={"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z"}
b={"n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
#--------------------------------------------------------------------------------------------------------------#
def rot(frase):
    traducido=""
    for i in frase:
        if i in a:
            traducido=traducido+a.get(i)
        
        if i in b:
            traducido=traducido+b.get(i)
    return traducido

def procss():
    traducir=raw_input("Ingrese frase a traducir: ")
    traduccion=rot(traducir)
    print traduccion
    
while out==1:   
    os.system('clear')
    procss()
    out=int(raw_input("Do you want still translate?0/1 "))
    







