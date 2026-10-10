document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");
    const navLinksContainer = document.querySelector(".nav-links");
    const currentPath = window.location.pathname.toLowerCase();

    // 1. Highlight active navigation item based on current URL path
    if (navLinksContainer) {
        const links = navLinksContainer.querySelectorAll("a");
        links.forEach((link) => {
            const linkHref = link.getAttribute("href").toLowerCase();
            // Match exact path or sub-routes (e.g. /Aircraft/update/1 matches /Aircraft)
            if (currentPath === linkHref || (linkHref !== "/" && currentPath.startsWith(linkHref))) {
                links.forEach((l) => l.classList.remove("active"));
                link.classList.add("active");
            }
        });
    }

    // 2. Add an elevation shadow when scrolling down
    window.addEventListener("scroll", function () {
        if (window.scrollY > 10) {
            navbar.classList.add("navbar-scrolled");
        } else {
            navbar.classList.remove("navbar-scrolled");
        }
    });

    // 3. Responsive hamburger menu toggle for mobile devices
    const navContainer = document.querySelector(".nav-container");
    if (navContainer && navLinksContainer) {
        const toggleBtn = document.createElement("button");
        toggleBtn.className = "nav-toggle-btn";
        toggleBtn.setAttribute("aria-label", "Toggle navigation");
        toggleBtn.innerHTML = `
            <span class="hamburger-bar"></span>
            <span class="hamburger-bar"></span>
            <span class="hamburger-bar"></span>
        `;

        navContainer.appendChild(toggleBtn);

        toggleBtn.addEventListener("click", function () {
            navLinksContainer.classList.toggle("nav-open");
            toggleBtn.classList.toggle("is-active");
        });

        // Close mobile dropdown when a link is clicked
        navLinksContainer.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navLinksContainer.classList.remove("nav-open");
                toggleBtn.classList.remove("is-active");
            });
        });
    }
});