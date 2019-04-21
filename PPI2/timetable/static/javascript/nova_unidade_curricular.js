let modal = document.getElementById("nova_unidade_curricular_modal");
let ncbtn = document.getElementById("nova_unidade_curricular_button");
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
