import os
import markdown
import yaml
from datetime import datetime
import shutil
from pathlib import Path

def read_md_with_frontmatter(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read().split('---')
        if len(content) >= 3:
            frontmatter = yaml.safe_load(content[1])
            md_content = '---'.join(content[2:])
            return frontmatter, md_content
        return {}, content[0]

def generate_blog_html():
    posts_dir = Path('blog/posts')
    blog_template_path = 'blog.html'
    posts = []

    # Read all markdown files
    for md_file in posts_dir.glob('*.md'):
        frontmatter, content = read_md_with_frontmatter(md_file)
        html_content = markdown.markdown(content)
        
        post_data = {
            'title': frontmatter.get('title', md_file.stem),
            'date': frontmatter.get('date', datetime.fromtimestamp(md_file.stat().st_mtime).strftime('%Y-%m-%d')),
            'content': html_content,
            'slug': md_file.stem
        }
        posts.append(post_data)

    # Sort posts by date
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Generate blog listing
    posts_html = ''
    for post in posts:
        posts_html += f'''
        <article class="blog-post">
            <h2>{post['title']}</h2>
            <div class="post-meta">{post['date']}</div>
            <div class="post-content">{post['content']}</div>
        </article>
        <hr class="section-divider">
        '''

    # Update blog.html
    with open(blog_template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    updated_content = template.replace(
        '<!-- Blog posts will be dynamically inserted here -->',
        posts_html
    )

    with open(blog_template_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == '__main__':
    generate_blog_html()
