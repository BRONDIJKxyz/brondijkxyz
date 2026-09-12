'use strict';
const root = document.documentElement;
const themeButton = document.querySelector('.theme');
function updateThemeLabel() {
  const label = root.dataset.theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
  themeButton.setAttribute('aria-label', label);
  themeButton.title = label;
}
updateThemeLabel();
themeButton.addEventListener('click', () => {
  const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  root.dataset.theme = theme;
  try { localStorage.setItem('trial-theme', theme); } catch (_) { /* Optional preference storage. */ }
  updateThemeLabel();
});
document.querySelector('#year').textContent = new Date().getFullYear();
const filters = document.querySelectorAll('.filter');
const projects = document.querySelectorAll('.project');
const featured = document.querySelector('.feature');
filters.forEach(button => button.addEventListener('click', () => {
  const category = button.dataset.filter;
  filters.forEach(filter => {
    const selected = filter === button;
    filter.classList.toggle('active', selected);
    filter.setAttribute('aria-pressed', String(selected));
  });
  featured.hidden = category === 'daily';
  let count = featured.hidden ? 0 : 1;
  projects.forEach(project => {
    project.hidden = category !== 'all' && project.dataset.category !== category;
    if (!project.hidden) count++;
  });
  document.querySelector('#result-count').textContent = `${count} projects`;
}));
const details = {
  stock: {
    title: 'Stock Dashboard · JJ',
    description: 'An operational stock dashboard for a nutrition brand. It tracks 51 SKUs across EU and US markets, flags safety-stock and critical-stock issues, and projects out-of-stock dates from the subscription queue. A Python pipeline turns Google Sheets master data into a fast static dashboard with reorder logic.',
    tags: ['Python', 'Google Sheets', 'EU + US', '51 SKUs']
  },
  insights: {
    title: 'Master Insights',
    description: 'A revenue dashboard that brings month-to-date performance and target pacing together. It aggregates Shopify and Recharge sales across international and US channels, converts USD into EUR, and compares the daily revenue curve with last year.',
    tags: ['Revenue pacing', 'Multi-channel', 'EUR + USD', 'Subscriptions']
  },
  orders: {
    title: 'Order Visualizer',
    description: 'A 3D globe showing orders shipped from Amsterdam to destinations around the world. Built with Mapbox GL and great-circle arcs generated from anonymised order geodata. Only city and postal code are used, with no personal data.',
    tags: ['Mapbox GL', '3D globe', 'Anonymised data', '2025 orders']
  }
};
const dialog = document.querySelector('#project-dialog');
let opener;
document.querySelectorAll('[data-detail]').forEach(button => button.addEventListener('click', () => {
  const detail = details[button.dataset.detail];
  opener = button;
  document.querySelector('#dialog-title').textContent = detail.title;
  document.querySelector('#dialog-description').textContent = detail.description;
  document.querySelector('#dialog-tags').replaceChildren(...detail.tags.map(tag => {
    const element = document.createElement('span');
    element.textContent = tag;
    return element;
  }));
  dialog.showModal();
}));
document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  const bounds = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
});
dialog.addEventListener('close', () => opener?.focus());
