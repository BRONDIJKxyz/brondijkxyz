import os
import markdown
import yaml
from datetime import datetime
from pathlib import Path
import shutil

def read_md_with_frontmatter(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read().split('---')
        if len(content) >= 3:
            frontmatter = yaml.safe_load(content[1])
            md_content = '---'.join(content[2:])
            return frontmatter, md_content
        return {}, content[0]

def get_first_paragraph(content):
    paragraphs = content.split('\n\n')
    for p in paragraphs:
        if p.strip() and not p.startswith('#'):
            return p.strip()
    return ""

def get_post_template():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - brondijk.xyz</title>
    <meta name="description" content="{description}">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-56LC4J0MT0"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-56LC4J0MT0');
    </script>
    
    <link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
    
    <!-- Favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="../assets/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../assets/favicon/favicon-16x16.png">
    <link rel="manifest" href="../assets/favicon/site.webmanifest">
    <link rel="shortcut icon" href="../assets/favicon/favicon.ico">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="../index.html" style="text-decoration: none; color: inherit;">brondijk.xyz</a></h1>
            <nav>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../blog.html">Blog</a></li>
                    <li><a href="../index.html#projects">Projects</a></li>
                    <li><a href="../index.html#resources">Resources</a></li>
                    <li><a href="https://github.com/brondijkxyz" target="_blank" rel="noopener noreferrer">GitHub</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container">
        <article class="blog-post">
            <h1 class="post-title">{title}</h1>
            <div class="post-meta">{date}</div>
            <div class="post-content">
                {content}
            </div>
            <div class="post-nav">
                <a href="../blog.html">← Back to Blog</a>
            </div>
        </article>
    </main>

    <footer class="container">
        <p>&copy; 2025 Maarten Brondijk</p>
    </footer>
</body>
</html>'''

def generate_blog_html():
    posts_dir = Path('blog/posts')
    blog_dir = Path('blog')
    blog_dir.mkdir(exist_ok=True)
    posts = []

    # Read all markdown files and generate individual posts
    for md_file in posts_dir.glob('*.md'):
        frontmatter, content = read_md_with_frontmatter(md_file)
        html_content = markdown.markdown(content)
        first_para = get_first_paragraph(content)
        
        post_data = {
            'title': frontmatter.get('title', md_file.stem),
            'date': frontmatter.get('date', datetime.fromtimestamp(md_file.stat().st_mtime).strftime('%Y-%m-%d')),
            'content': html_content,
            'slug': md_file.stem,
            'description': first_para[:160] if first_para else ""
        }
        posts.append(post_data)
        
        # Generate individual post HTML
        post_html = get_post_template().format(**post_data)
        post_path = blog_dir / f"{post_data['slug']}.html"
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(post_html)

    # Sort posts by date
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Generate blog index
    index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - brondijk.xyz</title>
    <meta name="description" content="Blog posts by Maarten Brondijk">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-56LC4J0MT0"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-56LC4J0MT0');
    </script>
    
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap">
    
    <!-- Favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="assets/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon/favicon-16x16.png">
    <link rel="manifest" href="assets/favicon/site.webmanifest">
    <link rel="shortcut icon" href="assets/favicon/favicon.ico">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="index.html" style="text-decoration: none; color: inherit;">brondijk.xyz</a></h1>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="blog.html" class="active">Blog</a></li>
                    <li><a href="index.html#projects">Projects</a></li>
                    <li><a href="index.html#resources">Resources</a></li>
                    <li><a href="https://github.com/brondijkxyz" target="_blank" rel="noopener noreferrer">GitHub</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container">
        <h1 class="page-title">Blog</h1>
        <section id="blog-posts">'''

    for post in posts:
        index_html += f'''
            <article class="blog-post-preview">
                <h2><a href="blog/{post['slug']}.html">{post['title']}</a></h2>
                <div class="post-meta">{post['date']}</div>
                <div class="post-excerpt">{post['description']}</div>
                <a href="blog/{post['slug']}.html" class="read-more">Read more →</a>
            </article>
            <hr class="section-divider">'''

    index_html += '''
        </section>
    </main>

    <footer class="container">
        <p>&copy; 2025 Maarten Brondijk</p>
    </footer>
</body>
</html>'''

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

if __name__ == '__main__':
    generate_blog_html()
