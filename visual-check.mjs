// visual-check.mjs — bucle de verificación visual con Playwright
// Uso:    node visual-check.mjs [baseURL]
// Setup (una vez):  npm i -D playwright  &&  npx playwright install chromium
//
// Este repo: captura el README de perfil renderizado por grip (localhost:6419)
// con el CSS real de GitHub. Ver CLAUDE.md para el bucle completo.
// Lo único que se cambia por proyecto es el bloque CONFIG.
import { chromium } from 'playwright';
import { mkdirSync, rmSync } from 'fs';

// ════════════════════════════════════════════════
//  CONFIG — lo único que cambias por proyecto
// ════════════════════════════════════════════════
const CONFIG = {
  baseURL: process.argv[2] || 'http://localhost:6419',
  routes: [
    { name: 'readme', path: '' },
  ],
  viewports: [
    { name: 'ancho',    width: 1280, height: 900 },  // contenedor grip = 830px ≈ 846px reales del README en github.com
    { name: 'medio',    width: 900,  height: 900 },  // ventana medio encogida: en vivo el contenedor cae a ~530px y los badges re-rompen
    { name: 'estrecho', width: 480,  height: 900 },  // app móvil de GitHub: aquí sufren las tablas
  ],
  geolocation: null,
  waitUntil: 'networkidle',
  extraWaitMs: 1500,   // shields.io, skillicons y los SVG de la rama output cargan por red
  autoScroll: true,
  fullPage: true,
};
// ════════════════════════════════════════════════

async function autoScroll(page) {
  await page.evaluate(() => new Promise((resolve) => {
    // scroll-behavior: smooth haría que scrollBy anime y nunca llegue abajo:
    // lo anulamos durante el barrido y medimos la posición real, no un contador.
    const prev = document.documentElement.style.scrollBehavior;
    document.documentElement.style.scrollBehavior = 'auto';
    const id = setInterval(() => {
      window.scrollBy(0, 500);
      const bottom = window.scrollY + window.innerHeight;
      if (bottom >= document.documentElement.scrollHeight - 1) {
        clearInterval(id);
        window.scrollTo(0, 0);
        document.documentElement.style.scrollBehavior = prev;
        resolve();
      }
    }, 80);
  }));
  await page.waitForTimeout(800);
}

const base = CONFIG.baseURL.endsWith('/') ? CONFIG.baseURL : CONFIG.baseURL + '/';

rmSync('shots', { recursive: true, force: true });
mkdirSync('shots', { recursive: true });

const browser = await chromium.launch();
const ctxOpts = {};
if (CONFIG.geolocation) {
  ctxOpts.geolocation = CONFIG.geolocation;
  ctxOpts.permissions = ['geolocation'];
}
const context = await browser.newContext(ctxOpts);

for (const vp of CONFIG.viewports) {
  const page = await context.newPage();
  await page.setViewportSize({ width: vp.width, height: vp.height });
  for (const route of CONFIG.routes) {
    const url = new URL(route.path.replace(/^\//, ''), base).href;
    try {
      await page.goto(url, { waitUntil: CONFIG.waitUntil, timeout: 30000 });
    } catch { /* seguimos aunque networkidle no llegue a estabilizarse */ }
    if (CONFIG.extraWaitMs) await page.waitForTimeout(CONFIG.extraWaitMs);
    if (CONFIG.autoScroll) await autoScroll(page);
    await page.screenshot({
      path: `shots/${route.name}-${vp.name}.png`,
      fullPage: CONFIG.fullPage,
    });
    console.log(`  ✓ ${route.name}-${vp.name}`);
  }
  await page.close();
}

await browser.close();
console.log('\n✓ Listo. Capturas en ./shots');
