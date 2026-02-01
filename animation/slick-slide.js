// slick slider
$(document).ready(function () {
    $('.slider').slick({
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
  $('.vision-img-slider').slick({
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

