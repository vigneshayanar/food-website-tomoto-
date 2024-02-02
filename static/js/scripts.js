function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let btns=document.querySelectorAll(".productbutton");
btns.forEach(btn=>{
    btn.addEventListener("click",addtocart)
})
function addtocart(e){
    let id_menu=e.target.value
    let url="/cart/";
    let data={id:id_menu};
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':"application/json",'X-CSRFToken': csrftoken},
        body:JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })
}