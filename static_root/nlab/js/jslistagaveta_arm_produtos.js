$("#id_armario").change(function () {
    const url = $("#reagentesForm").attr("data-gavetas_arm-url");  
    const armarioId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'armario_id': armarioId       
        },        

        success: function (data) {   
            $("#id_gaveta").html(data);                                                         
                    
        }

        
    });
});


         


