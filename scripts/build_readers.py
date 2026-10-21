"""Rebuild the teaching readers from Markdown using Pandoc (no runtime CDN).

Run from the repository root: python3 scripts/build_readers.py
Install Pandoc first. Generated readers retain all source text and headings.
"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
nav = '<nav aria-label="Main navigation"><a href="./">How to do it</a><a href="learning-path.html">Learning path</a><a href="workbook.html">Workbook</a><a href="continuing-practice.html">Further practice</a><a href="https://titanicparker.github.io/everything-fresh/">Everything Fresh</a><a href="white-paper.html">White paper</a><a href="https://titanicparker.github.io/">Project Museum</a></nav>'
footer = '<footer><a href="learning-path.html">Follow the learning path</a> · <a href="https://titanicparker.github.io/everything-fresh/">Everything Fresh research</a> · <a href="https://github.com/TitanicParker/how-to-do-it">Source repository</a></footer>'
for source, target, title in [
    ('Centre_Finding_Workbook.md', 'workbook.html', 'Finding the Operative Centre'),
    ('Learning_Path.md', 'learning-path.html', 'From Centre finding to resolution'),
    ('Continuing_Centre_Practice.md', 'continuing-practice.html', 'Further Centre practice'),
    ('operative-centre-white-paper.md', 'white-paper.html', 'The Study of Completed Intelligibility'),
]:
    html = subprocess.check_output(['pandoc', str(root/source), '--from=gfm', '--to=html5', '--standalone', '--toc', '--toc-depth=2', '--metadata', 'title='+title, '--metadata', 'lang=en', '--css', 'style.css'], text=True)
    html = html.replace('<body>', '<body><div class="reader">'+nav).replace('</body>', footer+'</div></body>')
    (root/target).write_text(html)
print('Built four source-based readers.')
