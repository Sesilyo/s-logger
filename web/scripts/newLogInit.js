/*  FILENAME: newLogInit.js
    Initialize a new log via modal prompt
*/

import { currentLog } from "./logState.js";

export function initNewLogModal() {

    // getting HTML elements
    const newLogModal  = document.getElementById("new-log-modal");
    const newLogForm   = document.getElementById("new-log-form");
    const newLogBtn    = document.getElementById("new-log-btn");
    const cancelLogBtn = document.getElementById("cancel-log-btn");
    
    const checkBox = document.getElementById("under-project-check");
    const logName  = document.getElementById("new-log-name-text");
    
    // guard clause to prevent errors if elements are missing
    // if (!newLogModal || !newLogForm || newLogBtn || !cancelLogBtn) return;

    // new log -> open modal
    newLogBtn.addEventListener('click', () => {
        console.log("new-log-btn clicked");
        newLogModal.classList.remove('hidden');
    });
    
    newLogForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = logName.value.trim();
        if (!title) return;

        console.log("Initialized new log");

        // populate current log
        currentLog.tag_id = document.getElementById('new-log-tags').value;
        currentLog.tag_name = document.getElementById('new-log-tags').selectedOptions[0].text;
        currentLog.proj_id = null;
        currentLog.proj_title = null;

        // update console header
        document.getElementById('log-title').textContent = title;

        // un-hide typing area
        document.getElementById('type-here').classList.remove('hidden');

        // close modal & reset form
        newLogModal.classList.add('hidden');
        newLogForm.reset();
    });
    
    // cancel log -> close modal
    cancelLogBtn.addEventListener('click', () => {
        console.log("cancel-log-btn clicked");
        newLogModal.classList.add('hidden');
    });
    
    // close via clicking outside modal content
    newLogModal.addEventListener('click', (e) => {
        if (e.target === newLogModal) {
            newLogModal.classList.add('hidden');
        }
    });
}
