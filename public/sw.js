// AprovaQuest Service Worker - PWA Offline Support
const CACHE_NAME = 'aprovaquest-cache-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './storage-adapter.js',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon.png',
  './data/questoes.json',
  './data/editais.json',
  'https://cdn.tailwindcss.com',
  'https://unpkg.com/lucide@latest'
];

// Install: Cache core application assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Caching app shell & assets...');
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn('[SW] Cache addAll partial failure, fallback will handle dynamically:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activate: Clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[SW] Removing old cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  return self.clients.claim();
});

// Fetch: Stale-while-revalidate / Network-first strategy
self.addEventListener('fetch', (event) => {
  const request = event.request;
  
  // Non-GET requests (e.g. POST to backend) pass through
  if (request.method !== 'GET') {
    return;
  }

  // Handle API or static requests
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      const fetchPromise = fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // If offline and request is HTML navigation, fallback to cached index.html
          if (request.headers.get('accept') && request.headers.get('accept').includes('text/html')) {
            return caches.match('./index.html') || caches.match('./');
          }
        });

      return cachedResponse || fetchPromise;
    })
  );
});
