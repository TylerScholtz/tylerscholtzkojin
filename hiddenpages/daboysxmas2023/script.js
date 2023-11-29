document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector('.container');
    container.style.opacity = 0;
    setTimeout(() => {
        container.style.opacity = 1;
        container.style.transition = 'opacity 2s';
    }, 100);
});
