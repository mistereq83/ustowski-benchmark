/**
 * Ustowski Content Loader
 * Dynamically loads pricing, reviews, and projects from /api/content
 */
(function() {
  fetch('/api/content')
    .then(r => r.json())
    .then(data => {
      loadPricing(data.pricing);
      loadReviews(data.reviews);
      loadProjects(data.projects);
    })
    .catch(() => {}); // Silent fail — static content stays

  // === PRICING ===
  function loadPricing(pricing) {
    if (!pricing || !pricing.services) return;
    pricing.services.forEach(s => {
      document.querySelectorAll(`[data-price="${s.id}"]`).forEach(el => {
        if (s.priceFrom !== null && s.priceTo !== null) {
          el.textContent = `${s.priceFrom}–${s.priceTo}`;
        }
      });
      document.querySelectorAll(`[data-price-unit="${s.id}"]`).forEach(el => {
        el.textContent = s.unit;
      });
      document.querySelectorAll(`[data-price-note="${s.id}"]`).forEach(el => {
        el.textContent = s.note;
      });
      document.querySelectorAll(`[data-price-full="${s.id}"]`).forEach(el => {
        if (s.priceFrom !== null) {
          el.textContent = `${s.priceFrom}–${s.priceTo} ${s.unit}`;
        } else {
          el.textContent = s.unit;
        }
      });
    });
  }

  // === REVIEWS ===
  function loadReviews(reviews) {
    if (!reviews || !reviews.length) {
      document.querySelectorAll('[data-reviews]').forEach(container => {
        const section = container.closest('section');
        if (section) section.style.display = 'none';
      });
      return;
    }
    document.querySelectorAll('[data-reviews]').forEach(container => {
      const filter = container.dataset.reviews;
      const limit = parseInt(container.dataset.reviewsLimit) || 3;
      let filtered = reviews;
      if (filter !== 'all') {
        filtered = reviews.filter(r => r.city === filter || r.service === filter);
      }
      filtered = filtered.slice(0, limit);
      if (!filtered.length) {
        const section = container.closest('section');
        if (section) section.style.display = 'none';
        return;
      }
      container.innerHTML = filtered.map(r => `
        <div class="bg-bg rounded-2xl p-6 border border-primary/5">
          <div class="flex items-center gap-1 mb-3">
            ${Array(r.rating).fill('<span class="text-yellow-400 text-lg">★</span>').join('')}${Array(5-r.rating).fill('<span class="text-gray-300 text-lg">★</span>').join('')}
          </div>
          <p class="text-primary/80 mb-4 italic leading-relaxed">"${r.text}"</p>
          <div class="flex items-center justify-between">
            <span class="font-heading font-medium text-sm">${r.name}</span>
            <span class="text-primary/40 text-xs font-mono">${CITY_NAMES[r.city] || r.city}</span>
          </div>
        </div>
      `).join('');
    });
  }

  // === PROJECTS ===
  function loadProjects(projects) {
    if (!projects || !projects.length) {
      document.querySelectorAll('[data-projects]').forEach(c => {
        const section = c.closest('section');
        if (section) section.style.display = 'none';
      });
      return;
    }

    document.querySelectorAll('[data-projects]').forEach(container => {
      const pageFilter = container.dataset.projects; // "index", "mycie-elewacji", "all", etc.
      const limit = parseInt(container.dataset.projectsLimit) || 6;

      let filtered = projects;
      if (pageFilter !== 'all') {
        filtered = projects.filter(p => p.pages && p.pages.includes(pageFilter));
      }
      // Sort by date descending (newest first)
      filtered.sort((a, b) => (b.date || '').localeCompare(a.date || ''));
      filtered = filtered.slice(0, limit);

      if (!filtered.length) {
        const section = container.closest('section');
        if (section) section.style.display = 'none';
        return;
      }

      // Determine layout: homepage uses mini-sliders (grid 2-3 col), service pages use large sliders (grid 1-2 col)
      const isHomepage = pageFilter === 'index';
      
      container.innerHTML = filtered.map(p => {
        const hasImages = p.imageBefore && p.imageAfter;
        const serviceName = SERVICE_NAMES[p.service] || p.service;
        const cityName = CITY_NAMES[p.city] || p.city;
        const location = cityName + (p.district ? ' ' + p.district : '');
        
        if (!hasImages) {
          // No images — simple card
          return `
            <div class="space-y-3">
              <div class="${isHomepage ? 'h-[160px] md:h-[220px]' : 'h-[220px] md:h-[400px]'} rounded-2xl bg-secondary flex items-center justify-center text-primary/20">
                <svg class="w-12 h-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              </div>
              <div class="flex justify-between items-center px-1">
                <span class="font-heading font-bold ${isHomepage ? 'text-base md:text-xl' : 'text-lg'}">${serviceName}</span>
                <span class="text-primary/50 text-xs md:text-sm font-mono">${location}</span>
              </div>
            </div>`;
        }

        if (isHomepage) {
          // Mini slider (homepage style)
          return `
            <div class="space-y-3">
              <div class="mini-slider js-mini-slider rounded-2xl overflow-hidden ${isHomepage ? 'h-[160px] md:h-[220px]' : ''}">
                <img src="${p.imageAfter}" class="mini-after" alt="Po" loading="lazy">
                <img src="${p.imageBefore}" class="mini-before grayscale brightness-75" alt="Przed" loading="lazy">
                <div class="mini-handle"></div>
              </div>
              <div class="flex justify-between items-center px-1">
                <span class="font-heading font-bold text-base md:text-xl">${serviceName}</span>
                <span class="text-primary/50 text-xs md:text-sm font-mono flex items-center gap-1">
                  <svg class="w-3 h-3 md:w-4 md:h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                  ${location}
                </span>
              </div>
            </div>`;
        } else {
          // Large slider (service page style)
          return `
            <div class="gs-card">
              <div class="h-[220px] md:h-[400px] w-full mb-4 ba-container relative rounded-[2rem] overflow-hidden bg-secondary">
                <div class="ba-slider">
                  <img src="${p.imageAfter}" class="ba-after" alt="Po">
                  <img src="${p.imageBefore}" class="ba-before grayscale brightness-75 contrast-125" alt="Przed">
                  <div class="ba-handle"></div>
                </div>
              </div>
              <div class="flex justify-between items-center px-2">
                <span class="font-medium">${serviceName}</span>
                <span class="text-primary/50 text-sm font-mono">${location}</span>
              </div>
            </div>`;
        }
      }).join('');

      // Initialize sliders for dynamically added elements
      initDynamicSliders(container);
    });
  }

  // === SLIDER INIT ===
  function initDynamicSliders(container) {
    // Mini sliders (homepage style)
    container.querySelectorAll('.js-mini-slider').forEach(slider => {
      const before = slider.querySelector('.mini-before');
      const handle = slider.querySelector('.mini-handle');
      if (!before || !handle) return;
      let dragging = false;

      const move = (e) => {
        if (!dragging) return;
        e.preventDefault();
        const rect = slider.getBoundingClientRect();
        const x = Math.max(0, Math.min((e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left, rect.width));
        const pct = (x / rect.width) * 100;
        before.style.clipPath = `polygon(0 0, ${pct}% 0, ${pct}% 100%, 0 100%)`;
        handle.style.left = pct + '%';
      };

      handle.addEventListener('mousedown', () => dragging = true);
      handle.addEventListener('touchstart', () => dragging = true, {passive: true});
      window.addEventListener('mouseup', () => dragging = false);
      window.addEventListener('touchend', () => dragging = false);
      window.addEventListener('mousemove', move);
      window.addEventListener('touchmove', move, {passive: false});
    });

    // Large ba-sliders (service page style)
    container.querySelectorAll('.ba-container').forEach(c => {
      const slider = c.querySelector('.ba-slider');
      const before = slider?.querySelector('.ba-before');
      const handle = slider?.querySelector('.ba-handle');
      if (!slider || !before || !handle) return;
      let dragging = false;

      const move = (e) => {
        if (!dragging) return;
        e.preventDefault();
        const rect = slider.getBoundingClientRect();
        const x = Math.max(0, Math.min((e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left, rect.width));
        const pct = (x / rect.width) * 100;
        before.style.clipPath = `polygon(0 0, ${pct}% 0, ${pct}% 100%, 0 100%)`;
        handle.style.left = pct + '%';
      };

      handle.addEventListener('mousedown', () => dragging = true);
      handle.addEventListener('touchstart', () => dragging = true, {passive: true});
      window.addEventListener('mouseup', () => dragging = false);
      window.addEventListener('touchend', () => dragging = false);
      window.addEventListener('mousemove', move);
      window.addEventListener('touchmove', move, {passive: false});
    });
  }

  // === LOOKUP TABLES ===
  const CITY_NAMES = {
    'gdansk': 'Gdańsk', 'gdynia': 'Gdynia', 'sopot': 'Sopot',
    'wejherowo': 'Wejherowo', 'rumia': 'Rumia', 'reda': 'Reda',
    'pruszcz-gdanski': 'Pruszcz Gdański', 'tczew': 'Tczew', 'starogard-gdanski': 'Starogard Gdański',
    'kartuzy': 'Kartuzy', 'zukowo': 'Żukowo', 'koscierzyna': 'Kościerzyna',
    'goreczyno': 'Goręczyno', 'lebork': 'Lębork', 'bytow': 'Bytów'
  };
  const SERVICE_NAMES = {
    'mycie-elewacji': 'Mycie elewacji', 'mycie-dachu': 'Mycie dachu',
    'malowanie-elewacji': 'Malowanie elewacji', 'malowanie-dachu': 'Malowanie dachu',
    'impregnacja': 'Impregnacja'
  };
})();
