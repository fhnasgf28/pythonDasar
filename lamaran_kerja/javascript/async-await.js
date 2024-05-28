function fetchData(){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            const data = 'data fetched(Async/await)';
            resolve(data);
        }, 1000);
    });
}

async function getData() {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

getData();