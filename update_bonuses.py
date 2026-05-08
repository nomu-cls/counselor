import glob
import re

skill_replacements = [
    (r'<h4>言語化力<br><span.*?>(.*?)</span></h4>', 
     r'<h4>言語化力<br><span style="display:inline-block; font-size:16px; color:var(--primary); font-weight:800; margin-top:10px; padding:4px 8px; background:linear-gradient(transparent 60%, rgba(202,152,81,0.5) 60%);">― 想いを「届く言葉」に変換する力</span></h4>'),
    
    (r'<h4>体験設計力<br><span.*?>(.*?)</span></h4>', 
     r'<h4>体験設計力<br><span style="display:inline-block; font-size:16px; color:var(--primary); font-weight:800; margin-top:10px; padding:4px 8px; background:linear-gradient(transparent 60%, rgba(202,152,81,0.5) 60%);">― セッションを"変容の体験"にする力</span></h4>'),

    (r'<h4>対応力<br><span.*?>(.*?)</span></h4>', 
     r'<h4>対応力<br><span style="display:inline-block; font-size:16px; color:var(--primary); font-weight:800; margin-top:10px; padding:4px 8px; background:linear-gradient(transparent 60%, rgba(202,152,81,0.5) 60%);">― 台本を超え、相手に最適化する力</span></h4>')
]

