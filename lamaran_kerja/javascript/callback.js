function fetchData(callback) {
    setTimeout(() => {
      const data = 'data fetched';
      callback(null, data);
    }, 1000);
  }
  
  fetchData((error, data) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(data); // Output: data fetched
    }
  });
  