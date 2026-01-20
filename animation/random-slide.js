const images = [
  "images/activities/1.jpeg",
  "images/activities/2.jpeg",
  "images/activities/4.jpeg",
  "images/activities/5.jpeg",
  "images/activities/6.jpeg",
  "images/activities/7.jpeg"
];

const directions = [
  { x: "-100%", y: "0" },   // left
  { x: "100%", y: "0" },    // right
  { x: "0", y: "-100%" },   // top
  { x: "0", y: "100%" }     // bottom
];

const img = document.getElementById("randomSliderImg");
let currentIndex = 0;

function getRandomIndex() {
  let newIndex;
  do {
    newIndex = Math.floor(Math.random() * images.length);
  } while (newIndex === currentIndex);
  return newIndex;
}

setInterval(() => {
  const dir = directions[Math.floor(Math.random() * directions.length)];
  const nextIndex = getRandomIndex();

  // slide out
  img.style.opacity = "0";
  img.style.transform = `translate(${dir.x}, ${dir.y})`;

  setTimeout(() => {
    currentIndex = nextIndex;
    img.src = images[currentIndex];

    // slide in
    img.style.transform = "translate(0,0)";
    img.style.opacity = "1";
  }, 800);

}, 3000);
