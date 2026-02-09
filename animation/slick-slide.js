// slick slider
$(document).ready(function () {
    if (!($.fn && typeof $.fn.slick === "function")) {
        return;
    }
    const $slider = $(".slider");
    if (!$slider.length) {
        return;
    }
    $slider.slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: false,
        autoplaySpeed: 6000,
        arrows: true,
        dots: false,
        pauseOnHover: false,
        adaptiveHeight: true
    });
});


// vision image slider
$(document).ready(function () {
    if (!($.fn && typeof $.fn.slick === "function")) {
        return;
    }
    const $visionSlider = $(".vision-img-slider");
    if (!$visionSlider.length) {
        return;
    }
    $visionSlider.slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3500,
        infinite: true,
        arrows: true,
        dots: false,
        pauseOnHover: false,
        responsive: [
            {
                breakpoint: 992,
                settings: { slidesToShow: 3 }
            },
            {
                breakpoint: 768,
                settings: { slidesToShow: 2 }
            },
            {
                breakpoint: 576,
                settings: { slidesToShow: 1 }
            }
        ]
    });
});


