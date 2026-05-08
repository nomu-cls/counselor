import glob
import re

new_hero_css = """.hero { position:relative; background:url('img/image1.jpg') center/cover; padding:60px 20px 50px; text-align:center; color:var(--white); z-index:1; }
.hero::before { content:''; position:absolute; top:0; left:0; width:100%; height:100%; background:linear-gradient(135deg, rgba(30,41,59,0.96) 0%, rgba(15,23,42,0.9) 100%); z-index:-1; }
.hero-inner { position:relative; z-index:1; max-width:600px; margin:0 auto; }
.hero-pretitle { display:inline-block; font-size:11px; font-weight:700; letter-spacing:3px; margin-bottom:24px; color:var(--accent); border:1px solid var(--accent); padding:4px 12px; border-radius:30px; }
.hero-pain { font-size:16px; line-height:2.0; color:var(--white); margin-bottom:0px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12); padding:24px 16px; border-radius:12px; backdrop-filter:blur(4px); }
.hero-pain strong { color:#fff; font-weight:800; font-size:20px; background:linear-gradient(transparent 60%, rgba(202,152,81,0.7) 60%); padding:0 6px; display:inline-block; margin:2px 0; }
.hero-pain-em { display:block; font-size:13px; color:rgba(255,255,255,0.6); margin-top:24px; margin-bottom:12px; }
.hero-turn { font-size:18px; color:var(--accent-light); margin:32px 0 16px; font-weight:700; letter-spacing:1px; }
.hero-question { font-size:15px; color:rgba(255,255,255,0.7); line-height:2; margin-bottom:8px; }
.hero-question-main { font-size:24px; color:var(--white); font-weight:800; line-height:1.7; margin:16px 0 12px; padding-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.1); }
.hero-question-sub { font-size:14px; color:rgba(255,255,255,0.5); line-height:1.9; margin-bottom:32px; }
.hero-bridge { font-size:15px; line-height:2.2; color:rgba(255,255,255,0.85); background:radial-gradient(ellipse at center, rgba(202,152,81,0.08) 0%, transparent 70%); padding:20px 0; margin-bottom:40px; }
.hero-title-block { background:rgba(15,23,42,0.6); border:1px solid rgba(202,152,81,0.4); box-shadow:0 0 40px rgba(202,152,81,0.15), inset 0 0 20px rgba(255,255,255,0.03); border-radius:16px; padding:48px 16px; margin:0 0 28px; }
.hero-catch { display:inline-block; font-size:13px; color:var(--primary); background:var(--accent-light); padding:6px 14px; border-radius:4px; font-weight:800; margin-bottom:24px; letter-spacing:1px; }
.hero-title { font-size:clamp(36px, 8vw, 48px); font-weight:900; color:var(--white); letter-spacing:1px; line-height:1.3; margin-bottom:16px; }
.hero-subtitle { font-size:clamp(16px, 5vw, 24px); color:var(--accent); font-weight:800; letter-spacing:2px; margin-bottom:32px; }
.hero-offer { display:inline-block; background:linear-gradient(135deg, var(--accent), var(--accent-light)); color:var(--primary); font-size:16px; font-weight:900; padding:18px 40px; border-radius:50px; letter-spacing:1px; box-shadow:0 8px 30px rgba(202,152,81,0.3); transition:transform 0.3s; }
/* ===== CTA ===== */"""

files = glob.glob('/Users/nomura/antigravity/TK/カウンセラー/LP0*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex replace the hero CSS section
    content = re.sub(r'\.hero \{.*?/\* ===== CTA ===== \*/', new_hero_css, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated Hero CSS in {file}")

