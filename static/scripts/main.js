// static/scripts/script.js

document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const nav = document.getElementById('navLinks');

    if (hamburger && nav) {
        hamburger.addEventListener('click', function () {
            nav.classList.toggle('show');
        });
    }
});