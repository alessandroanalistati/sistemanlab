$(document).ready(function() {
    //Select para mostrar e esconder divs
    $('#select').on('change',function(){
        var selectValue = '#'+$(this).val();
        $('#pai').children('div').hide();
        $('#pai').children(selectValue).show();
 

       
    });
});

