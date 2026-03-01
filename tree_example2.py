class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # Anak kiri (lebih kecil)
        self.right = None  # Anak kanan (lebih besar)

class BinaryTreeEdukasi:
    def __init__(self):
        self.root = None

    def tambah_data(self, data):
        """Fungsi utama untuk menambah data"""
        if self.root is None:
            self.root = Node(data)
            print(f"[ROOT] Menaruh {data} sebagai akar pohon.")
        else:
            self._tambah_recursive(self.root, data)

    def _tambah_recursive(self, current_node, data):
        """Logika pencarian posisi: Kiri jika kecil, Kanan jika besar"""
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
                print(f"--- Menaruh {data} di sebelah KIRI {current_node.data}")
            else:
                self._tambah_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
                print(f"--- Menaruh {data} di sebelah KANAN {current_node.data}")
            else:
                self._tambah_recursive(current_node.right, data)

    def tampilkan_urut(self, node):
        """In-order Traversal: Mencetak dari yang terkecil ke terbesar"""
        if node:
            self.tampilkan_urut(node.left)
            print(f"[{node.data}]", end=" ")
            self.tampilkan_urut(node.right)

# --- SIMULASI OTOMATIS ---
pohon = BinaryTreeEdukasi()

# Memasukkan angka secara acak
data_masuk = [50, 30, 70, 20, 40, 60, 80]
print("Membangun Pohon...")
for d in data_masuk:
    pohon.tambah_data(d)

print("\nIsi Pohon (Urut dari Terkecil ke Terbesar):")
pohon.tampilkan_urut(pohon.root)
print("\n")