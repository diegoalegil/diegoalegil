#!/usr/bin/env python3
"""Inyecta animaciones SMIL Apple-style en el SVG de activity-graph."""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
with open(src) as f:
    svg = f.read()

# 1. Línea principal: stroke-draw con easing ease-in-out (apple style)
def animate_line(m):
    inner = m.group(1).rstrip()
    return inner + (
        '><animate attributeName="stroke-dashoffset" '
        'from="5000" to="0" dur="2.4s" begin="0.3s" '
        'fill="freeze" calcMode="spline" '
        'keyTimes="0;1" keySplines="0.42 0 0.58 1"/></path>'
    )

svg = re.sub(
    r'(<path\b[^>]*?class="ct-line"[^>]*?)\s*/?>',
    animate_line, svg, count=1
)

# 2. Área bajo la línea: fade-in suave después de que la línea ya está dibujada
def animate_area(m):
    inner = m.group(1).rstrip()
    if 'opacity=' not in inner:
        inner += ' opacity="0"'
    return inner + (
        '><animate attributeName="opacity" '
        'from="0" to="1" dur="1.0s" begin="1.6s" '
        'fill="freeze" calcMode="spline" '
        'keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/></path>'
    )

svg = re.sub(
    r'(<path\b[^>]*?class="ct-area"[^>]*?)\s*/?>',
    animate_area, svg, count=1
)

# 3. Puntos: aparecen escalonados de izquierda a derecha siguiendo el dibujo
counter = {'i': 0}
def animate_point(m):
    inner = m.group(1).rstrip()
    if 'opacity=' not in inner:
        inner += ' opacity="0"'
    # 2.4s de la línea / 31 puntos ≈ delay incremental de ~0.07s
    delay = 0.3 + counter['i'] * 0.075
    counter['i'] += 1
    return inner + (
        f'><animate attributeName="opacity" '
        f'from="0" to="1" dur="0.35s" begin="{delay:.2f}s" '
        f'fill="freeze" calcMode="spline" '
        f'keyTimes="0;1" keySplines="0.16 1 0.3 1"/></line>'
    )

svg = re.sub(
    r'(<line\b[^>]*?class="ct-point"[^>]*?)\s*/?>',
    animate_point, svg
)

with open(dst, 'w') as f:
    f.write(svg)
print(f'OK. Inyectado: 1 línea + 1 área + {counter["i"]} puntos')
