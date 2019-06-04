let modalExcluirCurso = document.getElementById("excluir_curso_modal");
let excluir_curso_button = document.getElementById("deleta_curso_button");
// let close_button = document.getElementsByClassName("close")[0];

excluir_curso_button.onclick = function() {
  modalExcluirCurso.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == modalExcluirCurso) {
    modalExcluirCurso.style.display = "none";
  }
}
