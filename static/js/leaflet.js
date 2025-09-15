document.addEventListener("DOMContentLoaded", () => {
  if (!window.L) {
    console.error(
      "Leaflet no se cargó. Revisa la etiqueta <script> de Leaflet."
    );
    return;
  }

  // Centrar mapa en las coordenadas nuevas
  const map = L.map("map").setView([4.628128297027238, -74.06594839013594], 18);

  L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    {
      attribution:
        "Tiles © Esri — Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, etc.",
      maxZoom: 20,
    }
  ).addTo(map);

  // Agregar marcador en las coordenadas
  L.marker([4.628128297027238, -74.06594839013594])
    .addTo(map)
    .bindPopup("<b>UDFJC</b><br>Sede de Ingeiería")
    .openPopup();
});
