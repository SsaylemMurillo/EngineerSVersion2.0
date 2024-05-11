function toggleDropdown(){
  let dropdown = document.querySelector('#dropdownButton #dropdown');
  dropdown.classList.toggle("hidden");
}

function onBurguerClick(){
  const navLinks = document.querySelector(".nav-links");
  const menu = document.querySelector("#imageButton")
  if(menu.name === 'menu'){
    menu.setAttribute("src", "/static/icons/feather/x3.svg");
    navLinks.classList.remove('top-[-100%]');
    navLinks.classList.add('top-[9%]');
  }
  else{
    menu.setAttribute("src", "/static/icons/feather/menu3.svg");
    navLinks.classList.remove('top-[9%]');
    navLinks.classList.add('top-[-100%]');
  }
  menu.name = menu.name === 'menu' ? 'close' : 'menu';
}

function esNumero(event) {
    var charCode = (event.which) ? event.which : event.keyCode;

    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        // Bloquea la entrada de caracteres que no son números
        event.preventDefault();
        return false;
    }

    return true;
}

function limpiarCampos(...campos) {
    // Limpiar los campos del formulario
    campos.forEach((campo) => {
      document.getElementById(campo).value = "";
    });
  }

function closeTab() {
    window.history.back();
}