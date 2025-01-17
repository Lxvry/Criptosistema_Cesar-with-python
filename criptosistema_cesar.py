import sys

#Variable Global
ABCD = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", " "]

valores_abcd = []
valores_nuevos_abcd = []
result = []

print("[+] INGRESE EL TEXTO O MENSAJE A CIFRAR: \n")
text = str(input("")).upper()

def criptosistema_cesar(key, texto):

    for i in texto:
        if i in ABCD:
            valores_abcd.append(ABCD.index(i))
    for e in valores_abcd:
        if e + key >= 26:
            encryptation = e + key - 26
            valores_nuevos_abcd.append(encryptation)
        else:
            encryptation = e + key
            valores_nuevos_abcd.append(encryptation)

    for numer in valores_nuevos_abcd:
        letter = ABCD[numer]
        result.append(letter)
    print ("".join(result).lower())
            


if "-c" in sys.argv:
    c_index = sys.argv.index("-c")

    if c_index + 1 < len(sys.argv):
        try:
            numero = int(sys.argv[c_index + 1])
            criptosistema_cesar(numero, text)
        except ValueError:
            print("[!] El valor ingresado en el parametro -c no es correcto.")
    else:
        print("Error: El valor despues de '-c' debe ser un numero")
else:
    print("Error: el argumento '-c' no fue proporcionado")




