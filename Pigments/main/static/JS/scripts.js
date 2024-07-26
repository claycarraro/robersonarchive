let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}

let item = document.querySelector('.icon-hamburger');
    item.addEventListener("click", function() {
      document.body.classList.toggle('menu-open');
    });



let currentIndex = 0;
const images = [
    "{% static 'Rectos/MS788-1993_001_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_002_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_003_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_004_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_005_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_006_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_007_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_008_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_009_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_010_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_011_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_012_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_013_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_014_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_015_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_016_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_017_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_018_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_019_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_020_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_021_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_022_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_023_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_024_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_025_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_026_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_027_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_028_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_029_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_030_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_031_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_032_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_033_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_034_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_035_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_036_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_037_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_038_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_039_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_040_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_041_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_042_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_043_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_044_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_045_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_046_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_047_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_048_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_049_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_050_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_051_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_052_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_053_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_054_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_055_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_056_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_057_20240625_sr854_MAS.jpg' %}",
            "{% static 'Rectos/MS788-1993_058_20240625_sr854_MAS.jpg' %}"
];

function changeImage(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    } else if (currentIndex >= images.length) {
        currentIndex = 0;
    }
    console.log("Current Index: ", currentIndex);  // Debugging
    document.getElementById("carousel-image").src = images[currentIndex];
}

// Imposta l'immagine iniziale
window.onload = function() {
    if (images.length > 0) {
        document.getElementById("carousel-image").src = images[0];
    }
};