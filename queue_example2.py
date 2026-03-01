from collections import deque

class Queue:
    # """Implementasi struktur data Queue menggunakan deque."""
    
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        # """Mengecek apakah antrean kosong."""
        return len(self.items) == 0

    def enqueue(self, item):
        # """Menambahkan elemen ke belakang antrean."""
        self.items.append(item)
        print(f"[+] '{item}' masuk ke antrean.")

    def dequeue(self):
        # """Menghapus elemen dari depan antrean (FIFO)."""
        if self.is_empty():
            return "Queue Underflow! Antrean kosong."
        return self.items.popleft()

    def peek_front(self):
        # """Melihat elemen terdepan."""
        return self.items[0] if not self.is_empty() else None

    def size(self):
        # """Melihat jumlah orang/data dalam antrean."""
        return len(self.items)

# Simulasi
antrean_bank = Queue()
antrean_bank.enqueue("Nasabah 1")
antrean_bank.enqueue("Nasabah 2")

print(f"Dilayani: {antrean_bank.dequeue()}")