-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.4.3 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for geohealthtracker_db_2510010102
CREATE DATABASE IF NOT EXISTS `geohealthtracker_db_2510010102` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `geohealthtracker_db_2510010102`;

-- Dumping structure for table geohealthtracker_db_2510010102.balita
CREATE TABLE IF NOT EXISTS `balita` (
  `nik_balita` char(10) NOT NULL,
  `nm_balita` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jk` char(1) DEFAULT NULL,
  `nm_ortu` varchar(50) DEFAULT NULL,
  `kd_kel` char(5) DEFAULT NULL,
  PRIMARY KEY (`nik_balita`),
  KEY `idx_nik_balita` (`nik_balita`),
  KEY `idx_kd_kel` (`kd_kel`),
  CONSTRAINT `balita_ibfk_1` FOREIGN KEY (`kd_kel`) REFERENCES `kelurahan` (`kd_kel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.balita: ~15 rows (approximately)
INSERT INTO `balita` (`nik_balita`, `nm_balita`, `tgl_lahir`, `jk`, `nm_ortu`, `kd_kel`) VALUES
	('B001', 'Andi', '2022-01-01', 'L', 'Budi', 'K001'),
	('B002', 'Siti', '2021-05-10', 'P', 'Ani', 'K002'),
	('B003', 'Rina', '2022-03-15', 'P', 'Dedi', 'K001'),
	('B004', 'Dina', '2021-08-20', 'P', 'Sari', 'K001'),
	('B005', 'Rudi', '2022-06-11', 'L', 'Agus', 'K002'),
	('B006', 'Lina', '2021-12-01', 'P', 'Wati', 'K002'),
	('B007', 'Bayu', '2022-09-09', 'L', 'Joko', 'K001'),
	('B008', 'Nina', '2022-02-02', 'P', 'Rudi', 'K001'),
	('B009', 'Fajar', '2021-11-11', 'L', 'Siti', 'K002'),
	('B010', 'Rahma', '2022-04-12', 'P', 'Sulastri', 'K001'),
	('B011', 'Yoga', '2021-07-17', 'L', 'Hendra', 'K002'),
	('B012', 'Alya', '2022-10-05', 'P', 'Nina', 'K001'),
	('B013', 'Rizki', '2021-09-30', 'L', 'Hasan', 'K002'),
	('B014', 'Putri', '2022-01-25', 'P', 'Dewi', 'K001'),
	('B015', 'Rizky Jr', '2026-01-01', 'L', 'M. Rizky Rinaldy (2510010102)', 'K001');

-- Dumping structure for table geohealthtracker_db_2510010102.kelurahan
CREATE TABLE IF NOT EXISTS `kelurahan` (
  `kd_kel` char(5) NOT NULL,
  `nm_kel` varchar(50) DEFAULT NULL,
  `poly_wil` text,
  `kd_puskesmas` char(5) DEFAULT NULL,
  PRIMARY KEY (`kd_kel`),
  KEY `kd_puskesmas` (`kd_puskesmas`),
  CONSTRAINT `kelurahan_ibfk_1` FOREIGN KEY (`kd_puskesmas`) REFERENCES `puskesmas` (`kd_puskesmas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.kelurahan: ~2 rows (approximately)
INSERT INTO `kelurahan` (`kd_kel`, `nm_kel`, `poly_wil`, `kd_puskesmas`) VALUES
	('K001', 'Kelurahan Melati', 'POLYGON(...)', 'P001'),
	('K002', 'Kelurahan Mawar', 'POLYGON(...)', 'P002');

-- Dumping structure for table geohealthtracker_db_2510010102.log_imunisasi
CREATE TABLE IF NOT EXISTS `log_imunisasi` (
  `id_log` int NOT NULL AUTO_INCREMENT,
  `no_transaksi` int DEFAULT NULL,
  `aktivitas` varchar(100) DEFAULT NULL,
  `waktu` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_log`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.log_imunisasi: ~4 rows (approximately)
INSERT INTO `log_imunisasi` (`id_log`, `no_transaksi`, `aktivitas`, `waktu`) VALUES
	(1, 23, 'Data imunisasi baru ditambahkan untuk Balita: B012', '2026-05-16 12:32:46'),
	(2, 24, 'Data imunisasi baru ditambahkan untuk Balita: B012', '2026-05-16 12:39:16'),
	(3, 25, 'Data imunisasi baru ditambahkan untuk Balita: B012', '2026-05-16 12:41:28'),
	(4, 26, 'Data imunisasi baru ditambahkan untuk Balita: B012', '2026-05-16 12:42:05');

-- Dumping structure for table geohealthtracker_db_2510010102.puskesmas
CREATE TABLE IF NOT EXISTS `puskesmas` (
  `kd_puskesmas` char(5) NOT NULL,
  `nm_puskesmas` varchar(25) DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL,
  `lat` decimal(10,6) DEFAULT NULL,
  `long` decimal(10,6) DEFAULT NULL,
  PRIMARY KEY (`kd_puskesmas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.puskesmas: ~3 rows (approximately)
INSERT INTO `puskesmas` (`kd_puskesmas`, `nm_puskesmas`, `alamat`, `lat`, `long`) VALUES
	('P001', 'Puskesmas A', 'Jl. Sehat 1', -6.200000, 106.800000),
	('P002', 'Puskesmas B', 'Jl. Sehat 2', -6.210000, 106.810000),
	('P03', 'Puskesmas Rizky Rinaldy', 'Jl. Sultan Adam (NIM: 2510010102)', NULL, NULL);

-- Dumping structure for table geohealthtracker_db_2510010102.riwayat_imunisasi
CREATE TABLE IF NOT EXISTS `riwayat_imunisasi` (
  `no_transaksi` int NOT NULL AUTO_INCREMENT,
  `tanggal` date DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `nik_balita` char(10) DEFAULT NULL,
  `kd_vaksin` char(10) DEFAULT NULL,
  `kd_puskesmas` char(5) DEFAULT NULL,
  PRIMARY KEY (`no_transaksi`),
  KEY `nik_balita` (`nik_balita`),
  KEY `kd_vaksin` (`kd_vaksin`),
  KEY `kd_puskesmas` (`kd_puskesmas`),
  KEY `idx_tanggal_imunisasi` (`tanggal`),
  CONSTRAINT `riwayat_imunisasi_ibfk_1` FOREIGN KEY (`nik_balita`) REFERENCES `balita` (`nik_balita`),
  CONSTRAINT `riwayat_imunisasi_ibfk_2` FOREIGN KEY (`kd_vaksin`) REFERENCES `vaksin` (`kd_vaksin`),
  CONSTRAINT `riwayat_imunisasi_ibfk_3` FOREIGN KEY (`kd_puskesmas`) REFERENCES `puskesmas` (`kd_puskesmas`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.riwayat_imunisasi: ~26 rows (approximately)
INSERT INTO `riwayat_imunisasi` (`no_transaksi`, `tanggal`, `status`, `nik_balita`, `kd_vaksin`, `kd_puskesmas`) VALUES
	(1, '2023-01-01', 'Lengkap', 'B001', 'V001', 'P001'),
	(2, '2023-01-10', 'Lengkap', 'B002', 'V002', 'P002'),
	(3, '2023-01-15', 'Tidak', 'B003', 'V001', 'P001'),
	(4, '2023-01-01', 'Lengkap', 'B001', 'V001', 'P001'),
	(5, '2023-01-10', 'Lengkap', 'B002', 'V002', 'P002'),
	(6, '2023-01-15', 'Tidak', 'B003', 'V001', 'P001'),
	(7, '2023-02-01', 'Lengkap', 'B001', 'V002', 'P001'),
	(8, '2023-02-05', 'Lengkap', 'B001', 'V003', 'P001'),
	(9, '2023-02-10', 'Lengkap', 'B004', 'V001', 'P001'),
	(10, '2023-02-12', 'Tidak', 'B005', 'V002', 'P002'),
	(11, '2023-02-15', 'Lengkap', 'B006', 'V001', 'P002'),
	(12, '2023-02-20', 'Lengkap', 'B006', 'V003', 'P002'),
	(13, '2023-02-25', 'Lengkap', 'B006', 'V004', 'P002'),
	(14, '2023-03-01', 'Lengkap', 'B008', 'V001', 'P001'),
	(15, '2023-03-05', 'Lengkap', 'B008', 'V002', 'P001'),
	(16, '2023-03-10', 'Tidak', 'B009', 'V001', 'P002'),
	(17, '2023-03-15', 'Lengkap', 'B010', 'V001', 'P001'),
	(18, '2023-03-18', 'Lengkap', 'B010', 'V002', 'P001'),
	(19, '2023-03-20', 'Tidak', 'B011', 'V003', 'P002'),
	(20, '2023-03-22', 'Lengkap', 'B012', 'V001', 'P001'),
	(21, '2023-03-25', 'Lengkap', 'B013', 'V004', 'P002'),
	(22, '2023-03-28', 'Lengkap', 'B014', 'V002', 'P001'),
	(23, '2023-04-01', 'Lengkap', 'B012', 'V002', 'P001'),
	(24, '2023-04-01', 'Lengkap', 'B012', 'V002', 'P001'),
	(25, '2023-04-01', 'Lengkap', 'B012', 'V002', 'P001'),
	(26, '2023-04-01', 'Lengkap', 'B012', 'V002', 'P001');

-- Dumping structure for procedure geohealthtracker_db_2510010102.sp_imunisasi_kelurahan
DELIMITER //
CREATE PROCEDURE `sp_imunisasi_kelurahan`(
	IN `p_nama_kelurahan` VARCHAR(50),
	IN `p_status` VARCHAR(10)
)
    COMMENT 'Dibuat oleh M. Rizky Rinaldy (2510010102)'
BEGIN
SELECT
b.nm_balita,
k.nm_kel,
v.nm_vaksin,
r.tanggal,
r.status
FROM riwayat_imunisasi r
JOIN balita b ON r.nik_balita = b.nik_balita
JOIN kelurahan k ON b.kd_kel = k.kd_kel
JOIN vaksin v ON r.kd_vaksin = v.kd_vaksin
WHERE k.nm_kel = p_nama_kelurahan
AND r.status = p_status;
END//
DELIMITER ;

-- Dumping structure for procedure geohealthtracker_db_2510010102.sp_total_imunisasi
DELIMITER //
CREATE PROCEDURE `sp_total_imunisasi`()
    COMMENT 'Dibuat oleh M. Rizky Rinaldy (2510010102)'
BEGIN
SELECT
COUNT(DISTINCT nik_balita) AS total_sudah_imunisasi
FROM riwayat_imunisasi;
END//
DELIMITER ;

-- Dumping structure for table geohealthtracker_db_2510010102.vaksin
CREATE TABLE IF NOT EXISTS `vaksin` (
  `kd_vaksin` char(10) NOT NULL,
  `nm_vaksin` varchar(50) DEFAULT NULL,
  `usia_min` int DEFAULT NULL,
  PRIMARY KEY (`kd_vaksin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Dibuat oleh M. Rizky Rinaldy (2510010102)';

-- Dumping data for table geohealthtracker_db_2510010102.vaksin: ~5 rows (approximately)
INSERT INTO `vaksin` (`kd_vaksin`, `nm_vaksin`, `usia_min`) VALUES
	('V001', 'BCG', 0),
	('V002', 'Polio', 2),
	('V003', 'DPT-HB-Hib 1', 2),
	('V004', 'Campak', 9),
	('V05', 'Vaksin Rinaldy-2510010102', NULL);

-- Dumping structure for view geohealthtracker_db_2510010102.v_imunisasi
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_imunisasi` (
	`nm_balita` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`nm_kel` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`nm_vaksin` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`status` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci'
) ENGINE=MyISAM;

-- Dumping structure for view geohealthtracker_db_2510010102.v_zona_merah
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_zona_merah` (
	`nm_kel` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`total` BIGINT NOT NULL,
	`imunisasi` BIGINT NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for trigger geohealthtracker_db_2510010102.trg_after_insert_imunisasi
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `trg_after_insert_imunisasi` AFTER INSERT ON `riwayat_imunisasi` FOR EACH ROW BEGIN
 INSERT INTO log_imunisasi
 (no_transaksi, aktivitas)
 VALUES
 (
 NEW.no_transaksi,
 CONCAT('Data imunisasi baru ditambahkan untuk Balita: ', NEW.nik_balita)
 );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_imunisasi`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `geohealthtracker_db_2510010102`.`v_imunisasi` AS select `b`.`nm_balita` AS `nm_balita`,`k`.`nm_kel` AS `nm_kel`,`v`.`nm_vaksin` AS `nm_vaksin`,`r`.`status` AS `status` from (((`geohealthtracker_db_2510010102`.`riwayat_imunisasi` `r` join `geohealthtracker_db_2510010102`.`balita` `b` on((`r`.`nik_balita` = `b`.`nik_balita`))) join `geohealthtracker_db_2510010102`.`kelurahan` `k` on((`b`.`kd_kel` = `k`.`kd_kel`))) join `geohealthtracker_db_2510010102`.`vaksin` `v` on((`r`.`kd_vaksin` = `v`.`kd_vaksin`)));

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_zona_merah`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `geohealthtracker_db_2510010102`.`v_zona_merah` AS select `k`.`nm_kel` AS `nm_kel`,count(`b`.`nik_balita`) AS `total`,count(`r`.`nik_balita`) AS `imunisasi` from ((`geohealthtracker_db_2510010102`.`kelurahan` `k` left join `geohealthtracker_db_2510010102`.`balita` `b` on((`k`.`kd_kel` = `b`.`kd_kel`))) left join `geohealthtracker_db_2510010102`.`riwayat_imunisasi` `r` on((`b`.`nik_balita` = `r`.`nik_balita`))) group by `k`.`nm_kel`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
