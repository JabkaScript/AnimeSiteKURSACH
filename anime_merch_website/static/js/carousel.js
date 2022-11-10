
function change_active_to(n){
    imgs = document.querySelectorAll('img')
    for (let i = 0; i < imgs.length; i++) {
        imgs[i].className = 'notactive'
    }
    imgs[n].className = 'active' 
}

function change_active_dot_to(n){
    dots = document.querySelectorAll('.dot')
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = 'dot'
    }
    dots[n].className += ' active'
}
