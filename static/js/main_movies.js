let carousel = null;
let isDragStart = false;
let prevPageX = false;
let prevScrollLeft = false;

// this function will target the carousel which the mouse is currently hovering over and all below functions will apply to that carousel
function targetCarousel(carouselID){
    if (!carousel) {
        carousel = document.getElementById(carouselID);
        carousel.addEventListener('mousedown', dragStart)
        carousel.addEventListener('touchstart', dragStart)
        
        carousel.addEventListener('mousemove', dragging)
        carousel.addEventListener('touchmove', dragging)
        
        carousel.addEventListener('mouseup', dragStop)
    }
}

function carouselMouseLeaveEvent(){
    if(carousel){
        dragStop()
        carousel = null;
    }
}

function dragStart(e){
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = carousel.scrollLeft;
    carousel.style.cursor = 'grabbing';
    carousel.style.scrollBehavior = 'auto';
}

function dragStop() {
    isDragStart = false;
    carousel.style.cursor = 'grab';
    carousel.style.scrollBehavior = 'smooth';
}

function dragging(e){
    if(!isDragStart) return;
    e.preventDefault();
    let positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX;
    carousel.scrollLeft = prevScrollLeft - positionDiff;
    toggleCarouselButtons();
}

function toggleCarouselButtons(){
    let carouselBTNs = document.querySelectorAll('.carouselBTN')
                                                  
    carouselBTNs[0].style.display = carousel.scrollLeft == 0 ? 'none' : 'block' 
    carouselBTNs[1].style.display = carousel.scrollLeft == carousel.scrollWidth - carousel.clientWidth ? 'none' : 'block'
}


function scrollCarousel(direction){
    toggleCarouselButtons()
    if (direction == 'left'){
        carousel.scrollLeft -= carousel.clientWidth
    } else {
        carousel.scrollLeft += carousel.clientWidth
    }
} 

function handle_params(param, value){
    url = new URLSearchParams(window.location.search)
    if (url.has(param)) {
        url.set(param, value)
    } else {
        url.append(param, value)
    }

    window.location.replace(window.location.origin + window.location.pathname + '?' + url.toString())
}

function openURL(url){
    document.location.href = url;
}