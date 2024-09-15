// Ensure the script runs only after the page is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll("nav ul li a");

    // Smooth scroll with null check
    document.querySelectorAll('nav ul li a:not(.resume-btn)').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            } else {
                console.warn("Target not found for", this.getAttribute('href'));
            }
        });
    });

    // Sticky Navbar
    window.onscroll = function () {
        const navbar = document.getElementById('navbar');
        if (window.pageYOffset > 50) {
            navbar.classList.add('sticky');
        } else {
            navbar.classList.remove('sticky');
        }

        // Call function to activate nav link based on scroll position
        updateActiveNavLink();
    };

    // Function to add 'active' class to the current nav link
    function updateActiveNavLink() {
        let currentSection = "";

        // Get the current section in view
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
                currentSection = section.getAttribute("id");
            }
        });

        // Add 'active' class to the current link and remove it from others
        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(currentSection)) {
                link.classList.add("active");
            }
        });
    }

    // Light/Dark Mode Toggle
    document.getElementById('modeToggle').addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
    });

    // Modals for Projects
    document.querySelectorAll('.project-item').forEach(item => {
        item.addEventListener('click', function () {
            const modalId = this.getAttribute('onclick').replace('openModal(', '').replace(')', '').replace(/['"]/g, '');
            openModal(modalId);
        });
    });

    document.querySelectorAll('.close').forEach(closeButton => {
        closeButton.addEventListener('click', function () {
            const modal = this.parentElement.parentElement;
            modal.style.display = 'none';
        });
    });

    // Close modal when clicking outside of the modal content
    window.addEventListener('click', function (event) {
        document.querySelectorAll('.modal').forEach(modal => {
            const modalContent = modal.querySelector('.modal-content');
            if (event.target == modal) {  // If the target of the click is the modal (not the content)
                modal.style.display = 'none';
            }
        });
    });

});

function openModal(id) {
    document.getElementById(id).style.display = 'block';
}

function closeModal(id) {
    document.getElementById(id).style.display = 'none';
}


function toggleMode() {
    // Toggle the icon based on the current mode
    const icon = document.getElementById('toggleIcon');
    if (document.body.classList.contains('light-mode')) {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun'); // Change to sun icon for dark mode
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon'); // Change to moon icon for light mode
    }
}

function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('#hamburger');
    navLinks.classList.toggle('active');

    if (navLinks.classList.contains('active')) {
        hamburger.classList.remove('fa-bars');
        hamburger.classList.add('fa-times'); // Change to close icon when menu is open
    } else {
        hamburger.classList.remove('fa-times');
        hamburger.classList.add('fa-bars'); // Change to hamburger icon when menu is closed
    }
}
