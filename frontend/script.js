const ctx = document.getElementById('chart').getContext('2d');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Solar Power',
            data: []
        }]
    },
    options: {
        responsive: true,
        animation: false,
        scales: {
            x: { title: { display: true, text: 'Hour' } },
            y: { title: { display: true, text: 'Power (W)' }, beginAtZero: true }
        }
    }
});

async function updateStatus() {
    try {
        const res = await fetch("/status");
        const data = await res.json();

        document.getElementById("solar").innerText = data.solar_power;
        document.getElementById("battery").innerText = data.battery;
        document.getElementById("load").innerText = data.load;
   
        chart.data.labels.push(data.hour);
        chart.data.datasets[0].data.push(data.solar_power);

        if(chart.data.labels.length > 20){
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }

        chart.update();

    } catch (err) {
        console.error("Fetch error:", err);
    }
}

setInterval(updateStatus, 1000);
updateStatus(); 