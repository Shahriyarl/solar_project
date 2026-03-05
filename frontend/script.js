const ctx = document.getElementById('chart');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Solar Power',
            data: [],
            borderWidth: 2
        }]
    }
});

async function updateStatus() {

    const res = await fetch("/status");
    const data = await res.json();

    document.getElementById("solar").innerText = data.solar_power;
    document.getElementById("battery").innerText = data.battery_percent;
    document.getElementById("load").innerText = data.load;

}

async function loadHistory(){

    const res = await fetch("/history");
    const data = await res.json();

    chart.data.labels = data.map(d => d.hour);
    chart.data.datasets[0].data = data.map(d => d.solar);

    chart.update();
}

setInterval(updateStatus,1000)

loadHistory()