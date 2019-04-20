let modal = document.getElementById("novo_curso_modal");
let ncbtn = document.getElementById("novo_curso_button");
let close_button = document.getElementsByClassName("close")[0];

ncbtn.onclick = function() {
  modal.style.display = "block";
}

// close_button.onclick = function () {
//   modal.style.display = "none";
// }

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
