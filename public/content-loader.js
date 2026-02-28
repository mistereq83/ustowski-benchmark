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

  function loadPricing(pricing) {
    if (!pricing || !pricing.services) return;
    
    // Update all elements with data-price="service-id"
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
      // Full price display: "13–18 zł/m²"
      document.querySelectorAll(`[data-price-full="${s.id}"]`).forEach(el => {
        if (s.priceFrom !== null) {
          el.textContent = `${s.priceFrom}–${s.priceTo} ${s.unit}`;
        } else {
          el.textContent = s.unit;
        }
      });
    });
  }

  function loadReviews(reviews) {
    // Hide review sections if no reviews yet
    if (!reviews || !reviews.length) {
      document.querySelectorAll('[data-reviews]').forEach(container => {
        const section = container.closest('section');
        if (section) section.style.display = 'none';
      });
      return;
    }
    
    // Find all review containers
    document.querySelectorAll('[data-reviews]').forEach(container => {
      const filter = container.dataset.reviews; // "all", city slug, or service slug
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
            <span class="text-primary/40 text-xs font-mono">${cityNames[r.city] || r.city}</span>
          </div>
        </div>
      `).join('');
    });
  }

  function loadProjects(projects) {
    if (!projects || !projects.length) {
      // Hide empty dynamic project containers
      document.querySelectorAll('[data-projects]').forEach(c => c.style.display = 'none');
      return;
    }
    
    // Find all project containers
    document.querySelectorAll('[data-projects]').forEach(container => {
      const filter = container.dataset.projects;
      const limit = parseInt(container.dataset.projectsLimit) || 4;
      
      let filtered = projects;
      if (filter !== 'all') {
        filtered = projects.filter(p => p.city === filter || p.service === filter);
      }
      filtered = filtered.slice(0, limit);
      
      if (!filtered.length) return;
      
      container.innerHTML = filtered.map(p => `
        <div class="rounded-2xl overflow-hidden border border-primary/5">
          <div class="relative h-[200px] md:h-[300px] ba-container">
            <div class="ba-slider" style="position:relative;width:100%;height:100%;overflow:hidden;">
              <img src="${p.imageAfter}" class="ba-after" alt="Po" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;">
              <img src="${p.imageBefore}" class="ba-before grayscale brightness-75 contrast-125" alt="Przed" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;clip-path:polygon(0 0,50% 0,50% 100%,0 100%);z-index:2;">
              <div class="ba-handle" style="position:absolute;top:0;bottom:0;left:50%;width:2px;background:#F06820;z-index:3;transform:translateX(-50%);cursor:ew-resize;">
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:36px;height:36px;background:#F06820;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;box-shadow:0 4px 12px rgba(240,104,32,0.3);">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18-6-6 6-6"/><path d="m15 18 6-6-6-6"/></svg>
                </div>
              </div>
            </div>
          </div>
          <div class="p-3 bg-white flex justify-between items-center">
            <span class="font-medium text-sm">${serviceNames[p.service] || p.service}</span>
            <span class="text-primary/40 text-xs font-mono">${cityNames[p.city] || p.city}${p.district ? ', ' + p.district : ''}</span>
          </div>
        </div>
      `).join('');
      
      // Init sliders for dynamically loaded projects
      initDynamicSliders(container);
    });
  }
  
  function initDynamicSliders(container) {
    container.querySelectorAll('.ba-container').forEach(c => {
      const slider = c.querySelector('.ba-slider');
      const before = slider.querySelector('.ba-before');
      const handle = slider.querySelector('.ba-handle');
      if (!handle) return;
      let dragging = false;
      
      const move = (e) => {
        if (!dragging) return;
        e.preventDefault();
        const rect = slider.getBoundingClientRect();
        let x = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
        x = Math.max(0, Math.min(x, rect.width));
        const pct = (x / rect.width) * 100;
        before.style.clipPath = `polygon(0 0, ${pct}% 0, ${pct}% 100%, 0 100%)`;
        handle.style.left = pct + '%';
      };
      
      handle.addEventListener('mousedown', () => dragging = true);
      window.addEventListener('mouseup', () => dragging = false);
      window.addEventListener('mousemove', move);
      handle.addEventListener('touchstart', () => dragging = true, {passive: true});
      window.addEventListener('touchend', () => dragging = false);
      window.addEventListener('touchmove', move, {passive: false});
    });
  }

  const cityNames = {
    'gdansk': 'Gdańsk', 'gdynia': 'Gdynia', 'sopot': 'Sopot',
    'wejherowo': 'Wejherowo', 'rumia': 'Rumia', 'reda': 'Reda',
    'pruszcz-gdanski': 'Pruszcz Gdański', 'tczew': 'Tczew', 'starogard-gdanski': 'Starogard Gdański',
    'kartuzy': 'Kartuzy', 'zukowo': 'Żukowo', 'koscierzyna': 'Kościerzyna',
    'goreczyno': 'Goręczyno', 'lebork': 'Lębork', 'bytow': 'Bytów'
  };
  
  const serviceNames = {
    'mycie-elewacji': 'Mycie elewacji', 'mycie-dachu': 'Mycie dachu',
    'malowanie-elewacji': 'Malowanie elewacji', 'malowanie-dachu': 'Malowanie dachu', 'impregnacja': 'Impregnacja'
  };
})();
