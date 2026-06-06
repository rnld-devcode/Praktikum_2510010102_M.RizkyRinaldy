/*
M. Rizky Rinaldy
2510010102
*/

/*Membuat DATABASE*/
CREATE DATABASE GeoHealthTracker_db;

/*Membuat Tabel dan Atribut*/
CREATE TABLE puskesmas (
 kd_puskesmas CHAR(5) PRIMARY KEY,
 nm_puskesmas VARCHAR(25),
 alamat VARCHAR(50),
 lat DECIMAL(10,6),
 `long` DECIMAL(10,6)
);
CREATE TABLE kelurahan (
 kd_kel CHAR(5) PRIMARY KEY,
 nm_kel VARCHAR(50),
 poly_wil TEXT,
 kd_puskesmas CHAR(5),
 FOREIGN KEY (kd_puskesmas) REFERENCES puskesmas(kd_puskesmas)
);
CREATE TABLE balita (
 nik_balita CHAR(10) PRIMARY KEY,
 nm_balita VARCHAR(50),
 tgl_lahir DATE,
 jk CHAR(1),
 nm_ortu VARCHAR(50),
 kd_kel CHAR(5),
 FOREIGN KEY (kd_kel) REFERENCES kelurahan(kd_kel)
);
CREATE TABLE vaksin (
 kd_vaksin CHAR(10) PRIMARY KEY,
 nm_vaksin VARCHAR(50),
 usia_min INT
);
CREATE TABLE riwayat_imunisasi (
 no_transaksi INT AUTO_INCREMENT PRIMARY KEY,
 tanggal DATE,
 status VARCHAR(10),
 nik_balita CHAR(10),
 kd_vaksin CHAR(10),
 kd_puskesmas CHAR(5),
 FOREIGN KEY (nik_balita) REFERENCES balita(nik_balita),
 FOREIGN KEY (kd_vaksin) REFERENCES vaksin(kd_vaksin),
 FOREIGN KEY (kd_puskesmas) REFERENCES puskesmas(kd_puskesmas)
);

/*Mengsisi Data Record*/
INSERT INTO puskesmas VALUES
('P001','Puskesmas A','Jl. Sehat 1',-6.200000,106.800000),
('P002','Puskesmas B','Jl. Sehat 2',-6.210000,106.810000);
INSERT INTO kelurahan VALUES
('K001','Kelurahan Melati','POLYGON(...)','P001'),
('K002','Kelurahan Mawar','POLYGON(...)','P002');
INSERT INTO balita VALUES
('B001','Andi','2022-01-01','L','Budi','K001'),
('B002','Siti','2021-05-10','P','Ani','K002'),
('B003','Rina','2022-03-15','P','Dedi','K001');
INSERT INTO vaksin VALUES
('V001','BCG',0),
('V002','Polio',2);

INSERT INTO riwayat_imunisasi (tanggal, status, nik_balita, kd_vaksin, kd_puskesmas)
VALUES
('2023-01-01','Lengkap','B001','V001','P001'),
('2023-01-10','Lengkap','B002','V002','P002'),
('2023-01-15','Tidak','B003','V001','P001');


/*Menggabungkan data 2 tabel*/
SELECT b.nm_balita, k.nm_kel
FROM balita b
INNER JOIN kelurahan k 
ON b.kd_kel = k.kd_kel;

/*Menampilkan dari 3 atau lebih tabel induk*/
SELECT b.nm_balita, v.nm_vaksin, p.nm_puskesmas, r.`status`
FROM riwayat_imunisasi r
JOIN balita b ON r.nik_balita = b.nik_balita
JOIN vaksin v ON r.kd_vaksin = v.kd_vaksin
JOIN puskesmas p ON r.kd_puskesmas = p.kd_puskesmas;

/*Menampilkan yang Null*/
SELECT b.nm_balita
FROM balita b
LEFT JOIN riwayat_imunisasi r ON b.nik_balita = r.nik_balita
WHERE r.nik_balita IS NULL;