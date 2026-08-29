from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Adiciona Bege Acinzentado ao seletor de cores, usando a foto 0 do carrossel.
needle = '              <div class="option-buttons" role="group" aria-label="Escolha a cor">\n                <button class="option-btn color-btn" type="button" data-color="Fendi Claro" data-slide="1">Fendi Claro</button>'
replacement = '              <div class="option-buttons" role="group" aria-label="Escolha a cor">\n                <button class="option-btn color-btn" type="button" data-color="Bege Acinzentado" data-slide="0">Bege Acinzentado</button>\n                <button class="option-btn color-btn" type="button" data-color="Fendi Claro" data-slide="1">Fendi Claro</button>'
if 'data-color="Bege Acinzentado"' not in s:
    if needle not in s:
        raise SystemExit('Não encontrei o bloco do seletor de cores.')
    s = s.replace(needle, replacement, 1)

# Atualiza a lista textual de cores.
s = s.replace('✓ Cores: Fendi Claro, Cinza, Cinza Pérola e Rosa Blush',
              '✓ Cores: Bege Acinzentado, Fendi Claro, Cinza, Cinza Pérola e Rosa Blush')

# Inclui a foto Bege Acinzentado na galeria, se ainda não estiver lá.
gallery_anchor = '                  <div class="gallery-grid">\n                    <div class="gallery-card">\n                      <img src="assets/fendi-claro-ambiente.png" data-carousel-index="1" alt="Jogo de cama Fendi Claro em ambiente">'
beige_card = '                  <div class="gallery-grid">\n                    <div class="gallery-card">\n                      <img src="assets/bege-acinzentado.png" data-carousel-index="0" alt="Jogo de cama Bege Acinzentado">\n                      <div class="caption"><b>Bege Acinzentado</b><span>Close do bordado</span></div>\n                    </div>\n                    <div class="gallery-card">\n                      <img src="assets/fendi-claro-ambiente.png" data-carousel-index="1" alt="Jogo de cama Fendi Claro em ambiente">'
if 'data-carousel-index="0" alt="Jogo de cama Bege Acinzentado"' not in s:
    if gallery_anchor not in s:
        raise SystemExit('Não encontrei o início da galeria.')
    s = s.replace(gallery_anchor, beige_card, 1)

p.write_text(s, encoding='utf-8')
