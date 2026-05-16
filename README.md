# Portal Alumni SMK Telkom Lampung

Website manajemen data portal resmi alumni SMK Telkom Lampung berbasis PHP & MySQLi.
Dilengkapi dengan tema warna sekolah, slideshow background dinamis, dan komentar edukatif untuk pembelajaran pemula.

---

## Struktur Proyek

```
MANAJEMEN-DATA-ALUMNI/
├── database/
│   └── db_alumni.sql          # File SQL untuk import database
├── assets/
│   ├── bg-sekolah.jpg         # Foto background utama
│   ├── bg-slideshow.js        # Script slideshow login/register
│   └── bg-slideshow-dashboard.js # Script slideshow dashboard
├── uploads/
│   └── foto_profil/           # Folder penyimpanan foto profil
├── style/
│   ├── index.css              # CSS halaman login & register (tema SMK Telkom)
│   └── dashboard.css          # CSS halaman dashboard (tema SMK Telkom)
├── index.php                  # Redirect otomatis (login/dashboard)
├── login.php                  # Halaman masuk
├── register.php               # Halaman daftar alumni
├── logout.php                 # Proses logout
├── auth.php                   # Helper autentikasi (berkomentar)
├── koneksi.php                # Koneksi database MySQLi Procedural (berkomentar)
├── navbar.php                 # Komponen navbar dengan Logo Sekolah
├── dashboard_admin.php        # Dashboard admin/superadmin
├── dashboard_user.php         # Dashboard user alumni
├── profile.php                # Halaman profil & edit
├── users.php                  # Manajemen pengguna (admin)
├── tambah.php                 # Tambah data alumni (admin)
├── tambah_user.php            # Tambah pengguna (admin)
├── edit.php                   # Edit data alumni (admin)
├── edit_user.php              # Edit pengguna (admin)
├── delete.php                 # Hapus data alumni (admin)
└── delete_user.php            # Aksi approve/reject/hapus user
```

---

## Cara Install

### 1. Persyaratan
- PHP 7.4+
- MySQL 5.7+ / MariaDB 10.3+
- Web server: Apache/Nginx (atau XAMPP/Laragon)

### 2. Setup Database
1. Buka **phpMyAdmin** atau MySQL client
2. Import file `database/db_alumni.sql`
3. Database `db_alumni` akan dibuat otomatis

### 3. Konfigurasi Koneksi
Edit file `koneksi.php` sesuai konfigurasi server Anda:
```php
$host     = 'localhost';
$dbname   = 'db_alumni';
$username = 'root';     // sesuaikan
$password = '';          // sesuaikan
```

### 4. Izin Folder
Pastikan folder `uploads/foto_profil/` dapat ditulis:
```bash
chmod 775 uploads/foto_profil/
```

### 5. Jalankan
Letakkan folder di `htdocs` (XAMPP) atau `www` (Laragon), lalu buka:
```
http://localhost/MANAJEMEN-DATA-ALUMNI/
```

---

## Akun Default

| Username    | Password   | Role       |
|-------------|------------|------------|
| admin       | password   | Admin      |
| superadmin  | password   | Superadmin |

> **Penting:** Ganti password setelah pertama kali login!

---

## Alur Penggunaan

### Alumni Baru (Register)
1. Buka halaman utama → otomatis ke `login.php`
2. Klik **"Daftar sebagai Alumni"** → `register.php`
3. Isi data akun + data alumni lengkap
4. Kirim pendaftaran → status **Pending**
5. Tunggu verifikasi admin
6. Setelah disetujui → bisa login

### Admin
- **Approve / Reject** pendaftaran dari dashboard
- **Kelola** semua data alumni (tambah, edit, hapus)
- **Kelola** pengguna (ubah role, status, reset password)

### Superadmin (semua akses admin +)
- Dapat **menghapus** akun pengguna secara permanen
- Dapat mengubah role ke **admin**

---

## Fitur Utama

- ✅ Register alumni dengan verifikasi data lengkap
- ✅ Sistem pending → approve/reject oleh admin
- ✅ Login otomatis redirect sesuai role
- ✅ Dashboard statistik (admin)
- ✅ Profil alumni + upload foto profil
- ✅ Edit profil sendiri (user hanya data miliknya)
- ✅ Pencarian & filter data alumni
- ✅ 3 level akses: user, admin, superadmin
- ✅ Keamanan: password di-hash (bcrypt), MySQLi prepared statements
- ✅ Desain Modern & Responsif (Tema Resmi SMK Telkom Lampung)
- ✅ Komentar Edukatif pada File PHP untuk Panduan Belajar Pemula

---

## Catatan Keamanan & Edukasi
- File utama `.php` telah dilengkapi komentar penjelasan (Bahasa Indonesia) untuk memudahkan pemula mempelajari logika sistem.
- Password di-hash menggunakan `password_hash()` PHP (bcrypt).
- Semua query database menggunakan **MySQLi Procedural Prepared Statements** untuk mencegah SQL Injection.
- Session-based authentication untuk pengelolaan login.
- Input disanitasi menggunakan `htmlspecialchars()`.
