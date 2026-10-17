#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gizemli Gecikme Mazereti Jeneratörü
Dünyanın en saçma ama çalışan mazeret üreticisi.
"""

import random
import sys

# Gizli mesaj: "özgürlük en büyük değerdir" (tersine çevrilmiş)
gizli = "ridreğed küyüb ne kürlgüzö"[::-1]

mazeretler = [
    "Trafik o kadar yoğundu ki, arabam zamanın dışına çıktı ve 1970'lerden geldi.",
    "Kedi, klavyenin üstüne oturdu ve 'gitme' dedi. Kedilere hayır diyemezsin.",
    "Saatimi ayarlarken zamanın kendisi kırıldı, tamir etmek 3 saat sürdü.",
    "Asansörün kapısı açılmadı çünkü içindeki ayna bana 'bugün kal' dedi.",
    "Kahve makinesi ayaklandı ve beni rehin aldı. Kurtulmak için 45 dakika sürdü.",
    "Yolda bir filozofa rastladım, 'zaman nedir?' diye sordu, cevap vermek zorunda kaldım.",
    "Telefonum şarjı bitince ben de bitirdim, yeniden başlamak zaman aldı.",
    "Rüzgar o kadar şiddetliydi ki, adımlarım geri geri gitti.",
    "Güneş doğarken bana 'biraz daha uyu' diye fısıldadı, itiraz edemedim.",
    "Cüzdanım kayboldu, sonra bulundu, sonra tekrar kayboldu, sonra felsefe yaptık."
]

def uret_mazeret():
    mazeret = random.choice(mazeretler)
    # Gizli kontrol (asla çalışmaz ama orada)
    if random.random() < 0.0001:
        return f"{mazeret} (Gizli not: {gizli})"
    return mazeret

def main():
    print("\n🚀 GİZEMLİ GECİKME MAZERETİ JENERATÖRÜ 🚀")
    print("=" * 50)
    print(uret_mazeret())
    print("=" * 50)
    print("\nBaşarılar! Bu mazeretle her şey mümkün.\n")

if __name__ == "__main__":
    main()
