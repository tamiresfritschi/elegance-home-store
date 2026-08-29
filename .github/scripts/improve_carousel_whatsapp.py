from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''

/* Botão flutuante do WhatsApp */
.whatsapp-float{
  position:fixed;right:22px;bottom:22px;z-index:60;
  display:flex;align-items:center;gap:9px;
  background:#2d2824;color:#fff;border:1px solid rgba(255,255,255,.18);
  border-radius:999px;padding:13px 17px;
  font-weight:800;font-size:14px;
  box-shadow:0 14px 34px rgba(35,29,25,.28);
  transition:transform .2s ease,box-shadow .2s ease,background .2s ease;
}
.whatsapp-float:hover{transform:translateY(-2px);box-shadow:0 18px 38px rgba(35,29,25,.34);background:#201d1a}
.whatsapp-float .wa-icon{
  width:28px;height:28px;border-radius:50%;background:#fff;color:#2d2824;
  display:grid;place-items:center;font-size:16px;line-height:1
}
@media(max-width:620px){
  .whatsapp-float{right:14px;bottom:14px;padding:12px 14px}
  .whatsapp-float .wa-text{display:none}
  .whatsapp-float .wa-icon{width:31px;height:31px}
}
'''

if '/* Botão flutuante do WhatsApp */' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

float_html = r'''
  <a class="whatsapp-float" href="https://wa.me/5567998547135?text=Ol%C3%A1%21%20Gostaria%20de%20ver%20as%20op%C3%A7%C3%B5es%20de%20jogos%20de%20cama%20da%20Elegance%20Home." target="_blank" rel="noopener" aria-label="Falar com a Elegance Home pelo WhatsApp">
    <span class="wa-icon" aria-hidden="true">✆</span>
    <span class="wa-text">Falar no WhatsApp</span>
  </a>
'''
if 'class="whatsapp-float"' not in s:
    s = s.replace('  <footer>', float_html + '\n  <footer>', 1)

new_script = r'''<script>
(() => {
  const carousel = document.getElementById('productCarousel');
  if (!carousel) return;

  const slides = [...carousel.querySelectorAll('.carousel-slide')];
  const dots = [...carousel.querySelectorAll('.carousel-dot')];
  const label = document.getElementById('carouselLabel');
  const prev = carousel.querySelector('.carousel-prev');
  const next = carousel.querySelector('.carousel-next');
  const colorButtons = [...document.querySelectorAll('.color-btn')];
  const sizeButtons = [...document.querySelectorAll('.size-btn')];
  const buyWhatsapp = document.getElementById('buyWhatsapp');
  const selectionTitle = document.getElementById('selectionTitle');
  const selectionDetail = document.getElementById('selectionDetail');
  const selectionPrice = document.getElementById('selectionPrice');

  let current = 0;
  let timer;
  let selectedColor = '';
  let selectedSize = '';
  let selectedPrice = '';
  let visibleIndices = slides.map((_, i) => i);

  function refreshVisibleSlides() {
    visibleIndices = selectedColor
      ? slides.map((slide, i) => slide.dataset.label === selectedColor ? i : -1).filter(i => i >= 0)
      : slides.map((_, i) => i);

    dots.forEach((dot, i) => { dot.hidden = !visibleIndices.includes(i); });
    const multiple = visibleIndices.length > 1;
    if (prev) prev.style.display = multiple ? '' : 'none';
    if (next) next.style.display = multiple ? '' : 'none';
  }

  function show(index) {
    if (!visibleIndices.length) return;
    if (!visibleIndices.includes(index)) index = visibleIndices[0];
    current = index;
    slides.forEach((slide, i) => slide.classList.toggle('active', i === current));
    dots.forEach((dot, i) => dot.classList.toggle('active', i === current));
    if (label) label.textContent = slides[current].dataset.label || '';
  }

  function move(step) {
    const pos = visibleIndices.indexOf(current);
    const safePos = pos >= 0 ? pos : 0;
    const nextPos = (safePos + step + visibleIndices.length) % visibleIndices.length;
    show(visibleIndices[nextPos]);
  }

  function start() {
    stop();
    if (visibleIndices.length > 1) timer = setInterval(() => move(1), 4000);
  }

  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  function selectColor(color, requestedSlide) {
    selectedColor = color || '';
    colorButtons.forEach(btn => btn.classList.toggle('active', btn.dataset.color === selectedColor));
    refreshVisibleSlides();
    const target = visibleIndices.includes(requestedSlide) ? requestedSlide : visibleIndices[0];
    show(target);
    start();
    updatePurchase();
  }

  prev?.addEventListener('click', () => { move(-1); start(); });
  next?.addEventListener('click', () => { move(1); start(); });

  dots.forEach(dot => dot.addEventListener('click', () => {
    const index = Number(dot.dataset.slide);
    const color = slides[index]?.dataset.label || '';
    if (selectedColor && color !== selectedColor) selectColor(color, index);
    else { show(index); start(); }
  }));

  document.querySelectorAll('[data-carousel-index]').forEach(img => {
    img.addEventListener('click', () => {
      const index = Number(img.dataset.carouselIndex);
      const color = slides[index]?.dataset.label || '';
      selectColor(color, index);
      carousel.scrollIntoView({behavior:'smooth', block:'center'});
    });
  });

  carousel.addEventListener('mouseenter', stop);
  carousel.addEventListener('mouseleave', start);
  carousel.addEventListener('focusin', stop);
  carousel.addEventListener('focusout', start);

  function updatePurchase() {
    const ready = selectedColor && selectedSize && selectedPrice;
    if (selectionTitle) selectionTitle.textContent = ready ? `${selectedSize} · ${selectedColor}` : 'Selecione cor e tamanho';
    if (selectionDetail) selectionDetail.textContent = ready ? 'Jogo de Cama 4 Peças 3200 Fios Bordado Premium' : 'Monte seu pedido antes de abrir o WhatsApp.';
    if (selectionPrice) selectionPrice.textContent = ready ? `R$ ${selectedPrice}` : '—';
    if (!buyWhatsapp) return;

    if (ready) {
      const msg = `Olá! Quero comprar o Jogo de Cama 4 Peças 3200 Fios Bordado Premium, tamanho ${selectedSize}, cor ${selectedColor}, por R$ ${selectedPrice}. Pode confirmar a disponibilidade?`;
      buyWhatsapp.href = `https://wa.me/5567998547135?text=${encodeURIComponent(msg)}`;
      buyWhatsapp.classList.remove('disabled');
      buyWhatsapp.setAttribute('aria-disabled', 'false');
      buyWhatsapp.target = '_blank';
      buyWhatsapp.rel = 'noopener';
    } else {
      buyWhatsapp.href = '#productOptions';
      buyWhatsapp.classList.add('disabled');
      buyWhatsapp.setAttribute('aria-disabled', 'true');
      buyWhatsapp.removeAttribute('target');
    }
  }

  colorButtons.forEach(btn => btn.addEventListener('click', () => {
    const slideIndex = Number(btn.dataset.slide);
    selectColor(btn.dataset.color || '', Number.isFinite(slideIndex) ? slideIndex : undefined);
  }));

  sizeButtons.forEach(btn => btn.addEventListener('click', () => {
    selectedSize = btn.dataset.size || '';
    selectedPrice = btn.dataset.price || '';
    sizeButtons.forEach(b => b.classList.toggle('active', b === btn));
    updatePurchase();
  }));

  buyWhatsapp?.addEventListener('click', (event) => {
    if (buyWhatsapp.getAttribute('aria-disabled') === 'true') event.preventDefault();
  });

  refreshVisibleSlides();
  updatePurchase();
  show(0);
  start();
})();
</script>'''

s, n = re.subn(r'<script>.*?</script>', new_script, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Não encontrei o script principal para atualizar.')

p.write_text(s, encoding='utf-8')
