def donustur(paragraf):
    kelimeler = []  
    kelime = ""  
    for karakter in paragraf:
        if karakter.isalnum():  
            kelime += karakter
        else:
            if kelime:  
                kelimeler.append(kelime)
                kelime = ""  
    if kelime:  
        kelimeler.append(kelime)

    return kelimeler  

paragraf = input("Bir paragraf girin: ")

kelimeler_listesi = donustur(paragraf)

print(kelimeler_listesi)
