const dropdownMenu = document.getElementById("dropdownMenu");
let showDropdown = false;
const options = document.getElementsByClassName("option");

function toggleMenu() {
  if (showDropdown) {
    dropdownMenu.classList.remove("dropdown");
    dropdownMenu.classList.add("dropdownClose");
    showDropdown = false;
  } else {
    dropdownMenu.classList.remove("dropdownClose");
    dropdownMenu.classList.add("dropdown");
    showDropdown = true;
  }
}

for (let i = 0; i < options.length; i++) {
  options[i].addEventListener("click", () => toggleMenu());
}
