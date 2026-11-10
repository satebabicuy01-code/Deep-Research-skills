const { chromium } = require('playwright');
const path = require('path');
const out = path.resolve(__dirname, '..', 'IKEA_Business_Model_Store_Format_Report_BOD.pdf');
const tmp = path.resolve(__dirname, '_body.pdf'), tmpc = path.resolve(__dirname, '_cover.pdf');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(__dirname, 'report.html'), { waitUntil: 'networkidle' });
  const base = { format: 'A4', printBackground: true, margin: { top: '18mm', bottom: '16mm', left: '16mm', right: '16mm' } };
  await p.pdf({ ...base, path: tmp, displayHeaderFooter: true,
    headerTemplate: '<div style="font-family:Inter;font-size:7px;color:#8A94A3;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>IKEA — Business Model, Store Format &amp; Investment Strategy</span><span>Laporan BOD · Nov 2026</span></div>',
    footerTemplate: '<div style="font-family:Inter;font-size:7px;color:#8A94A3;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>Rahasia — untuk penggunaan internal</span><span class="pageNumber"></span></div>' });
  await p.pdf({ ...base, path: tmpc, pageRanges: '1', margin: { top: '0', bottom: '0', left: '0', right: '0' } });
  await b.close();
})();
