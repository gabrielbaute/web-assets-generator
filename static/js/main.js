// main.js (ubicado en static/js)
document.addEventListener("DOMContentLoaded", () => {
    // Constantes para detectar el boton de cambio de theme
    const themeToggle = document.getElementById("theme-toggle");
    const htmlElement = document.documentElement;

    // Leer el tema inicial desde localStorage
    const currentTheme = localStorage.getItem("theme") || "light";
    htmlElement.setAttribute("data-theme", currentTheme);

    // Función para actualizar el ícono del botón
    const updateIcon = () => {
        const activeTheme = htmlElement.getAttribute("data-theme");
        themeToggle.innerHTML = activeTheme === "dark" 
            ? '<i class="fa-solid fa-sun"></i>' 
            : '<i class="fa-solid fa-moon"></i>';
    };

    // Actualizar ícono según el tema inicial
    updateIcon();

    // Manejar el clic en el botón para cambiar el tema
    themeToggle.addEventListener("click", () => {
        const activeTheme = htmlElement.getAttribute("data-theme");
        const newTheme = activeTheme === "light" ? "dark" : "light";

        // Cambiar el tema en el atributo y guardar en localStorage
        htmlElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);

        // Actualizar el ícono dinámicamente
        updateIcon();
    });
});