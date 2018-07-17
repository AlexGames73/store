jQuery.preloadImages = function()
 {
  for (let i = 0; i < arguments.length; i++)
  {
   jQuery("<img>").attr("src", arguments[ i ]);
  }
 };

let o = false;
window.onscroll = function() {
    if (pageYOffset === 0) {
        if (o === true) {
            $('.containir').animate({
                'marginTop': '+=140px'
            }, 1000);
            o = !o;
        }
    } else {
        if (o === false) {
            $('.containir').animate({
                'marginTop': '-=140px'
            });
            o = !o;
        }
    }
};

function menu_open() {
    $('.menu').animate({
        'marginLeft': '+=400px'
    }, 1000);
}

function menu_close() {
    $('.menu').animate({
        'marginLeft': '-=400px'
    }, 1000);
}
