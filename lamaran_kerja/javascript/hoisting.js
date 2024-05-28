// contoh : Hoisting Deklarasi Variabel
console.log(x); 
var x = 10;

// Contoh 2: Hoisting Deklarasi Fungsi
sayHello(); // Output: Hello!
function sayHello() {
  console.log("Hello!");
}