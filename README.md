# User-Defined Data Structure Python


Struktur data dalam Python secara umum dibagi menjadi dua kategori: **Built-in** (bawaan dari Python) dan **User-Defined** (yang kita buat sendiri menggunakan logika pemrograman).


## User-Defined Data Structure

Jika struktur bawaan tidak cukup efisien untuk menangani algoritma yang kompleks, kita biasanya membangun struktur ini sendiri (atau menggunakan modul seperti collections). Berikut merupakan rangkuman 5 tipe struktur data buatan:

| Struktur Data | Karakteristik Utama | Operasi Utama | Operasi Paling Sering (*Most Used*) |
| :---: | :---: | :---: | :---: |
| Stack | LIFO (*Last In, First Out*). Satu pintu masuk & keluar. | `Push`, `Pop`, `Peek`, `isEmpty` | `Push`, `Pop` |
| Queue | FIFO (*First In, First Out*). Dua pintu (depan & belakang). | `Enqueue`, `Dequeue`, `Front`, `Rear` | `Enqueue`, `Dequeue` |
| Linked List | Linear, node terhubung lewat pointer (alamat memori). | `Insert`, `Delete`, `Search`, `Traversing` | `Insert`, `Delete` |
| Tree | Hierarkis (*Parent-Child*), bercabang dari satu akar (*Root*). | `Insert`, `Search`, `Traversal` (Pre/In/Post-order) | `Search`, `Traversal` |
| Graph | Jaringan bebas (*Vertex & Edge*), bisa saling terhubung antar titik. | `Add Vertex`, `Add Edge`, `BFS`, `DFS` | `BFS`, `DFS` (Cari Rute) |
