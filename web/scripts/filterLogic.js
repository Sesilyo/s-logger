// FILENAME: filterLogic.js

let allLogs = [];
const activeChips = new Set();
const chips = document.querySelectorAll('.filter-chip');

async function loadLogs() {
    const res = await fetch('http://localhost:8080/logs');
    allLogs = await res.json();
    renderLogs(allLogs);
}

function renderLogs(logs) {
    const container = document.getElementById('logs-container');
    container.innerHTML = '';

    logs.forEach( log => {
        const div = document.createElement('div');
        div.innerHTML = `
            <div class="log">
                <p class="log-id">${log.log_id}</p>
                <p class="log-datetime">${log.date_created} ${log.time_created}</p>
                <p class="log-content">${log.log_content}</p>
            </div>
        `;
        container.appendChild(div);
    });
}

function applyFilters() {
    if ( activeChips.size == 0 ) {
        renderLogs(allLogs);
    }

    else {
        const filtered = allLogs.filter( log => 
            activeChips.has(log.tag_id) || activeChips.has(log.proj_id)
        );
        renderLogs(filtered);
    }
}


chips.forEach( chip => {
    chip.addEventListener('click', () => {
        const filter = chip.dataset.filter;

        if ( activeChips.has(filter) ) {
            activeChips.delete(filter);
            chip.classList.remove('active');
        }

        else {
            activeChips.add(filter);
            chip.classList.add('active');
        }

        applyFilters();
    });

});

