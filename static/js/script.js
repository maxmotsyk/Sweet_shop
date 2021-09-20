//burger menu
const iconMenu = document.querySelector('.burger_menu');
if(iconMenu){
    const burgerBody = document.querySelector('.col-md-12.burger_body');
    iconMenu.addEventListener("click",function(e){
    iconMenu.classList.toggle('active');
    burgerBody.classList.toggle('active');
    });
}

// rgb(147, 69, 238) f
//#7148FF; h