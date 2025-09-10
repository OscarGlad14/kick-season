Link Website : [Kick Season](https://oscar-glad-kickseason.pbp.cs.ui.ac.id/)

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
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

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
Jawab :
Bagan : [Bagan Request Client](https://drive.google.com/file/d/1a2xNUO2gD6PqS5Qh6Tr2Oq_QnOsDz4aD/view?usp=sharing)
Sumber bagan : [Sumber Bagan](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1/)

Berdasarkan bagan yang disajikan, request client (request HTTP) akan diterima oleh web aplikasi Django ketika user memasukkan URL pada browser. Kemudian, request tersebut diteruskan ke urls.py untuk mencocokkan alamat URL dan meneruskan ke views.py yang didefinisikan untuk memproses permintaan tersebut. Apabila diperlukan interaksi dengan database, views.py akan memanggil query ke models.py dan database akan mengembalikan hasil ke views.py. Lalu, views.py akan memilih dan mengatur tampilan dengan menggunakan template (file html) yang sesuai, lalu dikirimkan kembali ke user sebagai HTTP response yang dapat dilihat melalui browser mereka.

3. Jelaskan peran settings.py dalam proyek Django!
Settings.py berfungsi sebagai file yang menyimpan semua konfigurasi project django yang kita buat. Beberapa hal yang dapat dikonfigurasi antara lain:
- Daftar aplikasi (di bagian INSTALLED_APPS)
- Daftar host (di bagian ALLOWED HOST)
- Database
- Static file -> mengatur lokasi file statis seperti CSS, Javascript
- Middleware
- Template
Selain itu, settings.py juga digunakan untuk menyimpan informasi rahasia seperti secret key.

4. Bagaimana cara kerja migrasi database di Django?
Django menggunakan sistem migrasi berbasis file. Artinya, setiap perubahan yang kita buat pada model akan menghasilkan file migrations. File tersebut mencatat apa saja hal yang perlu diubah pada struktur database. Ketika kita menjalankan perintah manage.py makemigrations, kita akan memperoleh file yang merepresentasikan perubahan pada model. Lalu, kita jalankan perintah manage.py migrate untuk menjalankan semua perubahan yang tercantum pada file migrasi.
Referensi : [Referensi Migrasi Database pada Django](https://blog.unmaha.ac.id/migrasi-database-django-langkah-langkah-yang-benar-untuk-pengembangan-tanpa-masalah/)

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab : Menurut saya, Django dijadikan permulaan pembelajaran perangkat lunak karena memiliki dokumentasi yang lengkap. Lalu, Django juga dipilih karena memiliki fitur-fitur bawaan yang lengkap, seperti administrasi yang kuat, sistem autentikasi user, URL map, template engine, dan dukungan ORM (Object-Relational Mapping) untuk memudahkan interaksi dengan database menggunakan Python. Terakhir, Django juga memiliki sistem kemanan built-in yang cukup baik.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab :
Saya senang dengan kinerja asisten dosen pada tutorial 1 karena selalu siap membantu mahasiswa yang mengalami kesulitan atau kendala, sehingga proses tutorial yang berjalan secara online terasa mudah dan berjalan lancar.