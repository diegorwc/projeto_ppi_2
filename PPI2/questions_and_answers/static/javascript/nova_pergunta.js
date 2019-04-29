let modal = document.getElementById("new_question_modal");
let nqbtn = document.getElementById("new_question_button");
let close_button = document.getElementsByClassName("close")[0];

nqbtn.onclick = function() {
  modal.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
