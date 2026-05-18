import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix mobile sizes and grey void for nav-pages
# 1. Remove background: var(--rule) from .nav-pages
content = content.replace("background: var(--rule);", "/* background: var(--rule); */")

# 2. Add border to nav-page-link instead
content = re.sub(r"(\.nav-page-link\s*{[^}]*)", r"\1 border-right: 1px solid var(--rule); ", content)

# 3. Fix 36 character blocks padding on mobile
mobile_fixes = """
  @media (max-width: 768px) {
    .card-top { padding: 24px 20px 0; }
    .card-quote { padding: 0 20px; }
    .card-bottom { padding: 20px; }
    .nav-pages { background: transparent !important; }
  }
"""
content = content.replace("</style>", mobile_fixes + "\n</style>", 1)

# 4. Remove the font-size: 1rem that breaks card-name
content = content.replace(".card-name { font-size: 1rem; }", "/* .card-name { font-size: 1rem; } */")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("index-en.html", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("background: var(--rule);", "/* background: var(--rule); */")
content = re.sub(r"(\.nav-page-link\s*{[^}]*)", r"\1 border-right: 1px solid var(--rule); ", content)
content = content.replace("</style>", mobile_fixes + "\n</style>", 1)
content = content.replace(".card-name { font-size: 1rem; }", "/* .card-name { font-size: 1rem; } */")
with open("index-en.html", "w", encoding="utf-8") as f:
    f.write(content)
