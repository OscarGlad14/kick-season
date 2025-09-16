# [Kick Season](https://oscar-glad-kickseason.pbp.cs.ui.ac.id/)

## TUGAS 1

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
Jawab :
Berikut adalah langkah-langkah yang saya lakukan untuk menyelesaikan seluruh checklist pada tugas 2.
- Membuat direktori lokal, inisiasi git, lalu menghubungkan direktori lokal dengan repo git
- Mengaktifkan virtual environment
- Menyiapkan dependencies di dalam file requirements.txt, lalu menginstall depedencies tersebut
- Membuat project django bernama kick season (nama football shop yang saya buat)
- Membuat file .env dan mengatur konfigurasi production menjadi false
- Membuat file .env.prod -> mengatur schema menjadi tugas_individu, meng-set production menjadi true, dan memasukkan kredensial database (nanti akan digunakan untuk production deployment)
- Melakukan konfigurasi pada file settings.py (environment varaiable, daftar host, production, dan database)
- Membuat app django bernama main
- Mengatur route pada file urls.py (di level project)
- Membuat model, templates (main.html), serta menghubungkan view dan templates pada app main
- Melakukan migrasi
- Membuat project baru di PWS dan membuat konfigurasi sesuai .env.prod
- Meng-copy link PWS, lalu memasukkan ke daftar host (allowed host)
- Melakukan add, commit, dan push ke repo git dan PWS

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
Jawab :
Bagan : [Bagan Request Client](https://drive.google.com/file/d/1a2xNUO2gD6PqS5Qh6Tr2Oq_QnOsDz4aD/view?usp=sharing)
Sumber bagan : [Sumber Bagan](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1/)

Berdasarkan bagan yang disajikan, request client (request HTTP) akan diterima oleh web aplikasi Django ketika user memasukkan URL pada browser. Kemudian, request tersebut diteruskan ke urls.py untuk mencocokkan alamat URL dan meneruskan ke views.py yang didefinisikan untuk memproses permintaan tersebut. Apabila diperlukan interaksi dengan database, views.py akan memanggil query ke models.py dan database akan mengembalikan hasil ke views.py. Lalu, views.py akan memilih dan mengatur tampilan dengan menggunakan template (file html) yang sesuai, lalu dikirimkan kembali ke user sebagai HTTP response yang dapat dilihat melalui browser mereka.

### 3. Jelaskan peran settings.py dalam proyek Django!
Settings.py berfungsi sebagai file yang menyimpan semua konfigurasi project django yang kita buat. Beberapa hal yang dapat dikonfigurasi antara lain:
- Daftar aplikasi (di bagian INSTALLED_APPS)
- Daftar host (di bagian ALLOWED HOST)
- Database
- Static file -> mengatur lokasi file statis seperti CSS, Javascript
- Middleware
- Template
Selain itu, settings.py juga digunakan untuk menyimpan informasi rahasia seperti secret key.

### 4. Bagaimana cara kerja migrasi database di Django?
Django menggunakan sistem migrasi berbasis file. Artinya, setiap perubahan yang kita buat pada model akan menghasilkan file migrations. File tersebut mencatat apa saja hal yang perlu diubah pada struktur database. Ketika kita menjalankan perintah manage.py makemigrations, kita akan memperoleh file yang merepresentasikan perubahan pada model. Lalu, kita jalankan perintah manage.py migrate untuk menjalankan semua perubahan yang tercantum pada file migrasi.
Referensi : [Referensi Migrasi Database pada Django](https://blog.unmaha.ac.id/migrasi-database-django-langkah-langkah-yang-benar-untuk-pengembangan-tanpa-masalah/)

### 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab : Menurut saya, Django dijadikan permulaan pembelajaran perangkat lunak karena memiliki dokumentasi yang lengkap. Lalu, Django juga dipilih karena memiliki fitur-fitur bawaan yang lengkap, seperti administrasi yang kuat, sistem autentikasi user, URL map, template engine, dan dukungan ORM (Object-Relational Mapping) untuk memudahkan interaksi dengan database menggunakan Python. Terakhir, Django juga memiliki sistem kemanan built-in yang cukup baik.

### 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab :
Saya senang dengan kinerja asisten dosen pada tutorial 1 karena selalu siap membantu mahasiswa yang mengalami kesulitan atau kendala, sehingga proses tutorial yang berjalan secara online terasa mudah dan berjalan lancar.

## TUGAS 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab : Data delivery diperlukan agar data yang telah dimiliki dapat tersampaikan ke client atau sistem lainnya secara cepat, akurat, dan aman melalui metode seperti XML dan JSON. Salah satu contohnya adalah mengirimkan context ke file template HTML untuk kemudian di-render dan ditampilkan ke user.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab : Menurut saya JSON lebih baik karena memiliki kemudahan dalam hal parsing. Mungkin hal ini juga yang membuat JSON lebih populer dibandingkan XML, dimana JSON dapat diparsing secara langsung oleh JavaScript (bahasa yang umum digunakan untuk membuat web), sementara XML membutuhkan parser khusus yang membuat parsing sedikit lebih panjang. Selain itu, JSON juga memiliki struktur yang lebih mudah untuk dibaca manusia karena pasangan key dan value disajikan dengan jelas, berbeda dengan XML yang agak rumit dibaca karena menggunakan banyak tag.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab : Method_is_valid pada form berfungsi untuk memeriksa dan memastikan bahwa semua field yang diisi oleh user sudah sesuai dengan tipe data dan aturan yang di-inisiasi pada file model. Method ini diperlukan agar tidak sembarang input dari user tidak langsung disimpan ke database.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab : Token CSRF dibutuhkan saat membuat form untuk mencegah terjadinya serangan CSRF. Token ini akan dibuat oleh django untuk memastikan bahwa request benar-benar berasal dari user yang mengakses website kita, bukan dari pihak lain yang tidak terpercaya. Jika tidak menambahkan csrf_token pada Django, form bisa saja menerima input dari sumber yang tidak aman. Ketiadaan csrf_django dapat dimanfaatkan oleh penyerang untuk membuat form palsu, kemudian mengirimkan requestnya ke web kita dan web akan menganggap request tersebut berasal dari user yang sah. Aksi tersebut bisa saja dimanfaatkan oleh penyerang untuk melakukan hal-hal yang tidak diinginkan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab : 
- Membuat directory template di root dan mengisinya dengan base.html (agar file html nya konsisten)
- Mengubah aturan templates pada settings.py agar base html dapat diterapkan
- Menerapkan base.html ke seluruh file HTML
- Membuat 6 function di views.py untuk menangani pembuatan produk, melihat detail produk, melihat XML, melihat JSON, melihat XML  berdasarkan ID, dan melihat JSON berdasarkan ID
- Mengatur route keenam function tersebut pada file urls.py
- Membuat file html yang berfungsi untuk membuat dan menampilkan detail produk, kemudian memasukkan nama file HTML ke render yg - ada di views.py (base.html juga diterapkan di file HTML ini)
- Mencoba runserver di lokal untuk memastikan semua berjalan sesuai harapan
- Setelah berjalan sesuai harapan, melakukan commit add push ke Git dan PWS

### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawab : Saya senang dengan kinerja asisten dosen pada tutorial 2 karena dokumen tutorial ditulis dengan jelas. Selain itu, asisten dosen juga selalu siap membantu mahasiswa yang mengalami kesulitan atau kendala, sehingga proses tutorial dapat berjalan lancar.

## Screenshoot hasil postman
### Show XML
![Show XML](./assets/ShowXML.png)

### Show JSON
![Show JSON](./assets/ShowJSON.png)

### Show XML by ID
![Show XML By ID](./assets/ShowXMLbyID.png)

### Show JSON by ID
![Show JSON By ID](./assets/ShowJSONbyID.png)
