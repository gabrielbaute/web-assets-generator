// Registro del Service Worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then(registration => {
          console.log('ServiceWorker registrado con éxito:', registration.scope);
        })
        .catch(err => {
          console.log('Error al registrar ServiceWorker:', err);
        });
    });
  }
  
  // Archivo sw.js (debe estar en la raíz de /static)
  // Crea este archivo en static/sw.js
  const CACHE_NAME = 'octopus-icons-v1';
  const ASSETS_TO_CACHE = [
    '/',
    '/static/css/styles.css',
    '/static/js/app.js',
    '/static/android-192x192.png'
  ];
  
  self.addEventListener('install', event => {
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(cache => cache.addAll(ASSETS_TO_CACHE))
    );
  });
  
  self.addEventListener('fetch', event => {
    event.respondWith(
      caches.match(event.request)
        .then(response => response || fetch(event.request))
    );
  });