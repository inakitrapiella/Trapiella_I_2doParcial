fetch(`https:https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY)
  .then(response => response.json())
  .then(data => {
    const galeria = document.getElementById("galeria");
    data.results.forEach(img => {
      const div = document.createElement("div");
      div.classList.add("col-md-4", "mb-4");
      div.innerHTML = `
        <div class="card shadow-sm">
          <img src="${img.urls.small}" class="card-img-top" alt="${img.alt_description}">
          <div class="card-body">
            <p class="card-text">${img.alt_description || 'Imagen de diseño'}</p>
          </div>
        </div>`;
      galeria.appendChild(div);
    });
  })
  .catch(error => {
    console.error("Error al cargar la galeria:", error);
    document.getElementById("galeria").innerHTML = "<p>No se pudieron cargar imagenes.</p>";
  });