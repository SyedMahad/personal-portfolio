// Ensure the script runs only after the page is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    
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
    };

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

    function openModal(id) {
        document.getElementById(id).style.display = 'block';
    }

    function closeModal(id) {
        document.getElementById(id).style.display = 'none';
    }

    document.querySelectorAll('.close').forEach(closeButton => {
        closeButton.addEventListener('click', function () {
            const modal = this.parentElement.parentElement;
            modal.style.display = 'none';
        });
    });

});

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
    navLinks.classList.toggle('active');
}