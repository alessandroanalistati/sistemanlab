$("#id_sala").change(function () {
    const url = $("#reagentesForm").attr("data-bancadas-url");  
    const salaId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'sala_id': salaId       
        },        

        success: function (data) {   
            $("#id_bancada").html(data);                                                         
                    
        }

        
    });
});




         


