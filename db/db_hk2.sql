-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Okt 2021 pada 17.25
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_hk2`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('ae62025a3cf8');

-- --------------------------------------------------------

--
-- Struktur dari tabel `antrianp`
--

CREATE TABLE `antrianp` (
  `id` int(11) NOT NULL,
  `id_pasien` bigint(20) DEFAULT NULL,
  `id_poli` int(11) DEFAULT NULL,
  `no_antrianp` int(11) DEFAULT NULL,
  `tgl_daftar` date DEFAULT NULL,
  `tgl_update` datetime DEFAULT NULL,
  `status` enum('1','0') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `antrianp`
--

INSERT INTO `antrianp` (`id`, `id_pasien`, `id_poli`, `no_antrianp`, `tgl_daftar`, `tgl_update`, `status`) VALUES
(1, 6, 1, 1, '2021-09-19', '2021-09-19 17:05:24', '1'),
(2, 6, 1, 2, '2021-09-19', '2021-09-19 19:22:00', '1'),
(3, 17, 1, 3, '2021-09-19', '2021-09-19 17:34:18', '1'),
(4, 6, 4, 4, '2021-09-19', '2021-09-19 17:36:43', '1'),
(5, 16, 4, 5, '2021-09-19', '2021-09-19 19:16:03', '1'),
(6, 17, 3, 6, '2021-09-19', '2021-09-19 19:21:50', '1'),
(7, 16, 2, 7, '2021-09-19', '2021-09-19 19:55:03', '1'),
(8, 6, 2, 1, '2021-09-19', '2021-09-19 22:48:06', '1'),
(9, 16, 3, 1, '2021-09-19', '2021-09-19 23:23:10', '1'),
(10, 17, 4, 1, '2021-09-19', '2021-09-19 23:22:50', '1'),
(11, 18, 1, 8, '2021-09-19', '2021-09-19 20:34:28', '1'),
(12, 6, 1, 9, '2021-09-19', '2021-09-19 21:09:32', '1'),
(13, 18, 1, 10, '2021-09-19', '2021-09-19 21:10:39', '1'),
(14, 19, 1, 11, '2021-09-19', '2021-09-19 21:17:27', '1'),
(15, 17, 2, 2, '2021-09-19', '2021-09-19 22:55:47', '1'),
(16, 20, 1, 1, '2021-09-20', NULL, '0'),
(17, 7, 1, 1, '2021-09-30', NULL, '0'),
(18, 19, 1, 2, '2021-09-30', NULL, '0'),
(19, 20, 1, 3, '2021-09-30', NULL, '0'),
(20, 20, 1, 4, '2021-09-21', NULL, '0'),
(21, 21, 1, 5, '2021-09-20', NULL, '0'),
(23, 26, 2, 1, '2021-09-20', NULL, '0'),
(24, 27, 2, 2, '2021-09-19', NULL, '0'),
(25, 29, 2, 3, '2021-09-20', NULL, '0'),
(26, 30, 3, 1, '2021-09-21', NULL, '0'),
(27, 29, 4, 1, '2021-09-30', NULL, '0'),
(28, 35, 3, 2, '2021-09-20', NULL, '0'),
(29, 34, 3, 3, '2021-09-22', NULL, '0'),
(30, 22, 1, 2, '2021-09-22', NULL, '0'),
(31, 21, 3, 1, '2021-09-30', NULL, '0'),
(32, 25, 3, 1, '2021-09-30', NULL, '0'),
(33, 25, 2, 1, '2021-09-30', NULL, '0'),
(35, 21, 1, 2, '2021-09-30', NULL, '0'),
(36, 22, 2, 1, '2021-09-21', NULL, '0'),
(37, 20, 1, 2, '2021-09-30', NULL, '0'),
(38, 9, 2, 1, '2021-09-30', NULL, '0'),
(39, 11, 2, 1, '2021-09-30', NULL, '0'),
(40, 12, 3, 1, '2021-09-24', NULL, '0'),
(41, 12, 4, 1, '2021-09-23', NULL, '0'),
(42, 9, 3, 1, '2021-09-21', NULL, '0'),
(43, 10, 3, 1, '2021-09-22', NULL, '0'),
(44, 12, 3, 1, '2021-09-30', NULL, '0'),
(45, 12, 3, 1, '2021-09-30', NULL, '0'),
(46, 12, 4, 1, '2021-09-18', NULL, '0');

-- --------------------------------------------------------

--
-- Struktur dari tabel `gender`
--

CREATE TABLE `gender` (
  `id` int(11) NOT NULL,
  `jk` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `gender`
--

INSERT INTO `gender` (`id`, `jk`) VALUES
(1, 'Pria'),
(2, 'Wanita');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pasien`
--

