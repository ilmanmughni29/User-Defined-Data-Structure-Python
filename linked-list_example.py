class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Awalnya tidak menunjuk ke mana pun

class LinkedListEdukasi:
    def __init__(self):
        self.head = None  # Linked List dimulai dengan kosong

    def tambah_di_akhir(self, data):
        print(f"--- OPERASI: Tambah '{data}' di akhir ---")
        new_node = Node(data)
        
        # Jika list kosong, node baru jadi Head
        if not self.head:
            self.head = new_node
        else:
            # Jika tidak, cari sampai ke ujung (node yang next-nya None)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.tampilkan_list()

    def hapus_data(self, kunci):
        print(f"--- OPERASI: Hapus data '{kunci}' ---")
        temp = self.head

        # Kasus 1: Data yang dihapus ada di Head
        if temp is not None and temp.data == kunci:
            self.head = temp.next
            temp = None
            self.tampilkan_list()
            return

        # Kasus 2: Cari data di tengah atau akhir
        prev = None
        while temp is not None and temp.data != kunci:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Data '{kunci}' tidak ditemukan.")
            return

        # Putuskan sambungan dan hubungkan ke node setelahnya
        prev.next = temp.next
        temp = None
        self.tampilkan_list()

    def tampilkan_list(self):
        if not self.head:
            print("List Kosong.")
        else:
            temp = self.head
            rantai = ""
            while temp:
                rantai += f"[{temp.data}] -> "
                temp = temp.next
            print(f"Rantai: {rantai}None")
        print("-" * 45)



# MULAI SIMULASI OTOMATIS

ll = LinkedListEdukasi()

# 1. Menambah data (Insertion)
ll.tambah_di_akhir("Gerbong 1")
ll.tambah_di_akhir("Gerbong 2")
ll.tambah_di_akhir("Gerbong 3")

# 2. Menghapus data di tengah (Deletion)
# Logika: Memutus rantai dari Gerbong 1 ke Gerbong 2, 
# lalu menyambungkan Gerbong 1 langsung ke Gerbong 3.
ll.hapus_data("Gerbong 2")

# 3. Menghapus Head
ll.hapus_data("Gerbong 1")