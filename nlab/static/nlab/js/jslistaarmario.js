$("#id_sala").change(function () {
    const url = $("#equipamentosForm").attr("data-armarios-url");  
    const salaId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'sala_id': salaId       
        },        

        success: function (data) {   
            $("#id_armario").html(data);                                                         
                    
        }

        
    });
});




         


