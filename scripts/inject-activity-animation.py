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

# Bloque <style> con keyframes en loop infinito (ciclo de 14 s).
# Los SVG cargados como <img> no pueden ser scroll-triggered (no JS), así que
# loopeamos para que el visitante pille la animación sin importar cuándo
# llegue a la sección. Easings tipo Apple: ease-in-out para el dibujado,
# ease para el fade-out final.
style_block = '''<style>
  @keyframes act-line {
    0%   { stroke-dashoffset: 5000; opacity: 0;
           animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1); }
    4%   { opacity: 1; }
    25%  { stroke-dashoffset: 0; opacity: 1;
           animation-timing-function: linear; }
    87%  { stroke-dashoffset: 0; opacity: 1;
           animation-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1); }
    100% { stroke-dashoffset: 0; opacity: 0; }
  }
  @keyframes act-area {
    0%   { opacity: 0;
           animation-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1); }
    12%  { opacity: 0; }
    30%  { opacity: 1;
           animation-timing-function: linear; }
    87%  { opacity: 1;
           animation-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1); }
    100% { opacity: 0; }
  }
  @keyframes act-point {
    0%   { opacity: 0;
           animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1); }
    3%   { opacity: 1;
           animation-timing-function: linear; }
    87%  { opacity: 1;
           animation-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1); }
    100% { opacity: 0; }
  }
  .ct-line  { animation: act-line  14s linear infinite; }
  .ct-area  { opacity: 0; animation: act-area  14s linear infinite; }
  .ct-point { opacity: 0; animation: act-point 14s linear infinite var(--d, 0s); }
</style>'''

# Insertar el <style> justo antes de </svg>
svg = svg.replace('</svg>', style_block + '</svg>', 1)

with open(dst, 'w') as f:
    f.write(svg)
print(f'OK. CSS inyectado. Puntos escalonados: {counter["i"]}')
