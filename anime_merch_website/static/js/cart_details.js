function updateQuantity(product_id, input_element){
    let xhr = new XMLHttpRequest()
    xhr.responseType = 'text'
    link = 'quantity/'+product_id.toString()
    xhr.open('GET', link, true);
    xhr.send();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
          input_element.textContent = xhr.response;
          input_element.setAttribute('value', xhr.response);
          removeContainer(input_element);
        }
    }
}

function removeContainer(element){
    if (element.textContent == '0'){
        element.parentNode.parentNode.remove()
    }
}

aboba = document.querySelectorAll('a.cart-button')
aboba.forEach(element => element.onclick = () =>{
    id = 0;
    quantity = 0;
    input_element = element;
    if (element.parentNode.getAttribute('class') === 'cart-quantity-container'){
        id = element.parentNode.parentNode.getAttribute('value');
        quantity = element.getAttribute('value');
        input_element = element.parentNode.children[1];
    }
    else{
        id = element.parentNode.getAttribute('value');
        quantity = -1*parseInt(element.parentNode.children[2].children[1].getAttribute('value'));
        input_element = element.parentNode.children[2].children[1];
    }
    
    let xhr = new XMLHttpRequest()
    xhr.open('POST', 'cart')
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); 
    xhr.send("id="+id+"&quantity="+quantity);
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            updateQuantity(id, input_element);;
        }
    }
});

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
