window.addEventListener("load", function () {
  if (document.querySelector(".turtini-shell-header")) return;

  const header = document.createElement("div");
  header.className = "turtini-shell-header";
  header.innerHTML = `
    <div class="turtini-shell-header-inner">
      <nav class="turtini-shell-nav" aria-label="Turtini global navigation">
        <a href="https://turtini.com/" target="_blank" rel="noopener">Turtini</a>
        <a href="https://turtini.com/events" target="_blank" rel="noopener">Events</a>
        <a href="https://trident.turtini.com/login" target="_blank" rel="noopener">Trident</a>
      </nav>
    </div>
  `;

  document.body.appendChild(header);
  document.body.classList.add("turtini-shell-header-enabled");
});
