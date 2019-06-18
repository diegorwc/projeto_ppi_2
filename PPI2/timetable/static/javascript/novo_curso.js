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

  // $("#span-username").css("display", "none");

  $("#filtra_professor").change(function() {
    console.log($(this).val());
  })

  $("#id_username").change(function() {
    // console.log("Teste: " + $("#id_username").val());
    let usuario = $("#id_username").val();
    $.ajax({
      url: '/valida_usuario/',
      data: {
        'usuario': usuario
      },
      dataType: 'json',
      success: function (data) {
        if (data.em_uso) {
          // alert("Este nome de usuário já existe!")
          let data = {
            message: 'Este nome de usuário já existe!'
          };
          var snackbarContainer = document.querySelector('#username-toast');
          snackbarContainer.MaterialSnackbar.showSnackbar(data);
          $("#username-wrapper").addClass("is-invalid");
        }
        console.log('Em uso: ' + data.em_uso + '\nUsuario: ' + data.usuario)
      }
    });
  });

  $(".close-alert").click(function() {
    $(".alert").css("display", "none");
  })

});
