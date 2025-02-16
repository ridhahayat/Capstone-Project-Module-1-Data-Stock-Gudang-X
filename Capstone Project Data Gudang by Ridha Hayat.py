

list_supplier = ['PT. Adibas', 'PT. Kastile', 'PT. Acryl Tex', 'PT. Lucky Print', 'PT. Sunrise', 'PT. Hanabi', 'PT. Kinmuster'] # List Supplier bisa ditambah sesuai kebutuhan secara manual
list_kategori = ['Textile', 'Stationary', 'Kitchen Set', 'Tools', 'Sembako'] # List Kategori bisa ditambah sesuai kebutuhan secara manual
list_uom = ['kg', 'pcs', 'lusin', 'ball', 'box', 'btg'] # List UoM bisa ditambah sesuai kebutuhan secara manual

list_product = [
    {'ID' : 1, 'Product Name' : 'Beras', 'Stock' : 30, 'Supplier' : 'PT. Wilmar', 'Category' : 'Sembako', 'UoM' : 'kg'},
    {'ID' : 2, 'Product Name' : 'Pensil', 'Stock' : 100, 'Supplier' : 'PT. Kastile', 'Category' : 'Stationary', 'UoM' : 'pcs'},
    {'ID' : 3, 'Product Name' : 'Handuk', 'Stock' : 50, 'Supplier' : 'PT. Acryl Tex', 'Category' : 'Textile', 'UoM' : 'pcs'}
    ] # Tampilan List Product bisa ditambah secara manual (tampilan menu 1) ataupun secara program menu

def ReadProduct():
    PrintProduct()
    while True:
        if len(list_product) < 1: 
            print("Tidak ada data")
            print()
            break
        else:
            pilihan = input("Masukkan ID Product yang ingin dilihat atau ketik 'exit' untuk kembali ke menu utama: ")
            if pilihan.lower() == 'exit':  # User bisa keluar dengan ketik 'exit'
                break
                
            pilihan_int = int(pilihan)
            try: 
                pilihan_int = int(pilihan)
                if AdaData(pilihan_int):  # Cek apakah ID ada di list_product
                    PrintSpesifikData(pilihan_int)
                    print()
                else:
                    print("ID Product tidak ditemukan.")
                    print()

            except ValueError:
                print("Input tidak valid. Masukkan angka ID atau ketik 'exit' untuk keluar.")
                print()
        

def PrintProduct():
    print(' ID | Product Name     | Stock   | Supplier            | Category      | UoM         ') #untuk tampilin kolom
    print("-" * 80)
    for i, product in enumerate(list_product): #untuk tampilin isi kolom
        print(f"{product['ID']:3} | {product['Product Name']:16} | {product['Stock']:7} | {product['Supplier']:19} | {product ['Category']:13} | {product['UoM']:15}")
        print("-" * 80)

def CheckDuplicate(index_yang_dipilih):
    # set flag 0 sebagai tanda kalau index loop yang dicari belum ketemu ada yang sama
    flag = 0

    for i, product in enumerate(list_product): #looping dari list_product
        if index_yang_dipilih == product['ID']: #yg bakal diinput itu "ID"
            flag = 1

    if flag == 1: # Klo id yang di input sama dengan prodoct id yang ada di list product
        return True
    else : #kalo ga = ga ada duplicate
        return False

def InsertProduct(index, nama_product, stock, supplier, category, UoM): #mendefinisikan fungsi
    product = {'ID' : index, 'Product Name' : nama_product, 'Stock' : stock, 'Supplier' : supplier, 'Category' : category, 'UoM' : UoM} #membuat dictionary berisi informasi dari product

    list_product.insert(index, product)

def CreateProduct():
    while True:
        try:
            choice = int(input('Apakah anda ingin menambahkan Product? Yes=1, No=2 : ')) #pilihannya integer (angka)
            if choice == 1: #digunakan untuk pilihan "yes = 1"
                PrintProduct()
                index_product = int(input('Masukkan ID Product yang ingin ditambah: '))
                duplicate = CheckDuplicate(index_product) #digunakan untuk cek, index yg diinput itu ada yg duplikat atau ga
                if duplicate == True: #kalo ada yg duplikat, akan print "data sudah ada"
                    print('Data Sudah Ada')
                else: #kalo ga ada duplikat, langsung input product name & stock
                    nama_product = input('Masukkan Product Name: ')
                    stock_product = int(input('Masukkan Stock Product: '))

                    for i, supply in enumerate(list_supplier): #looping data list_supplier
                        i += 1 #dimulai dari 1 bukan 0
                        print(i, supply)
                    supplier_product = int(input('Masukkan Daftar Supplier: ')) #memilih menu
                    supplier_product -= 1

                    for i, category in enumerate(list_kategori): #looping untuk list_kategori
                        i += 1
                        print(i, category)
                    category_product = int(input('Masukkan Category: ')) #memilih pilihan kategori 1-5
                    category_product -= 1
                    
                    for i, uom in enumerate(list_uom): #looping untuk list_Uom
                        i += 1
                        print(i, uom)
                    uom_product = int(input('Masukkan Uom (Satuan Ukur): ')) #memilih pilihan Uom
                    uom_product -= 1

                    InsertProduct(index_product, nama_product, stock_product, list_supplier[supplier_product], list_kategori[category_product], list_uom[uom_product])
                    print('Data sudah tersimpan')
            elif choice == 2:
                break
        except ValueError:
                print("Input tidak valid. Masukkan Yes=1  atau No=2 untuk keluar.")    
        

