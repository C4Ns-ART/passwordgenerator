import random
import string

def sifre_olustur(length, level, output=[]): # def Fonksiyonu açtık parametrelere uzunluk, seviye, çıktı ekledik.
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits) # Sayıları dahil edecektir.
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation) # Noktalama işaretlerinide kullandırıyoruz.
    
    for i in range(length): # Burada uzunluk kadar for döngüsü yapmasını istiyoruz.
        output.append(random.choice(chars)) # Burada ascii_letters işerisinden random seçmesini istiyoruz
    return "".join(output)

print(("-" * 30) + "\n Sifre Olusturucu\n" + ("-" * 30)) # 30 Tane - yaparak arayüzü güçlendiriyoruz.

password_length = int(input("Uzunluk: "))
password_level = int(input("Zorluk: "))

password = sifre_olustur(password_length, password_level)
print("\nOluşturulan Şifre: {}".format(password))