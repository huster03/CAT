var search = document.getElementById(search);
var source = document.getElementsByClassName(table);

function display_selection()
{
    new Selection = window.getSelection();
    alert(selection);
    search.textContent = `${selection.textContent}`;
}

source.addEventListener("move", display_selection);