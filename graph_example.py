from collections import deque

class GraphLengkap:
    def __init__(self):
        self.peta = {}

    # --- 1. OPERASI DASAR (TAMBAH & CEK) ---

    def tambah_vertex(self, vertex):
        if vertex not in self.peta:
            self.peta[vertex] = []
            print(f"[+] Vertex '{vertex}' berhasil ditambahkan.")

    def tambah_edge(self, v1, v2):
        if v1 in self.peta and v2 in self.peta:
            if v2 not in self.peta[v1]: # Hindari duplikasi jalur
                self.peta[v1].append(v2)
                self.peta[v2].append(v1)
                print(f"[+] Edge ditambahkan: {v1} <---> {v2}")
        else:
            print(f"[!] Gagal: Salah satu atau kedua vertex ({v1}, {v2}) tidak ditemukan.")

    def cek_vertex(self, vertex):
        ada = vertex in self.peta
        print(f"[?] Cek Vertex '{vertex}': {'Ada' if ada else 'Tidak Ada'}")
        return ada

    def cek_edge(self, v1, v2):
        if v1 in self.peta and v2 in self.peta:
            ada = v2 in self.peta[v1]
            print(f"[?] Cek Edge {v1}-{v2}: {'Ada' if ada else 'Tidak Ada'}")
            return ada
        return False

    # --- 2. OPERASI HAPUS ---

    def hapus_edge(self, v1, v2):
        if self.cek_edge(v1, v2):
            self.peta[v1].remove(v2)
            self.peta[v2].remove(v1)
            print(f"[-] Edge {v1} <---> {v2} berhasil dihapus.")
        else:
            print(f"[!] Gagal: Edge {v1}-{v2} tidak ditemukan.")

    def hapus_vertex(self, vertex):
        if vertex in self.peta:
            # 1. Hapus semua jejak vertex ini dari daftar tetangganya
            for tetangga in self.peta[vertex]:
                self.peta[tetangga].remove(vertex)
            
            # 2. Hapus vertex itu sendiri dari dictionary utama
            del self.peta[vertex]
            print(f"[-] Vertex '{vertex}' dan semua jalurnya berhasil dihapus secara permanen.")
        else:
            print(f"[!] Gagal: Vertex '{vertex}' tidak ditemukan.")

    # --- 3. PENELUSURAN (TRAVERSAL) ---

    def bfs(self, start_node):
        """Breadth-First Search: Menyapu menyamping, level demi level"""
        if start_node not in self.peta:
            print(f"[!] BFS Gagal: '{start_node}' tidak ditemukan.")
            return

        print(f"\n>> Memulai BFS dari '{start_node}' (Menyapu level per level):")
        visited = set()     # Untuk mencatat siapa yang sudah dikunjungi
        queue = deque([start_node]) # Queue (FIFO) untuk menyusun rute kunjungan

        while queue:
            # Ambil elemen paling depan dari antrean
            node = queue.popleft()
            
            if node not in visited:
                print(node, end=" -> ")
                visited.add(node)
                
                # Masukkan semua tetangganya yang belum dikunjungi ke antrean
                for tetangga in self.peta[node]:
                    if tetangga not in visited:
                        queue.append(tetangga)
        print("Selesai")

    def dfs(self, start_node, visited=None):
        """Depth-First Search: Menyelam sedalam mungkin per cabang (Rekursif)"""
        if start_node not in self.peta:
            print(f"[!] DFS Gagal: '{start_node}' tidak ditemukan.")
            return

        if visited is None:
            print(f"\n>> Memulai DFS dari '{start_node}' (Menyelam sedalam mungkin):")
            visited = set()

        # Tandai sebagai dikunjungi dan cetak
        visited.add(start_node)
        print(start_node, end=" -> ")

        # Cek semua tetangganya, kalau belum dikunjungi, langsung selami!
        for tetangga in self.peta[start_node]:
            if tetangga not in visited:
                self.dfs(tetangga, visited)

    def tampilkan_peta(self):
        print("\n=== Adjacency List (Peta Jaringan) ===")
        for kota, tetangga in self.peta.items():
            print(f"[{kota}] terhubung dengan: {tetangga}")
        print("======================================\n")


# --- SIMULASI OTOMATIS (MENGGUNAKAN SEMUA FITUR) ---

g = GraphLengkap()

# 1. Bangun Peta dan Cek
print("--- TAHAP 1: MEMBANGUN PETA ---")
kota_list = ["Jakarta", "Bandung", "Semarang", "Surabaya", "Yogyakarta"]
for kota in kota_list:
    g.tambah_vertex(kota)

g.tambah_edge("Jakarta", "Bandung")
g.tambah_edge("Jakarta", "Semarang")
g.tambah_edge("Bandung", "Yogyakarta")
g.tambah_edge("Semarang", "Yogyakarta")
g.tambah_edge("Semarang", "Surabaya")
g.tambah_edge("Yogyakarta", "Surabaya")

g.tampilkan_peta()

# 2. Fitur Pengecekan
print("--- TAHAP 2: PENGECEKAN DATA ---")
g.cek_vertex("Bali")           # Harusnya Tidak Ada
g.cek_edge("Jakarta", "Bandung") # Harusnya Ada

# 3. Penelusuran (Traversal)
print("\n--- TAHAP 3: TRAVERSAL ---")


# BFS akan mengunjungi tetangga terdekat dulu (Bandung & Semarang), baru berlanjut.
g.bfs("Jakarta")


# DFS akan terus menelusuri satu rute (misal: Jakarta -> Bandung -> Yogyakarta -> ...) sampai ujung
g.dfs("Jakarta")
print("Selesai\n")

# 4. Fitur Hapus Edge & Vertex
print("--- TAHAP 4: PENGHAPUSAN DATA ---")
# Menghapus satu jalan saja (antara Semarang & Surabaya)
g.hapus_edge("Semarang", "Surabaya")

# Terjadi bencana, kota Bandung hilang dari peta
# Program harus pintar: Hapus vertex "Bandung", DAN hapus jalan ke Bandung dari "Jakarta" dan "Yogyakarta".
g.hapus_vertex("Bandung")

g.tampilkan_peta()