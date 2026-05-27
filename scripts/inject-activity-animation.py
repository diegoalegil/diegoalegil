#!/usr/bin/env python3
"""Inyecta animaciones CSS Apple-style en el SVG de activity-graph.

GitHub sirve los SVG con CSP `sandbox`, lo cual bloquea SMIL `<animate>`
cuando el SVG se carga como `<img>`. Las animaciones CSS dentro de un
`<style>` interno SÍ pasan (es lo que usa la animación de la snake del
mismo perfil). Por eso este script inyecta `<style>` con `@keyframes`.

Uso:
    python3 inject-activity-animation.py SVG_ENTRADA SVG_SALIDA
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
with open(src) as f:
    svg = f.read()

# Cada <line class="ct-point"> recibe un --d (animation-delay) incremental
counter = {'i': 0}
def stamp_point(m):
    inner = m.group(1).rstrip()
    delay = 0.30 + counter['i'] * 0.075
    counter['i'] += 1
    closing = ' />' if m.group(0).endswith('/>') else '>'
    return f'{inner} style="--d:{delay:.2f}s"{closing}'

svg = re.sub(
    r'(<line\b[^>]*?class="ct-point"[^>]*?)\s*(/?>)',
    stamp_point, svg
)

# Bloque <style> con @keyframes y cubic-bezier Apple-style
style_block = '''<style>
  @keyframes act-draw { to { stroke-dashoffset: 0; } }
  @keyframes act-fade { to { opacity: 1; } }
  .ct-line {
    animation: act-draw 2.4s cubic-bezier(0.42, 0, 0.58, 1) 0.3s forwards;
  }
  .ct-area {
    opacity: 0;
    animation: act-fade 1.0s cubic-bezier(0.25, 0.1, 0.25, 1) 1.6s forwards;
  }
  .ct-point {
    opacity: 0;
    animation: act-fade 0.35s cubic-bezier(0.16, 1, 0.3, 1) var(--d, 0s) forwards;
  }
</style>'''

# Insertar el <style> justo antes de </svg>
svg = svg.replace('</svg>', style_block + '</svg>', 1)

with open(dst, 'w') as f:
    f.write(svg)
print(f'OK. CSS inyectado. Puntos escalonados: {counter["i"]}')
