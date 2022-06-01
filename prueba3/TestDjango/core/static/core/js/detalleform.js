$('#formulario').submit(function(evento){
    evento.preventDefault();
    alert("Comentario recibido");


})



  
  document.addEventListener('DOMContentLoaded', function(){
    let formulario = document.getElementById('formulario');
    formulario.addEventListener('submit', function() {
      formulario.reset();
    });
  });