def AdaData(cari_data): #cek ID product
    flag = 0 #permulaian data

    for i, product in enumerate(list_product):
        if product['ID'] == cari_data: #bakal cari data product berdasarkan "ID"
            flag = 1
     
    if flag == 1: #jika data ditemukan, maka akan muncul
        return True
    else: #kalo ga, ga muncul
        print('Data yang anda cari tidak ada')
        return False

def PrintSpesifikData(cari_data):
    for i, product in enumerate(list_product):
        if product['ID'] == cari_data: #mengecek data berdasarkan ID
            print(' ID | Product Name     | Stock   | Supplier            | Category      | UoM         ')
            print('-'*80)
            print(f"{product['ID']:3} | {product['Product Name']:16} | {product['Stock']:7} | {product['Supplier']:19} | {product['Category']:13} | {product['UoM']:15}")
            print('-'*80)

def UpdateKolom(kolom_update, cari_data, value_kolom): #untuk update salah satu kolom
    for i, product in enumerate(list_product):
        if product['ID'] == cari_data: #berdasarkan ID
            product[kolom_update] = value_kolom #updatean apa yg mau diinput

def PrintProductColumn(cari_data):
     for i, product in enumerate(list_product):
        if product['ID'] == cari_data: #jika ID product cocok dengan yang dicari
            print("/".join(product.keys())) #menggabungkan semua nama kolom jadi 1 string

def EditProduct():
    while True:
        try:
            choice = int(input('Apakah anda ingin Update Stock Product? Yes=1 No=2 : '))

            if choice == 1 :
                cari_data = (int(input('Masukkan ID Product yang ingin di Update: ')))

                # Jika Ada data, boleh lanjut kodingan yang bawah
                if AdaData(cari_data) == True: #utk pastiin datanya ada/ga
                    PrintSpesifikData(cari_data)

                    choice2 = int(input('Lanjut Update? Yes=1 No=2: ')) 
                    if choice2 == 1: #kalo pilih 1, akan lanjut ke inputan untuk lakukan update data
                        PrintProductColumn(cari_data)
                        kolom_update = input('Input kolom yang akan di Update: ')
                        value_kolom = input('Input Data yang ingin di Update: ')
                        UpdateKolom(kolom_update, cari_data, value_kolom) #akan melakukan perubahan pada data
                        print('Data telah di Update')
            elif choice == 2 :
                break
        except ValueError:
                print("Input tidak valid. Masukkan Yes=1  atau No=2 untuk keluar.")    


def DeleteData(cari_data):
    for i, product in enumerate(list_product): #variabel -> product & data akan diambil dari variabel list_product berupa "ID"
        if product['ID'] == cari_data:
            list_product.remove(product) #akan menghapus data berdasarkan ID yang diinput
            print("Data berhasil dihapus")


def DeleteProduct():
    while True :
        try:
            choice = int(input('Apakah anda ingin Delete Stock Product? Yes=1 No=2 : ')) #input berupa angka 1 (yes) atau 2 (No)

            if choice == 1 :
                cari_data = int(input('Masukkan ID Product yang ingin di Delete: '))
                
                if AdaData(cari_data) == True: #untuk cek datanya (ada atau ga)
                    PrintSpesifikData(cari_data)
                    hapus_product = int(input('lanjut Delete? Yes=1 No=2: ')) #input angka 1(yes) atau 2(no)
                    if hapus_product == 1: #kalo yes, maka data tersebut akan ter-delete
                        DeleteData(cari_data)
            elif choice == 2:
                break
            else:
                print('Inputan tidak sesuai')
        
        except ValueError:
                print("Input tidak valid. Masukkan Yes=1  atau No=2 untuk keluar.")    


def main(): #untuk nampilin apa yg akan tampil ketika klik "run"
    while True:
        print("\tSelamat Datang di Gudang X")
        print()
        print("list Menu: ")
        print('\n1. Menampilkan Daftar Product' '\n2. Menambah Product' '\n3. Mengupdate Stock Product' '\n4. Menghapus Product' '\n5. Exit Program')
        
        menu = int(input("Masukkan angka Menu yang ingin dijalankan : "))

        if menu > 5 or menu < 1:
            print('Pilihan Yang anda masukkan salah')

        elif menu == 5:
            break
        elif menu == 1:
            ReadProduct()
        elif menu == 2:
            CreateProduct()
        elif menu == 3:
            EditProduct()
        elif menu == 4:
            DeleteProduct()


main()
