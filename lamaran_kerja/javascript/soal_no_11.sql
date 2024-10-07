CREATE TABLE Transaksi (
    TransaksiID INT PRIMARY KEY,
    PesananID INT,
    Jumlah DECIMAL(10, 2)
);

-- Menambahkan Data ke Tabel Transaksi
INSERT INTO Transaksi (TransaksiID, PesananID, Jumlah)
VALUES
(1, 1, 50.00),
(2, 1, 75.00),
(3, 2, 100.00),
(4, 2, 125.00);

CREATE TABLE Pesanan (
    PesananID INT PRIMARY KEY,
    NamaPelanggan VARCHAR(50),
    TotalHarga DECIMAL(10, 2)
);

-- Menambahkan Data ke Tabel Pesanan
INSERT INTO Pesanan (PesananID, NamaPelanggan, TotalHarga)
VALUES
(1, 'Pelanggan A', 0.00),
(2, 'Pelanggan B', 0.00);

CREATE PROCEDURE UpdateTotalHargaPesanan
    @PesananID INT
AS
BEGIN
    -- Deklarasi variabel untuk total harga
    DECLARE @Total DECIMAL(10, 2);

    -- Menghitung total harga berdasarkan PesananID
    SELECT @Total = SUM(Jumlah)
    FROM Transaksi
    WHERE PesananID = @PesananID;

    -- Update total harga dalam tabel Pesanan
    UPDATE Pesanan
    SET TotalHarga = @Total
    WHERE PesananID = @PesananID;
END;
