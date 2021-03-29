$(function () {
    $(window).scroll(function() {
        if ($(this).scrollTop() - 500 > 0) {
            $('.scroll-to-top').stop().slideDown('fast'); // show the button
        } else {
            $('.scroll-to-top').stop().slideUp('fast'); // hide the button
        }
    });
});



$(function () {
    // previous detection logic

    $(".scroll-to-top").on("click", function () {
        $("html, body").animate({
            scrollTop: 0
        }, 1000);
    });
});