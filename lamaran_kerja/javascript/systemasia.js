// contoh penggunaan sebuah array dengan const 

// mendeklarasikan sebuah aray dengan const
const numbers = [3,4,5,62,5,2];

// membuat variabel

let total = 0;

// melakukan perulangan untuk menghitung jumlah total

for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];
}

console.log(`jumlah total: ${total}`); // tidak error

// kita coba inisialisasikan ulang array number
numbers = [10, 20, 40];
console.log(numbers); // akan error 



// contoh let
// deklarasi variabel dengan let di dalam blok kode 

for (let i = 0; i < 5; i++) {
    console.log(i);
}