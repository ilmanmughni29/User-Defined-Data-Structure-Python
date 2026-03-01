class GraphEdukasi:
    def __init__(self):
        # Menggunakan Adjacency List (Dictionary)
        self.adj_list = {}

    def tambah_kota(self, kota):
        if kota not in self.adj_list:
            self.adj_list[kota] = []

    def tambah_jalur(self, kota1, kota2):
        """Membuat jalur dua arah (Undirected)"""
        if kota1 in self.adj_list and kota2 in self.adj_list:
            self.adj_list[kota1].append(kota2)
            self.adj_list[kota2].append(kota1)

    def tampilkan_peta(self):
        for kota, tetangga in self.adj_list.items():
            print(f"{kota} -> {tetangga}")

# Simulasi
peta = GraphEdukasi()
peta.tambah_kota("Jakarta")
peta.tambah_kota("Bandung")
peta.tambah_jalur("Jakarta", "Bandung")
peta.tampilkan_peta()