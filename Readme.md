#### *Disclaimer*:
1. *This program was created to fulfill an assignment in the Python learning module at Purwadhika Digital Technology School.*
2. *This program is written in the Python programming language and is created in Indonesian Language. The available ReadMe file is also written in Indonesian*
3. *The naming of the program 'Gudang X' is merely a designation and is not intended to infringe on any copyright or intellectual property rights of anyone. This program is also created not for education purposes.*
4. *The data used by the user is dummy data, so any similarities in supplier names or titles are not intended for profit. They are solely for educational purposes and are not meant to harm any parties.

# Data Stock Gudang X

Sebuah program sederhana yang berfokus untuk pengelolaan data stock dalam pergudangan. Ditujukan untuk penyimpanan data stock gudang dengan fungsi yang lebih sederhana. Terdapat fitur pengelolaan list Produk yang berbasis CRUD (Create, Read, Update, Delete) agar pengguna bisa lebih mudah.

### Struktur Data
Struktur data adalah hal-hal yang berkaitan dengan data-dataa yang ditampilkan dan digunakan di dalam program. Data di program ini menggunakan data-data *dummy* yang tidak nyata dengan struktur sebagai berikut.

1. **Index** (Int): Sebuah penomoran unik, digunakan untuk pemanggilan baris yang ingin digunakan dalam sistem
2. **Nama Produk** (String): Nama-nama Produk dimasukan dalam data ini.
3. **Stock Barang** (int): jumlah stock barang bernilai angka.
4. **Nama Supplier** (String): Nama Supplier dari setiap produk
5. **Kategori Produk** (String): sebuah informasi dari setiap produk berdasarkan jenis-jenisnya
6. **OuM(Satuan Unit)** (String): sebuah informasi satuan unit untuk menjelaskan produk secara detail.


### Penjelasan Program
Program ini utamanya bertujuan untuk mengorganisir data-data produk yang dipunyai oleh pengguna. Pada fase pertama ini, program dijalankan menampilkan produk-produk yang terseimpan dalam Gudang X. Program ini juga mempunyai fitur, antara lain:
1. `List Produk`: sebuah fitur untuk menampilkan seluruh data dari nama-nama produk yang dimiliki.
2. CRUD : Konsep dasar dari program Data stock Gudang, untuk menampilkan, menambah, mengubah, dan menghapus data produk dalam program.

### Aplikasi CRUD Dalam Program
CRUD adalah sebuah konsep dalam pengembangan aplikasi berbasis data. Singkatan dari *Create*, *Read*, *Update*, *Delete*
1. Create: dalam program ini pengguna dapat menambahkan sebuah produk baru. Ini merupakan implementasi dari fitur *CreateProduct*. Penambahan data produk dalam `List Product` juga bisa dikatakan sebagai fungsi *Create* atau menambah produk.
2. *Read*: `ReadProduct` adalah fungsi untuk menampilkan data-data `List Product`.
3. *Update*: `UpdateProduct` ini berfungsi agar user atau pengguna dapat mengupdate atau merubah data-data dari `Product Name`, `Stock`, `Supplier`, `Category`, serta satuan unit `UoM` juga merupakan bentuk implementasi fungsi *update*. Termasuk menampilkan pengubahan-pengubahan yang terjadi pada sistem dari program Data Stock Gudang.
4. *Delete*: Menghapus Produk menggunakan `DeleteProduct` (untuk hapus produk dari `List Product`)  adalah bentuk pemakaian fitur *Delete*


### Kekurangan dan Ruang Perbaikan Pada Program
Program sangatlah sederhana. Masih banyak kekurangan yang bisa diperbaiki untuk versi lanjutannya. Beberapa kekurangannya adalah:
1. Program menggunakan data *dummy* sehingga keabsahannya harus diteliti lebih lanjut.
2. Ini merupakan program demo pembuatan aplikasi *Data Stock* Gudang/penyimpanan . Jika ingin dikembangkan, ada baiknya menambah fiture tanggal masuk/keluar nya barang agar lebih informatif dan detail sama seperti Warehouse Management System (WMS)
3. Pada fase kali ini, program memiliki keterbatasan yaitu hanya dapat menghapus produk dengan menginput `ID` dari produk yang ingin di hapus. Program dapat menghapus dengan `Product Name` jika menembangkan syntax dengan merubah dari `ID` menjadi `Product Name` serta variablenya yang awalnya `int(input)` dirubah menjadi hanya `input()`
4. Sistem `List Supplier`, `list Category`, dan `List Uom` dibuat dengan menggunakan metode input `Prime Key`, jadi daftar dari `List Supplier`, `list Category`, dan `List Uom` dapat ditambahkan melalui Syntax program.
5. Metode dalam menjalankan program masih banyak menggunakan opsi `Yes=1` dan `No=2`
6. Segala bentuk perubahan dalam sistem program dapat diubah/ditambahkan melalui syntax, sehingga jauh dari kata sempurna.
7. Segala bentuk kritikan dan saran sangat diharapkan demi mengembangkan program ini agar lebih baik untuk kedepannya.

### Kesimpulan
Program ini bertujuan untuk membantu pengguna membuat suatu data penyimpanan atau Data Stock dari gudang secara sederhana dan mudah dimengerti. Ruang perbaikan juga dapat menjadi acuan untuk pengembangan program, atau bisa juga menjadi referensi program-program lain yang sejenis.

---


Dibuat oleh Ridha Shahnabiel Hayat

JCDS 2602, Purwadhika Digital Technology School, BSD

2025