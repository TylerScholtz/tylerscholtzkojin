
var navbar = document.getElementById('navbar');
var hamburger = document.getElementById('hamburger');

hamburger.addEventListener('click', function() {
    navbar.style.display = navbar.style.display === 'none' ? 'flex' : 'none';
});
