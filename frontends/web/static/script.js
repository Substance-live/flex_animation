document.addEventListener("DOMContentLoaded", function() {
    const startButton = document.getElementById("startAnimation");
    const canvas = document.getElementById("animationCanvas");
    const ctx = canvas.getContext("2d");

    let animationRunning = false;
    let animationInterval;
    let color = [255, 255, 255];

    const FPS = 60;


    fetch("/get_initial_data")
        .then(response => response.json())
        .then(data => {
            color = data.color;
        });



    startButton.addEventListener("click", function() {
        if (!animationRunning) {
            animationRunning = true;
            startButton.textContent = "Stop Animation";
            startAnimation();
        } else {
            animationRunning = false;
            startButton.textContent = "Start Animation";
            clearInterval(animationInterval);
        }
    });

    function startAnimation() {
        animationInterval = setInterval(() => {
            updateAnimation();
        }, 1000 / FPS);
    }

    function drawCircles(circles) {
        circles.forEach(circle => {
            ctx.beginPath();
            ctx.arc(circle.pos[0], circle.pos[1], circle.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
            ctx.fill();
            ctx.closePath();
        });
    }

    function drawLines(lines) {
        lines.forEach(line => {
            const brightness = line.brightness;

            if (brightness == null) {
                return;}

            const scaledColor = color.map(channel => Math.round(channel * brightness));

            ctx.beginPath();
            ctx.moveTo(line.start_pos[0], line.start_pos[1]);
            ctx.lineTo(line.end_pos[0], line.end_pos[1]);
            ctx.lineWidth = line.width;
            ctx.strokeStyle = `rgb(${scaledColor[0]}, ${scaledColor[1]}, ${scaledColor[2]})`;;
            ctx.stroke();
            ctx.closePath();
        });
    }

    function updateAnimation() {
        fetch("/state")
            .then(response => response.json())
            .then(data => {
                ctx.fillStyle = "black";
//                ctx.clearRect(0, 0, canvas.width, canvas.height)
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                drawLines(data.lines);
                drawCircles(data.circles);
            });
    }

    updateAnimation();
});
