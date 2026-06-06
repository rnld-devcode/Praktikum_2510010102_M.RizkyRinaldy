/*
M. Rizky Rinaldy
2510010102
*/

/*Tambahan  DATA*/
INSERT INTO balita VALUES
('B010','Rahma','2022-04-12','P','Sulastri','K001'),
('B011','Yoga','2021-07-17','L','Hendra','K002'),
('B012','Alya','2022-10-05','P','Nina','K001'),
('B013','Rizki','2021-09-30','L','Hasan','K002'),
('B014','Putri','2022-01-25','P','Dewi','K001');

INSERT INTO riwayat_imunisasi
(tanggal, status, nik_balita, kd_vaksin, kd_puskesmas)
VALUES
('2023-03-15','Lengkap','B010','V001','P001'),
('2023-03-18','Lengkap','B010','V002','P001'),
('2023-03-20','Tidak','B011','V003','P002'),
('2023-03-22','Lengkap','B012','V001','P001'),
('2023-03-25','Lengkap','B013','V004','P002'),
('2023-03-28','Lengkap','B014','V002','P001');

/*Membuat Indeks*/
CREATE INDEX idx_nik_balita
ON balita(nik_balita);

CREATE INDEX idx_kd_kel
ON balita(kd_kel);

CREATE INDEX idx_tanggal_imunisasi
ON riwayat_imunisasi(tanggal);

/*Pemanfaatan Indeks*/
/*Mencari Balita Berdasarkan NIK*/
SELECT *
FROM balita
WHERE nik_balita = 'B010';
/*Pencarian Riwayat Informasi Berdasarkan Tanggal*/
SELECT *
FROM riwayat_imunisasi
WHERE tanggal BETWEEN '2023-03-01' AND '2023-03-31';

/*Menyimpan Query dalam Prosedure*/

/*Prosedure1. Menampilkan Data Imunisasi Berdasarkan Kelurahan*/
DELIMITER //
CREATE PROCEDURE sp_imunisasi_kelurahan (
IN p_nama_kelurahan VARCHAR(50))
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
WHERE k.nm_kel = p_nama_kelurahan;
END //
DELIMITER ;
/*Menampilkan Prosedure1*/
CALL sp_imunisasi_kelurahan('Kelurahan Melati');

/*Prosedure2. Menghitung Total Balita yang sudah Imunisasi*/
DELIMITER //
CREATE PROCEDURE sp_total_imunisasi ()
BEGIN
SELECT
COUNT(DISTINCT nik_balita) AS total_sudah_imunisasi
FROM riwayat_imunisasi;
END //
DELIMITER ;
/*Menampilkan Prosedure2*/
CALL sp_total_imunisasi();