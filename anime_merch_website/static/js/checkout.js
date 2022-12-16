function confirm_order(address, commentary){
    let xhr = new XMLHttpRequest()
    console.log()
    link = 'confirm_order'+'/address='+address+'&commentary='+commentary
    xhr.open('POST', link)
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); 
    xhr.send();
    alert('Заказ принят. Для перехода к главной странице нажмите "ОК"')
    window.location = '.'
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    
}
