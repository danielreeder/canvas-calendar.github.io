

// fs.readFile('assignments.txt', 'ascii', (err, data) => {
//     if (err){
//         console.error(err);
//         return;
//     }
//     console.log(data)
// })
document.querySelector("#button").addEventListener("click", () => {
    fetch('/user').then(res => res.json()).then(data => {
        console.log(data)
    })
})