$().ready(() =>{
    $("#botton_tooltip1").on('click', function(){
        alert("El correo fue enviado correctamente")
    })
})
$(document).scroll( function(e){
    const y = $("html").scrolltop();
    if (y > 300) $("nav").addClass("nav-black")
    else $("nav").removeclass("nav-black")
        
    })