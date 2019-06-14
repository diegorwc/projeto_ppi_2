$(function() {

  $("#novo_curso_modal .close").click(function() {
    $("#novo_curso_modal").css("display", "none");
  })

  $("#novo_curso_button").click(function() {
    $("#novo_curso_modal").css("display", "block");
  })

  $("#cancelar").click(function() {
    $("#excluir_curso_modal").css("display", "none");
  })

  $("#novo_professor_button").click(function() {
    $("#novo_professor_modal").css("display", "block");
  })

  $("#nova_unidade_curricular_button").click(function() {
    $("#nova_unidade_curricular_modal").css("display", "block");
  })

  $("#nova_uc_fechar").click(function() {
    $("#nova_unidade_curricular_modal").css("display", "none");
  })

  $("#filtra_professor").change(function() {
    console.log($(this).val());
  })

});
