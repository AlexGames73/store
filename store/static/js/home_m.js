function menu_open() {
    $('.menu').animate({
        'marginLeft': '+=100%'
    }, 1000);
}

function menu_close() {
    $('.menu').animate({
        'marginLeft': '-=100%'
    }, 1000);
}