'use strict';
(() => {
  const grid = document.querySelector('#activity-grid');
  const months = document.querySelector('#activity-months');
  const total = document.querySelector('#activity-total');
  const controls = document.querySelectorAll('[data-period]');
  let days = [], period = 365;
  function draw() {
    const end = new Date(); end.setUTCHours(0, 0, 0, 0);
    const start = new Date(end); start.setUTCDate(start.getUTCDate() - period + 1);
    const visible = days.filter(day => day.time >= start && day.time <= end);
    if (!visible.length) {
      total.textContent = 'No activity data available for this period.';
      grid.replaceChildren(); months.replaceChildren();
      grid.setAttribute('aria-label', 'No contribution data available');
      return;
    }
    const count = visible.reduce((sum, day) => sum + day.count, 0);
    const summary = `${count.toLocaleString()} contributions · ${period === 365 ? 'last year' : 'last 6 months'}`;
    total.textContent = summary;
    grid.setAttribute('aria-label', summary);
    const cells = Array(visible[0].time.getUTCDay()).fill(null).concat(visible);
    const columns = Math.ceil(cells.length / 7);
    grid.style.setProperty('--columns', columns); months.style.setProperty('--columns', columns);
    grid.replaceChildren(...cells.map(day => {
      const cell = document.createElement('span');
      cell.className = day ? `activity-cell level-${day.level}` : 'activity-cell empty';
      if (day) cell.title = `${day.date}: ${day.count} contributions`;
      return cell;
    }));
    let lastMonth = -1;
    months.replaceChildren(...Array.from({length: columns}, (_, column) => {
      const label = document.createElement('span');
      const day = cells.slice(column * 7, column * 7 + 7).find(Boolean);
      if (day && day.time.getUTCMonth() !== lastMonth) {
        label.textContent = day.time.toLocaleDateString('en', {month: 'short', timeZone: 'UTC'});
        lastMonth = day.time.getUTCMonth();
      }
      return label;
    }));
  }
  controls.forEach(button => button.addEventListener('click', () => {
    period = Number(button.dataset.period);
    controls.forEach(control => control.setAttribute('aria-pressed', String(control === button)));
    if (days.length) draw();
  }));
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12000);
  fetch('https://github-contributions-api.jogruber.de/v4/brondijkxyz?y=last', {signal: controller.signal})
    .then(response => { if (!response.ok) throw new Error('Activity request failed'); return response.json(); })
    .then(data => {
      if (!Array.isArray(data.contributions)) throw new Error('Invalid activity data');
      days = data.contributions.filter(day => /^\d{4}-\d{2}-\d{2}$/.test(day.date) && Number.isFinite(day.count) && day.count >= 0)
        .map(day => ({...day, time: new Date(`${day.date}T00:00:00Z`), level: Math.min(4, Math.max(0, Math.round(Number(day.level) || 0)))}))
        .sort((a, b) => a.time - b.time);
      draw();
    })
    .catch(() => { total.textContent = 'Activity is unavailable right now. View it on GitHub ↗'; grid.setAttribute('aria-label', 'GitHub activity unavailable'); })
    .finally(() => clearTimeout(timeout));
})();
