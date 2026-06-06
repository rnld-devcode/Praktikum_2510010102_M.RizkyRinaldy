/*
M. Rizky Rinaldy
2510010102
*/

/*Studi Kasus Trigger*/
CREATE TABLE log_imunisasi (
 id_log INT AUTO_INCREMENT PRIMARY KEY,
 no_transaksi INT,
 aktivitas VARCHAR(100),
 waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/*AFTER INSERT*/
DELIMITER //
CREATE TRIGGER trg_after_insert_imunisasi
AFTER INSERT ON riwayat_imunisasi
FOR EACH ROW
BEGIN
 INSERT INTO log_imunisasi
 (no_transaksi, aktivitas)
 VALUES
 (
 NEW.no_transaksi,
 CONCAT('Data imunisasi baru ditambahkan untuk Balita: ', NEW.nik_balita)
 );
END //
DELIMITER ;

/*Uji Coba Trigger*/
INSERT INTO riwayat_imunisasi
(tanggal, status, nik_balita, kd_vaksin, kd_puskesmas)
VALUES
('2023-04-01','Lengkap','B012','V002','P001');

/*Hasil Trigger*/
SELECT * FROM log_imunisasi;

/*Pakai Command Line*/
/*Backup Database My*/
mysqldump -u root -p geohealth_tracker > geohealth_backup.sql

/*Restore Database*/
mysql -u root -p geohealth_tracker < geohealth_backup.sql

/*Back up Tabel Tertentu*/
mysqldump -u root -p geohealth_tracker balita > backup_balita.sql

/*Praktik Validasi BackUp*/
SELECT COUNT(*) FROM balita;
SELECT COUNT(*) FROM riwayat_imunisasi;