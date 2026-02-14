#!/usr/bin/env python3
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
html_files = list(root.rglob('*.html'))

pattern = re.compile(r'<h2\b([^>]*)>', flags=re.IGNORECASE)
class_attr_re = re.compile(r'class\s*=\s*"([^"]*)"', flags=re.IGNORECASE)

updated_files = []
for fp in html_files:
    text = fp.read_text(encoding='utf-8')
    def repl(m):
        attrs = m.group(1)
        ca = class_attr_re.search(attrs)
        if ca:
            classes = ca.group(1)
            if 'head-title' in classes.split():
                return m.group(0)
            new_classes = 'head-title ' + classes
            new_attrs = class_attr_re.sub(f'class="{new_classes}"', attrs, count=1)
            return f'<h2{new_attrs}>'
        else:
            return f'<h2 class="head-title"{attrs}>'

    new_text, n = pattern.subn(repl, text)
    if n > 0 and new_text != text:
        fp.write_text(new_text, encoding='utf-8')
        updated_files.append(str(fp.relative_to(root)))

print('Updated files:', len(updated_files))
for f in updated_files:
    print('-', f)
