document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const sugu = document.getElementById('sugu').value;
    const userInput = document.getElementById('userInput').value;

    fetch('/generate_report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sugu: sugu, userInput: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('report').innerText = data.report;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
