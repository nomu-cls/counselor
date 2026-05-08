import glob

old_section_title = """.section-title {
  font-size: 24px;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 24px;
  line-height: 1.4;
}"""

new_section_title = """.section-title {
  font-size: clamp(26px, 7vw, 32px);
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 36px;
  line-height: 1.4;
  position: relative;
  display: block;
  padding-bottom: 16px;
}
.section-title::after {
  content: '';
  position: absolute;
  bottom: 0px; left: 50%;
  transform: translateX(-50%);
  width: 48px; height: 3px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  border-radius: 2px;
}
.misconception-bg .section-title::after {
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
}
.hero-title {
  text-shadow: 0 4px 24px rgba(0,0,0,0.4);
}"""

old_skill_css = """.skill-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; }
.skill-card {
  background:var(--white); border-radius:16px; padding:32px 24px;
  text-align:center; box-shadow:0 4px 20px rgba(0,0,0,0.04);
  position:relative; overflow:hidden; border:1px solid rgba(200,164,92,0.15);
  transition:transform 0.3s;
}
.skill-card:hover { transform:translateY(-4px); }
.skill-number {
  display:inline-block; font-size:12px; font-weight:700; color:var(--accent);
  letter-spacing:2px; margin-bottom:12px;
}
.skill-icon { width:72px; height:72px; margin:0 auto 16px; }
.skill-name { font-size:18px; font-weight:700; color:var(--primary); line-height:1.5; margin-bottom:12px; }"""

new_skill_css = """.skill-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:28px; }
.skill-card {
  background: linear-gradient(145deg, #ffffff, #faf9f6);
  border-radius: 24px; padding: 40px 24px;
  text-align: center; 
  box-shadow: 0 12px 40px rgba(0,0,0,0.06), inset 0 2px 0 rgba(255,255,255,0.8);
  position: relative; overflow: hidden; 
  border: 1px solid rgba(200,164,92,0.25);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.skill-card:hover { 
  transform: translateY(-8px) scale(1.02); 
  box-shadow: 0 24px 50px rgba(200,164,92,0.15);
  border-color: rgba(200,164,92,0.6);
}
.skill-card:hover .skill-icon {
  transform: scale(1.1) rotate(4deg);
}
.skill-card::before {
  content: ''; position: absolute; top:0; left:0; width:100%; height:4px;
  background: linear-gradient(90deg, var(--accent), var(--accent-light));
}
.skill-number {
  display: inline-block; font-size: 13px; font-weight: 800; color: var(--accent);
  letter-spacing: 3px; margin-bottom: 20px;
  background: rgba(200,164,92,0.1); padding: 6px 16px; border-radius: 20px;
}
.skill-icon { 
  width: 88px; height: 88px; margin: 0 auto 24px; 
  background: var(--bg); border-radius: 50%; padding: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  transition: transform 0.4s ease;
}
.skill-name { font-size: 21px; font-weight: 800; color: var(--primary); line-height: 1.5; margin-bottom: 8px; }"""

files = glob.glob('LP0*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_section_title, new_section_title)
    content = content.replace(old_skill_css, new_skill_css)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Upgraded CSS in {file}")

