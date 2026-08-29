from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if 'assets/begeacizentado.jpg' not in s:
    old = '<img class="carousel-slide active" src="assets/bege-acinzentado.png" alt="Jogo de cama Bege Acinzentado" data-label="Bege Acinzentado" loading="eager">'
    new = '<img class="carousel-slide active" src="assets/begeacizentado.jpg" alt="Jogo de cama Bege Acinzentado" data-label="Bege Acinzentado" loading="eager"><img class="carousel-slide" src="assets/bege-acinzentado.png" alt="Jogo de cama Bege Acinzentado" data-label="Bege Acinzentado" loading="lazy">'
    if old not in s:
        raise SystemExit('Foto inicial do Bege Acinzentado não encontrada.')
    s = s.replace(old, new, 1)

# Atualiza os índices do seletor de cores após inserir a nova foto em primeiro.
repls = {
    'data-color="Fendi Claro" data-slide="1"':'data-color="Fendi Claro" data-slide="2"',
    'data-color="Cinza" data-slide="4"':'data-color="Cinza" data-slide="5"',
    'data-color="Cinza Pérola" data-slide="5"':'data-color="Cinza Pérola" data-slide="6"',
    'data-color="Rosa Blush" data-slide="7"':'data-color="Rosa Blush" data-slide="8"',
}
for a,b in repls.items():
    s = s.replace(a,b)

# Recria os pontos do carrossel para 10 fotos.
dots = ''.join(
    f'<button class="carousel-dot{" active" if i == 0 else ""}" type="button" aria-label="Mostrar foto {i+1}" data-slide="{i}"></button>'
    for i in range(10)
)
s = re.sub(r'<div class="carousel-dots">\s*.*?\s*</div>', '<div class="carousel-dots">\n            ' + dots + '\n          </div>', s, count=1, flags=re.S)

# Atualiza os índices das miniaturas da galeria.
idx = {
    'assets/fendi-claro-ambiente.png': 2,
    'assets/fendi-claro-kit.png': 3,
    'assets/fendi-claro-dobrado.png': 4,
    'assets/cinza-produto-dobrado.png': 5,
    'assets/cinza-perola-ambiente.png': 6,
    'assets/cinza-perola-dobrado.png': 7,
    'assets/rosa-blush-ambiente.png': 8,
    'assets/rosa-blush-dobrado.png': 9,
}
for src, n in idx.items():
    s = re.sub(rf'(<img src="{re.escape(src)}" data-carousel-index=")\d+(" )', rf'\g<1>{n}\2', s)

# Coloca as duas fotos do Bege Acinzentado no início da galeria, caso ainda não estejam lá.
if 'src="assets/begeacizentado.jpg" data-carousel-index="0"' not in s:
    anchor = '<div class="gallery-grid">'
    cards = '''<div class="gallery-grid">
                    <div class="gallery-card">
                      <img src="assets/begeacizentado.jpg" data-carousel-index="0" alt="Jogo de cama Bege Acinzentado em destaque">
                      <div class="caption"><b>Bege Acinzentado</b><span>Foto principal</span></div>
                    </div>
                    <div class="gallery-card">
                      <img src="assets/bege-acinzentado.png" data-carousel-index="1" alt="Jogo de cama Bege Acinzentado">
                      <div class="caption"><b>Bege Acinzentado</b><span>Close do bordado</span></div>
                    </div>'''
    if anchor not in s:
        raise SystemExit('Galeria não encontrada.')
    s = s.replace(anchor, cards, 1)

p.write_text(s, encoding='utf-8')
