const { chromium } = require(process.env.PW || 'playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(()=>chromium.launch());
  const p = await b.newPage();
  const src = path.resolve(__dirname, 'brand-x-report.html');
  let html = fs.readFileSync(src, 'utf8');
  const pages = process.argv[2] ? JSON.parse(fs.readFileSync(process.argv[2],'utf8')) : {};
  for (const [k,v] of Object.entries(pages)) html = html.replace(`data-for="${k}"></span>`, `data-for="${k}">${v}</span>`);
  fs.writeFileSync('/tmp/claude-0/pdf/render.html', html);
  await p.goto('file:///tmp/claude-0/pdf/render.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fam = await p.evaluate(() => [document.fonts.check('12px "IBM Plex Sans"'), document.fonts.check('700 12px "Source Serif 4"')]);
  console.log('fonts', fam);
  await p.pdf({ path: process.argv[3] || '/tmp/claude-0/pdf/out.pdf', preferCSSPageSize: true, printBackground: true, displayHeaderFooter: false });
  await b.close();
})();
