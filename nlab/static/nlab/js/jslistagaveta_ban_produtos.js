$("#id_bancada").change(function () {
    const url = $("#reagentesForm").attr("data-gavetas_ban-url");  
    const bancadaId = $(this).val();     
    $.ajax({                       
        url: url,                    
        data: {
            'bancada_id': bancadaId       
        },        

        success: function (data) {   
            $("#id_gaveta").html(data);                                                         
                    
        }

        
    });
});


         


