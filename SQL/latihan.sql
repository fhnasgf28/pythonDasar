CREATE TABLE produk (
    id INT PRIMARY KEY,
    nama_produk VARCHAR(50),
    kategori VARCHAR(50),
    harga INT,
    stok INT
);

INSERT INTO produk(id, nama_produk, kategori, harga, stok) VALUES
(1, 'Buku Tulis', 'Alat Tulis', 5000, 100),
(2, 'Pulpen', 'Alat Tulis', 2000, 150),
(3, 'Pensil', 'Alat Tulis', 1000, 200),
(4, 'Penghapus', 'Alat Tulis', 500, 300),
(5, 'Spidol', 'Alat Tulis', 3000, 120),
(6, 'Rautan', 'Alat Tulis', 1500, 100),
(7, 'Buku Gambar', 'Alat Tulis', 8000, 80),
(8, 'Penggaris', 'Alat Tulis', 2500, 200),
(9, 'Map Plastik', 'Alat Tulis', 1000, 300),
(10, 'Gunting', 'Alat Tulis', 5000, 50),
(11, 'Lem Kertas', 'Alat Tulis', 2000, 180),
(12, 'Kalkulator', 'Elektronik', 25000, 30),
(13, 'Flashdisk 16GB', 'Elektronik', 60000, 25),
(14, 'Mouse', 'Elektronik', 45000, 40),
(15, 'Keyboard', 'Elektronik', 75000, 35),
(16, 'Charger HP', 'Elektronik', 30000, 50),
(17, 'Kabel USB', 'Elektronik', 10000, 100),
(18, 'Headset', 'Elektronik', 50000, 45),
(19, 'Speaker Bluetooth', 'Elektronik', 150000, 20),
(20, 'Power Bank', 'Elektronik', 200000, 15);

SELECT * FROM produk

--where
SELECT * FROM produk WHERE harga > 10000;

SELECT * FROM produk WHERE kategori = 'Alat Tulis';

SELECT * FROM produk WHERE harga = '10000' AND stok > 50;

SELECT * FROM produk WHERE harga < 10000 OR stok > 100;

SELECT * FROM produk WHERE nama_produk LIKE O'%buku%';
SELECT * FROM produk WHERE harga BETWEEN 5000 AND 50000;

SELECT * FROM produk WHERE NOT harga = 60000 AND NOT kategori = 'Elektronik';

--ORDER BY

SELECT * FROM produk ORDER BY nama_produk desc;
SELECT * FROM produk ORDER BY nama_produk, kategori desc;
SELECT * FROM produk ORDER BY nama_produk ASC, kategori DESC;

--Insert
--Insert Data Only in Specified Columns
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');

--UPDATE QUERY
UPDATE produk SET harga = 65500 WHERE id = 11;
SELECT * FROM produk WHERE id = 11;

UPDATE produk SET stok = stok + 10 WHERE kategori = 'Elektronik';
SELECT * FROM produk WHERE stok;

UPDATE produk
SET harga = 1200, stok = 210
WHERE id = 3;

UPDATE produk SET kategori = 'premium' WHERE harga > 100000;
SELECT * FROM produk WHERE stok;

