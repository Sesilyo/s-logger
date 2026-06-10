// FILENAME: main.js

// imports
import { showSearchBar } from "./showSearchLogic.js";
import { displayDateTime } from "./dateTimeLogics.js";
import { initNewLogModal } from "./newLogInit.js";
import {initFilterChips, loadLogs } from "./filterLogic.js"
import './submitLog.js';

// call functions
showSearchBar();
displayDateTime();
initNewLogModal();
initFilterChips();
loadLogs();