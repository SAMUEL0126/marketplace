
/*
    este es un comentario multilinea
*/

//alert("pagina cargada!!!!!!!!");

//console.log("este es un mensaje en la consola");
/*
var nombre = "matusalen"
var edad = 80

console.log("Nombre=" + nombre +" Edad="+ edad)

if(edad >= 18 && edad <= 64) {
    console.log("es mayor de edad")
} else if(edad <= 0 || edad > 120) {
    console.log("la edad es incorrecta")
} else if(edad >= 65) {
    console.log("adulto mayor")
} else {
    console.log("es menor de edad")
}

var i = 0;

while(i < 10) {
    console.log(i)
    i++
}
console.log("--------------")
for(j=0;j<20;j++) {
    console.log(j)
}

var nombres = ["adrian", "javier", "lulu", "ramon", "matias"]

console.log(nombres[0])

nombres.forEach(function(item) {
    console.log(item)
})

var persona = {
    nombre: "roberto",
    edad: 30,
    altura: 1.8
}

console.log(persona)*/


//programacion boton formulario contacto

var btnEnviar = document.getElementById("btnEnviar")

btnEnviar.addEventListener("click", function() {
    
    //traer los datos del formulario
    let nombre = document.getElementById("nombre").value
    let email  = document.getElementById("email").value
    let telefono = document.getElementById("telefono").value
    let tipoConsulta = document.getElementById("tipoconsulta").value
    let mensaje = document.getElementById("mensaje").value
    let aviso = document.getElementById("avisos").checked

    
    
    console.log(nombre)
    console.log(email)
    console.log(telefono)
    console.log(tipoConsulta)
    console.log(mensaje)
    console.log(aviso)

})
