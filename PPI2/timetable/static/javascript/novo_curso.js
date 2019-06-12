// let modalNovoCurso = document.getElementById("novo_curso_modal");
// let ncbtn = document.getElementById("novo_curso_button");
// let close_button = document.getElementsByClassName("close")[0];
//
// ncbtn.onclick = function() {
//   modalNovoCurso.style.display = "block";
// }
//
// window.onclick = function(event) {
//   if (event.target == modalNovoCurso) {
//     modalNovoCurso.style.display = "none";
//   }
// }

$(function() {
  $("#novo_curso_modal .close").click(function() {
    $("#novo_curso_modal").css("display", "none");
  })

  $("#novo_curso_button").click(function() {
    $("#novo_curso_modal").css("display", "block");
  })

  // $("a[id*=deleta_curso").click(function() {
  //   $("#excluir_curso_modal").css("display", "block");
  // })

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
});
