## 🔐 Secrets Management
- Store secrets (API keys, DB credentials) in `.env` files  
- NEVER expose secrets to client-side code  
- Add `.env` and other sensitive files to `.gitignore`

## 📝 Documentation
- Always use Markdown for documentation and `README.md` files  
- Each project must include a `README.md` with:
  - Title  
  - Description  
  - Setup instructions  
  - Usage examples  
  - License information  

## 🧭 Project Planning
- Every project must begin with an `instructions.md` file  
- This file should describe:
  - The end goal and success criteria  
  - Scope and key features  
  - Tech stack decisions  
- It must be written before any code is committed  

## 🧪 Local Testing
- Kill any running local servers before starting a new one  
- Always run Python-related tests using Python 3 (`python3`)

## 🪓 File Size & Modularity
- Avoid single files exceeding 500 lines unless justified (e.g., auto-generated code)
- For styles: split large `styles.css` files into domain-based or component-based partials
  - Use `@import` or PostCSS includes to compose them
  - Example: `layout.css`, `buttons.css`, `modals.css`
- For JS/TS: split functions and classes into separate modules or services when possible
- For Markdown: split long documentation into logical subpages (e.g., `usage.md`, `api.md`)
- Use folder-based organization with an index file for clean exports (e.g., `index.ts`)
