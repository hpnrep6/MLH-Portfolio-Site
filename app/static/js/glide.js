document.addEventListener('DOMContentLoaded', function() {
  let hobbySlider = document.querySelector('.hobby-slider');

  if (hobbySlider) {
    new Glide(hobbySlider, {
      type: "carousel",
      rewind: false,
      perView: 1,
      focusAt: "center"
    }).mount();
  }

  let visitedSlider = document.querySelector('.visited-slider');

  if (visitedSlider) {
    new Glide(visitedSlider, {
      type: "carousel",
      rewind: false,
      perView: 2,
      breakpoints: {
        1800: {
          perView: 1,
          focusAt: "center"
        }
      }
    }).mount();
  }
});