let search_input = document.getElementById("search_input");
let search_form = document.getElementById("search_form");

// Click butt on enter key press
search_input.onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        search_form.submit();
    }
};