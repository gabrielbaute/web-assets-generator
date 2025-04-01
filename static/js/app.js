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

  const CACHE_NAME = 'octopus-icons-v1';
  const ASSETS_TO_CACHE = [
    // HTML principal
    '/',
    
    // CSS (todos los críticos)
    '/static/css/bulma.min.css',       // Framework Bulma
    '/static/css/all.min.css',   // Iconos locales
    '/static/css/styles.css',          // Tus estilos personalizados
    
    // JS
    '/static/js/app.js',               // Tu lógica PWA
    
    // Imágenes/Icons
    '/static/img/android-192x192.png',
    '/static/img/android-512x512.png',
    '/static/img/apple-touch-icon.png',
    '/static/img/favicon.ico',
    '/static/img/favicon-16x16.png',
    '/static/img/favicon-32x32.png',
    '/static/img/logo.png',

    // Fuentes locales
    '/static/webfonts/fa-solid-900.woff2'
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