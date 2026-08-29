from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''

/* Avaliações de clientes */
.reviews-section{background:#f2ebe3}
.reviews-header{max-width:700px;margin:0 auto 38px;text-align:center}
.reviews-badge{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border:1px solid #dbcfc4;border-radius:999px;background:#fffdf9;color:var(--accent);font-size:12px;font-weight:800;letter-spacing:.04em;margin-bottom:14px}
.reviews-header h2{font-family:Georgia,serif;font-size:clamp(36px,5vw,48px);font-weight:500;margin:0 0 10px}
.reviews-header p{color:var(--muted);line-height:1.6;margin:0}
.reviews-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.review-card{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 12px 30px rgba(54,42,32,.06);display:flex;flex-direction:column;min-height:210px}
.review-stars{font-size:18px;letter-spacing:2px;color:#b8872f;margin-bottom:16px}
.review-text{font-family:Georgia,serif;font-size:21px;line-height:1.45;margin:0 0 22px;color:var(--ink)}
.review-meta{margin-top:auto;padding-top:15px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:14px;align-items:flex-end}
.review-meta strong{display:block;font-size:13px;margin-bottom:4px}
.review-meta span{color:var(--muted);font-size:12px;line-height:1.4}
.review-source{white-space:nowrap;background:#f3ede7;border-radius:999px;padding:7px 10px;color:var(--accent)!important;font-weight:800}
.reviews-note{text-align:center;color:var(--muted);font-size:12px;margin-top:18px}
@media(max-width:760px){.reviews-grid{grid-template-columns:1fr}.review-card{min-height:0}.review-meta{align-items:flex-start;flex-direction:column}.review-source{white-space:normal}}
'''

if '/* Avaliações de clientes */' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

reviews = r'''
  <section class="reviews-section" id="avaliacoes">
    <div class="container">
      <div class="reviews-header">
        <div class="reviews-badge">★★★★★ &nbsp; Avaliações no TikTok Shop</div>
        <h2>Quem comprou, aprovou.</h2>
        <p>Feedbacks reais recebidos de compradores dos nossos jogos de cama no TikTok Shop.</p>
      </div>

      <div class="reviews-grid">
        <article class="review-card">
          <div class="review-stars" aria-label="5 de 5 estrelas">★★★★★</div>
          <p class="review-text">“Amei, de boa qualidade, vou voltar a comprar.”</p>
          <div class="review-meta">
            <div><strong>Cliente TikTok</strong><span>Bege Acinzentado · Queen<br>27 de agosto de 2026</span></div>
            <span class="review-source">TikTok Shop</span>
          </div>
        </article>

        <article class="review-card">
          <div class="review-stars" aria-label="5 de 5 estrelas">★★★★★</div>
          <p class="review-text">“Perfeito, adorei, super macio, lindo.”</p>
          <div class="review-meta">
            <div><strong>Cliente TikTok</strong><span>Bege Acinzentado · King<br>17 de agosto de 2026</span></div>
            <span class="review-source">TikTok Shop</span>
          </div>
        </article>

        <article class="review-card">
          <div class="review-stars" aria-label="5 de 5 estrelas">★★★★★</div>
          <p class="review-text">“Adoreiiiii, lindo, macio.”</p>
          <div class="review-meta">
            <div><strong>Cliente TikTok</strong><span>Fendi Claro · King<br>17 de agosto de 2026</span></div>
            <span class="review-source">TikTok Shop</span>
          </div>
        </article>

        <article class="review-card">
          <div class="review-stars" aria-label="5 de 5 estrelas">★★★★★</div>
          <p class="review-text">“Excelente, lindo.”</p>
          <div class="review-meta">
            <div><strong>Cliente TikTok</strong><span>Cinza · King<br>17 de agosto de 2026</span></div>
            <span class="review-source">TikTok Shop</span>
          </div>
        </article>
      </div>

      <div class="reviews-note">Avaliações reproduzidas a partir do painel de avaliações da loja no TikTok Shop.</div>
    </div>
  </section>
'''

if 'id="avaliacoes"' not in s:
    anchor = '  <section id="sobre">'
    if anchor not in s:
        raise SystemExit('Não encontrei a seção Sobre para inserir as avaliações.')
    s = s.replace(anchor, reviews + '\n' + anchor, 1)

# Adiciona link de avaliações no menu desktop, sem duplicar.
if '<a href="#avaliacoes">Avaliações</a>' not in s:
    s = s.replace('<a href="#sobre">Sobre</a>', '<a href="#avaliacoes">Avaliações</a>\n        <a href="#sobre">Sobre</a>', 1)

p.write_text(s, encoding='utf-8')
