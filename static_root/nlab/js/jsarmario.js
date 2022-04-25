$(function () {

    // Oculta as opções do segundo select:
    $("#t-shift option").hide();
    
    // Observa o evento change do primeiro select:
    $("#p-shift").on("change", function () {
    
      // Recupera o valor selecionado:
      let sala = $("#p-shift").val();
      
      // Oculta as opções atuais:
      $("#t-shift option").hide();
      
      // Exibe as opções conforme a seleção:
      $("#t-shift option[data-sala="+ sala +"]").show();
    
    });
  
  });