$("#id_sala").change(function () {
    const url = $("#reagentesForm").attr("data-estantes-url");  
    const salaId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'sala_id': salaId       
        },        

        success: function (data) {   
            $("#id_estante").html(data);                                                         
                    
        }

        
    });
});




         


