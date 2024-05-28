// menggunakan promise
function firstTask(){
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('first task complete');
            resolve();
        }, 1000)
    })
}

function secondTask(){
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('second task complete');
            resolve();
        }, 1000)
    })
}

function thirdTask(){
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('third task complete');
            resolve();
        }, 1000)
    })
}

async function performTasks() {
    try {
        await firstTask();
        await secondTask();
        await thirdTask();
        console.log('All tasks complete(Async/await)');
    } catch (error) {
        console.log('Error:', error);
    }
}

performTasks()