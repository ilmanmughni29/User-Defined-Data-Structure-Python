class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # Anak kiri
        self.right = None  # Anak kanan

class TreeEdukasi:
    def __init__(self):
        self.root = None
            
    def cetak_pohon(self, node, level=0):
        """Fungsi Rekursif: Membaca semua anak dan cucu tanpa batas"""
        if node is not None:
            # Membuat visualisasi indentasi (jarak) berdasarkan levelnya
            print("    " * level + "|-- " + str(node.data))
            
            # Rekursi ke anak kiri dan kanan
            self.cetak_pohon(node.left, level + 1)
            self.cetak_pohon(node.right, level + 1)

    def simulasi_visual(self, pesan):
        print(f"\n--- {pesan} ---")
        self.cetak_pohon(self.root)
        print("-" * 30)

    def telusuri_preorder(self, node):
        """Metode membaca: Root -> Kiri -> Kanan"""
        if node:
            print(f"{node.data} > ", end="")
            self.telusuri_preorder(node.left)
            self.telusuri_preorder(node.right)


# --- MULAI SIMULASI OTOMATIS ---

t = TreeEdukasi()

# 1. Membuat Root
t.root = Node("Manager")
t.simulasi_visual("Membuat Root")

# 2. Menambah Anak (Level 1)
t.root.left = Node("Staf A")
t.root.right = Node("Staf B")
t.simulasi_visual("Menambah Staf A & B")

# 3. Menambah Cucu (Level 2) - Sekarang akan terbaca!
t.root.left.left = Node("Magang 1")
t.root.left.right = Node("Magang 2")
t.simulasi_visual("Menambah Magang di bawah Staf A")

# 4. Menambah Cicit (Level 3) - Untuk membuktikan rekursi bekerja
t.root.left.left.left = Node("Tugas Akhir")
t.simulasi_visual("Menambah Tugas di bawah Magang 1")

# 5. Traversal (Penelusuran)
# Cara komputer "membaca" seluruh isi pohon
print("\nLOGIKA: Cara Komputer Membaca Pohon (Pre-order Traversal):")
t.telusuri_preorder(t.root)
print("\n(Alur: Manager -> Staf A -> Magang 1 -> Tugas Akhir -> Magang 2 -> Staf B)")