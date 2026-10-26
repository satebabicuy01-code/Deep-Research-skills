// Rakit ebook: render sampul dan isi ke PDF dengan Chromium (Playwright).
// Jalankan dari root repo: node ebook/scripts/build_pdf.js
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const SRC = path.join(ROOT, 'src');
const BUILD = path.join(ROOT, 'build');

(async () => {
  const fs = require('fs');
  fs.mkdirSync(BUILD, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file://' + path.join(SRC, 'cover.html'), { waitUntil: 'networkidle' });
  await page.pdf({ path: path.join(BUILD, 'cover.pdf'), format: 'A4', printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }, preferCSSPageSize: true });

  await page.goto('file://' + path.join(SRC, 'buku.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const footer = `<div style="width:100%;font-family:Inter,Arial,sans-serif;font-size:7.5px;color:#5b6878;
      padding:0 18mm;display:flex;justify-content:space-between">
      <span>Membaca Dunia 2026 · Edisi terverifikasi · data per 26 Okt 2026</span>
      <span>Bukan saran investasi · <span class="pageNumber"></span></span></div>`;
  await page.pdf({ path: path.join(BUILD, 'isi.pdf'), format: 'A4', printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: footer,
    margin: { top: '20mm', right: '18mm', bottom: '22mm', left: '18mm' } });

  await browser.close();
  console.log('ok');
})();
