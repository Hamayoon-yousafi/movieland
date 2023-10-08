let trailer = document.querySelector('.trailer');
let play = document.querySelector('.video-play');
let pause = document.querySelector('.video-pause');


function playVideo() {
    play.classList.remove('show');
    play.classList.add('hide');
    
    pause.classList.remove('hide');
    pause.classList.add('show');
    setTimeout(() => {
        pause.classList.remove('show');
        pause.classList.add('hide');
    }, 1000);
    trailer.play();
}

function pauseVideo() {
    pause.classList.remove('show');
    pause.classList.add('hide');
    
    play.classList.remove('hide');
    play.classList.add('show');

    trailer.pause();
}

function hoverOverTrailer(){
    if(!trailer.paused && !pause.classList.contains('show')){
        pause.classList.remove('hide');
        pause.classList.add('show');
        setTimeout(() => {
            pause.classList.remove('show');
            pause.classList.add('hide');
        }, 1000);
    }
}

trailer.addEventListener('mousemove', hoverOverTrailer)
trailer.addEventListener('touch', hoverOverTrailer)