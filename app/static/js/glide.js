// let sliders = document.querySelectorAll(".image-slider")

// for (let slider of sliders) {
//   new Glide(slider, {
//     rewind: false,
//     perView: 1,
//     focusAt: "center"
//   }).mount()

// }

let hobbySlider = document.querySelector('.hobby-slider')

new Glide(hobbySlider, {
  type: "carousel",
  rewind: false,
  perView: 1,
  focusAt: "center"
}).mount()

let visitedSlider = document.querySelector('.visited-slider')

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
}).mount()