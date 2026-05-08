import glob
import re

for file in glob.glob('/Users/nomura/antigravity/TK/カウンセラー/LP0*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the wrongly inserted top bonus section
    content = re.sub(
        r'<!-- ===== BONUSES ===== -->\n<section class="section-wide" style="background:linear-gradient\(180deg, #fafaf9, #ffffff\); padding:80px 20px;">.*?</section>\n\n<!-- ===== CTA: UTAGE FORM ===== -->',
        r'<!-- ===== CTA: UTAGE FORM ===== -->',
        content,
        flags=re.DOTALL
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned up top bonuses in {file}")
