<?php
session_start();
require 'auth.php';
require 'koneksi.php';
requireAdmin();

$action = $_GET['action'] ?? '';
$id     = (int)($_GET['id'] ?? 0);

switch ($action) {
    case 'approve':
        $pdo->prepare("UPDATE users SET status='approved' WHERE user_id=?")->execute([$id]);
        header('Location: ' . ($_SERVER['HTTP_REFERER'] ?? 'dashboard_admin.php'));
        break;
    case 'reject':
        $pdo->prepare("UPDATE users SET status='rejected' WHERE user_id=?")->execute([$id]);
        header('Location: ' . ($_SERVER['HTTP_REFERER'] ?? 'users.php'));
        break;
    case 'delete':
        if (!isSuperAdmin()) { header('Location: users.php'); exit; }
        // Cari id_alumni terhubung
        $stmt = $pdo->prepare("SELECT id_alumni FROM users WHERE user_id=?");
        $stmt->execute([$id]);
        $u = $stmt->fetch();
        $pdo->prepare("DELETE FROM users WHERE user_id=?")->execute([$id]);
        // Jangan hapus alumni datanya, hanya putus relasi
        header('Location: users.php');
        break;
    default:
        header('Location: dashboard_admin.php');
}
exit;
?>
