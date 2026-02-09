window.addEventListener("scroll", function () {
    const navbar = document.getElementById("mainNavbar");
    if (!navbar) {
        return;
    }
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});


// slick slider
if (window.jQuery && $.fn && typeof $.fn.slick === "function") {
    const $slider = $(".slider");
    if ($slider.length) {
        $slider.slick({
            dots: true,
            infinite: true,
            speed: 800,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 1000,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });
    }
}

