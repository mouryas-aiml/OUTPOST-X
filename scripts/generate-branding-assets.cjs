const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function generate() {
  const markSvgPath = path.resolve(__dirname, '../apps/web/public/branding/outpost-x-mark.svg');
  const markSvg = fs.readFileSync(markSvgPath);

  const iconsDir = path.resolve(__dirname, '../apps/web/public/icons');
  if (!fs.existsSync(iconsDir)) fs.mkdirSync(iconsDir, { recursive: true });

  // 1. icon-192.png
  await sharp(markSvg)
    .resize(192, 192)
    .png()
    .toFile(path.join(iconsDir, 'icon-192.png'));
  console.log('icon-192.png generated');

  // 2. icon-512.png
  await sharp(markSvg)
    .resize(512, 512)
    .png()
    .toFile(path.join(iconsDir, 'icon-512.png'));
  console.log('icon-512.png generated');

  // 3. icon-512-maskable.png (with safe-zone inset padding)
  await sharp(markSvg)
    .resize(410, 410)
    .extend({
      top: 51,
      bottom: 51,
      left: 51,
      right: 51,
      background: { r: 6, g: 13, b: 26, alpha: 1 }
    })
    .png()
    .toFile(path.join(iconsDir, 'icon-512-maskable.png'));
  console.log('icon-512-maskable.png generated');

  // 4. Generate high-res 1200x630 Open Graph banner
  const ogSvg = `
  <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
    <defs>
      <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#050816"/>
        <stop offset="50%" stop-color="#080e22"/>
        <stop offset="100%" stop-color="#0a1530"/>
      </linearGradient>
      <radialGradient id="nebula-cyan" cx="20%" cy="30%" r="50%">
        <stop offset="0%" stop-color="#0284c7" stop-opacity="0.35"/>
        <stop offset="100%" stop-color="#050816" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="nebula-orange" cx="80%" cy="70%" r="60%">
        <stop offset="0%" stop-color="#ea580c" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#050816" stop-opacity="0"/>
      </radialGradient>
      <linearGradient id="glow-grad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#38bdf8"/>
        <stop offset="100%" stop-color="#7dd3fc"/>
      </linearGradient>
      <linearGradient id="dome-g" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.95"/>
        <stop offset="100%" stop-color="#0284c7" stop-opacity="0.6"/>
      </linearGradient>
    </defs>

    <!-- Deep Space Background -->
    <rect width="1200" height="630" fill="url(#bg)"/>
    <rect width="1200" height="630" fill="url(#nebula-cyan)"/>
    <rect width="1200" height="630" fill="url(#nebula-orange)"/>

    <!-- Decorative Grid Lines -->
    <g stroke="rgba(56, 189, 248, 0.08)" stroke-width="1">
      <line x1="0" y1="100" x2="1200" y2="100"/>
      <line x1="0" y1="200" x2="1200" y2="200"/>
      <line x1="0" y1="300" x2="1200" y2="300"/>
      <line x1="0" y1="400" x2="1200" y2="400"/>
      <line x1="0" y1="500" x2="1200" y2="500"/>
      <line x1="200" y1="0" x2="200" y2="630"/>
      <line x1="400" y1="0" x2="400" y2="630"/>
      <line x1="600" y1="0" x2="600" y2="630"/>
      <line x1="800" y1="0" x2="800" y2="630"/>
      <line x1="1000" y1="0" x2="1000" y2="630"/>
    </g>

    <!-- Starfield Particles -->
    <circle cx="95" cy="80" r="1.5" fill="#fff" opacity="0.8"/>
    <circle cx="280" cy="140" r="2" fill="#38bdf8" opacity="0.9"/>
    <circle cx="510" cy="65" r="1.5" fill="#fff" opacity="0.7"/>
    <circle cx="730" cy="180" r="2.5" fill="#fff" opacity="0.9"/>
    <circle cx="920" cy="90" r="1.5" fill="#38bdf8" opacity="0.8"/>
    <circle cx="1110" cy="160" r="2" fill="#fff" opacity="0.8"/>
    <circle cx="150" cy="480" r="1.5" fill="#fff" opacity="0.6"/>
    <circle cx="340" cy="550" r="2" fill="#fff" opacity="0.8"/>
    <circle cx="680" cy="520" r="1.5" fill="#38bdf8" opacity="0.7"/>
    <circle cx="1040" cy="490" r="2" fill="#fff" opacity="0.9"/>
    <circle cx="860" cy="420" r="1.5" fill="#fff" opacity="0.6"/>

    <!-- Left Badge / Logo Mark (Scaled at 220x220) -->
    <g transform="translate(80, 160)">
      <!-- Outer Glow -->
      <circle cx="110" cy="110" r="120" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="2"/>
      <circle cx="110" cy="110" r="95" fill="#0b172e" stroke="rgba(56, 189, 248, 0.4)" stroke-width="2"/>
      <!-- Planet Surface Glow -->
      <ellipse cx="110" cy="155" rx="75" ry="24" fill="#f97316" opacity="0.25"/>
      <line x1="30" y1="155" x2="190" y2="155" stroke="#f97316" stroke-width="2" opacity="0.7"/>
      <!-- Dome -->
      <path d="M72 155 Q72 105 110 102 Q148 105 148 155Z" fill="url(#dome-g)" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Struts -->
      <line x1="110" y1="102" x2="110" y2="155" stroke="#7dd3fc" stroke-width="1.2" opacity="0.5"/>
      <line x1="84" y1="130" x2="136" y2="130" stroke="#7dd3fc" stroke-width="1.2" opacity="0.5"/>
      <!-- Base -->
      <rect x="86" y="152" width="48" height="6" rx="2" fill="#0284c7"/>
      <!-- Dish -->
      <path d="M142 125 Q158 116 162 130" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
      <line x1="142" y1="125" x2="146" y2="155" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M158 112 Q170 107 178 117" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.75"/>
      <!-- Orbit ring -->
      <ellipse cx="110" cy="110" rx="98" ry="30" fill="none" stroke="url(#glow-grad)" stroke-width="2.5" opacity="0.75" transform="rotate(-15 110 110)"/>
      <circle cx="195" cy="95" r="7" fill="#38bdf8"/>
    </g>

    <!-- Main Content Block -->
    <g transform="translate(360, 140)">
      <!-- Eyebrow Pill -->
      <rect x="0" y="0" width="370" height="34" rx="17" fill="rgba(12, 26, 48, 0.85)" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1.5"/>
      <circle cx="18" cy="17" r="4" fill="#38bdf8"/>
      <text x="32" y="22" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="800" fill="#7dd3fc" letter-spacing="2">NEXT-GEN MISSION CONTROL PLATFORM</text>

      <!-- Main Headline: OUTPOST-X -->
      <text x="0" y="105" font-family="Arial Black, Impact, 'Montserrat', sans-serif" font-size="76" font-weight="900" letter-spacing="3">
        <tspan fill="#ffffff">OUTPOST</tspan>
        <tspan fill="#38bdf8">-X</tspan>
      </text>

      <!-- Tagline -->
      <text x="0" y="152" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="700" fill="#e0f2fe" letter-spacing="0.5">
        Take Command. Build Beyond Earth.
      </text>
      <text x="0" y="185" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="600" fill="#94a3b8">
        Shape Humanity’s Next Frontier.
      </text>

      <!-- Subtitle Description -->
      <text x="0" y="225" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" fill="#cbd5e1">
        Authentic planetary habitat simulator powered by real NASA open data &amp; telemetry.
      </text>

      <!-- Feature Pill Badges -->
      <g transform="translate(0, 260)">
        <!-- Badge 1 -->
        <rect x="0" y="0" width="165" height="36" rx="8" fill="rgba(20, 35, 60, 0.7)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
        <text x="14" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">🚀 REALITY DIAL (3 TIERS)</text>

        <!-- Badge 2 -->
        <rect x="180" y="0" width="175" height="36" rx="8" fill="rgba(20, 35, 60, 0.7)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
        <text x="194" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">🛰️ LIVE NASA TELEMETRY</text>

        <!-- Badge 3 -->
        <rect x="370" y="0" width="180" height="36" rx="8" fill="rgba(20, 35, 60, 0.7)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
        <text x="384" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">🌑 LUNAR &amp; MARS BASES</text>

        <!-- Badge 4 -->
        <rect x="565" y="0" width="195" height="36" rx="8" fill="rgba(20, 35, 60, 0.7)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
        <text x="579" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">⚡ 3D HABITAT COCKPIT</text>
      </g>
    </g>

    <!-- Bottom Footer Bar -->
    <rect x="0" y="580" width="1200" height="50" fill="rgba(4, 8, 18, 0.9)"/>
    <line x1="0" y1="580" x2="1200" y2="580" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1"/>
    <text x="80" y="612" font-family="sans-serif" font-size="13" font-weight="600" fill="#64748b">
      © 2026 OUTPOST-X · BUILT BY TEAM XYZ · MISSION-READY PWA
    </text>
    <text x="960" y="612" font-family="sans-serif" font-size="13" font-weight="700" fill="#38bdf8">
      outpostx.vercel.app
    </text>
  </svg>
  `;

  const brandingDir = path.resolve(__dirname, '../apps/web/public/branding');
  if (!fs.existsSync(brandingDir)) fs.mkdirSync(brandingDir, { recursive: true });

  await sharp(Buffer.from(ogSvg))
    .resize(1200, 630)
    .png()
    .toFile(path.join(brandingDir, 'og-preview.png'));
  console.log('og-preview.png (1200x630) generated successfully!');
}

generate().catch(err => {
  console.error('Error generating branding assets:', err);
  process.exit(1);
});
