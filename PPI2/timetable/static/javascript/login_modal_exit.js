let modal = document.getElementById('login_modal');

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
