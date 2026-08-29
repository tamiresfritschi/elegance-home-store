from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''

/* Informações de compra, FAQ e CTA mobile */
.purchase-trust{
  display:grid;grid-template-columns:repeat(2,1fr);gap:9px;margin:18px 0 10px
}
.purchase-trust-item{
  display:flex;align-items:center;gap:9px;padding:11px 12px;
  border:1px solid var(--line);border-radius:13px;background:#faf6f1;
  color:var(--ink);font-size:12px;font-weight:700;line-height:1.35
}
.purchase-trust-icon{
  flex:0 0 25px;width:25px;height:25px;border-radius:50%;background:#e9dfd5;
  display:grid;place-items:center;color:var(--accent);font-size:12px;font-weight:900
}

.faq-section{background:#fffdf9}
.faq-header{max-width:680px;margin:0 auto 34px;text-align:center}
.faq-header .eyebrow{color:var(--accent);margin-bottom:12px}
.faq-header h2{font-family:Georgia,serif;font-size:clamp(36px,5vw,48px);font-weight:500;margin:0 0 10px}
.faq-header p{color:var(--muted);line-height:1.6;margin:0}
.faq-list{max-width:860px;margin:0 auto;display:grid;gap:12px}
.faq-item{border:1px solid var(--line);border-radius:17px;background:#fff;overflow:hidden;box-shadow:0 8px 24px rgba(54,42,32,.04)}
.faq-item summary{list-style:none;cursor:pointer;padding:18px 54px 18px 19px;font-weight:800;position:relative;line-height:1.4}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:'+';position:absolute;right:18px;top:50%;transform:translateY(-50%);width:27px;height:27px;border-radius:50%;background:#f2ebe3;display:grid;place-items:center;color:var(--accent);font-size:20px;font-weight:500}
.faq-item[open] summary::after{content:'−'}
.faq-answer{padding:0 19px 19px;color:var(--muted);font-size:14px;line-height:1.65;border-top:1px solid #f0e8e0;padding-top:15px}
.faq-cta{text-align:center;margin-top:25px;color:var(--muted);font-size:13px}
.faq-cta a{color:var(--accent);font-weight:800;text-decoration:underline;text-underline-offset:3px}

.mobile-product-cta{display:none}
@media(max-width:620px){
  .purchase-trust{grid-template-columns:1fr}
  body{padding-bottom:76px}
  .mobile-product-cta{
    display:flex;position:fixed;left:12px;right:72px;bottom:12px;z-index:59;
    align-items:center;justify-content:center;min-height:52px;padding:12px 16px;
    background:var(--dark);color:#fff;border:1px solid rgba(255,255,255,.15);
    border-radius:999px;font-size:13px;font-weight:800;box-shadow:0 12px 30px rgba(35,29,25,.28)
  }
  .whatsapp-float{z-index:60}
}
'''

if '/* Informações de compra, FAQ e CTA mobile */' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

trust = r'''
  <div class="purchase-trust" aria-label="Informações de compra">
    <div class="purchase-trust-item"><span class="purchase-trust-icon">✓</span><span>Jogo de cama com 4 peças</span></div>
    <div class="purchase-trust-item"><span class="purchase-trust-icon">✓</span><span>Tamanhos Casal, Queen e King</span></div>
    <div class="purchase-trust-item"><span class="purchase-trust-icon">✓</span><span>Confirme a disponibilidade da cor</span></div>
    <div class="purchase-trust-item"><span class="purchase-trust-icon">✓</span><span>Envio para todo o Brasil</span></div>
  </div>
'''

if 'class="purchase-trust"' not in s:
    anchor = '  <div class="selection-note">Você poderá confirmar a disponibilidade antes de finalizar.</div>\n</div>'
    if anchor not in s:
        raise SystemExit('Não encontrei o bloco de compra para adicionar as informações.')
    s = s.replace(anchor, '  <div class="selection-note">Você poderá confirmar a disponibilidade antes de finalizar.</div>\n' + trust + '</div>', 1)

faq = r'''
  <section class="faq-section" id="duvidas">
    <div class="container">
      <div class="faq-header">
        <div class="eyebrow">Dúvidas frequentes</div>
        <h2>Antes de fazer o pedido</h2>
        <p>As principais informações para escolher seu jogo de cama e falar com a gente pelo WhatsApp.</p>
      </div>

      <div class="faq-list">
        <details class="faq-item">
          <summary>O que vem no jogo de cama?</summary>
          <div class="faq-answer">O produto anunciado é um jogo de cama com 4 peças. Antes de finalizar o pedido, você pode confirmar todos os detalhes do produto pelo WhatsApp.</div>
        </details>

        <details class="faq-item">
          <summary>Quais tamanhos estão disponíveis?</summary>
          <div class="faq-answer">Trabalhamos com Casal, Queen e King. No produto em destaque, escolha o tamanho para visualizar o valor correspondente.</div>
        </details>

        <details class="faq-item">
          <summary>Como escolho a cor?</summary>
          <div class="faq-answer">Na área do produto, clique na cor desejada. O carrossel passa a mostrar somente as fotos daquela cor. Depois, confirme a disponibilidade pelo WhatsApp.</div>
        </details>

        <details class="faq-item">
          <summary>Vocês enviam para todo o Brasil?</summary>
          <div class="faq-answer">Sim. Enviamos para todo o Brasil. Fale conosco pelo WhatsApp para consultar as opções e condições de envio para o seu CEP.</div>
        </details>

        <details class="faq-item">
          <summary>Como faço o pedido?</summary>
          <div class="faq-answer">Escolha a cor e o tamanho na página, depois clique em “Comprar pelo WhatsApp”. A mensagem já vai pronta com sua escolha para você confirmar a disponibilidade antes de finalizar.</div>
        </details>
      </div>

      <div class="faq-cta">Ainda ficou com alguma dúvida? <a href="https://wa.me/5567998547135" target="_blank" rel="noopener">Fale com a Elegance Home no WhatsApp.</a></div>
    </div>
  </section>
'''

if 'id="duvidas"' not in s:
    anchor = '  <section id="sobre">'
    if anchor not in s:
        raise SystemExit('Não encontrei a seção Sobre para inserir o FAQ.')
    s = s.replace(anchor, faq + '\n' + anchor, 1)

if '<a href="#duvidas">Dúvidas</a>' not in s:
    s = s.replace('<a href="#sobre">Sobre</a>', '<a href="#duvidas">Dúvidas</a>\n        <a href="#sobre">Sobre</a>', 1)

mobile_cta = r'''
  <a class="mobile-product-cta" href="#productOptions" aria-label="Escolher cor e tamanho do jogo de cama">Escolher cor e tamanho</a>
'''
if 'class="mobile-product-cta"' not in s:
    anchor = '  <a class="whatsapp-float"'
    if anchor not in s:
        raise SystemExit('Não encontrei o botão flutuante do WhatsApp.')
    s = s.replace(anchor, mobile_cta + '\n' + anchor, 1)

p.write_text(s, encoding='utf-8')
