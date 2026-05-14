<?php
function requireLogin() {
    if (!isset($_SESSION['user_id'])) {
        header('Location: login.php');
        exit;
    }
}
function requireAdmin() {
    requireLogin();
    if (!in_array($_SESSION['role'], ['admin', 'superadmin'])) {
        header('Location: dashboard_user.php');
        exit;
    }
}
function requireSuperAdmin() {
    requireLogin();
    if ($_SESSION['role'] !== 'superadmin') {
        header('Location: dashboard_admin.php');
        exit;
    }
}
function isAdmin() {
    return in_array($_SESSION['role'] ?? '', ['admin', 'superadmin']);
}
function isSuperAdmin() {
    return ($_SESSION['role'] ?? '') === 'superadmin';
}
?>
