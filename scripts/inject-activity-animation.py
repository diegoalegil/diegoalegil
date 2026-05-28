#!/usr/bin/env python3
"""Inyecta animaciones CSS Apple-style en el SVG de activity-graph.

GitHub sirve los SVG con CSP `sandbox`, lo cual bloquea SMIL `<animate>`
cuando el SVG se carga como `<img>`. Las animaciones CSS dentro de un
`<style>` interno SÍ pasan (es lo que usa la animación de la snake del
mismo perfil). Por eso este script inyecta `<style>` con `@keyframes`.

El bloque inyectado es autosuficiente: fija él mismo los trazos, colores y
el `stroke-dasharray` de los que depende la animación, en lugar de heredarlos
del CSS del servicio externo. Así, si el upstream cambia sus clases, la
animación sigue funcionando (o falla de forma ruidosa, no en silencio).

Además:
  - Fuerza un fondo opaco oscuro (legible también en el tema claro de GitHub).
  - Respeta `prefers-reduced-motion`: con esa preferencia el gráfico se
    muestra completo y estático, sin bucle.
  - Es idempotente: si se ejecuta sobre un SVG ya inyectado, primero limpia
    la inyección anterior y vuelve a aplicarla.

Uso:
    python3 inject-activity-animation.py SVG_ENTRADA SVG_SALIDA
"""
import re
import sys

# Identificador del bloque inyectado, para poder limpiarlo y ser idempotente.
MARKER = "act-line"
CARD_BG = "#1a1b27"  # tokyonight: mismo fondo que el resto de badges/tarjetas


def strip_previous_injection(svg: str) -> str:
    """Elimina cualquier inyección previa (bloque <style> + atributos --d)."""
    # Quita solo los <style> que contengan nuestras keyframes (no el de upstream).
    svg = re.sub(
        r"<style[^>]*>(?:(?!</style>).)*?</style>",
        lambda m: "" if MARKER in m.group(0) else m.group(0),
        svg,
        flags=re.S,
    )
    # Quita los style="--d:..." que añadimos a cada punto.
    svg = re.sub(r'\s*style="--d:[^"]*"', "", svg)
    return svg


def force_dark_background(svg: str) -> str:
    """Pone el fondo de la tarjeta opaco y oscuro para legibilidad en tema claro."""
    new_svg, n = re.subn(
        r'(<rect\b[^>]*id="cardBg"[^>]*\bfill=")[^"]*(")',
        rf"\g<1>{CARD_BG}\g<2>",
        svg,
    )
    if n == 0:
        print("AVISO: no se encontró el rect #cardBg; fondo sin modificar.",
              file=sys.stderr)
    return new_svg


def stamp_points(svg: str) -> tuple[str, int]:
    """Añade un --d (animation-delay) incremental a cada <line class="ct-point">."""
    counter = {"i": 0}

    def stamp(m: "re.Match[str]") -> str:
        inner = m.group(1).rstrip()
        delay = 0.30 + counter["i"] * 0.075
        counter["i"] += 1
        closing = " />" if m.group(0).endswith("/>") else ">"
        return f'{inner} style="--d:{delay:.2f}s"{closing}'

    svg = re.sub(
        r'(<line\b[^>]*?class="ct-point"[^>]*?)\s*(/?>)',
        stamp,
        svg,
    )
    return svg, counter["i"]


STYLE_BLOCK = """<style>
  /* === inyectado por scripts/inject-activity-animation.py === */
  /* Estilos autosuficientes: no dependen del CSS del servicio externo. */
  .ct-line  { fill: none; stroke: #BB9AF7; stroke-width: 4px; stroke-dasharray: 5000; }
  .ct-point { stroke: #F7768E; stroke-width: 10px; stroke-linecap: round; }
  .ct-area  { stroke: none; fill: #70a5fd; fill-opacity: 0.1; }

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

  /* Accesibilidad: sin movimiento, gráfico completo y estático. */
  @media (prefers-reduced-motion: reduce) {
    .ct-line, .ct-area, .ct-point {
      animation: none !important;
      opacity: 1 !important;
      stroke-dashoffset: 0 !important;
    }
  }
</style>"""


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} SVG_ENTRADA SVG_SALIDA", file=sys.stderr)
        return 2

    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        svg = f.read()

    svg = strip_previous_injection(svg)
    svg = force_dark_background(svg)
    svg, n_points = stamp_points(svg)

    if n_points == 0:
        print("ERROR: no se encontró ningún <line class=\"ct-point\">. "
              "¿Cambió el formato del SVG de upstream?", file=sys.stderr)
        return 1

    if "</svg>" not in svg:
        print("ERROR: el SVG no contiene </svg>.", file=sys.stderr)
        return 1

    # Insertar el <style> justo antes del último </svg> (mayor especificidad por orden).
    head, sep, tail = svg.rpartition("</svg>")
    svg = head + STYLE_BLOCK + sep + tail

    with open(dst, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"OK. CSS inyectado. Puntos escalonados: {n_points}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
