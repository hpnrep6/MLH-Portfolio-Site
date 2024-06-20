
// makes the navbar contract when the user scrolls down
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.nav-bar'); // replace '.nav-bar' with the selector for your navbar
    if (window.pageYOffset > 0) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});

//hambuerger menu toggle function
document.addEventListener("DOMContentLoaded", function() {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const navLinks = document.querySelector(".nav-links");

    hamburgerMenu.addEventListener("click", function() {
        navLinks.classList.toggle("active");
    });
});

// smooth scroll to sections
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(function(link) {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const target = e.target.getAttribute("href");
            document.querySelector(target).scrollIntoView({
                behavior: "smooth"
            });
        });
    });
});
