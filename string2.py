def count_string(string):
    """
    Menghitung jumlah huruf vokal dalam sebuah string.

    args:
        string: String yang ingin di hitung jumlah huruf vokalnya
    Returns:
        jumlah huruf vokal dalam string
    """

    vowels = "jumlah huruf vokal dalam string"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = "Halo Dunia apa kabar kamu"
jumlah_vokal = count_string(string)
print(f"jumlah huruf vokal dalam string '{string}' adalah {jumlah_vokal}")