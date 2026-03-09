function init() {
    const name = 'Farhan Assegaf';
  
    function greet() {
      console.log(`Halo, ${name}`);
    }
  
    return greet;
  }
  
  const myFunction = init();
  myFunction();