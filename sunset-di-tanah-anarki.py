import time
import sys
import os

# Lirik lagu lengkap
lyrics = [
    "Andai ku malaikat",
    "Kupotong sayapku",
    "Dan rasakan perih di dunia bersamamu",
    "",
    "Perang kan berakhir",
    "Cinta kan abadi",
    "Di tanah anarki",
    "Romansa terjadi",
    "",
    "Jika aku relakan",
    "Jiwaku mati",
    "Itu bukan bunuh diri",
    "Tapi demi kamu",
    "",
    "Jika aku menolak",
    "Hidup kembali",
    "Itu bukan menyerah",
    "Hanya takut kehilanganmu",
    "",
    "Andai ku malaikat",
    "Kupotong sayapku",
    "Dan rasakan perih di dunia bersamamu",
    "",
    "Perang kan berakhir",
    "Cinta kan abadi",
    "Di tanah anarki",
    "Romansa terjadi",
    "",
    "Jika aku relakan",
    "Jiwaku mati",
    "Itu bukan bunuh diri",
    "Tapi demi kamu",
    "",
    "Jika aku menolak",
    "Hidup kembali",
    "Itu bukan menyerah",
    "Hanya takut kehilanganmu",
    "",
    "Hanya takut kehilanganmu",
    "Hanya takut kehilanganmu"
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def nyanyikan():
    clear_screen()
    print("🎵 Sunset di Tanah Anarki – Superman Is Dead 🎵\n")
    time.sleep(1)
    
    for baris in lyrics:
        type_text(baris)
        time.sleep(0.8 if baris.strip() != "" else 1.5)

if __name__ == "__main__":
    nyanyikan()
