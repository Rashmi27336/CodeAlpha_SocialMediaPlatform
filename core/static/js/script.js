document.addEventListener("DOMContentLoaded", function () {

    /* ==============================
       PAGE FADE-IN ANIMATION
    ============================== */

    document.body.classList.add("page-loaded");


    /* ==============================
       POST CHARACTER COUNTER
    ============================== */

    const textareas = document.querySelectorAll("textarea");

    textareas.forEach(function (textarea) {

        const counter = document.createElement("div");

        counter.className = "character-counter";
        counter.textContent = "0 characters";

        textarea.parentNode.appendChild(counter);

        function updateCounter() {
            const count = textarea.value.length;
            counter.textContent = count + " characters";
        }

        textarea.addEventListener("input", updateCounter);

        updateCounter();
    });


    /* ==============================
       FORM SUBMIT LOADING STATE
    ============================== */

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const button = form.querySelector(
                'button[type="submit"], input[type="submit"]'
            );

            if (button) {
                button.dataset.originalText = button.textContent;

                button.textContent = "Processing...";
                button.disabled = true;

                setTimeout(function () {
                    button.disabled = false;
                    button.textContent = button.dataset.originalText;
                }, 3000);
            }

        });

    });


    /* ==============================
       MOBILE MENU
    ============================== */

    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {

            navLinks.classList.toggle("active");

            menuToggle.classList.toggle("active");

        });

        navLinks.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function () {
                navLinks.classList.remove("active");
                menuToggle.classList.remove("active");
            });

        });

    }


    /* ==============================
       CONFIRM LOGOUT
    ============================== */

    const logoutLinks = document.querySelectorAll(
        'a[href*="logout"]'
    );

    logoutLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const confirmLogout = confirm(
                "Are you sure you want to log out?"
            );

            if (!confirmLogout) {
                event.preventDefault();
            }

        });

    });


    /* ==============================
       AUTO HIDE DJANGO MESSAGES
    ============================== */

    const messages = document.querySelectorAll(
        ".message, .alert, .success-message"
    );

    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 4000);

    });

});