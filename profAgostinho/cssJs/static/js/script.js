document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("formCadastro");

    form.addEventListener("submit", function (event) {

        let username = document.getElementById("username").value.trim();
        let email = document.getElementById("email").value.trim();
        let password = document.getElementById("password").value.trim();

        // validações simples
        if (username === "" || email === "" || password === "") {
            alert("Todos os campos devem ser preenchidos.");
            event.preventDefault();
            return;
        }

        // validação básica de e-mail
        if (!email.includes("@") || !email.includes(".")) {
            alert("Digite um email válido.");
            event.preventDefault();
            return;
        }

    });

});
