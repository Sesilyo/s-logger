const searchItem = document.getElementById("search-logs");
const searchInput = document.getElementById("search-input");

searchItem.addEventListener('click', (e) => {
    // prevents bar closing if clicked
    if (e.target === searchInput) return;

    searchItem.classList.toggle('active');

    if (searchItem.classList.contains('active')) {
        searchInput.focus();
    }
});