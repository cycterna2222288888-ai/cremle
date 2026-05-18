import glob

def process_file(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    if "quotes" in f:
        content = content.replace(".qc-text { font-size: 15px !important;", ".quote-text { font-size: 18px !important;")
        content = content.replace(".qc-year { font-size: 20px !important;", ".qc-date { font-size: 14px !important;")
        content = content.replace(".fq-text { font-size: 20px !important; }", ".fq-text { font-size: 20px !important; line-height: 1.5 !important; }")

    if "sanctions" in f:
        if "@media (max-width: 480px) {" in content and ".stat-card" not in content.split("@media (max-width: 480px) {")[1][:500]:
            stat_fixes = "    .stat-card { padding: 24px 16px !important; }\n    .stat-val { font-size: 32px !important; }\n"
            content = content.replace("@media (max-width: 480px) {\n", "@media (max-width: 480px) {\n" + stat_fixes, 1)

    if "media-empire" in f:
        if "@media (max-width: 480px) {" in content and ".funding-flow" not in content.split("@media (max-width: 480px) {")[1][:500]:
            empire_fixes = """    .funding-flow { grid-template-columns: 1fr !important; }
    .hier-row { grid-template-columns: 1fr !important; gap: 12px !important; }
    .hierarchy { padding: 24px 16px !important; }
    .flow-card { padding: 24px !important; }
"""
            content = content.replace("@media (max-width: 480px) {\n", "@media (max-width: 480px) {\n" + empire_fixes, 1)

    if "glossary" in f:
        if "@media (max-width: 480px) {" in content and ".term-entry {" not in content.split("@media (max-width: 480px) {")[1][:500]:
            glossary_fixes = "    .term-entry { padding: 24px 20px !important; gap: 12px !important; }\n"
            content = content.replace("@media (max-width: 480px) {\n", "@media (max-width: 480px) {\n" + glossary_fixes, 1)

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

for f in glob.glob("*.html"):
    if any(x in f for x in ["quotes", "sanctions", "media-empire", "glossary"]):
        process_file(f)
