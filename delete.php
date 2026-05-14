<?php
session_start();
require 'auth.php';
require 'koneksi.php';
requireAdmin();

$id = (int)($_GET['id'] ?? 0);
if ($id) {
    // Hapus foto jika ada
    $stmt = $pdo->prepare("SELECT foto_profil FROM alumni WHERE id_alumni=?");
    $stmt->execute([$id]);
    $a = $stmt->fetch();
    if ($a && $a['foto_profil'] && file_exists("uploads/foto_profil/".$a['foto_profil'])) {
        unlink("uploads/foto_profil/".$a['foto_profil']);
    }
    // Set id_alumni di users menjadi null
    $pdo->prepare("UPDATE users SET id_alumni=NULL WHERE id_alumni=?")->execute([$id]);
    $pdo->prepare("DELETE FROM alumni WHERE id_alumni=?")->execute([$id]);
}
header('Location: dashboard_admin.php');
exit;
?>
