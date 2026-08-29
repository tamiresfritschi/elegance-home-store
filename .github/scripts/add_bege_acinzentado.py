from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Usa a foto que já existe no repositório: assets/bege-acinzentado.png
# Ela já é o slide 0 do carrossel.
bege_btn = '      <button class="option-btn color-btn" type="button" data-color="Bege Acinzentado" data-slide="0">Bege Acinzentado</button>\n'
fendi_btn = '      <button class="option-btn color-btn" type="button" data-color="Fendi Claro" data-slide="1">Fendi Claro</button>'

if 'data-color="Bege Acinzentado"' not in s:
    if fendi_btn not in s:
        raise SystemExit('Não encontrei o botão Fendi Claro no seletor.')
    s = s.replace(fendi_btn, bege_btn + fendi_btn, 1)

s = s.replace(
    '✓ Cores: Fendi Claro, Cinza, Cinza Pérola e Rosa Blush',
    '✓ Cores: Bege Acinzentado, Fendi Claro, Cinza, Cinza Pérola e Rosa Blush'
)

p.write_text(s, encoding='utf-8')
