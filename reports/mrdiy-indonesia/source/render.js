const { chromium } = require('playwright');
(async () => {
  const [,, html, pdf] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.pdf({ path: pdf, format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-family:Inter,sans-serif;font-size:7px;color:#898781;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>MR.D.I.Y. Indonesia · Laporan BOD · Internal &amp; Rahasia</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '14mm', bottom: '16mm', left: '15mm', right: '15mm' } });
  await browser.close();
})();
