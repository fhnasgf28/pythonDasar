--SELECT *
--FROM table1
--INNER JOIN table2
--ON table1.field = table2.field;

SELECT *
FROM mahasiswa
RIGHT JOIN transaksi
ON mahasiswa.nim = transaksi.nim;