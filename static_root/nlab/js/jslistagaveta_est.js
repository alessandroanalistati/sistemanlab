$("#id_estante").change(function () {
    const url = $("#equipamentosForm").attr("data-gavetas_est-url");  
    const estanteId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'estante_id': estanteId       
        },        

        success: function (data) {   
            $("#id_gaveta").html(data);                                                         
                    
        }

        
    });
});


         


