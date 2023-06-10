import base64
import sys

# Author: MSVerse
# Pesan: Jangan Lupa Istirahat Kawan :)
# Website: https://www.msverse.site
# Note: Buat Kalian Yang Mau Modifikasi Program Ini Tolong Titip URL Website Saya Terima Kasih. 

def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def base64_decode(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

def encode_from_text():
    text = input("Masukkan teks untuk diencode: ")
    encoded_text = base64_encode(text)
    print("Teks terenkripsi:", encoded_text)

def decode_from_text():
    encoded_text = input("Masukkan teks terenkripsi untuk didecode: ")
    decoded_text = base64_decode(encoded_text)
    print("Teks terdekripsi:", decoded_text)

def encode_from_file():
    filename = input("Masukkan nama file teks untuk diencode (dengan ekstensi .txt): ")
    try:
        with open(filename, 'r') as file:
            text = file.read()
            encoded_text = base64_encode(text)
            print("Teks terenkripsi:", encoded_text)
    except IOError:
        print(f"Gagal membaca file: {filename}")
        print("Pastikan file ada dan dapat dibaca.")
        print("Mohon cek kembali nama file dan izin akses file.")

def decode_from_file():
    filename = input("Masukkan nama file teks terenkripsi untuk didecode (dengan ekstensi .txt): ")
    try:
        with open(filename, 'r') as file:
            encoded_text = file.read()
            decoded_text = base64_decode(encoded_text)
            print("Teks terdekripsi:", decoded_text)
    except IOError:
        print(f"Gagal membaca file: {filename}")
        print("Pastikan file ada dan dapat dibaca.")
        print("Mohon cek kembali nama file dan izin akses file.")

while True:
    print("××× 64ED-Tool ×××")
    print("1. Encode dari teks")
    print("2. Decode dari teks")
    print("3. Encode dari file")
    print("4. Decode dari file")
    print("5. Keluar")
    choice = input("Pilih opsi (1/2/3/4/5): ")

    if choice == '1':
        encode_from_text()
    elif choice == '2':
        decode_from_text()
    elif choice == '3':
        encode_from_file()
    elif choice == '4':
        decode_from_file()
    elif choice == '5':
        break
    else:
        print("Opsi yang tidak valid. Silakan pilih opsi yang sesuai.")

print("Terima kasih telah menggunakan program ini!")
