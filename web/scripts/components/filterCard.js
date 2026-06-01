// FILENAME: filterCard.js

const { createElement } = require("react");

async function loadProjectFilterChips() {
    const res = await fetch('http://localhost:8080/projects');
    const projects = await res.json();

    const container = document.getElementById('proj-filter');
    projects.forEach(proj => {
        const chip = createElement('div');
        chip.clasList.add('filter-chip');
        chip.dataset.filter = 'proj.proj_id';
        chip.textContent    = 'proj.proj_title';
        container.appendChild(chip);
    });
}