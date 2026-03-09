function firstTask(callback) {
    setTimeout(() => {
        console.log('first task complete');
        callback();
    }, 1000)
}

function secondTask(callback) {
    setTimeout(() => {
        console.log('second task complete');
        callback();
    }, 1000)
}

// dst
firstTask(() => {
    secondTask(() => {
        // dst dst
        console.log('All tasks complete')
    })
})