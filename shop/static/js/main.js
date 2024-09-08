window.addEventListener("DOMContentLoaded", event => {
sortButton1 = document.getElementById('sort-button1');
sortButton2 = document.getElementById('sort-button2');

sortButton1.onclick = SortFunction;
sortButton2.onclick = SortFunction;

function SortFunction(event) {
    sortInput = document.getElementById('sort');
    if (event.target.id == sortButton1.id)
        sortInput.value = 'price-down';
    else if (event.target.id == sortButton2.id)
        sortInput.value = 'price-up';
    console.log(sortInput.value)
}
})
