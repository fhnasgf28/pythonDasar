function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = 'Data Fetched Promise';
            resolve(data)
        }, 1000);
    })
}

fetchData()
    .then(data => {
        console.log(data);
    })
    .catch(err => {
        console.error(err);
    })