# Contoh program sederhana struktur data STACK

class StackEdukasi:
    def __init__(self):
        self.items = []

    def push(self, data):
        print(f"--- OPERASI PUSH: '{data}' ---")
        self.items.append(data)
        self.tampilkan_status()

    def pop(self):
        if len(self.items) == 0:
            print("--- OPERASI POP: Gagal (Stack Kosong) ---")
            return
        
        data_keluar = self.items.pop()
        print(f"--- OPERASI POP: '{data_keluar}' keluar ---")
        self.tampilkan_status()

    def tampilkan_status(self):
        # Menampilkan visualisasi tumpukan saat ini
        if not self.items:
            print("Isi Stack saat ini: [ KOSONG ]")
        else:
            # Menggunakan reversed agar data terakhir (Top) muncul paling atas
            visual = " -> ".join(reversed(self.items))
            print(f"Isi Stack (Top ke Bottom): {visual}")
            print(f"Elemen Teratas (TOP): {self.items[-1]}")
        print("-" * 40)


# MULAI SIMULASI OTOMATIS

# 1. Inisialisasi
print("LOGIKA PERTAMA: Membuat tumpukan kosong.\n")
s = StackEdukasi()

# 2. Menambah data (Push)
# Data yang masuk terakhir akan selalu berada di posisi paling atas (Top)
s.push("Buku Matematika")
s.push("Buku Fisika")
s.push("Buku Sejarah")



# 3. Mengambil data (Pop)
# Perhatikan bahwa 'Buku Sejarah' yang terakhir masuk, dialah yang pertama keluar (LIFO)
print("\nLOGIKA KEDUA: Mengambil data (LIFO - Last In First Out).\n")
s.pop()
s.pop()



# 4. Push lagi setelah Pop
print("\nLOGIKA KETIGA: Menambah data baru ke tumpukan yang tersisa.\n")
s.push("Buku Biologi")