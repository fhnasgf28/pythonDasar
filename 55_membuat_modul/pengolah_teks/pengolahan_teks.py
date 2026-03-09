def hitung_kata(teks):
    """
    Menghitung jumlah kata dalam teks

    Args:
        Jumlah kata dalam teks
    Returns:
        Jumlah kata dalam teks.
    """
    return len(teks.split())

def hitung_huruf(teks):
    """
    Menghitung jumlah huruf dalam teks

    args:
    teks:Sebuah teks

    Returns:
        jumlah huruf dalam teks
    """
    return len(teks.replace(" ", ""))

def change_teks_toUpper(teks):
    """
    Mengubah teks menjadi huruf besar

    Args:
        teks: Sebuah teks
    Returns:
        Teks dengan huruf besar
    """
    return teks.upper()

def hitung_kemunculan_kata(teks):
    """
    Menghitung kemunculan kata dalam teks

    Args:
        teks:sebuah teks
        kata: kata yang ingin dihitung kemunculannya
    Returns:
        Jumlah kemunculan kata dalam teks
    """
    return teks.count(teks)

def gabungkan_teks(teks1, teks2):
    """
    Menggabungkan 2 teks
    Args:
        teks1: Teks Pertama
        teks2: Teks Kedua
    Returns:
        Teks yang digabungkan dari teks1 dan teks2
    """
    return teks1 + teks2
