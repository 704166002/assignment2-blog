# Deployment Process and Version Control

## Framework Choice
I selected **Sphinx** equipped with **MyST-Parser**. This combination provides robust static site generation while natively supporting Markdown and complex LaTeX equations (e.g., $$\nabla \cdot \mathbf{v} = 0$$), which aligns perfectly with academic needs.

## Git Strategy
Version control is strictly maintained with atomic, logical commits covering environment setup, configuration, content integration, and CI/CD pipelines.

## Deployment
The site is hosted on **GitHub Pages**. I configured a custom **GitHub Actions** workflow (`deploy.yml`) that automatically compiles the Sphinx documentation and deploys the generated HTML upon every push to the main branch.
