from collections import deque

class QueueEdukasi:
    def __init__(self):
        # Menggunakan deque untuk efisiensi operasi di kedua ujung
        self.items = deque()

    def enqueue(self, data):
        print(f"--- OPERASI ENQUEUE: '{data}' masuk antrean ---")
        self.items.append(data) # Menambah ke ujung kanan (belakang)
        self.tampilkan_status()

    def dequeue(self):
        if len(self.items) == 0:
            print("--- OPERASI DEQUEUE: Gagal (Antrean Kosong) ---")
            return
        
        data_keluar = self.items.popleft() # Mengambil dari ujung kiri (depan)
        print(f"--- OPERASI DEQUEUE: '{data_keluar}' keluar antrean ---")
        self.tampilkan_status()

    def tampilkan_status(self):
        if not self.items:
            print("Status Antrean: [ KOSONG ]")
        else:
            # Visualisasi antrean dari depan ke belakang
            visual = " -> ".join(self.items)
            print(f"Posisi Antrean (Depan ke Belakang): {visual}")
            print(f"Orang di DEPAN (Next): {self.items[0]}")
            print(f"Orang di BELAKANG (Last): {self.items[-1]}")
        print("-" * 50)


# MULAI SIMULASI OTOMATIS

print("LOGIKA PERTAMA: Memulai antrean kosong.\n")
q = QueueEdukasi()

# 1. Menambah data (Enqueue)
# Data baru selalu masuk ke barisan paling belakang
q.enqueue("Pelanggan A")
q.enqueue("Pelanggan B")
q.enqueue("Pelanggan C")



# 2. Mengambil data (Dequeue)
# Perhatikan bahwa Pelanggan A (yang pertama masuk) akan keluar duluan
print("\nLOGIKA KEDUA: Melayani antrean (FIFO - First In First Out).\n")
q.dequeue() # Pelanggan A keluar
q.dequeue() # Pelanggan B keluar



# 3. Menambah data lagi
print("\nLOGIKA KETIGA: Pelanggan baru datang saat antrean masih berjalan.\n")
q.enqueue("Pelanggan D")