CREATE TABLE `pasien` (
  `id` bigint(20) NOT NULL,
  `no_identitas_p` bigint(20) NOT NULL,
  `nama_p` varchar(80) NOT NULL,
  `id_jk_p` int(11) DEFAULT NULL,
  `tgl_lahir_p` date NOT NULL,
  `alamat_p` text DEFAULT NULL,
  `telp_p` varchar(20) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `slug` varchar(80) NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id_user` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pasien`
--

INSERT INTO `pasien` (`id`, `no_identitas_p`, `nama_p`, `id_jk_p`, `tgl_lahir_p`, `alamat_p`, `telp_p`, `created_at`, `slug`, `updated_at`, `id_user`) VALUES
(40, 81101170509920002, 'Ari Efendi', 1, '1992-09-05', 'Tello Baru', '085253886660', '2021-10-16', 'ari-efendi', NULL, 32);

-- --------------------------------------------------------

--
-- Struktur dari tabel `poli`
--

CREATE TABLE `poli` (
  `id_poli` int(11) NOT NULL,
  `kode_poli` varchar(30) NOT NULL,
  `nama_poli` varchar(30) NOT NULL,
  `slug` varchar(30) NOT NULL,
  `jumlah_maks` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `poli`
--

INSERT INTO `poli` (`id_poli`, `kode_poli`, `nama_poli`, `slug`, `jumlah_maks`) VALUES
(1, 'PLUM', 'Poli Umum', 'poli-umum', 30),
(2, 'PLGG', 'Poli Gigi', 'poli-gigi', 30),
(3, 'PLSP', 'Poli Spesialis', 'poli-spesialis', 30),
(4, 'PLKIA', 'Poli Kesehatan Ibu & Anak', 'poli-kesehatan-ibu-anak', 30);

-- --------------------------------------------------------

--
-- Struktur dari tabel `role`
--

CREATE TABLE `role` (
  `id` bigint(20) NOT NULL,
  `tipe_akun` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `role`
--

INSERT INTO `role` (`id`, `tipe_akun`) VALUES
(1, 'Admin'),
(2, 'Dokter'),
(3, 'Pasien');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_antrian`
--

CREATE TABLE `tbl_antrian` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `no_antrian` int(11) DEFAULT NULL,
  `status` enum('1','0') DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_antrian`
--

INSERT INTO `tbl_antrian` (`id`, `tanggal`, `no_antrian`, `status`, `updated_date`) VALUES
(1, '2021-09-17', 1, '1', '2021-09-17 18:30:35');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(80) NOT NULL,
  `slug` varchar(80) NOT NULL,
  `telp` varchar(15) NOT NULL,
  `password` text NOT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `role_id` bigint(20) DEFAULT NULL,
  `username` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `nama`, `slug`, `telp`, `password`, `created_at`, `updated_at`, `role_id`, `username`) VALUES
(30, 'Ari Efendi', 'ari-efendi', '085253886661', '$2b$12$OE5tFE80NNl3cAMt0RGZbeaeS4TrCYvRpDmmrlRYcBds8jqZ8IX8q', '2021-09-17', '2021-09-17 10:08:06', 1, 'beta'),
(31, 'Admin', 'admin', '086426708643', '$2b$12$PEKuyAHa6CHvy7uU.PrFwepkLjGWuvQXz2fs5.B8LIo/OE75i10om', '2021-09-17', '2021-09-17 10:15:56', 1, 'admin'),
(32, 'dahlan', 'dahlan', '0824531334', '$2b$12$LCDpiwbtjChy/OTzJBYAXOeb59fdb0ItNkNBe5C9yyM3BP02H5UcO', '2021-10-16', '2021-10-16 08:06:32', 3, 'pasien'),
(33, 'yusril', 'yusril', '081343265173', '$2b$12$4uPfh599y9SiHCA6imuXi.mjcP9Up5gCkM11Mr8Z5HVQ9Yy.bmm6W', '2021-10-17', '2021-10-17 04:36:45', 3, 'pasien2'),
(35, 'Icha', 'icha', '085243114711', '$2b$12$ASBZlddRqgXMMH490h71HuhgJMIDdncQlDsgPkN/a6Il8SelM7arW', '2021-10-23', '2021-10-23 13:45:56', 3, 'icha');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indeks untuk tabel `antrianp`
--
ALTER TABLE `antrianp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pasien` (`id_pasien`),
  ADD KEY `id_poli` (`id_poli`);

--
-- Indeks untuk tabel `gender`
--
ALTER TABLE `gender`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `jk` (`jk`);

--
-- Indeks untuk tabel `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_jk_p` (`id_jk_p`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `poli`
--
ALTER TABLE `poli`
  ADD PRIMARY KEY (`id_poli`),
  ADD UNIQUE KEY `kode_poli` (`kode_poli`),
  ADD UNIQUE KEY `nama_poli` (`nama_poli`);

--
-- Indeks untuk tabel `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tipe_akun` (`tipe_akun`);

--
-- Indeks untuk tabel `tbl_antrian`
--
ALTER TABLE `tbl_antrian`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `antrianp`
--
ALTER TABLE `antrianp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT untuk tabel `gender`
--
ALTER TABLE `gender`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `pasien`
--
ALTER TABLE `pasien`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT untuk tabel `poli`
--
ALTER TABLE `poli`
  MODIFY `id_poli` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `role`
--
ALTER TABLE `role`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `tbl_antrian`
--
ALTER TABLE `tbl_antrian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `antrianp`
--
ALTER TABLE `antrianp`
  ADD CONSTRAINT `antrianp_ibfk_1` FOREIGN KEY (`id_pasien`) REFERENCES `pasien` (`id`),
  ADD CONSTRAINT `antrianp_ibfk_2` FOREIGN KEY (`id_poli`) REFERENCES `poli` (`id_poli`);

--
-- Ketidakleluasaan untuk tabel `pasien`
--
ALTER TABLE `pasien`
  ADD CONSTRAINT `pasien_ibfk_1` FOREIGN KEY (`id_jk_p`) REFERENCES `gender` (`id`),
  ADD CONSTRAINT `pasien_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`);

--
-- Ketidakleluasaan untuk tabel `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
