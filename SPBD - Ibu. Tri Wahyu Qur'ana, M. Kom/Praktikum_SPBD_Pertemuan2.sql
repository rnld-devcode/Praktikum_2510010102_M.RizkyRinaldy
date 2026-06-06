/*
M. Rizky Rinaldy
2510010102
*/

/*Tambahan Data*/
INSERT INTO balita VALUES
('B004','Dina','2021-08-20','P','Sari','K001'),
('B005','Rudi','2022-06-11','L','Agus','K002'),
('B006','Lina','2021-12-01','P','Wati','K002'),
('B007','Bayu','2022-09-09','L','Joko','K001'),
('B008','Nina','2022-02-02','P','Rudi','K001'),
('B009','Fajar','2021-11-11','L','Siti','K002');

INSERT INTO vaksin VALUES
('V003','DPT-HB-Hib 1',2),
('V004','Campak',9);

INSERT INTO riwayat_imunisasi (tanggal, status, nik_balita, kd_vaksin, kd_puskesmas)
VALUES
('2023-02-01','Lengkap','B001','V002','P001'),
('2023-02-05','Lengkap','B001','V003','P001'),
('2023-02-10','Lengkap','B004','V001','P001'),
('2023-02-12','Tidak','B005','V002','P002'),
('2023-02-15','Lengkap','B006','V001','P002'),
('2023-02-20','Lengkap','B006','V003','P002'),
('2023-02-25','Lengkap','B006','V004','P002'),
('2023-03-01','Lengkap','B008','V001','P001'),
('2023-03-05','Lengkap','B008','V002','P001'),
('2023-03-10','Tidak','B009','V001','P002');

/*Analisis Cakupan Per Wilayah*/
SELECT k.nm_kel,
COUNT(DISTINCT b.nik_balita) AS total_balita,
COUNT(DISTINCT r.nik_balita) AS sudah_imunisasi
FROM kelurahan k
LEFT JOIN balita b ON k.kd_kel = b.kd_kel
LEFT JOIN riwayat_imunisasi r ON b.nik_balita = r.nik_balita
GROUP BY k.nm_kel;

/*Perhitungan Umur Dinamis*/
SELECT nm_balita,
TIMESTAMPDIFF(YEAR, tgl_lahir, CURDATE()) AS umur
FROM balita;

/*Kita menggunakan HAVING untuk menyaring wilayah yang cakupan imunisasinya
belum mencapai 100%.
*/
SELECT k.nm_kel
FROM kelurahan k
LEFT JOIN balita b ON k.kd_kel = b.kd_kel
LEFT JOIN riwayat_imunisasi r ON b.nik_balita = r.nik_balita
GROUP BY k.nm_kel
HAVING COUNT(r.nik_balita) < COUNT(b.nik_balita);

/*SubQuery*/
SELECT nm_balita
FROM balita
WHERE nik_balita NOT IN 
(
SELECT nik_balita FROM riwayat_imunisasi
);

/*correlated subquery*/
SELECT b.nm_balita
FROM balita b
WHERE (
 SELECT COUNT(*)
 FROM riwayat_imunisasi r
 WHERE r.nik_balita = b.nik_balita
) >= 2;

/*Kelurahan dengan  Imunisasi di Bawah Rata-rata. */
SELECT nm_kel
FROM kelurahan
WHERE kd_kel IN (
 	SELECT k.kd_kel
 	FROM kelurahan k
 	LEFT JOIN balita b ON k.kd_kel = b.kd_kel
 	LEFT JOIN riwayat_imunisasi r ON b.nik_balita = r.nik_balita
 	GROUP BY k.kd_kel
 	HAVING COUNT(r.nik_balita) < (
 		SELECT AVG(jumlah)
 		FROM (
 			SELECT COUNT(r2.nik_balita) AS jumlah
 			FROM kelurahan k2
 			LEFT JOIN balita b2 ON k2.kd_kel = b2.kd_kel
 			LEFT JOIN riwayat_imunisasi r2 ON b2.nik_balita = r2.nik_balita
 			GROUP BY k2.kd_kel
 		) AS sub
 )
);

/*VIEW: Detail Laporan Imunisasi*/
CREATE VIEW v_imunisasi AS
SELECT b.nm_balita, k.nm_kel, v.nm_vaksin, r.status
FROM riwayat_imunisasi r
JOIN balita b ON r.nik_balita = b.nik_balita
JOIN kelurahan k ON b.kd_kel = k.kd_kel
JOIN vaksin v ON r.kd_vaksin = v.kd_vaksin;

/* VIEW: Analitik Zona Merah*/
CREATE VIEW v_zona_merah AS
SELECT k.nm_kel,
COUNT(b.nik_balita) AS total,
COUNT(r.nik_balita) AS imunisasi
FROM kelurahan k
LEFT JOIN balita b ON k.kd_kel = b.kd_kel
LEFT JOIN riwayat_imunisasi r ON b.nik_balita = r.nik_balita
GROUP BY k.nm_kel;