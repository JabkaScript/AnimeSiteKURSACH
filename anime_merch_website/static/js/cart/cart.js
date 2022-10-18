function change_price(a, b){
    var p = a.parentElement;
    var i = p.children[1];
    i.value = Number(i.value) + b;
    if (Number(i.value) === 0){delete_row(p)}
    calculate_total_price(a)
}

function calculate_total_price(a){
    var q = a.parentElement.children[1].value;
    var tp = a.parentElement.parentElement.parentElement.children[4];
    var cp = a.parentElement.parentElement.parentElement.children[2].children[0].innerHTML;
    tp.children[0].innerHTML = cp[0] + String(q * Number(cp.substring(1)))
}
function delete_row(e){
    e.parentElement.parentElement.remove()
}