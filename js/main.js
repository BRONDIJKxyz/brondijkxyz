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
