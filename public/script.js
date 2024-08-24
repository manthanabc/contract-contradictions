
document.getElementById('diffButton').addEventListener('click', async () => {
    const text1 = document.getElementById('text1').value;
    const text2 = document.getElementById('text2').value;

    const diffOutput = document.getElementById('diffOutput');
    diffOutput.innerHTML = '';

    const diffs = await getDiffs(text1, text2);
    diffs.forEach(diff => {
        const diffContainer = document.createElement('div');
        diffContainer.classList.add('diff-container');

        const originalElement = document.createElement('div');
        originalElement.classList.add('diff-original');
        originalElement.textContent = diff.original;

        const laterElement = document.createElement('div');
        laterElement.classList.add('diff-later');
        laterElement.textContent = diff.later;

        diffContainer.appendChild(originalElement);
        diffContainer.appendChild(laterElement);
        diffOutput.appendChild(diffContainer);
    });
    
});

async function getDiffs(text1, text2) {
    const lines1 = text1.split('\n');
    const lines2 = text2.split('\n');

    let diffs = await func(text1, text2);
    console.log(diffs)
    return diffs;
}

let func = async (a, b) => {
            const response = await fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ contract1:a, contract2:b})
            });
            let data = await response.json()
            console.log(data)
            let h = await JSON.parse(data)
            return h;
}
