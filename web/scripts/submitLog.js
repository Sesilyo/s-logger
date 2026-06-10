// FILENAME: submitLog.js

// imports
import { currentLog } from "./logState.js";
import { loadLogs } from "./filterLogic.js";

const submitLogBtn = document.getElementById('submit-log');

submitLogBtn.addEventListener('click', async () => {
    const content = document.getElementById('type-log-here').value.trim();
    if (!content) return;

    const now = new Date();
    const date = now.toISOString().split('T')[0];
    const time = now.toTimeString().split(' ')[0];

    await fetch('http://localhost:8080/logs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            content,
            tag_id: currentLog.tag_id,
            tag_name: currentLog.tag_name,
            proj_id: currentLog.proj_id,
            proj_title: currentLog.proj_title,
            date,
            time
        })
    });

    // clear textarea & reload logs
    document.getElementById('type-log-here').value = '';
    loadLogs();
});