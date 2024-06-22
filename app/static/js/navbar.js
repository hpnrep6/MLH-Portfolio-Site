function initialiseNavbar() {
  // contract navbar on scroll
  window.addEventListener('scroll', function() {
      const navbar = document.querySelector('.nav-bar');
      if (window.pageYOffset > 0) {
          navbar.classList.add('navbar-scrolled');
      } else {
          navbar.classList.remove('navbar-scrolled');
      }
  });

  //hamburger menu toggle function
  document.addEventListener("DOMContentLoaded", function() {
      const hamburgerMenu = document.querySelector(".hamburger-menu");
      const closeButton = document.querySelector(".close-button");
      const navLinks = document.querySelector(".nav-links");

      hamburgerMenu.addEventListener("click", function() {
          navLinks.classList.toggle("drawer-active");
      });

      closeButton.addEventListener("click", function() {
          navLinks.classList.remove("drawer-active");
      });
  });
  // smooth scroll to sections
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(function(link) {
        link.addEventListener("click", function(e) {
            const target = e.target.getAttribute("href");
            // Check if the target is an anchor link on the same page
            if (target.startsWith("#")) {
                e.preventDefault(); // Prevent default only for anchor links
                document.querySelector(target).scrollIntoView({
                    behavior: "smooth"
                });
            }

            // Close the drawer menu after clicking a link (for mobile view)
            if (window.innerWidth <= 768) {
                document.querySelector(".nav-links").classList.remove("drawer-active");
            }
        });
    });
});
}

initialiseNavbar();

// highlight active section in navbar when user watches it
/*
document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-links a');

    let currentActive = null;

    function highlightSection() {
        let smallestDistance = Infinity;
        let closestSection = null;

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            const distance = Math.abs(rect.top - window.innerHeight / 2);

            if (distance < smallestDistance) {
                smallestDistance = distance;
                closestSection = section;
            }
        });

        if (currentActive) {
            currentActive.classList.remove('active');
        }

        if (closestSection) {
            const id = closestSection.getAttribute('id');
            currentActive = document.querySelector(`.nav-links a[href="#${id}"]`);
            currentActive.classList.add('active');
        }
    }

    window.addEventListener('scroll', highlightSection);
    highlightSection();
});
*/