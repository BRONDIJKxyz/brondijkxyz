// Apply saved theme as early as possible (default light, remembers choice)
(function () {
    try {
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark');
        }
    } catch (e) {}
    document.documentElement.classList.remove('pre-dark');
})();

// Set current year in footer
document.addEventListener('DOMContentLoaded', () => {
    // Update copyright year
    const currentYearElement = document.getElementById('current-year');
    if (currentYearElement) {
        currentYearElement.textContent = new Date().getFullYear();
    }

    // Dark-mode toggle: show the icon of the mode you'll switch TO
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        const moon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
        const sun = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
        const render = () => {
            const isDark = document.body.classList.contains('dark');
            themeToggle.innerHTML = isDark ? sun : moon;
            const label = isDark ? 'Switch to light mode' : 'Switch to dark mode';
            themeToggle.setAttribute('aria-label', label);
            themeToggle.setAttribute('title', label);
        };
        render();
        themeToggle.addEventListener('click', () => {
            const isDark = document.body.classList.toggle('dark');
            try { localStorage.setItem('theme', isDark ? 'dark' : 'light'); } catch (e) {}
            render();
        });
    }

    // Hide a card's placeholder tile once its screenshot actually loads
    // (the .ph is absolutely positioned, so without this it paints over the image)
    document.querySelectorAll('.shot img').forEach(img => {
        const reveal = () => img.closest('.shot')?.classList.add('has-shot');
        if (img.complete && img.naturalWidth > 0) reveal();
        else img.addEventListener('load', reveal);
    });

    // GitHub contribution heatmap — last 6 months, month labels + hover tooltip (front page only)
    const contribGraph = document.getElementById('contrib-graph');
    if (contribGraph) {
        const totalEl = document.getElementById('contrib-total');
        const monthsEl = document.getElementById('contrib-months');
        const tip = document.getElementById('contrib-tip');
        const card = contribGraph.closest('.contrib');
        const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        fetch('https://github-contributions-api.jogruber.de/v4/brondijkxyz?y=last')
            .then(r => r.ok ? r.json() : Promise.reject(r.status))
            .then(data => {
                const cutoff = new Date(); cutoff.setUTCHours(0, 0, 0, 0);
                cutoff.setUTCDate(cutoff.getUTCDate() - 183); // ~last 6 months
                const days = (data.contributions || []).filter(d => new Date(d.date + 'T00:00:00Z') >= cutoff);
                const sum = days.reduce((s, d) => s + d.count, 0);
                if (totalEl) totalEl.textContent = sum.toLocaleString() + ' contributions · last 6 months';

                // column-major cells, padded so weekday rows line up (row 0 = Sunday)
                const cells = [];
                if (days.length) {
                    const dow = new Date(days[0].date + 'T00:00:00Z').getUTCDay();
                    for (let i = 0; i < dow; i++) cells.push(null);
                }
                days.forEach(d => cells.push(d));
                const numCols = Math.ceil(cells.length / 7);
                contribGraph.style.setProperty('--cols', numCols);   // drives the fill grid
                if (monthsEl) monthsEl.style.setProperty('--cols', numCols);

                const gfrag = document.createDocumentFragment();
                cells.forEach(d => {
                    const c = document.createElement('span');
                    if (!d) { c.className = 'contrib-cell pad'; }
                    else {
                        c.className = 'contrib-cell l' + (d.level || 0);
                        const nice = new Date(d.date + 'T00:00:00Z').toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
                        c.dataset.tip = d.count + (d.count === 1 ? ' contribution' : ' contributions') + ' · ' + nice;
                    }
                    gfrag.appendChild(c);
                });
                contribGraph.replaceChildren(gfrag);

                // month labels above the columns where a new month begins
                if (monthsEl) {
                    const mfrag = document.createDocumentFragment();
                    let lastMonth = -1;
                    for (let col = 0; col < numCols; col++) {
                        const span = document.createElement('span');
                        const colDay = cells.slice(col * 7, col * 7 + 7).find(Boolean);
                        if (colDay) {
                            const m = new Date(colDay.date + 'T00:00:00Z').getUTCMonth();
                            if (m !== lastMonth) { span.textContent = MON[m]; lastMonth = m; }
                        }
                        mfrag.appendChild(span);
                    }
                    monthsEl.replaceChildren(mfrag);
                }

                // GitHub-style hover tooltip — works fine even though the card is a link
                if (tip && card) {
                    contribGraph.addEventListener('mouseover', e => {
                        const cell = e.target.closest('.contrib-cell');
                        if (!cell || !cell.dataset.tip) { tip.classList.remove('show'); return; }
                        tip.textContent = cell.dataset.tip;
                        const cr = cell.getBoundingClientRect(), pr = card.getBoundingClientRect();
                        tip.style.left = (cr.left - pr.left + cr.width / 2) + 'px';
                        tip.style.top = (cr.top - pr.top) + 'px';
                        tip.classList.add('show');
                    });
                    contribGraph.addEventListener('mouseout', () => tip.classList.remove('show'));
                }
            })
            .catch(() => { if (totalEl) totalEl.textContent = 'GitHub activity unavailable right now.'; });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Offset for header
                    behavior: 'smooth'
                });
            }
        });
    });
});
