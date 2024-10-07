async function performTasks() {
    try {
        await firstTask();
        await secondTask();
        await thirdTask();
        console.log('All tasks complete');
    } catch (error) {
        console.log('Error:', error);
    }
}

performTasks()