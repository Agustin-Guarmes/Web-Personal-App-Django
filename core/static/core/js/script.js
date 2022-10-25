const nombre = document.getElementById("txtNombre")
const email = document.getElementById("txtCorreo")
const sms = document.getElementById("message")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,6})+$/ //extraido de https://www.w3resource.com/javascript/form/email-validation.php
    parrafo.innerHTML = ""
    if(nombre.value.length <3){
        warnings += `El nombre no es valido <br>`
        entrar = true
    }
    else if(!regexEmail.test(email.value)){      //debe tener "texto @ texto . texto (de 2 a 6 letras)"
        warnings += `El email no es valido <br>`
        entrar = true
    }
    else if(sms.value.length < 5){
        warnings += `El mensaje es corto <br>`
        entrar = true
    }

/*     if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = 'Enviado'
    } */
})