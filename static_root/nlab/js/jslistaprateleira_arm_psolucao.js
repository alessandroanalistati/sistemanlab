$("#id_armario").change(function () {
    const url = $("#pedidosolucaoForm").attr("data-prateleiras_arm-url");  
    const armarioId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'armario_id': armarioId       
        },        

        success: function (data) {   
            $("#id_prateleira").html(data);                                                         
                    
        }

        
    });
});


         


