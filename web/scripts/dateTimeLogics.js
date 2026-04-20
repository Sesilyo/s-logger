/* DISPLAY MAIN TIME BLOCK */
const dateDisplayer = document.getElementById("date-displayer");
const timeDisplayer = document.getElementById("time-displayer");

setInterval(() => {
    const now = new Date();

    // customized format for day & day
    const dateFormat = {
        weekday: 'long',
        month: '2-digit',
        day: '2-digit',
        year: 'numeric'
    };

    const formattedDate = now.toLocaleDateString('en-US', dateFormat)
        .replace(',', '-')
        .replaceAll('/', '-');

    // getting time
    const hh = String(now.getHours()).padStart(2,   '0');
    const mm = String(now.getMinutes()).padStart(2, '0');
    const ss = String(now.getSeconds()).padStart(2, '0');

    const formattedTime = `${hh}:${mm}:${ss}`;

    timeDisplayer.textContent = formattedTime;
    dateDisplayer.textContent = formattedDate;
}, 1000);