$("#id_estante").change(function () {
    const url = $("#reagentesForm").attr("data-prateleiras_est-url");  
    const estanteId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'estante_id': estanteId       
        },        

        success: function (data) {   
            $("#id_prateleira").html(data);                                                         
                    
        }

        
    });
});


         


