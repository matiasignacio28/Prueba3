/*price range*/

if ($.fn.slider) {
    $('#sl2').slider();
}

var RGBChange = function () {
    $('#RGB').css('background', 'rgb(' + r.getValue() + ',' + g.getValue() + ',' + b.getValue() + ')')
};

/*scroll to top*/

$(document).ready(function () {
    $(function () {
        $.scrollUp({
            scrollName: 'scrollUp', // Element ID
            scrollDistance: 300, // Distance from top/bottom before showing element (px)
            scrollFrom: 'top', // 'top' or 'bottom'
            scrollSpeed: 300, // Speed back to top (ms)
            easingType: 'linear', // Scroll to top easing (see http://easings.net/)
            animation: 'fade', // Fade, slide, none
            animationSpeed: 200, // Animation in speed (ms)
            scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
            //scrollTarget: false, // Set a custom target element for scrolling to the top
            scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
            scrollTitle: false, // Set a custom <a> title if required.
            scrollImg: false, // Set true to use image
            activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
            zIndex: 2147483647 // Z-Index for the overlay
        });
    });
});




$("#buscadordor").ready(function(){

var url = [
    {
      "id": 1,
      "nombre": "Bolso Transportador Huella",
      "sku": "2123124123",
      "precio": "$18.990"
    },
    {
        "id": 2,
        "nombre": "Bolso Diseño Flores",
        "sku": "2123124124",
        "precio": "$19.990"
    },
    {
        "id": 3,
        "nombre": "Bolso Con Diseño Gato",
        "sku": "2123124125",
        "precio": "$21.990"
    },
    {
        "id": 4,
        "nombre": "Bolso Con Bolsillos",
        "sku": "2123124126",
        "precio": "$28.990"
    },
    {
        "id": 5,
        "nombre": "Collar Con Luz M",
        "sku": "2123124127",
        "precio": "$3.990"
    },
    {
        "id": 6,
        "nombre": "Collar Gato Reflectante Lila",
        "sku": "2123124128",
        "precio": "$2.990"
    },
    {
        "id": 7,
        "nombre": "Collar Gato Full-Color",
        "sku": "2123124129",
        "precio": "$6.990"
    },
    {
        "id": 8,
        "nombre": "Collar Gato Reflectante Verde",
        "sku": "2123124130",
        "precio": "$2.990"
    },
    {
        "id": 9,
        "nombre": "Arnés + Correa",
        "sku": "2123124131",
        "precio": "$7.990"
    },
    {
        "id": 10,
        "nombre": "Arnés H Marge Simpson",
        "sku": "2123124132",
        "precio": "$12.990"
    },
    {
        "id": 11,
        "nombre": "Rasguñador Jirafa",
        "sku": "2123124133",
        "precio": "$48.990"
    }
  ];

  var fuseOptions = {keys: ["nombre", "id"]};
  var options = {display:"nombre", key:"id", fuseOptions: fuseOptions};
 
  $("#buscador").fuzzyComplete(url, options);
   }

);  



//buscador global con live server
/*$("#buscadordor").ready(function(){
    
  var url = 'js/productosCiberPet.json';  
    
   

  $.ajax({
       url: url,
       type:"GET",
       datatype:"json",
       success:function(data){
           console.log(data);
           var fuseOptions = {keys: ["nombre","id"]};
           var opciones = {display: "nombre", key: "id", fuseOptions: fuseOptions};
           $("#buscador").fuzzyComplete(data, opciones)
       }
    });
});*/    
