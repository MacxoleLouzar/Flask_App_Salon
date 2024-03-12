function validateLoginForm() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (email === "" || password === "") {
    alert("Please fill in all fields");
    return false;
  }
  if(email.length < 5){
    alert("Email is too short");
    return false;
  }
  if (password.length < 5) {
    alert("Password is too short");
    return false;
  }
  if(!email.includes("@")){
    alert("Email is invalid");
    return false;
  }
  if(email.includes(" ")){
    alert("Email is invalid");
    return false;
  }
  if (password.includes(" ")) {
    alert("Password is invalid");
    return false;
  }
  return true;
}

function validateRegisterForm() {
  const email = document.getElementById("email").value;
  const name = document.getElementById("name").value;
  const address = document.getElementById("address").value;
  const contact = document.getElementById("contact").value;
  const password = document.getElementById("password").value;
  const confirm_password = document.getElementById("confirm_password").value;

  if (
    name === "" ||
    address === "" ||
    contact === "" ||
    email === "" ||
    password === "" ||
    confirm_password === ""
  ) {
    alert("Please fill in all fields");
    console.log(email, password);
    return false;
  }

  if (password !== confirm_password) {
    alert("Passwords do not match");
    return false;
  }

  return true;
}
