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

### HTTPS Setup for Production

For production deployment, it's important to serve the site over HTTPS to avoid the "Not Secure" warning in browsers:

1. If using a hosting service like Netlify, Vercel, or GitHub Pages, HTTPS is typically provided automatically
2. For custom hosting:
   - Obtain an SSL certificate (Let's Encrypt offers free certificates)
   - Configure your web server (Apache, Nginx, etc.) to use the certificate
   - Set up automatic redirects from HTTP to HTTPS

Note: The "Not Secure" warning is normal when testing locally with `http://localhost` and doesn't require fixing in the development environment.

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
