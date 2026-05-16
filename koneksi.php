<?php
// ==============================================================================
// KONEKSI DATABASE (koneksi.php)
// File ini berfungsi sebagai jembatan penghubung antara kode PHP dan database MySQL
// Setiap halaman yang butuh data dari database wajib meng-include file ini.
// ==============================================================================

$host     = 'localhost'; // Server database (biasanya localhost jika pakai XAMPP)
$dbname   = 'db_alumni'; // Nama database yang ada di phpMyAdmin
$username = 'root';      // Username default bawaan XAMPP
$password = '';          // Password default bawaan XAMPP (kosong)

// 1. Melakukan koneksi menggunakan fungsi mysqli_connect
$conn = mysqli_connect($host, $username, $password, $dbname);

// 2. Mengecek apakah koneksi berhasil atau gagal
// Jika $conn bernilai false, artinya gagal terhubung
if (!$conn) {
    // Fungsi die() akan menghentikan seluruh proses PHP dan menampilkan pesan error
    die('Koneksi database gagal: ' . mysqli_connect_error());
}

// 3. Mengatur karakter encoding (opsional tapi disarankan)
// utf8mb4 memungkinkan database menyimpan semua jenis karakter, termasuk emoji.
mysqli_set_charset($conn, 'utf8mb4');
?>
