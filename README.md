<!--
═══════════════════════════════════════════════════════════════════════════════
  README de @diegoalegil  ·  paleta tokyonight + acento rojo CTA
  ───────────────────────────────────────────────────────────────────────────
  ZONAS QUE CAMBIAN MÁS A MENUDO  (busca el emoji ✏️):
   ✏️ HERO          → título, subtítulo y botones CTA
   ✏️ PRODUCCIÓN    → bloque destacado (Canarias Convive · en producción real)
   ✏️ PRINCIPAL     → bloque estrella (AnimeShowdown)
   ✏️ TRABAJANDO    → sección oculta (Fuerteventura, reactivar al salir a prod)
   ✏️ APRENDIENDO   → 3 líneas con lo que estás trasteando ahora
   ✏️ DESTACADOS    → fila de 2 + línea extra (rotar cuando cambien tus repos top)
   ✏️ CIERRE        → frase final + CTA repetido
═══════════════════════════════════════════════════════════════════════════════
-->

<!-- ─── BANNER ───────────────────────────────────────────────────────────── -->
<!-- width=100%: ocupa todo el ancho del contenedor del README (846px en
     desktop, y escala solo en móvil/anchos intermedios sin distorsión).
     Sin contadores de followers/stars/visitas: números pequeños son
     prueba social negativa. -->
<p align="center">
  <img src="images/banner-tokyo.svg" alt="Diego Gil · banner Tokyo Night animado" width="100%" />
</p>

<!-- ─── HERO  ✏️ ─────────────────────────────────────────────────────────── -->
<div align="center">
  <h1>Hola, soy Diego 👋🏻</h1>
  <p><b>Backend y bases de datos · código en producción para la Universidad de La Laguna · Tenerife 🇮🇨</b></p>
  <p><i>Estudiante de DAM. Me obsesiono con entender por qué algo funciona — o por qué se rompe a las 3 de la mañana.</i></p>
  <br />
  <a href="https://diegoalegil.github.io/"><img src="images/conoceme-badge.svg" alt="Conóceme" height="36" /></a>
  <a href="mailto:diegogildam@gmail.com"><img src="images/gmail-badge.svg" alt="Gmail" height="36" /></a>
</div>

---

<!-- ─── 🚀 EN PRODUCCIÓN  ✏️ ──────────────────────────────────────────────── -->
## 🚀 En producción

> Código mío sirviendo en una web institucional real, ahora mismo.

<table align="center">
  <tr>
    <td width="48%" valign="middle" align="center">
      <a href="https://canariasconvive.com/mapa-interactivo/"><img src="images/canarias-convive.svg" alt="Mapa de agentes Canarias Convive en producción" width="100%" /></a>
    </td>
    <td width="52%" valign="middle">
      <p>
        <!-- 1+1 forzado: el par status+entidad re-rompía a anchos estrechos
             (el badge de la entidad es el más ancho del README); con <br/>
             queda estable en todo contenedor. -->
        <img src="https://img.shields.io/badge/EN_PRODUCCIÓN-2EA043?style=for-the-badge&labelColor=1a1b27" alt="En producción" />
        <br />
        <img src="https://img.shields.io/badge/Universidad_de_La_Laguna-1a1b27?style=for-the-badge" alt="Universidad de La Laguna" />
      </p>
      <h3>🗺️ Mapa de agentes — Canarias Convive</h3>
      <p>
        El mapa público que sirve <a href="https://canariasconvive.com/mapa-interactivo/"><b>canariasconvive.com</b></a> en producción. Una plataforma de la <b>Universidad de La Laguna</b> (Fundación General) depende de este repositorio para mostrar al público las <b>234 entidades</b> del programa por todo el archipiélago.
      </p>
      <p>
        <b>Mapbox GL JS</b> con estilo <b>custom de Mapbox Studio</b> (paleta corporativa), <b>clustering</b> automático, <b>filtros por sector</b> y <b>vista 3D</b>. Datos servidos desde la API REST oficial. HTML/CSS/JS vanilla, sin frameworks.
      </p>
      <p>
        <!-- 2+3 forzado (líneas ~194/~215px): Mapbox lidera y aguanta sin
             re-romper hasta contenedor ~530px (ventanas de 900px) -->
        <img src="https://img.shields.io/badge/Mapbox_GL_JS-000000?style=flat-square&logo=mapbox&logoColor=white" alt="Mapbox GL JS" />
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
        <br />
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
        <img src="https://img.shields.io/badge/GitHub_Pages-222222?style=flat-square&logo=github&logoColor=white" alt="GitHub Pages" />
      </p>
      <p>
        <a href="https://canariasconvive.com/mapa-interactivo/"><b>🟢 Ver en producción</b></a>
        &nbsp;·&nbsp;
        <a href="https://diegoalegil.github.io/canariasconvive-mapa/"><b>Demo</b></a>
        &nbsp;·&nbsp;
        <a href="https://github.com/diegoalegil/canariasconvive-mapa"><b>Repo →</b></a>
      </p>
    </td>
  </tr>
