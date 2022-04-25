$("#id_bancada").change(function () {
    const url = $("#pedidosolucaoForm").attr("data-prateleiras_ban-url");  
    const bancadaId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'bancada_id': bancadaId       
        },        

        success: function (data) {   
            $("#id_prateleira").html(data);                                                         
                    
        }

        
    });
});


         


