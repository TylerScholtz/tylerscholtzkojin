document.addEventListener('DOMContentLoaded', function() {
    var snowContainer = document.getElementById('snow-container');

    function createSnowflake() {
        var snowflake = document.createElement('div');
        snowflake.innerHTML = '❄'; // Snowflake character
        snowflake.className = 'snowflake';
        snowflake.style.left = Math.random() * 100 + '%';
        snowflake.style.animationDuration = (Math.random() * 3 + 2) + 's'; // Random animation speed
        snowflake.style.opacity = Math.random();
        snowflake.style.fontSize = Math.random() * 20 + 10 + 'px'; // Random size

        snowContainer.appendChild(snowflake);

        setTimeout(function() {
            snowflake.remove();
        }, 5000);
    }

    setInterval(createSnowflake, 200); // Adjust for more/less frequent snowflakes
});
