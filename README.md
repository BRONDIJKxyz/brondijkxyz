# brondijk.xyz

A minimalist, code-centric website showcasing technical projects.

## Project Purpose

This is a static website built to showcase technical projects in a minimalist, dark-themed layout. The site is designed to be simple, fast, and focused on the projects themselves without unnecessary design elements or personal content.

## How to Run/View the Project

### Local Development

1. Clone the repository:
   ```
   git clone <repository-url>
   cd brondijkxyz
   ```

2. Open the `index.html` file in your browser:
   ```
   open index.html
   ```

Alternatively, you can use a simple HTTP server:

```bash
# Using Python 3
python3 -m http.server

# The site will be available at http://localhost:8000
```

### Deployment

The site is designed to be deployed as static files to any web hosting service.

## Directory Structure

- `index.html` - Main page with project listings
- `css/` - Stylesheets
  - `styles.css` - Main stylesheet for colors and typography
  - `layout.css` - Layout-specific styles
- `js/` - JavaScript files
  - `main.js` - Minimal JavaScript for basic functionality
- `CHANGELOG.md` - Documents changes to the project list

## Design Principles

- Dark background with light text for a code-editor feel
- Monospaced font for a technical aesthetic
- Minimal design focusing only on project information
- Single accent color (cyan) for links and headings
- No images, only text and links

## Maintenance

- All changes to the project list should be documented in `CHANGELOG.md`
- Regularly check for dead links or outdated project descriptions
- Maintain the minimalist aesthetic when adding new projects

## License

MIT License
