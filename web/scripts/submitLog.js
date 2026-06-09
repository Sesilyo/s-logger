// FILENAME: submitLog.js

const submitLogBtn = document.getElementById('submit-log');

submitLogBtn.addEventListener('click', () => {
    const content = document.getElementById('type-log-here');


    fetch('http://localhost:8080/logs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            
        })
    });
});