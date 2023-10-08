let trailer = document.querySelector('.trailer');
let play = document.querySelector('.video-play');
let pause = document.querySelector('.video-pause');


function playVideo() {
    play.classList.remove('show-video-btn');
    play.classList.add('hide-video-btn');
    
    pause.classList.remove('hide-video-btn');
    pause.classList.add('show-video-btn');
    setTimeout(() => {
        pause.classList.remove('show-video-btn');
        pause.classList.add('hide-video-btn');
    }, 1000);
    trailer.play();
}

function pauseVideo() {
    pause.classList.remove('show-video-btn');
    pause.classList.add('hide-video-btn');
    
    play.classList.remove('hide-video-btn');
    play.classList.add('show-video-btn');

    trailer.pause();
}

function hoverOverTrailer(){
    if(!trailer.paused && !pause.classList.contains('show-video-btn')){
        pause.classList.remove('hide-video-btn');
        pause.classList.add('show-video-btn');
        setTimeout(() => {
            pause.classList.remove('show-video-btn');
            pause.classList.add('hide-video-btn');
        }, 1000);
    }
}

trailer.addEventListener('mousemove', hoverOverTrailer)
trailer.addEventListener('touch', hoverOverTrailer)