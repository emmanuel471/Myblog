
const activePage = window.location.pathname;
console.log(activePage);
const navLinks = document.querySelectorAll('li a').
forEach(link=>
{
  if((link.href.includes(`${activePage}`)))
   link.classList.add('active');
})


function createSlick(){

$(".slider").not('.slick-initialized').slick({
  centerMode: true,
    autoplay: true,
    dots: true,
      arrows: true,
    slidesToShow: 3,
    responsive: [{
        breakpoint: 768,
        settings: {
            dots: false,
            arrows: false,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1
        }
    }]
});

}
createSlick();

function myFunction() {
    document.getElementById('customAlert').style.display = 'block';
}

function closeAlert() {
    document.getElementById('customAlert').style.display = 'none';
}

function myFunctionP() {
    document.getElementById('projects').style.display = 'block';
}

function closeAlertP() {
    document.getElementById('projects').style.display = 'none';
}

function myFunctionE() {
    document.getElementById('education').style.display = 'block';
}

function closeAlertE() {
    document.getElementById('education').style.display = 'none';
}

// Optional: Close the modal when clicking outside of it
window.onclick = function(event) {
    if (event.target == document.getElementById('customAlert')) {
        document.getElementById('customAlert').style.display = 'none';
    }
}

//Will not throw error, even if called multiple times.
$(window).on( 'resize', createSlick );