bonus_html = """<!-- ===== BONUSES ===== -->
<section class="section-wide" style="background:#0f172a; color:#fff; padding:80px 20px;">
  <div class="section-inner" style="max-width:800px;">
    <p style="text-align:center; color:var(--accent); font-size:14px; font-weight:700; letter-spacing:3px; margin-bottom:16px;">EXCLUSIVE BONUSES</p>
    <h2 class="section-title" style="color:#fff; text-align:center; border:none; margin-bottom:24px;">
      ワークショップへご参加の皆様へ<br>
      <span style="color:var(--accent); font-size:1.1em; text-shadow:0 0 20px rgba(202,152,81,0.4);">超実践的・8大特典プレゼント</span>
    </h2>
    <p style="text-align:center; font-size:15px; line-height:2.0; color:rgba(255,255,255,0.7); margin-bottom:56px;">
      現場のリアルな悩みから生まれた「解答例と改善策」を、<br>参加状況に応じてプレゼントいたします。
    </p>

    <!-- 課題特典 -->
    <h3 style="color:var(--white); border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:32px; font-size:22px; font-weight:700;"><span style="margin-right:12px;">📝</span> 課題提出でもらえる特典</h3>
    <div style="display:grid; gap:20px; margin-bottom:56px;">
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(202,152,81,0.3); border-left:6px solid var(--accent); padding:32px; border-radius:12px; box-shadow:0 8px 30px rgba(0,0,0,0.2);">
        <span style="display:inline-block; font-size:14px; font-weight:800; color:var(--primary); background:var(--accent-light); padding:6px 16px; border-radius:20px; margin-bottom:16px;">DAY 1 課題提出</span>
        <h4 style="font-size:18px; margin-bottom:0; line-height:1.7; color:#fff; font-weight:700;">自分にがっかり！順調だと思ってたのに、突然来なくなったクライアント。期待に応えられなかった…と自分を責める代わりにできること</h4>
      </div>
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(202,152,81,0.3); border-left:6px solid var(--accent); padding:32px; border-radius:12px; box-shadow:0 8px 30px rgba(0,0,0,0.2);">
        <span style="display:inline-block; font-size:14px; font-weight:800; color:var(--primary); background:var(--accent-light); padding:6px 16px; border-radius:20px; margin-bottom:16px;">DAY 2 課題提出</span>
        <h4 style="font-size:18px; margin-bottom:0; line-height:1.7; color:#fff; font-weight:700;">信頼されてない？？…話してくれないクライアントがいる。「話せない」を「話したい」にしてしまう、クライアントへの質問の誤り</h4>
      </div>
    </div>

    <!-- コンプリート特典 -->
    <h3 style="color:var(--white); border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:32px; font-size:22px; font-weight:700;"><span style="margin-right:12px;">🏆</span> コンプリート特典</h3>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:24px; margin-bottom:56px;">
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(202,152,81,0.2); border-radius:12px; padding:32px;">
        <h4 style="font-size:17px; margin-bottom:0; line-height:1.7; color:#fff; font-weight:600;">「伝わってない？」納得いってない表情のクライアントは、あなたのマズい伝え方の鏡！寄り道・迷子の伝え方の改善法</h4>
      </div>
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(202,152,81,0.2); border-radius:12px; padding:32px;">
        <h4 style="font-size:17px; margin-bottom:0; line-height:1.7; color:#fff; font-weight:600;">プロ失格？？壮絶な人生のクライアントが来るといつも話に巻き込まれてしまう。そんな「聴くだけ」を終了するための方法は？</h4>
      </div>
    </div>

    <!-- リアルタイム参加特典 -->
    <h3 style="color:var(--white); border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:32px; font-size:22px; font-weight:700;"><span style="margin-right:12px;">🔴</span> リアルタイムLIVE参加特典</h3>
    <div style="display:grid; gap:16px; margin-bottom:16px;">
      <div style="background:linear-gradient(90deg, rgba(202,152,81,0.08) 0%, rgba(255,255,255,0.02) 100%); border:1px solid rgba(202,152,81,0.3); display:flex; align-items:center; padding:20px 24px; border-radius:12px; gap:20px;">
        <span style="color:var(--accent); font-weight:900; font-size:16px; min-width:60px;">DAY 2</span>
        <h4 style="font-size:16px; color:#fff; font-weight:600; margin:0; line-height:1.6;">頭真っ白！初めて来るクライアント！互いに緊張する初対面で安心感を高める入り方とは？</h4>
      </div>
      <div style="background:linear-gradient(90deg, rgba(202,152,81,0.08) 0%, rgba(255,255,255,0.02) 100%); border:1px solid rgba(202,152,81,0.3); display:flex; align-items:center; padding:20px 24px; border-radius:12px; gap:20px;">
        <span style="color:var(--accent); font-weight:900; font-size:16px; min-width:60px;">DAY 3</span>
        <h4 style="font-size:16px; color:#fff; font-weight:600; margin:0; line-height:1.6;">自己肯定感ゼロ…どうしたらいい？？"どうせ私なんて" "すみません"が口癖のクライアントへの声のかけ方</h4>
      </div>
      <div style="background:linear-gradient(90deg, rgba(202,152,81,0.08) 0%, rgba(255,255,255,0.02) 100%); border:1px solid rgba(202,152,81,0.3); display:flex; align-items:center; padding:20px 24px; border-radius:12px; gap:20px;">
        <span style="color:var(--accent); font-weight:900; font-size:16px; min-width:60px;">DAY 4</span>
        <h4 style="font-size:16px; color:#fff; font-weight:600; margin:0; line-height:1.6;">辛いクライアントにお金の話をしたくない！継続提案やクロージングへの苦手意識を克服する方法とは！？</h4>
      </div>
      <div style="background:linear-gradient(90deg, rgba(202,152,81,0.08) 0%, rgba(255,255,255,0.02) 100%); border:1px solid rgba(202,152,81,0.3); display:flex; align-items:center; padding:20px 24px; border-radius:12px; gap:20px;">
        <span style="color:var(--accent); font-weight:900; font-size:16px; min-width:60px;">DAY 5</span>
        <h4 style="font-size:16px; color:#fff; font-weight:600; margin:0; line-height:1.6;">経験不足？？深刻な悩みを打ち明けるクライアントにどう返したら良いかわからない？～相手の心を軽くする聴き方</h4>
      </div>
    </div>
  </div>
</section>

<!-- ===== CTA: UTAGE FORM ===== -->"""

for file in glob.glob('/Users/nomura/antigravity/TK/カウンセラー/LP0*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update skills styling
    for pattern, replacement in skill_replacements:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    # Insert Bonuses before the final CTA
    if '<!-- ===== BONUSES ===== -->' not in content:
        content = content.replace('<!-- ===== CTA: UTAGE FORM ===== -->', bonus_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file} with Bonuses and emphasized text.")
