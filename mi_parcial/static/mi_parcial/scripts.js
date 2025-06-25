document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("id_consultas");
    const resultado = document.getElementById("id_resultado");
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formulario.addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(formulario);
        fetch("/consultas/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": csrftoken
            }
        })
        .then(response => response.text())
        .then(data => {
            resultado.innerHTML = `<div class="alert alert-success">¡Consulta enviada con exito!</div>`;
            formulario.reset();
        })
        .catch(error => {
            console.error("Error:", error);
            resultado.innerHTML = `<div class="alert alert-danger">Hubo un error al enviar la consulta.</div>`;
        });
    });
});