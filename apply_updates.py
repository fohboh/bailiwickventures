from pathlib import Path
import shutil, sys

root = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
source = Path(__file__).resolve().parent
footer_link = '<a href="/downloads/bailiwick-ventures-overview.pdf" target="_blank" rel="noopener">Bailiwick Overview (PDF)</a>'
about_block = '''
<section class="bord on-warm" id="bailiwick-overview">
  <div class="shell">
    <p class="eyebrow">Bailiwick overview</p>
    <h2>How the venture model works</h2>
    <p class="lede" style="margin-top:20px">See how Bailiwick Ventures connects venture architecture, production engineering, and project-specific capital.</p>
    <a class="btn btn-p" style="margin-top:24px" href="/downloads/bailiwick-ventures-overview.pdf" target="_blank" rel="noopener">Download the Bailiwick Overview (PDF)</a>
  </div>
</section>
'''
investor_block = '''
    <div id="investment-perspective" style="margin-top:32px;margin-bottom:40px">
      <p class="eyebrow">Public investment perspective</p>
      <h3>Featuring FohBoh.ai</h3>
      <p class="body" style="margin-top:16px">Bailiwick Ventures invites prospective investors to discuss participation in FohBoh.ai's Stage 5 Seed round, supporting commercialization and go-to-market execution following MVP completion.</p>
      <a class="btn btn-p" style="margin-top:20px" href="/downloads/bailiwick-investment-perspective-fohboh.pdf" target="_blank" rel="noopener">Investment Perspective — Featuring FohBoh.ai (PDF)</a>
    </div>
'''
changed=[]
for path in root.rglob('*.html'):
    if any(p in {'.git','node_modules','website-update'} for p in path.relative_to(root).parts): continue
    text=path.read_text()
    before=text
    if '<footer' in text and footer_link not in text:
        start=text.index('<footer')
        head,foot=text[:start],text[start:]
        target='<a href="investing.html#investors">For Investors</a>'
        if target in foot: foot=foot.replace(target,footer_link+'\n        '+target,1)
        text=head+foot
    if path.name=='about.html' and 'id="bailiwick-overview"' not in text:
        text=text.replace('</main>',about_block+'\n</main>',1)
    if path.name=='investing.html' and 'id="investment-perspective"' not in text:
        anchor='<section class="bord on-warm" id="investors">'
        if anchor not in text: raise SystemExit('Investor section changed; review before applying.')
        start=text.index(anchor)
        pos=text.index('<div class="grid g2">',start)
        text=text[:pos]+investor_block+'\n    '+text[pos:]
        text=text.replace('We do not send materials on request. We have a conversation first.','Company diligence begins with a conversation.')
        text=text.replace('A short call is the only way either side can judge fit — and it means we know who we are dealing with before anything is shared.','The public overview above introduces our approach. A short call helps both sides judge fit before company-specific diligence and offering materials are shared.')
    if text!=before:
        path.write_text(text)
        changed.append(str(path.relative_to(root)))
(root/'downloads').mkdir(exist_ok=True)
for pdf in (source/'downloads').glob('*.pdf'):
    dest=root/'downloads'/pdf.name
    if pdf.resolve()!=dest.resolve(): shutil.copy2(pdf,dest)
print('Updated '+str(len(changed))+' pages: '+', '.join(changed))
