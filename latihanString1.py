def reverse_words(string):
    """
    Membalikan urutan kata dalam sebuah string
    Args: 
        string: String yang ingin dibalikkan ututan katanya
    Returns:
        String dengan urutan kata yang terbalik
    """

    words = string.split()
    words.reverse()
    return " ".join(words)

sentence = "Hallo Dunia, bagaimana kabarmu"
reversed_string = reverse_words(sentence)
print(f"String dengan urutan kata yang terbalik: {reversed_string}")

print("=========UPPERCASE=========")

def to_upper(string, case):

    if case == "upper":
        return string.upper()
    elif case == "lower":
        return string.lower()
    else:
        raise ValueError("Nilai `case` tidak valid. Harap masukkan 'upper' atau 'lower' ")

string = "FARHAN ASSEGAF"
case = input("Masukan 'upper' atau 'lower' : ")
changed_string = to_upper(string, case)
print(f"String dengan semua huruf besar yang diubah menjadi huruf besar: {changed_string}")