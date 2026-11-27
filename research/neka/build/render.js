const { chromium } = require('playwright');
(async () => {
  const [, , htmlPath, pdfPath, pngPrefix] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 1 });
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  await page.pdf({ path: pdfPath, width: '297mm', height: '210mm', printBackground: true });
  if (pngPrefix) {
    const secs = await page.$$('section.page');
    for (let i = 0; i < secs.length; i++) {
      await secs[i].screenshot({ path: `${pngPrefix}-${String(i + 1).padStart(2, '0')}.png` });
    }
  }
  await browser.close();
})();
