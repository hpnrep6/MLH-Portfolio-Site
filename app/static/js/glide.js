// let sliders = document.querySelectorAll(".image-slider")

// for (let slider of sliders) {
//   new Glide(slider, {
//     rewind: false,
//     perView: 1,
//     focusAt: "center"
//   }).mount()

// }

let hobbySlider = document.querySelector('.hobby-slider')
console.log(hobbySlider)
new Glide(hobbySlider, {
  type: "carousel",
  rewind: false,
  perView: 1,
  focusAt: "center"
}).mount()