</table>

---

<!-- ─── MI PROYECTO PRINCIPAL  ✏️ ───────────────────────────────────────── -->
## 🌟 Mi proyecto principal

> El producto donde mejor se ve cómo trabajo: full-stack de cero, decisiones técnicas defendibles y desplegado en producción real.

<!-- ── ⚔️ AnimeShowdown — proyecto estrella ────────────────────────────── -->
<table align="center">
  <tr>
    <td width="32%" valign="top" align="center">
      <a href="https://animeshowdown.dev"><img src="images/AnimeShowdown-banner.svg" alt="AnimeShowdown — banner animado" width="100%" /></a>
    </td>
    <td width="68%" valign="top">
      <h3>⚔️ AnimeShowdown</h3>
      <p>
        <b>Plataforma full-stack de duelos, torneos y ranking ELO de personajes anime.</b> Frontend, API, BBDD, auth y despliegue en producción real — construido de cero.
      </p>
      <p>
        <!-- 2 CTAs, ambos públicos y verificados (200, sin muro de auth). Se
             retiró el botón de Swagger/API: /swagger-ui y /v3/api-docs están
             tras el login OAuth de Spring Security (302 → /login "Please sign
             in"), así que prometía docs navegables y terminaba en un muro —
             peor que no tenerlo. La API REST y su OpenAPI se describen en las
             bullets; el backend es inspeccionable vía CÓDIGO. -->
        <a href="https://animeshowdown.dev"><img src="https://img.shields.io/badge/🌐_WEB_LIVE-CC0808?style=for-the-badge&labelColor=CC0808" alt="Web en vivo de AnimeShowdown" height="28" /></a>
        <a href="https://github.com/diegoalegil/AnimeShowdown"><img src="https://img.shields.io/badge/CÓDIGO-1a1b27?style=for-the-badge&logo=github&logoColor=white" alt="Código fuente de AnimeShowdown en GitHub" height="28" /></a>
      </p>
      <ul>
        <li><b>Ranking ELO</b> que reordena en tiempo real con cada votación y cierre de torneo.</li>
        <li><b>Brackets visuales</b> SVG y resolución transaccional de enfrentamientos por conteo de votos.</li>
        <li><b>Auth completa</b>: JWT con refresh por cookie httpOnly, 2FA TOTP y emails transaccionales.</li>
        <li><b>API REST</b> documentada con OpenAPI 3 + Swagger UI · desplegada en <b>Cloudflare Pages + Railway + Neon</b>.</li>
      </ul>
      <p>
        <!-- 2+3+3 agrupado por capa (frontend / backend / infra). La línea
             más larga (~255px) cabe en la celda del 68% incluso con el
             contenedor a 530px (ventana de 900): el 4+4 anterior rompía ahí
             en 3+1+4 (PostgreSQL huérfano). Vite y Framer Motion fuera:
             tooling/animación que diluía el posicionamiento backend. -->
        <img src="https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React 19" />
        <img src="https://img.shields.io/badge/Tailwind_v4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS v4" />
        <br />
        <img src="https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot 3" />
        <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
        <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT" />
        <br />
        <img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white" alt="Cloudflare" />
        <img src="https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white" alt="Railway" />
        <img src="https://img.shields.io/badge/Neon-00E599?style=flat-square&logo=neon&logoColor=black" alt="Neon" />
      </p>
    </td>
  </tr>
</table>

<!-- ─── 🚧 ESTOY TRABAJANDO EN — sección oculta hasta que Fuerteventura entre en producción ──
     Canarias Convive se promovió a la sección "🚀 En producción" (arriba del todo).
     La tarjeta de Fuerteventura Protagonista (todavía prototipo, con datos placeholder)
     queda guardada aquí para reactivar la sección cuando el proyecto esté listo.
     PARA REACTIVAR: retira este wrapper de comentario, restaura el encabezado
     "## 🚧 Estoy trabajando en" y añade un separador "---" justo encima.

  <table align="center">
    <tr>
      <td width="50%" valign="middle" align="center">
        <a href="https://diegoalegil.github.io/fuerteventuraprotagonista-mapa/"><img src="images/fuerteventura-mapa.jpg" alt="Mapa de agentes Fuerteventura Protagonista · prototipo con paleta marrón" width="100%" /></a>
      </td>
      <td width="50%" valign="middle">
        <h3>🏝️ Mapa de agentes — Fuerteventura Protagonista</h3>
        <p>
          <b>Mismo enfoque, otra isla.</b> Prototipo del mapa público de <b>Fuerteventura Protagonista</b> (Cabildo de Fuerteventura + ULL). Misma base técnica que el de Canarias Convive pero con <b>paleta marrón/tierra</b> y tipografía <b>Libre Baskerville</b> para casar con la identidad del programa.
        </p>
        <p>
          <b>HTML, CSS y JavaScript vanilla</b> sobre <b>Mapbox GL JS 3.21</b> + <b>Turf.js</b> para las geometrías 3D. <b>18 puntos placeholder</b> (ayuntamientos, Cabildo, entidades públicas) a la espera de importar el back-office real.
        </p>
        <p>
          Mapbox GL JS · Turf.js · JavaScript · HTML5 · CSS3 · GitHub Pages
        </p>
        <p>
          Demo: diegoalegil.github.io/fuerteventuraprotagonista-mapa
          · Repo: github.com/diegoalegil/fuerteventuraprotagonista-mapa
        </p>
      </td>
    </tr>
  </table>
─────────────────────────────────────────────────────────────────────────────────────── -->

---

## 🛠️ Stack

<!-- OJO: las tablas de GitHub son shrink-to-fit (CSS width: max-content, que
     pisa cualquier atributo width). Sin anchos % en las celdas, cada columna
     mide lo que su línea más ancha de badges: los <br /> forzados de abajo
     definen el ancho y el reparto queda determinista. No añadas width aquí. -->
<table align="center">
  <tr>
    <td valign="top">
      <h3 align="center">⚙️ Backend</h3>
      <p align="center">
        <!-- 2+1 forzado (igual que Bases de datos): sin <br/> el wrap era
             greedy y PHP caía huérfano de forma no determinista a 530/398px -->
        <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
        <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
        <br />
        <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP" />
      </p>
    </td>
    <td valign="top">
      <h3 align="center">🗄️ Bases de datos</h3>
      <p align="center">
        <!-- 2+1 forzado con la línea larga a ~223px: aguanta también los
             contenedores intermedios (ventana 900px → celda ~239px útiles) -->
        <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
        <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
        <br />
        <img src="https://img.shields.io/badge/CockroachDB-6933FF?style=for-the-badge&logo=cockroachlabs&logoColor=white" alt="CockroachDB" />
      </p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3 align="center">🌐 Web</h3>
      <p align="center">
        <!-- 2+2 forzado, emparejado para que la línea larga (~219px) quepa
             también en los contenedores intermedios (~239px útiles) -->
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
        <br />
        <img src="https://img.shields.io/badge/WordPress-21759B?style=for-the-badge&logo=wordpress&logoColor=white" alt="WordPress" />
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
      </p>
    </td>
    <td valign="top">
      <h3 align="center">🧰 Tooling</h3>
      <p align="center">
        <!-- 2+1 forzado (simétrico con las otras tres celdas): sin <br/> el
             wrap era greedy y GitHub caía huérfano a anchos intermedios -->
        <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
        <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
        <br />
        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
      </p>
    </td>
  </tr>
</table>

---

<!-- ─── APRENDIENDO  ✏️ ──────────────────────────────────────────────────── -->
## 🌱 Aprendiendo ahora

<table align="center">
  <tr>
    <td width="33%" align="center" valign="top">🐘 <b>PL/pgSQL avanzado</b><br/><sub>triggers, procedimientos, ACID</sub></td>
    <td width="34%" align="center" valign="top">🌍 <b>Sistemas distribuidos</b><br/><sub>réplicas y consenso con CockroachDB</sub></td>
    <td width="33%" align="center" valign="top">🔌 <b>APIs REST</b><br/><sub>arquitectura y diseño en Java / Node.js</sub></td>
  </tr>
</table>

---

<!-- ─── DESTACADOS  ✏️ ──────────────────────────────────────────────────── -->
## 💾 Proyectos destacados

<table align="center">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">💳 TinerPay</h3>
      <p align="center">
        Demo de un <b>sistema de pagos distribuido</b>. Replicación, consistencia y transacciones en una base de datos pensada para no caerse.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
        <img src="https://img.shields.io/badge/CockroachDB-6933FF?style=flat-square&logo=cockroachlabs&logoColor=white" alt="CockroachDB" />
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
      </p>
      <p align="center">
        <a href="https://github.com/diegoalegil/TinerPay"><b>Ver código →</b></a>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🐘 postgresql-avanzado</h3>
      <p align="center">
        PL/pgSQL real: <b>triggers, procedimientos almacenados, transacciones ACID</b> y estrategias de backup. Centrado en integridad y concurrencia.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
        <img src="https://img.shields.io/badge/PL%2FpgSQL-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PL/pgSQL" />
      </p>
      <p align="center">
        <a href="https://github.com/diegoalegil/postgresql-avanzado"><b>Ver código →</b></a>
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <sub>También: <a href="https://github.com/diegoalegil/miniature-car-shop">🏎️ <b>miniature-car-shop</b></a> — tienda WooCommerce premium con diseño oscuro y módulos JS/PHP propios.</sub>
</p>

---

## 📊 Stats

<!-- 3 cards: stats + streak arriba (los datos que venden: commits, PRs,
     racha), donut de lenguajes centrado debajo. Sin profile-details: era
     redundante y aireaba "Joined 8 months ago". Sin snake: decoración.
     Todas a height 195 (el CSS de GitHub nunca amplía una imagen por encima
     de su tamaño natural; el height solo sirve para REDUCIR):
     fila 1 → stats 340×200 + streak 400×195 a 195 px = 331 + 400 ≈ 736 ≤ 846 -->
<p align="center">
  <img height="195" src="https://raw.githubusercontent.com/diegoalegil/diegoalegil/output/stats.svg" alt="Resumen de estadísticas de GitHub de Diego" />
  <img height="195" src="https://raw.githubusercontent.com/diegoalegil/diegoalegil/output/streak.svg" alt="Racha de contribuciones de Diego" />
</p>

<p align="center">
  <img height="195" src="https://raw.githubusercontent.com/diegoalegil/diegoalegil/output/repos-per-language.svg" alt="Repositorios por lenguaje de Diego" />
</p>

---

<!-- ─── ACTIVIDAD ─────────────────────────────────────────────────────────
     Gráfico de área con la evolución de contribuciones del último año.
     Base: Ashutosh00710/github-readme-activity-graph (Vercel) — el SVG se
     genera ahí y se post-procesa con scripts/inject-activity-animation.py
     para inyectar animaciones SMIL Apple-style: stroke-draw de la línea
     con easing ease-in-out, fade-in del área tras dibujarse, y aparición
     escalonada de los puntos con un toque de spring. El SVG resultante
     se publica en la rama output (junto con el resto de assets) para que
     las animaciones sobrevivan al paso por el CDN de GitHub.
─────────────────────────────────────────────────────────────────────── -->
## 📈 Actividad

<p align="center">
  <img src="https://raw.githubusercontent.com/diegoalegil/diegoalegil/output/activity.svg" alt="Gráfico animado de contribuciones de Diego del último año" />
</p>


<!-- ─── MANTENIMIENTO (notas internas, no se renderizan) ──────────────────
  - Zonas editables marcadas con ✏️ en los comentarios HTML.
  - Gráfico de actividad y tarjetas de stats los genera y publica en la
    rama output el workflow .github/workflows/activity-graph.yml ("Update
    profile assets") cada noche. Primera vez: Actions → Run workflow.
    El workflow sigue publicando snake y profile-details aunque el README
    ya no los muestra (recorte editorial: el README vende, no decora).
  - Las imágenes viven en images/. Mantén cualquier nueva por debajo de
    ~500 KB (banner máx 1600 px de ancho, ilustraciones pequeñas a 800 px).
  - Acciones de terceros del workflow pineadas por SHA por seguridad de
    supply chain — si actualizas una versión, actualiza también el SHA.
─────────────────────────────────────────────────────────────────────────── -->

<!-- ─── CIERRE  ✏️ ───────────────────────────────────────────────────────── -->
<div align="center">
  <br />
  <br />
  <table align="center" border="0">
    <tr>
      <td width="32%" valign="middle" align="center">
        <img src="images/steve-jobs.png" alt="Steve Jobs · Apple" width="86%" />
      </td>
      <td width="68%" valign="middle">
        <p>
          <i>"Todo lo que te rodea que llamas vida fue hecho por gente que <b>no era más inteligente que tú</b> y lo puedes cambiar, puedes influenciar, puedes <b>construir tus propias cosas que otra gente pueda usar</b>."</i>
        </p>
        <br />
        <p align="right">
          <sub>—&nbsp;&nbsp;<kbd>&nbsp;<b>STEVE&nbsp;JOBS</b>&nbsp;</kbd></sub>&nbsp;&nbsp;
        </p>
      </td>
    </tr>
  </table>
  <br />
  <br />
  <!-- CTA repetido: quien llegó hasta aquí ya está medio convencido;
       este es el momento exacto de darle el botón -->
  <a href="https://diegoalegil.github.io/"><img src="images/conoceme-badge.svg" alt="Conóceme" height="36" /></a>
  <a href="mailto:diegogildam@gmail.com"><img src="images/gmail-badge.svg" alt="Gmail" height="36" /></a>
  <p>
    <sub><a href="mailto:diegogildam@gmail.com">diegogildam@gmail.com</a>&nbsp;·&nbsp;<a href="https://diegoalegil.github.io/">diegoalegil.github.io</a></sub>
  </p>
</div>
