function concatenate_strings(str1, str2) {
    // validasi input
    if (typeof str1 !== 'string' || typeof str2 !== 'string') {
        throw new Error('Tipe data input harus string');
    }

    //menggabngkan 2 string
    const concatenatedString = str1 + str2

    return concatenatedString;
}

try {
    const string1 = 'Hello';
    const string2 = ' World';
    const result = concatenate_strings(string1, string2);
    console.log(result);
} catch (error) {
    console.error(error.message);
}