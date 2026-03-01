class Stack:
    
    # Kelas untuk mengimplementasikan struktur data Stack (Tumpukan).
    # Mengikuti prinsip LIFO (Last In, First Out).
    

    def __init__(self):
        # """Inisialisasi tumpukan sebagai list kosong."""
        self.items = []

    def is_empty(self):
        # """Mengecek apakah tumpukan kosong. Mengembalikan Boolean."""
        return len(self.items) == 0

    def push(self, item):
        # """Menambahkan elemen baru ke posisi paling atas."""
        self.items.append(item)
        print(f"[PUSH] '{item}' dimasukkan ke tumpukan.")

    def pop(self):
        # """Menghapus dan mengambil elemen teratas. Mengatasi Underflow."""
        if self.is_empty():
            return "Stack Underflow! Tumpukan kosong."
        return self.items.pop()

    def peek(self):
        # """Melihat elemen teratas tanpa menghapusnya."""
        if self.is_empty():
            return "Tidak ada elemen untuk diintip."
        return self.items[-1]

    def size(self):
        # """Mengembalikan jumlah elemen dalam tumpukan."""
        return len(self.items)

# --- Contoh Penggunaan ---
my_stack = Stack()

my_stack.push("Koin Emas")
my_stack.push("Koin Perak")

print(f"Elemen teratas: {my_stack.peek()}")
print(f"Jumlah elemen: {my_stack.size()}")

print(f"Data yang di-pop: {my_stack.pop()}")
print(f"Sisa tumpukan: {my_stack.items}")