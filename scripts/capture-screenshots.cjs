const { chromium } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  
  const outDir = path.resolve(__dirname, '../docs/screenshots');
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  // 1. Landing Hero
  console.log('Capturing Landing Hero...');
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, '01-landing-hero.png'), fullPage: false });

  // 2. Click "Launch Outpost" (second CTA button)
  console.log('Clicking Launch Outpost...');
  await page.click('button.modern-hero-cta-btn:not(.modern-hero-play-btn)');
  await new Promise(r => setTimeout(r, 1500));
  await page.screenshot({ path: path.join(outDir, '02-setup-wizard.png'), fullPage: false });
  console.log('02-setup-wizard.png saved');

  // Click Launch in Setup Wizard
  const launchBtn = await page.$('button.setup-launch-btn, button.btn-primary');
  if (launchBtn) {
    console.log('Launching standard mission from setup...');
    await launchBtn.click();
    await new Promise(r => setTimeout(r, 2000));
  }

  // Standard Console Tabs
  const standardTabs = [
    { id: 'power', file: '03-power-console.png' },
    { id: 'lifeSupport', file: '04-lifesupport-console.png' },
    { id: 'comms', file: '05-comms-console.png' },
    { id: 'incidentCommand', file: '06-incident-command.png' },
    { id: 'missionCommand', file: '07-mission-command.png' },
    { id: 'habitat', file: '08-habitat-view.png' },
    { id: 'crisis', file: '09-crisis-view.png' }
  ];

  for (const tab of standardTabs) {
    const selector = `#tab-${tab.id}`;
    const btn = await page.$(selector);
    if (btn) {
      console.log(`Clicking tab ${tab.id}...`);
      await btn.click();
      await new Promise(r => setTimeout(r, 1200));
      await page.screenshot({ path: path.join(outDir, tab.file), fullPage: false });
      console.log(`${tab.file} saved`);
    } else {
      console.log(`Tab ${tab.id} not found`);
    }
  }

  console.log('All standard mission screenshots captured!');
  await browser.close();
})();
