const { chromium } = require('@playwright/test');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  
  const footer = await page.$('.app-footer');
  if (footer) {
    await footer.scrollIntoViewIfNeeded();
    await page.waitForTimeout(800);
    const outPath = path.resolve(__dirname, '../docs/screenshots/01-landing-footer.png');
    await footer.screenshot({ path: outPath });
    console.log('Footer screenshot saved to ' + outPath);
  } else {
    console.error('Footer not found!');
  }

  await browser.close();
})();
