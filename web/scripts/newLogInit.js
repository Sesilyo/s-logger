/*  FILENAME: newLogInit.js
    Initialize a new log via modal prompt
*/


// getting HTML elements
const newLogModal  = document.getElementById("new-log-modal");
const newLogForm   = document.getElementById("new-log-form");
const newLogBtn    = document.getElementById("new-log-btn");
const cancelLogBtn = document.getElementById("cancel-log-btn");

const checkBox = document.getElementById("");
const logName  = document.getElementById("new-log-name-text");

// new log -> open modal
newLogBtn.addEventListener('click', () => {
    console.log("new-log-btn clicked");
    newLogModal.classList.remove('hidden');
});

newLogForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("Initialized new log");

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