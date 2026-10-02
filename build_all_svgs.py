import base64
import os

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/avatar.b64', 'r') as f:
    avatar_b64 = f.read().strip()

avatar_uri = f"data:image/png;base64,{avatar_b64}"
github_avatar_url = "https://avatars.githubusercontent.com/u/148122455?v=4"

print("Building all SVGs with real profile photo...")

# ================= 1. HERO.SVG =================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 680" width="100%" height="100%" role="img" aria-label="Tazim Kassar - Full-Stack Architect &amp; AI Developer">
<title>Tazim Kassar — Full-Stack Architect &amp; AI Developer</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }}
.name-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
@keyframes popIn {{ 0% {{ opacity:0; transform:translateY(14px) scale(.7); }} 70% {{ opacity:1; transform:translateY(-3px) scale(1.06); }} 100% {{ opacity:1; transform:translateY(0) scale(1); }} }}
@keyframes blink {{ 0%,49% {{ opacity:1; }} 50%,100% {{ opacity:0; }} }}
@keyframes floaty {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-8px); }} }}
@keyframes floaty2 {{ 0%,100% {{ transform:translateY(0) rotate(0deg); }} 50% {{ transform:translateY(-10px) rotate(3deg); }} }}
@keyframes heartBeat {{ 0%,100% {{ transform:scale(1); }} 12% {{ transform:scale(1.25); }} 24% {{ transform:scale(1); }} 36% {{ transform:scale(1.18); }} 48% {{ transform:scale(1); }} }}
@keyframes neonFlicker {{ 0% {{ opacity:0; }} 5% {{ opacity:.7; }} 7% {{ opacity:.1; }} 10% {{ opacity:.9; }} 12% {{ opacity:.3; }} 16%,100% {{ opacity:1; }} }}
@keyframes neonPulse {{ 0%,100% {{ opacity:.6; }} 50% {{ opacity:1; }} }}
@keyframes twinkle {{ 0%,100% {{ opacity:0; transform:scale(.4); }} 50% {{ opacity:1; transform:scale(1); }} }}
@keyframes rise {{ 0% {{ transform:translateY(0); opacity:0; }} 12% {{ opacity:.55; }} 88% {{ opacity:.55; }} 100% {{ transform:translateY(-46px); opacity:0; }} }}
@keyframes lightTravel {{ 0% {{ stroke-dashoffset: 400; }} 100% {{ stroke-dashoffset: 0; }} }}

.pill {{ transition:transform .2s ease,filter .2s ease; transform-box:fill-box; transform-origin:center; cursor:pointer; }}
.pill:hover {{ transform:scale(1.08); filter:brightness(1.35); }}
.cur {{ animation:blink 1s step-end infinite; }}
.tw {{ transform-box:fill-box; transform-origin:center; animation:twinkle 2.6s ease-in-out infinite; }}
.hb {{ transform-box:fill-box; transform-origin:center; animation:heartBeat 2.2s ease-in-out infinite; }}
.fl {{ animation:floaty 5s ease-in-out infinite; }}
.fl2 {{ transform-box:fill-box; transform-origin:center; animation:floaty2 4.2s ease-in-out infinite; }}
.neon-on {{ animation:neonFlicker 2.4s ease 3.2s backwards; }}
.np {{ animation:neonPulse 2.6s ease-in-out infinite; }}
.rp {{ animation:rise linear infinite; }}
.sep {{ stroke:#2a1f3d; stroke-width:1; opacity:.7; }}
.frame-light {{ stroke-dasharray: 100, 300; animation: lightTravel 3s linear infinite; }}
]]></style>

<!-- Gradients -->
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#090a12"/><stop offset="55%" stop-color="#0f111f"/><stop offset="100%" stop-color="#080810"/>
</linearGradient>
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#a78bfa;#f472b6;#22d3ee" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="55%"><animate attributeName="stop-color" values="#f472b6;#22d3ee;#a78bfa;#f472b6" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#a78bfa;#f472b6;#22d3ee;#a78bfa" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#a78bfa" stop-opacity=".3"/>
  <stop offset="100%" stop-color="#f472b6" stop-opacity=".4"/>
</linearGradient>

<radialGradient id="orbP"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".12"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="orbV"><stop offset="0%" stop-color="#a78bfa" stop-opacity=".15"/><stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/></radialGradient>
<radialGradient id="orbB"><stop offset="0%" stop-color="#f472b6" stop-opacity=".10"/><stop offset="100%" stop-color="#f472b6" stop-opacity="0"/></radialGradient>

<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".6" fill="rgba(34,211,238,.12)"/></pattern>

<!-- Avatar Clip Path -->
<clipPath id="avatarCircle"><circle cx="75" cy="75" r="68"/></clipPath>
<clipPath id="avatarSquare"><rect width="140" height="150" rx="12"/></clipPath>

<!-- Typewriter Clip Paths -->
<clipPath id="cPrompt"><rect x="48" y="42" width="0" height="30"><animate attributeName="width" from="0" to="560" dur="1s" begin=".2s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="78" width="0" height="38"><animate attributeName="width" from="0" to="240" dur=".5s" begin="1.1s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="245" width="0" height="42"><animate attributeName="width" from="0" to="380" dur=".7s" begin="3.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="271" width="0" height="42"><animate attributeName="width" from="0" to="380" dur=".6s" begin="3.9s" fill="freeze"/></rect></clipPath>

<!-- Cycling Roles (4 roles, 24s cycle) -->
<clipPath id="r1"><rect x="48" y="202" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="2.7s"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="202" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="2.7s"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="202" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="2.7s"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="202" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="2.7s"/></rect></clipPath>
</defs>

<!-- Outer Canvas -->
<rect width="1280" height="680" rx="22" fill="url(#bg)"/>
<rect width="1280" height="680" rx="22" fill="url(#dots)"/>
<circle cx="230" cy="220" r="260" fill="url(#orbP)"><animate attributeName="r" values="260;290;260" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1000" cy="480" r="300" fill="url(#orbV)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="120" r="200" fill="url(#orbB)"><animate attributeName="r" values="200;225;200" dur="5.5s" repeatCount="indefinite"/></circle>
<rect x="1" y="1" width="1278" height="678" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- Rising Particles -->
<circle class="rp" cx="140" cy="580" r="1.4" fill="#22d3ee" style="animation-duration:5s"/>
<circle class="rp" cx="420" cy="620" r="1.1" fill="#a78bfa" style="animation-duration:6s;animation-delay:1s"/>
<circle class="rp" cx="620" cy="580" r="1.3" fill="#f472b6" style="animation-duration:4.6s;animation-delay:2s"/>
<circle class="rp" cx="1180" cy="610" r="1.2" fill="#22d3ee" style="animation-duration:5.4s;animation-delay:.6s"/>
<circle class="rp" cx="1240" cy="320" r="1" fill="#a78bfa" style="animation-duration:6.4s;animation-delay:1.6s"/>

<!-- Sparkles -->
<g class="tw" style="animation-delay:.4s"><path d="M470 100l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#38bdf8"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M880 90l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#f472b6"/></g>

<!-- ================= LEFT COLUMN: INFO & TYPOGRAPHY (No Overlap, width <= 660px) ================= -->
<!-- Terminal prompt -->
<text clip-path="url(#cPrompt)" x="48" y="60" font-size="13"><tspan fill="#4ade80" font-weight="bold">tazim@fullstack-architect</tspan><tspan fill="#8b949e">:~$ </tspan><tspan fill="#e6edf3">cat </tspan><tspan fill="#22d3ee">README.md</tspan></text>
<rect x="494" y="47" width="8" height="16" fill="#4ade80" opacity="0"><animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" begin="1.2s"/></rect>

<!-- Hi, I'm -->
<text clip-path="url(#cHi)" x="48" y="102" font-size="22" font-weight="bold" fill="#e6edf3">Hi, I'm 👋</text>

<!-- Name: Tazim Kassar -->
<g transform="translate(48,172)">
  <text class="name-text" font-size="48" font-weight="900" fill="url(#nameg)" filter="url(#glow)">Tazim Kassar</text>
  <g class="hb" transform="translate(325, -28)" style="animation-delay:3s">
    <path d="M12 0 C5 -10 -10 5 0 20 C10 30 12 32 12 32 C12 32 14 30 24 20 C34 5 19 -10 12 0 Z" fill="#f472b6" opacity=".95" filter="url(#glow)"/>
  </g>
</g>

<!-- Cycling Roles -->
<text clip-path="url(#r1)" x="48" y="224" font-size="16" fill="#22d3ee" filter="url(#glow)">&lt; Full-Stack Architect /&gt;</text>
<text clip-path="url(#r2)" x="48" y="224" font-size="16" fill="#a78bfa" filter="url(#glow)">&lt; AI IDE &amp; Copilot Creator /&gt;</text>
<text clip-path="url(#r3)" x="48" y="224" font-size="16" fill="#f472b6" filter="url(#glow)">&lt; Node.js &amp; React Specialist /&gt;</text>
<text clip-path="url(#r4)" x="48" y="224" font-size="16" fill="#38bdf8" filter="url(#glow)">&lt; Cloud &amp; SaaS Systems Architect /&gt;</text>
<rect x="48" y="211" width="2.5" height="16" fill="#22d3ee" opacity="0"><animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="2.7s"/></rect>

<!-- Quote Box -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="248" width="410" height="66" rx="8" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
  <rect x="48" y="252" width="3.5" height="58" rx="1.5" fill="#22d3ee"/>
</g>
<text clip-path="url(#q1)" x="74" y="275" font-size="14" fill="#e6edf3">I don't just write code,</text>
<text clip-path="url(#q2)" x="74" y="299" font-size="14"><tspan fill="#e6edf3">I </tspan><tspan fill="#22d3ee" font-weight="bold">build</tspan><tspan fill="#e6edf3"> AI Web IDEs &amp; Cloud SaaS.</tspan></text>

<!-- Tech I Know Pills -->
<text class="ii" x="48" y="348" font-size="14" fill="#a78bfa" font-weight="bold" style="animation:fadeIn .4s ease 4.2s forwards">🧩 Tech I Know</text>
<g transform="translate(48, 360)">
  <g class="pill" style="animation:fadeIn .3s ease 4.4s forwards"><rect x="0" y="0" width="76" height="24" rx="12" fill="rgba(34,211,238,.14)" stroke="#22d3ee" stroke-width="1"/><text x="38" y="16" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold">React 18</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 4.5s forwards"><rect x="84" y="0" width="70" height="24" rx="12" fill="rgba(167,139,250,.14)" stroke="#a78bfa" stroke-width="1"/><text x="119" y="16" text-anchor="middle" font-size="11" fill="#c084fc" font-weight="bold">Node.js</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 4.6s forwards"><rect x="162" y="0" width="90" height="24" rx="12" fill="rgba(244,114,182,.14)" stroke="#f472b6" stroke-width="1"/><text x="207" y="16" text-anchor="middle" font-size="11" fill="#f9a8d4" font-weight="bold">TypeScript</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 4.7s forwards"><rect x="260" y="0" width="68" height="24" rx="12" fill="rgba(74,222,128,.14)" stroke="#4ade80" stroke-width="1"/><text x="294" y="16" text-anchor="middle" font-size="11" fill="#86efac" font-weight="bold">Python</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="336" y="0" width="78" height="24" rx="12" fill="rgba(16,185,129,.14)" stroke="#10b981" stroke-width="1"/><text x="375" y="16" text-anchor="middle" font-size="11" fill="#6ee7b7" font-weight="bold">MongoDB</text></g>

  <g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="0" y="30" width="65" height="24" rx="12" fill="rgba(2,132,199,.14)" stroke="#0284c7" stroke-width="1"/><text x="32" y="46" text-anchor="middle" font-size="11" fill="#7dd3fc" font-weight="bold">Docker</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="73" y="30" width="130" height="24" rx="12" fill="rgba(251,191,36,.14)" stroke="#fbbf24" stroke-width="1"/><text x="138" y="46" text-anchor="middle" font-size="11" fill="#fde047" font-weight="bold">Monaco &amp; AI Copilots</text></g>
  <g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="211" y="30" width="85" height="24" rx="12" fill="rgba(232,121,249,.14)" stroke="#e879f9" stroke-width="1"/><text x="253" y="46" text-anchor="middle" font-size="11" fill="#f472b6" font-weight="bold">SAST Security</text></g>
</g>

<!-- About Me Bullet Points -->
<text class="ii" x="48" y="450" font-size="14" fill="#f472b6" font-weight="bold" style="animation:fadeIn .4s ease 5.3s forwards">💗 About Me</text>
<text class="ii" x="48" y="472" font-size="12.5" style="animation:fadeIn .4s ease 5.5s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">Building IntelliDev — AI code intelligence &amp; Web IDE platform.</tspan></text>
<text class="ii" x="48" y="494" font-size="12.5" style="animation:fadeIn .4s ease 5.7s forwards"><tspan fill="#fde047">💡 </tspan><tspan fill="#cdd3dd">Always learning, always architecting scalable cloud infrastructure.</tspan></text>
<text class="ii" x="48" y="516" font-size="12.5" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#22d3ee">🚀 </tspan><tspan fill="#cdd3dd">Turning complex ideas into high-performance software applications.</tspan></text>

<!-- Telemetry Stats Card -->
<g class="st" style="animation:fadeIn .5s ease 6.1s forwards">
  <rect x="48" y="534" width="560" height="62" rx="10" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
  <line x1="188" y1="544" x2="188" y2="586" class="sep"/>
  <line x1="328" y1="544" x2="328" y2="586" class="sep"/>
  <line x1="468" y1="544" x2="468" y2="586" class="sep"/>
  <text x="118" y="558" text-anchor="middle" font-size="11" fill="#94a3b8">📦 Repos</text>
  <text x="258" y="558" text-anchor="middle" font-size="11" fill="#94a3b8">💻 Commits</text>
  <text x="398" y="558" text-anchor="middle" font-size="11" fill="#94a3b8">⭐ Stars</text>
  <text x="538" y="558" text-anchor="middle" font-size="11" fill="#94a3b8">👥 Followers</text>
</g>
<text class="st" x="118" y="584" text-anchor="middle" font-size="17" font-weight="bold" fill="#22d3ee" filter="url(#glow)" style="animation:fadeIn .4s ease 6.3s forwards">50+</text>
<text class="st" x="258" y="584" text-anchor="middle" font-size="17" font-weight="bold" fill="#a78bfa" filter="url(#glow)" style="animation:fadeIn .4s ease 6.4s forwards">1.2M+</text>
<text class="st" x="398" y="584" text-anchor="middle" font-size="17" font-weight="bold" fill="#fde047" filter="url(#glow)" style="animation:fadeIn .4s ease 6.5s forwards">1.4k+</text>
<text class="st" x="538" y="584" text-anchor="middle" font-size="17" font-weight="bold" fill="#f472b6" filter="url(#glow)" style="animation:fadeIn .4s ease 6.6s forwards">100+</text>

<!-- ================= RIGHT COLUMN: CODE WINDOW & REAL GITHUB AVATAR CARD (Clean Layout x >= 720) ================= -->

<!-- 1. IDE Code Window (Top Right) -->
<g transform="translate(730, 42)" class="fl2">
  <rect width="500" height="195" rx="10" fill="#111322" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.2"/>
  <!-- Window Header -->
  <circle cx="16" cy="14" r="4.5" fill="#ef4444"/>
  <circle cx="29" cy="14" r="4.5" fill="#f59e0b"/>
  <circle cx="42" cy="14" r="4.5" fill="#10b981"/>
  <text x="250" y="17" text-anchor="middle" font-size="11" fill="#94a3b8">intellidev.jsx</text>
  <line x1="0" y1="28" x2="500" y2="28" stroke="#ffffff" stroke-opacity="0.08"/>

  <!-- Code Snippet -->
  <g transform="translate(16, 46)" font-size="11">
    <text y="0"><tspan fill="#f472b6">function </tspan><tspan fill="#38bdf8">buildIntelliDev</tspan><tspan fill="#cbd5e1">() {{</tspan></text>
    <text y="18" x="12"><tspan fill="#f472b6">return </tspan><tspan fill="#cbd5e1">(</tspan></text>
    <text y="36" x="24"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#22d3ee">Workspace </tspan><tspan fill="#fbbf24">app</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"intellidev"</tspan><tspan fill="#a78bfa">&gt;</tspan></text>
    <text y="54" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#38bdf8">AICopilot </tspan><tspan fill="#fbbf24">model</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"gpt-4o"</tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
    <text y="72" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#f472b6">MonacoEditor </tspan><tspan fill="#fbbf24">theme</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"vs-dark"</tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
    <text y="90" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#10b981">SASTSecurityScanner </tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
    <text y="108" x="24"><tspan fill="#a78bfa">&lt;/</tspan><tspan fill="#22d3ee">Workspace</tspan><tspan fill="#a78bfa">&gt;</tspan></text>
    <text y="126"><tspan fill="#cbd5e1">}} </tspan><tspan fill="#64748b">// export default intellidev</tspan></text>
  </g>
</g>

<!-- 2. Real GitHub Profile Photo Card (Bottom Right - REPLACES ALL ROBOT DRAWINGS!) -->
<g transform="translate(730, 255)" class="fl">
  <!-- Card Backdrop -->
  <rect width="500" height="340" rx="14" fill="#0d0f1c" stroke="url(#borderg)" stroke-width="1.5"/>
  <rect width="500" height="340" rx="14" fill="url(#dots)"/>

  <!-- Left: Real Profile Photo Frame with Traveling Neon Light -->
  <g transform="translate(25, 30)">
    <!-- Photo Frame Outer Backdrop -->
    <rect width="180" height="195" rx="14" fill="#070810" stroke="#1e293b" stroke-width="2"/>
    <!-- Traveling Light Border Animation -->
    <rect width="180" height="195" rx="14" fill="none" stroke="#22d3ee" stroke-width="2.5" class="frame-light" filter="url(#glow)"/>

    <!-- REAL GITHUB PROFILE PHOTO EMBEDDED -->
    <g transform="translate(15, 15)">
      <image href="{avatar_uri}" width="150" height="165" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarSquare)"/>
    </g>

    <!-- Verified Badge -->
    <g transform="translate(145, 160)">
      <circle cx="12" cy="12" r="14" fill="#090a12" stroke="#22d3ee" stroke-width="1.5"/>
      <path d="M7 12 L11 16 L17 8" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/>
    </g>
  </g>

  <!-- Right: Identity Details & Neon Sign -->
  <g transform="translate(230, 30)">
    <!-- Identity Badges -->
    <rect width="245" height="32" rx="6" fill="#16192c" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
    <text x="12" y="21" font-size="11" font-weight="700" fill="#22d3ee">VERIFIED DEVELOPER // #TZ-9042</text>

    <text x="0" y="62" class="name-text" font-size="24" font-weight="900" fill="#ffffff">Tazim Kassar</text>
    <text x="0" y="82" font-size="12" font-weight="700" fill="#a78bfa">@tazimcoder • San Francisco / Remote</text>

    <!-- Neon Sign Box -->
    <g transform="translate(0, 102)" class="neon-on">
      <rect width="245" height="110" rx="12" fill="#090a14" stroke="#f472b6" stroke-opacity="0.7" stroke-width="1.5" filter="url(#glowBig)"/>
      <g transform="translate(122, 35)">
        <text font-size="22" font-weight="bold" fill="#f472b6" text-anchor="middle" filter="url(#glow)">&lt;/&gt;</text>
        <text y="28" font-size="12" font-weight="bold" fill="#22d3ee" text-anchor="middle" letter-spacing="1" class="np">KEEP CODING</text>
        <text y="46" font-size="12" font-weight="bold" fill="#a78bfa" text-anchor="middle" letter-spacing="1" class="np">KEEP GROWING</text>
      </g>
    </g>
  </g>

  <!-- Bottom Badge Row -->
  <g transform="translate(25, 255)">
    <rect width="450" height="55" rx="8" fill="#131628" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
    <!-- Role Tags -->
    <text x="20" y="24" font-size="12" font-weight="700" fill="#38bdf8">⚡ Creator of IntelliDev SaaS &amp; Web IDE</text>
    <text x="20" y="42" font-size="11" fill="#94a3b8">★ Specializing in AI Engines, Node.js, React &amp; Cloud Systems</text>
  </g>
</g>

<!-- ================= FOOTER BAR ================= -->
<g transform="translate(0, 622)">
  <rect x="1" y="0" width="1278" height="57" rx="0" fill="#080911" fill-opacity="0.8"/>
  <line x1="0" y1="0" x2="1280" y2="0" stroke="#ffffff" stroke-opacity="0.08"/>

  <!-- GitHub Link -->
  <g transform="translate(48, 22)">
    <circle cx="10" cy="10" r="9" fill="#0f172a" stroke="#22d3ee" stroke-width="1"/>
    <!-- GitHub Octocat Icon -->
    <path d="M10 4 C6.7 4 4 6.7 4 10 C4 12.6 5.7 14.8 8.1 15.6 C8.4 15.7 8.5 15.5 8.5 15.3 C8.5 15.1 8.5 14.7 8.5 14.2 C6.8 14.6 6.5 13.4 6.5 13.4 C6.2 12.7 5.8 12.5 5.8 12.5 C5.3 12.1 5.9 12.1 5.9 12.1 C6.5 12.2 6.8 12.7 6.8 12.7 C7.3 13.6 8.2 13.4 8.5 13.2 C8.6 12.8 8.7 12.5 8.9 12.3 C7.6 12.2 6.2 11.7 6.2 9.4 C6.2 8.7 6.4 8.2 6.8 7.8 C6.7 7.6 6.5 7 6.9 6.1 C6.9 6.1 7.4 5.9 8.5 6.7 C9 6.6 9.5 6.5 10 6.5 C10.5 6.5 11 6.6 11.5 6.7 C12.6 5.9 13.1 6.1 13.1 6.1 C13.5 7 13.3 7.6 13.2 7.8 C13.6 8.2 13.8 8.7 13.8 9.4 C13.8 11.7 12.4 12.2 11.1 12.3 C11.3 12.5 11.5 12.9 11.5 13.5 C11.5 14.4 11.5 15.1 11.5 15.3 C11.5 15.5 11.6 15.7 11.9 15.6 C14.3 14.8 16 12.6 16 10 C16 6.7 13.3 4 10 4 Z" fill="#22d3ee"/>
    <text x="26" y="14" font-size="12" fill="#cbd5e1" font-weight="bold">tazimcoder</text>
  </g>

  <!-- Email Link -->
  <g transform="translate(200, 22)">
    <rect x="0" y="2" width="16" height="12" rx="2" fill="none" stroke="#f472b6" stroke-width="1.2"/>
    <path d="M0 4 L8 10 L16 4" fill="none" stroke="#f472b6" stroke-width="1.2"/>
    <text x="24" y="14" font-size="12" fill="#cbd5e1">tazimcoder@gmail.com</text>
  </g>

  <!-- Portfolio Link -->
  <g transform="translate(450, 22)">
    <circle cx="8" cy="10" r="7" fill="none" stroke="#a78bfa" stroke-width="1.2"/>
    <text x="22" y="14" font-size="12" fill="#cbd5e1">intellidev.dev</text>
  </g>

  <!-- Open to collaborate status -->
  <g transform="translate(630, 22)">
    <circle cx="8" cy="10" r="4" fill="#4ade80"/>
    <text x="18" y="14" font-size="12" fill="#86efac" font-weight="bold">open to collaborate</text>
  </g>

  <!-- Quote Right -->
  <g transform="translate(1232, 36)">
    <text text-anchor="end" font-size="12" fill="#94a3b8" font-style="italic">"Code is my art, AI is my superpower. ♥"</text>
  </g>
</g>

</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/hero.svg', 'w') as f:
    f.write(hero_svg)

print("✅ hero.svg updated successfully!")


# ================= 2. ABOUT-LIFE.SVG =================
about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 440" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090a10"/>
      <stop offset="100%" stop-color="#0f101b"/>
    </linearGradient>

    <linearGradient id="aurora-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.6"/>
    </linearGradient>

    <pattern id="dot-grid" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.03"/>
    </pattern>

    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glow-pink" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <clipPath id="avatarThumb"><circle cx="20" cy="20" r="16"/></clipPath>

    <style>
      .text-mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
      .text-sans {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
      
      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
      .cursor {{ animation: blink 1s infinite; }}

      @keyframes bar1 {{ 0% {{ width: 0%; }} 30% {{ width: 100%; }} 100% {{ width: 100%; }} }}
      @keyframes bar2 {{ 0%, 33% {{ width: 0%; }} 63% {{ width: 100%; }} 100% {{ width: 100%; }} }}
      @keyframes bar3 {{ 0%, 66% {{ width: 0%; }} 96%, 100% {{ width: 100%; }} }}

      .p-bar1 {{ animation: bar1 12s infinite linear; }}
      .p-bar2 {{ animation: bar2 12s infinite linear; }}
      .p-bar3 {{ animation: bar3 12s infinite linear; }}

      @keyframes slide1 {{ 0%, 30% {{ opacity: 1; transform: translateX(0); }} 33%, 100% {{ opacity: 0; transform: translateX(20px); }} }}
      @keyframes slide2 {{ 0%, 33% {{ opacity: 0; transform: translateX(-20px); }} 36%, 63% {{ opacity: 1; transform: translateX(0); }} 66%, 100% {{ opacity: 0; transform: translateX(20px); }} }}
      @keyframes slide3 {{ 0%, 66% {{ opacity: 0; transform: translateX(-20px); }} 69%, 96% {{ opacity: 1; transform: translateX(0); }} 100% {{ opacity: 0; transform: translateX(20px); }} }}

      .slide-1 {{ animation: slide1 12s infinite ease-in-out; }}
      .slide-2 {{ animation: slide2 12s infinite ease-in-out; }}
      .slide-3 {{ animation: slide3 12s infinite ease-in-out; }}

      @keyframes ring-fill1 {{ 0% {{ stroke-dashoffset: 220; }} 50%, 100% {{ stroke-dashoffset: 35; }} }}
      @keyframes ring-fill2 {{ 0% {{ stroke-dashoffset: 180; }} 50%, 100% {{ stroke-dashoffset: 25; }} }}
      @keyframes ring-fill3 {{ 0% {{ stroke-dashoffset: 140; }} 50%, 100% {{ stroke-dashoffset: 15; }} }}

      .ring-1 {{ stroke-dasharray: 220; animation: ring-fill1 4s ease-out forwards; }}
      .ring-2 {{ stroke-dasharray: 180; animation: ring-fill2 4.5s ease-out forwards; }}
      .ring-3 {{ stroke-dasharray: 140; animation: ring-fill3 5s ease-out forwards; }}
    </style>
  </defs>

  <rect width="900" height="440" rx="16" fill="#06070a"/>

  <!-- LEFT CARD: WHAT I BUILD -->
  <g transform="translate(15, 15)">
    <rect width="425" height="410" rx="14" fill="url(#card-bg)"/>
    <rect width="425" height="410" rx="14" fill="url(#dot-grid)"/>
    <rect width="423" height="408" x="1" y="1" rx="13" fill="none" stroke="url(#aurora-border)" stroke-width="1.2"/>

    <!-- Fake Browser Bar -->
    <path d="M0 14 C0 6.2 6.2 0 14 0 H411 C418.8 0 425 6.2 425 14 V42 H0 Z" fill="#131522"/>
    <line x1="0" y1="42" x2="425" y2="42" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
    <circle cx="20" cy="21" r="5.5" fill="#ff5f56"/>
    <circle cx="36" cy="21" r="5.5" fill="#ffbd2e"/>
    <circle cx="52" cy="21" r="5.5" fill="#27c93f"/>

    <!-- URL Bar -->
    <g transform="translate(75, 9)">
      <rect width="280" height="24" rx="6" fill="#0a0b12" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
      <path d="M12 11 V9 C12 7.3 13.3 6 15 6 C16.7 6 18 7.3 18 9 V11 M10 11 H20 V17 H10 Z" fill="none" stroke="#22d3ee" stroke-width="1.2"/>
      <text x="28" y="16" class="text-mono" font-size="11" fill="#94a3b8">https://tazim.dev/workspace <tspan class="cursor" fill="#22d3ee">█</tspan></text>
    </g>

    <!-- REAL AVATAR THUMBNAIL BADGE -->
    <g transform="translate(370, 1)">
      <circle cx="20" cy="20" r="17" fill="#090a12" stroke="#22d3ee" stroke-width="1.5"/>
      <image href="{avatar_uri}" x="0" y="0" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarThumb)"/>
    </g>

    <!-- Header Title -->
    <g transform="translate(24, 66)">
      <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" fill="#22d3ee" letter-spacing="1.5">⚡ WHAT I BUILD</text>
      <text x="0" y="20" class="text-sans" font-size="18" font-weight="800" fill="#ffffff">Engineering Core Systems</text>
    </g>

    <!-- 3 Capability Rows -->
    <g transform="translate(24, 115)">
      <g transform="translate(0, 0)">
        <rect width="377" height="82" rx="10" fill="#141727" stroke="#22d3ee" stroke-opacity="0.2" stroke-width="1"/>
        <rect x="14" y="14" width="54" height="54" rx="8" fill="#0c1929" stroke="#22d3ee" stroke-width="1.2"/>
        <text x="41" y="48" font-size="24" text-anchor="middle">⚡</text>
        <text x="82" y="34" class="text-sans" font-size="15" font-weight="700" fill="#f8fafc">AI Code Intelligence &amp; IDEs</text>
        <text x="82" y="55" class="text-sans" font-size="12" fill="#94a3b8">Monaco Web IDEs, AST analysis &amp; copilots</text>
      </g>
      <g transform="translate(0, 96)">
        <rect width="377" height="82" rx="10" fill="#141727" stroke="#a78bfa" stroke-opacity="0.2" stroke-width="1"/>
        <rect x="14" y="14" width="54" height="54" rx="8" fill="#19152b" stroke="#a78bfa" stroke-width="1.2"/>
        <text x="41" y="48" font-size="24" text-anchor="middle">🚀</text>
        <text x="82" y="34" class="text-sans" font-size="15" font-weight="700" fill="#f8fafc">Full-Stack SaaS Platforms</text>
        <text x="82" y="55" class="text-sans" font-size="12" fill="#94a3b8">Node.js, Express, React &amp; Microservices</text>
      </g>
      <g transform="translate(0, 192)">
        <rect width="377" height="82" rx="10" fill="#141727" stroke="#f472b6" stroke-opacity="0.2" stroke-width="1"/>
        <rect x="14" y="14" width="54" height="54" rx="8" fill="#241220" stroke="#f472b6" stroke-width="1.2"/>
        <text x="41" y="48" font-size="24" text-anchor="middle">🔒</text>
        <text x="82" y="34" class="text-sans" font-size="15" font-weight="700" fill="#f8fafc">Security &amp; Automated SAST</text>
        <text x="82" y="55" class="text-sans" font-size="12" fill="#94a3b8">Real-time static vulnerability scanning</text>
      </g>
    </g>
    <g transform="translate(24, 382)">
      <text x="0" y="0" class="text-mono" font-size="11" fill="#64748b">git main* | 0 errors | 100% TypeScript/JS</text>
    </g>
  </g>

  <!-- RIGHT CARD: HOBBIES & LIFESTYLE -->
  <g transform="translate(460, 15)">
    <rect width="425" height="410" rx="14" fill="url(#card-bg)"/>
    <rect width="425" height="410" rx="14" fill="url(#dot-grid)"/>
    <rect width="423" height="408" x="1" y="1" rx="13" fill="none" stroke="url(#aurora-border)" stroke-width="1.2"/>

    <!-- Progress Bars -->
    <g transform="translate(24, 20)">
      <rect x="0" y="0" width="118" height="4" rx="2" fill="#1e293b"/>
      <rect x="0" y="0" width="118" height="4" rx="2" fill="#22d3ee" class="p-bar1"/>
      <rect x="128" y="0" width="118" height="4" rx="2" fill="#1e293b"/>
      <rect x="128" y="0" width="118" height="4" rx="2" fill="#a78bfa" class="p-bar2"/>
      <rect x="256" y="0" width="118" height="4" rx="2" fill="#1e293b"/>
      <rect x="256" y="0" width="118" height="4" rx="2" fill="#f472b6" class="p-bar3"/>
    </g>

    <!-- Header Title -->
    <g transform="translate(24, 52)">
      <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" fill="#a78bfa" letter-spacing="1.5">🎨 HOBBIES &amp; LIFESTYLE</text>
      <text x="0" y="20" class="text-sans" font-size="18" font-weight="800" fill="#ffffff">Beyond The Code</text>
    </g>

    <!-- Slides -->
    <g transform="translate(24, 102)">
      <g class="slide-1">
        <rect width="377" height="150" rx="12" fill="#141829" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
        <text x="20" y="40" font-size="32">🎸</text>
        <text x="65" y="38" class="text-sans" font-size="17" font-weight="800" fill="#22d3ee">Synthwave &amp; Audio Crafting</text>
        <text x="20" y="78" class="text-sans" font-size="13" fill="#cbd5e1">Designing electronic soundscapes &amp; synth patches</text>
        <text x="20" y="98" class="text-sans" font-size="13" fill="#cbd5e1">for ambient flow during deep coding sessions.</text>
        <rect x="20" y="114" width="110" height="22" rx="4" fill="#0e2433"/><text x="28" y="129" class="text-mono" font-size="11" fill="#38bdf8">#AudioEngine</text>
      </g>
      <g class="slide-2" opacity="0">
        <rect width="377" height="150" rx="12" fill="#1c162b" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1"/>
        <text x="20" y="40" font-size="32">☕</text>
        <text x="65" y="38" class="text-sans" font-size="17" font-weight="800" fill="#a78bfa">Specialty Espresso Crafting</text>
        <text x="20" y="78" class="text-sans" font-size="13" fill="#cbd5e1">Dialing in precise extractions &amp; single-origin roasts</text>
        <text x="20" y="98" class="text-sans" font-size="13" fill="#cbd5e1">for peak architectural clarity.</text>
        <rect x="20" y="114" width="100" height="22" rx="4" fill="#241a3d"/><text x="28" y="129" class="text-mono" font-size="11" fill="#c084fc">#Espresso</text>
      </g>
      <g class="slide-3" opacity="0">
        <rect width="377" height="150" rx="12" fill="#291526" stroke="#f472b6" stroke-opacity="0.3" stroke-width="1"/>
        <text x="20" y="40" font-size="32">✈️</text>
        <text x="65" y="38" class="text-sans" font-size="17" font-weight="800" fill="#f472b6">Tech Travel &amp; Sci-Fi</text>
        <text x="20" y="78" class="text-sans" font-size="13" fill="#cbd5e1">Exploring global tech summits &amp; reading cyberpunk</text>
        <text x="20" y="98" class="text-sans" font-size="13" fill="#cbd5e1">&amp; speculative AI literature.</text>
        <rect x="20" y="114" width="110" height="22" rx="4" fill="#3b1734"/><text x="28" y="129" class="text-mono" font-size="11" fill="#f472b6">#TechSummits</text>
      </g>
    </g>

    <!-- Daily Progress Rings -->
    <g transform="translate(24, 275)">
      <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" fill="#cbd5e1" letter-spacing="1">⭕ DAILY PROGRESS RINGS</text>
      <g transform="translate(45, 65)">
        <circle cx="0" cy="0" r="35" fill="none" stroke="#1e293b" stroke-width="7"/>
        <circle cx="0" cy="0" r="35" fill="none" stroke="#22d3ee" stroke-width="7" stroke-linecap="round" class="ring-1" transform="rotate(-90)" filter="url(#glow-cyan)"/>
        <text x="0" y="4" class="text-mono" font-size="13" font-weight="800" fill="#22d3ee" text-anchor="middle">95%</text>
        <text x="0" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">Coding</text>
      </g>
      <g transform="translate(188, 65)">
        <circle cx="0" cy="0" r="35" fill="none" stroke="#1e293b" stroke-width="7"/>
        <circle cx="0" cy="0" r="35" fill="none" stroke="#a78bfa" stroke-width="7" stroke-linecap="round" class="ring-2" transform="rotate(-90)"/>
        <text x="0" y="4" class="text-mono" font-size="13" font-weight="800" fill="#a78bfa" text-anchor="middle">88%</text>
        <text x="0" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">Architecture</text>
      </g>
      <g transform="translate(330, 65)">
        <circle cx="0" cy="0" r="35" fill="none" stroke="#1e293b" stroke-width="7"/>
        <circle cx="0" cy="0" r="35" fill="none" stroke="#f472b6" stroke-width="7" stroke-linecap="round" class="ring-3" transform="rotate(-90)"/>
        <text x="0" y="4" class="text-mono" font-size="13" font-weight="800" fill="#f472b6" text-anchor="middle">92%</text>
        <text x="0" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">AI Research</text>
      </g>
    </g>
  </g>
</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/about-life.svg', 'w') as f:
    f.write(about_life_svg)

print("✅ about-life.svg updated successfully!")


# ================= 3. STACK.SVG =================
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stack-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090a10"/>
      <stop offset="50%" stop-color="#0e0f1a"/>
      <stop offset="100%" stop-color="#141224"/>
    </linearGradient>

    <linearGradient id="aurora-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.7"/>
    </linearGradient>

    <pattern id="dot-grid" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.03"/>
    </pattern>

    <filter id="glow-core" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="glow-cyan" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <clipPath id="avatarCore"><circle cx="450" cy="145" r="26"/></clipPath>

    <style>
      .text-mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
      .text-sans {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

      @keyframes orbit-rotate-1 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
      @keyframes orbit-rotate-2 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(-360deg); }} }}
      @keyframes orbit-rotate-3 {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}

      .orbit-path-1 {{ transform-origin: 450px 145px; animation: orbit-rotate-1 20s infinite linear; }}
      .orbit-path-2 {{ transform-origin: 450px 145px; animation: orbit-rotate-2 25s infinite linear; }}
      .orbit-path-3 {{ transform-origin: 450px 145px; animation: orbit-rotate-3 30s infinite linear; }}

      @keyframes moon-orbit {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
      .moon-group {{ transform-origin: 0px 0px; animation: moon-orbit 4s infinite linear; }}

      @keyframes chip-glow-1 {{ 0%, 25% {{ stroke: #22d3ee; stroke-opacity: 1; stroke-width: 1.8; }} 26%, 100% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} }}
      @keyframes chip-glow-2 {{ 0%, 25% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} 26%, 50% {{ stroke: #a78bfa; stroke-opacity: 1; stroke-width: 1.8; }} 51%, 100% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} }}
      @keyframes chip-glow-3 {{ 0%, 50% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} 51%, 75% {{ stroke: #f472b6; stroke-opacity: 1; stroke-width: 1.8; }} 76%, 100% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} }}
      @keyframes chip-glow-4 {{ 0%, 75% {{ stroke: #ffffff; stroke-opacity: 0.1; stroke-width: 1; }} 76%, 100% {{ stroke: #fbbf24; stroke-opacity: 1; stroke-width: 1.8; }} }}

      .chip-box-1 {{ animation: chip-glow-1 8s infinite linear; }}
      .chip-box-2 {{ animation: chip-glow-2 8s infinite linear; }}
      .chip-box-3 {{ animation: chip-glow-3 8s infinite linear; }}
      .chip-box-4 {{ animation: chip-glow-4 8s infinite linear; }}

      @keyframes core-pulse {{ 0%, 100% {{ r: 28px; opacity: 0.9; }} 50% {{ r: 34px; opacity: 1; }} }}
      .atom-core {{ animation: core-pulse 3s infinite ease-in-out; }}
    </style>
  </defs>

  <rect width="900" height="480" rx="16" fill="url(#stack-bg)"/>
  <rect width="900" height="480" rx="16" fill="url(#dot-grid)"/>
  <rect width="898" height="478" x="1" y="1" rx="15" fill="none" stroke="url(#aurora-border)" stroke-width="1.5"/>

  <g transform="translate(35, 32)">
    <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" fill="#22d3ee" letter-spacing="1.5">🪐 TECH ORBIT &amp; STACK ECOSYSTEM</text>
    <text x="0" y="20" class="text-sans" font-size="20" font-weight="800" fill="#ffffff">Architectural Skill Sphere</text>
  </g>

  <!-- TOP SECTION: 3D TECH ORBIT ATOM CORE WITH REAL AVATAR NUCLEUS -->
  <g transform="translate(0, 30)">
    <!-- Atom Core Nucleus with Real Avatar -->
    <g transform="translate(0, 0)">
      <circle cx="450" cy="145" r="38" fill="#22d3ee" fill-opacity="0.15" filter="url(#glow-core)"/>
      <circle cx="450" cy="145" r="28" fill="#090a12" stroke="#22d3ee" stroke-width="2" class="atom-core"/>
      <image href="{avatar_uri}" x="420" y="115" width="60" height="60" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarCore)"/>
    </g>

    <!-- Orbit 1 (Tilted 25 deg) -->
    <g transform="translate(450, 145) rotate(-25)">
      <ellipse cx="0" cy="0" rx="230" ry="70" fill="none" stroke="#22d3ee" stroke-opacity="0.25" stroke-width="1.5" stroke-dasharray="6,6"/>
      <g class="orbit-path-1" transform-origin="0 0">
        <g transform="translate(230, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#22d3ee" stroke-width="1.5" filter="url(#glow-cyan)"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">⚛️</text>
          <g class="moon-group">
            <circle cx="28" cy="0" r="5" fill="#f472b6"/>
            <text x="28" y="2" font-size="6" text-anchor="middle" fill="#ffffff" class="text-mono">v18</text>
            <circle cx="-28" cy="0" r="5" fill="#38bdf8"/>
            <text x="-28" y="2" font-size="6" text-anchor="middle" fill="#ffffff" class="text-mono">TS</text>
          </g>
        </g>
        <g transform="translate(-230, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🟩</text>
        </g>
        <g transform="translate(0, 70)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="0" y="4" class="text-mono" font-size="11" font-weight="800" fill="#38bdf8" text-anchor="middle">TS</text>
        </g>
        <g transform="translate(0, -70)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🐍</text>
        </g>
      </g>
    </g>

    <!-- Orbit 2 (Tilted 35 deg) -->
    <g transform="translate(450, 145) rotate(35)">
      <ellipse cx="0" cy="0" rx="310" ry="85" fill="none" stroke="#a78bfa" stroke-opacity="0.25" stroke-width="1.5" stroke-dasharray="8,6"/>
      <g class="orbit-path-2" transform-origin="0 0">
        <g transform="translate(310, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🍃</text>
        </g>
        <g transform="translate(-310, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🐳</text>
        </g>
        <g transform="translate(0, 85)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🎨</text>
        </g>
        <g transform="translate(0, -85)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#ffffff" stroke-opacity="0.6" stroke-width="1.5"/>
          <text x="0" y="4" class="text-mono" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">N</text>
        </g>
      </g>
    </g>

    <!-- Orbit 3 (Horizontal 0 deg) -->
    <g transform="translate(450, 145)">
      <ellipse cx="0" cy="0" rx="380" ry="100" fill="none" stroke="#f472b6" stroke-opacity="0.2" stroke-width="1.5" stroke-dasharray="10,6"/>
      <g class="orbit-path-3" transform-origin="0 0">
        <g transform="translate(380, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🤖</text>
        </g>
        <g transform="translate(-380, 0)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#e10098" stroke-width="1.5"/>
          <text x="0" y="4" class="text-mono" font-size="10" font-weight="800" fill="#e10098" text-anchor="middle">GQL</text>
        </g>
        <g transform="translate(0, 100)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#336791" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🐘</text>
        </g>
        <g transform="translate(0, -100)">
          <circle cx="0" cy="0" r="18" fill="#0f172a" stroke="#f05032" stroke-width="1.5"/>
          <text x="0" y="5" font-size="14" text-anchor="middle">🌱</text>
        </g>
      </g>
    </g>
  </g>

  <!-- BOTTOM SECTION: GROUPED CHIP GRID -->
  <g transform="translate(30, 290)">
    <text x="5" y="0" class="text-mono" font-size="11" font-weight="700" fill="#94a3b8" letter-spacing="1">SKILL DOMAINS &amp; TOOLING CHIPS:</text>
    <g transform="translate(0, 15)">
      <g transform="translate(0, 0)">
        <rect width="198" height="135" rx="10" fill="#111322" class="chip-box-1"/>
        <text x="14" y="24" class="text-mono" font-size="12" font-weight="700" fill="#22d3ee">[ Frontend ]</text>
        <g transform="translate(14, 38)">
          <rect x="0" y="0" width="75" height="22" rx="4" fill="#1e293b"/><text x="10" y="15" class="text-sans" font-size="11" fill="#cbd5e1">React 18</text>
          <rect x="83" y="0" width="85" height="22" rx="4" fill="#1e293b"/><text x="93" y="15" class="text-sans" font-size="11" fill="#cbd5e1">TypeScript</text>
          <rect x="0" y="28" width="50" height="22" rx="4" fill="#1e293b"/><text x="10" y="43" class="text-sans" font-size="11" fill="#cbd5e1">Vite</text>
          <rect x="58" y="28" width="110" height="22" rx="4" fill="#1e293b"/><text x="68" y="43" class="text-sans" font-size="11" fill="#cbd5e1">Tailwind CSS</text>
          <rect x="0" y="56" width="168" height="22" rx="4" fill="#1e293b"/><text x="10" y="71" class="text-sans" font-size="11" fill="#cbd5e1">Monaco Editor &amp; Recharts</text>
        </g>
      </g>
      <g transform="translate(212, 0)">
        <rect width="198" height="135" rx="10" fill="#111322" class="chip-box-2"/>
        <text x="14" y="24" class="text-mono" font-size="12" font-weight="700" fill="#a78bfa">[ Motion &amp; 3D ]</text>
        <g transform="translate(14, 38)">
          <rect x="0" y="0" width="90" height="22" rx="4" fill="#1e293b"/><text x="10" y="15" class="text-sans" font-size="11" fill="#cbd5e1">SVG + SMIL</text>
          <rect x="98" y="0" width="70" height="22" rx="4" fill="#1e293b"/><text x="108" y="15" class="text-sans" font-size="11" fill="#cbd5e1">Three.js</text>
          <rect x="0" y="28" width="110" height="22" rx="4" fill="#1e293b"/><text x="10" y="43" class="text-sans" font-size="11" fill="#cbd5e1">Framer Motion</text>
          <rect x="118" y="28" width="50" height="22" rx="4" fill="#1e293b"/><text x="126" y="43" class="text-sans" font-size="11" fill="#cbd5e1">CSS3</text>
          <rect x="0" y="56" width="168" height="22" rx="4" fill="#1e293b"/><text x="10" y="71" class="text-sans" font-size="11" fill="#cbd5e1">3D Contribution City</text>
        </g>
      </g>
      <g transform="translate(424, 0)">
        <rect width="206" height="135" rx="10" fill="#111322" class="chip-box-3"/>
        <text x="14" y="24" class="text-mono" font-size="12" font-weight="700" fill="#f472b6">[ Data &amp; Cloud ]</text>
        <g transform="translate(14, 38)">
          <rect x="0" y="0" width="65" height="22" rx="4" fill="#1e293b"/><text x="10" y="15" class="text-sans" font-size="11" fill="#cbd5e1">Node.js</text>
          <rect x="73" y="0" width="105" height="22" rx="4" fill="#1e293b"/><text x="83" y="15" class="text-sans" font-size="11" fill="#cbd5e1">MongoDB/Mongoose</text>
          <rect x="0" y="28" width="80" height="22" rx="4" fill="#1e293b"/><text x="10" y="43" class="text-sans" font-size="11" fill="#cbd5e1">Express.js</text>
          <rect x="88" y="28" width="90" height="22" rx="4" fill="#1e293b"/><text x="98" y="43" class="text-sans" font-size="11" fill="#cbd5e1">REST APIs</text>
          <rect x="0" y="56" width="178" height="22" rx="4" fill="#1e293b"/><text x="10" y="71" class="text-sans" font-size="11" fill="#cbd5e1">Docker &amp; Cloud Deployments</text>
        </g>
      </g>
      <g transform="translate(638, 0)">
        <rect width="202" height="135" rx="10" fill="#111322" class="chip-box-4"/>
        <text x="14" y="24" class="text-mono" font-size="12" font-weight="700" fill="#fbbf24">[ AI &amp; Intelligence ]</text>
        <g transform="translate(14, 38)">
          <rect x="0" y="0" width="90" height="22" rx="4" fill="#1e293b"/><text x="10" y="15" class="text-sans" font-size="11" fill="#cbd5e1">OpenAI SDK</text>
          <rect x="98" y="0" width="75" height="22" rx="4" fill="#1e293b"/><text x="108" y="15" class="text-sans" font-size="11" fill="#cbd5e1">Gemini API</text>
          <rect x="0" y="28" width="173" height="22" rx="4" fill="#1e293b"/><text x="10" y="43" class="text-sans" font-size="11" fill="#cbd5e1">AST Code Analyzers</text>
          <rect x="0" y="56" width="173" height="22" rx="4" fill="#1e293b"/><text x="10" y="71" class="text-sans" font-size="11" fill="#cbd5e1">SAST Vulnerability Engines</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/stack.svg', 'w') as f:
    f.write(stack_svg)

print("✅ stack.svg updated successfully!")


# ================= 4. ID-DASHBOARD.SVG =================
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 460" width="100%" height="100%">
  <defs>
    <linearGradient id="dash-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090a10"/>
      <stop offset="50%" stop-color="#0d0e17"/>
      <stop offset="100%" stop-color="#141122"/>
    </linearGradient>

    <linearGradient id="aurora-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.8"/>
    </linearGradient>

    <pattern id="dot-grid" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.03"/>
    </pattern>

    <linearGradient id="holo-foil" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0">
        <animate attributeName="stop-opacity" values="0;0.6;0" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#f472b6" stop-opacity="0.4">
        <animate attributeName="stop-opacity" values="0.4;0.8;0.4" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#a78bfa" stop-opacity="0">
        <animate attributeName="stop-opacity" values="0;0.6;0" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="gold-chip" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#fef08a"/>
    </linearGradient>

    <linearGradient id="bar-grad-cyan" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#083344"/>
      <stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>

    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <clipPath id="avatarIdSquare"><rect width="140" height="150" rx="10"/></clipPath>

    <style>
      .text-mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
      .text-sans {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

      @keyframes pendulum-swing {{
        0% {{ transform: rotate(0deg); }}
        20% {{ transform: rotate(4deg); }}
        40% {{ transform: rotate(-3deg); }}
        60% {{ transform: rotate(2deg); }}
        80% {{ transform: rotate(-1deg); }}
        100% {{ transform: rotate(0deg); }}
      }}
      .badge-swing {{ transform-origin: 155px 0px; animation: pendulum-swing 6s ease-in-out infinite; }}

      @keyframes light-travel {{
        0% {{ stroke-dashoffset: 320; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      .frame-light {{ stroke-dasharray: 80, 240; animation: light-travel 3s linear infinite; }}

      @keyframes bar-grow-1 {{ 0% {{ height: 0px; y: 150px; }} 100% {{ height: 120px; y: 30px; }} }}
      @keyframes bar-grow-2 {{ 0% {{ height: 0px; y: 150px; }} 100% {{ height: 95px; y: 55px; }} }}
      @keyframes bar-grow-3 {{ 0% {{ height: 0px; y: 150px; }} 100% {{ height: 75px; y: 75px; }} }}
      @keyframes bar-grow-4 {{ 0% {{ height: 0px; y: 150px; }} 100% {{ height: 60px; y: 90px; }} }}

      .bar-1 {{ animation: bar-grow-1 1.5s ease-out forwards; }}
      .bar-2 {{ animation: bar-grow-2 1.8s ease-out forwards; }}
      .bar-3 {{ animation: bar-grow-3 2.1s ease-out forwards; }}
      .bar-4 {{ animation: bar-grow-4 2.4s ease-out forwards; }}

      @keyframes pulse-dot {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.4; transform: scale(1.3); }} }}
      .live-dot {{ animation: pulse-dot 1.5s infinite ease-in-out; transform-origin: center; }}
    </style>
  </defs>

  <rect width="900" height="460" rx="16" fill="url(#dash-bg)"/>
  <rect width="900" height="460" rx="16" fill="url(#dot-grid)"/>
  <rect width="898" height="458" x="1" y="1" rx="15" fill="none" stroke="url(#aurora-border)" stroke-width="1.5"/>

  <!-- LEFT SIDE: SWINGING HOLOGRAPHIC ID BADGE WITH REAL GITHUB AVATAR -->
  <g class="badge-swing" transform="translate(25, 0)">
    <path d="M135 -20 L135 35 L175 35 L175 -20 Z" fill="#1e1b4b"/>
    <text x="155" y="15" class="text-mono" font-size="7" font-weight="700" fill="#a78bfa" text-anchor="middle" transform="rotate(90 155 15)">INTELLIDEV</text>

    <rect x="142" y="32" width="26" height="14" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="1"/>
    <circle cx="155" cy="42" r="4" fill="#090a10"/>

    <g transform="translate(20, 48)">
      <rect width="270" height="380" rx="16" fill="#0c0e18" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.5"/>
      <rect width="270" height="380" rx="16" fill="url(#holo-foil)"/>
      <rect width="268" height="378" x="1" y="1" rx="15" fill="none" stroke="url(#aurora-border)" stroke-width="1"/>

      <path d="M0 16 C0 7.2 7.2 0 16 0 H254 C262.8 0 270 7.2 270 16 V50 H0 Z" fill="#16182c"/>
      <text x="135" y="24" class="text-mono" font-size="10" font-weight="800" fill="#22d3ee" text-anchor="middle" letter-spacing="1">INTELLIDEV ARCHITECT</text>
      <text x="135" y="38" class="text-mono" font-size="9" fill="#94a3b8" text-anchor="middle">VERIFIED IDENTITY // ID-9042</text>

      <!-- REAL GITHUB AVATAR PHOTO FRAME -->
      <g transform="translate(65, 65)">
        <rect width="140" height="150" rx="10" fill="#090a10" stroke="#1e293b" stroke-width="2"/>
        <rect width="140" height="150" rx="10" fill="none" stroke="#22d3ee" stroke-width="2" class="frame-light" filter="url(#glow-cyan)"/>
        <image href="{avatar_uri}" x="0" y="0" width="140" height="150" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarIdSquare)"/>
      </g>

      <g transform="translate(25, 230)">
        <rect width="36" height="28" rx="4" fill="url(#gold-chip)" stroke="#b45309" stroke-width="1"/>
        <path d="M0 14 H36 M18 0 V28 M10 0 V28 M26 0 V28" stroke="#78350f" stroke-width="0.8"/>
      </g>

      <g transform="translate(75, 232)">
        <text x="0" y="0" class="text-sans" font-size="16" font-weight="900" fill="#ffffff">Tazim Kassar</text>
        <text x="0" y="16" class="text-mono" font-size="11" fill="#38bdf8" font-weight="600">Senior Platform Engineer</text>
      </g>

      <!-- Barcode -->
      <g transform="translate(25, 290)">
        <rect x="0" y="0" width="220" height="35" rx="4" fill="#ffffff"/>
        <g fill="#000000">
          <rect x="10" y="5" width="3" height="25"/><rect x="15" y="5" width="1" height="25"/><rect x="18" y="5" width="4" height="25"/><rect x="24" y="5" width="2" height="25"/><rect x="28" y="5" width="5" height="25"/><rect x="35" y="5" width="1" height="25"/><rect x="38" y="5" width="3" height="25"/><rect x="43" y="5" width="6" height="25"/><rect x="51" y="5" width="2" height="25"/><rect x="55" y="5" width="4" height="25"/><rect x="61" y="5" width="1" height="25"/><rect x="64" y="5" width="5" height="25"/><rect x="71" y="5" width="3" height="25"/><rect x="76" y="5" width="2" height="25"/><rect x="80" y="5" width="6" height="25"/><rect x="88" y="5" width="2" height="25"/><rect x="92" y="5" width="4" height="25"/><rect x="98" y="5" width="1" height="25"/><rect x="101" y="5" width="5" height="25"/><rect x="108" y="5" width="3" height="25"/><rect x="113" y="5" width="2" height="25"/><rect x="117" y="5" width="6" height="25"/><rect x="125" y="5" width="2" height="25"/><rect x="129" y="5" width="4" height="25"/><rect x="135" y="5" width="1" height="25"/><rect x="138" y="5" width="5" height="25"/><rect x="145" y="5" width="3" height="25"/><rect x="150" y="5" width="2" height="25"/><rect x="154" y="5" width="6" height="25"/><rect x="162" y="5" width="2" height="25"/><rect x="166" y="5" width="4" height="25"/><rect x="172" y="5" width="1" height="25"/><rect x="175" y="5" width="5" height="25"/><rect x="182" y="5" width="3" height="25"/><rect x="187" y="5" width="2" height="25"/><rect x="191" y="5" width="6" height="25"/><rect x="199" y="5" width="2" height="25"/><rect x="203" y="5" width="4" height="25"/>
        </g>
        <text x="110" y="32" class="text-mono" font-size="7" fill="#000000" text-anchor="middle" font-weight="700">TAZIMCODER-9042-AUTH-OK</text>
      </g>
      <text x="135" y="358" class="text-mono" font-size="10" fill="#a78bfa" font-weight="700" text-anchor="middle">★ TOP CONTRIBUTOR ★</text>
    </g>
  </g>

  <!-- RIGHT SIDE: DASHBOARD METRICS & REPO CHART -->
  <g transform="translate(335, 30)">
    <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" fill="#22d3ee" letter-spacing="1.5">📊 METRICS &amp; REPOSITORY DASHBOARD</text>
    <text x="0" y="20" class="text-sans" font-size="20" font-weight="800" fill="#ffffff">Live Platform Telemetry</text>

    <g transform="translate(0, 38)">
      <g transform="translate(0, 0)">
        <rect width="165" height="70" rx="10" fill="#131627" stroke="#22d3ee" stroke-opacity="0.2" stroke-width="1"/>
        <text x="16" y="32" class="text-mono" font-size="24" font-weight="900" fill="#22d3ee" filter="url(#glow-cyan)">99.9%</text>
        <text x="16" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8">Platform Uptime</text>
      </g>
      <g transform="translate(180, 0)">
        <rect width="165" height="70" rx="10" fill="#131627" stroke="#a78bfa" stroke-opacity="0.2" stroke-width="1"/>
        <text x="16" y="32" class="text-mono" font-size="24" font-weight="900" fill="#a78bfa">50+</text>
        <text x="16" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8">Active Repositories</text>
      </g>
      <g transform="translate(360, 0)">
        <rect width="170" height="70" rx="10" fill="#131627" stroke="#f472b6" stroke-opacity="0.2" stroke-width="1"/>
        <text x="16" y="32" class="text-mono" font-size="24" font-weight="900" fill="#f472b6">1.2M+</text>
        <text x="16" y="52" class="text-sans" font-size="11" font-weight="600" fill="#94a3b8">Lines of Code</text>
      </g>
    </g>

    <g transform="translate(0, 130)">
      <rect width="530" height="185" rx="12" fill="#0f111d" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
      <text x="20" y="24" class="text-mono" font-size="12" font-weight="700" fill="#cbd5e1">MOST STARRED &amp; IMPACT REPOSITORIES</text>
      <g transform="translate(20, 35)">
        <line x1="0" y1="30" x2="490" y2="30" stroke="#ffffff" stroke-opacity="0.05"/>
        <line x1="0" y1="60" x2="490" y2="60" stroke="#ffffff" stroke-opacity="0.05"/>
        <line x1="0" y1="90" x2="490" y2="90" stroke="#ffffff" stroke-opacity="0.05"/>
        <line x1="0" y1="120" x2="490" y2="120" stroke="#ffffff" stroke-opacity="0.1"/>

        <g transform="translate(30, 0)">
          <rect x="0" y="0" width="55" height="120" rx="6" fill="url(#bar-grad-cyan)" class="bar-1"/>
          <text x="27" y="-5" class="text-mono" font-size="11" font-weight="800" fill="#22d3ee" text-anchor="middle">1.4k ★</text>
          <text x="27" y="136" class="text-sans" font-size="11" font-weight="600" fill="#cbd5e1" text-anchor="middle">IntelliDev</text>
        </g>
        <g transform="translate(150, 0)">
          <rect x="0" y="25" width="55" height="95" rx="6" fill="url(#bar-grad-cyan)" class="bar-2"/>
          <text x="27" y="20" class="text-mono" font-size="11" font-weight="800" fill="#22d3ee" text-anchor="middle">980 ★</text>
          <text x="27" y="136" class="text-sans" font-size="11" font-weight="600" fill="#cbd5e1" text-anchor="middle">AI-Engine</text>
        </g>
        <g transform="translate(270, 0)">
          <rect x="0" y="45" width="55" height="75" rx="6" fill="url(#bar-grad-cyan)" class="bar-3"/>
          <text x="27" y="40" class="text-mono" font-size="11" font-weight="800" fill="#22d3ee" text-anchor="middle">720 ★</text>
          <text x="27" y="136" class="text-sans" font-size="11" font-weight="600" fill="#cbd5e1" text-anchor="middle">Web-IDE</text>
        </g>
        <g transform="translate(390, 0)">
          <rect x="0" y="60" width="55" height="60" rx="6" fill="url(#bar-grad-cyan)" class="bar-4"/>
          <text x="27" y="55" class="text-mono" font-size="11" font-weight="800" fill="#22d3ee" text-anchor="middle">540 ★</text>
          <text x="27" y="136" class="text-sans" font-size="11" font-weight="600" fill="#cbd5e1" text-anchor="middle">SAST-Scanner</text>
        </g>
      </g>
    </g>

    <g transform="translate(0, 332)">
      <rect width="530" height="72" rx="10" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
      <circle cx="20" cy="24" r="5" fill="#22d3ee" class="live-dot" filter="url(#glow-cyan)"/>
      <text x="34" y="28" class="text-mono" font-size="12" font-weight="800" fill="#22d3ee">NOW FOCUSING ON:</text>
      <text x="20" y="50" class="text-sans" font-size="13" font-weight="600" fill="#f8fafc">
        ⚡ Building IntelliDev AI IDE &amp; high-performance code intelligence platform.
      </text>
    </g>
  </g>
</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/id-dashboard.svg', 'w') as f:
    f.write(id_dashboard_svg)

print("✅ id-dashboard.svg updated successfully!")


# ================= 5. CONNECT.SVG =================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 240" width="100%" height="100%">
  <defs>
    <linearGradient id="connect-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090a10"/>
      <stop offset="50%" stop-color="#0e0f1b"/>
      <stop offset="100%" stop-color="#141022"/>
    </linearGradient>

    <linearGradient id="aurora-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.8"/>
    </linearGradient>

    <pattern id="dot-grid" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.03"/>
    </pattern>

    <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <clipPath id="avatarConnect"><rect width="100" height="110" rx="14"/></clipPath>

    <style>
      .text-mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
      .text-sans {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

      @keyframes arrow-nudge {{
        0%, 100% {{ transform: translateX(0px); }}
        50% {{ transform: translateX(6px); }}
      }}
      .nudge-arrow {{ animation: arrow-nudge 1.5s ease-in-out infinite; }}

      @keyframes neon-flicker {{
        0%, 100% {{ opacity: 1; filter: drop-shadow(0 0 8px #22d3ee); }}
        50% {{ opacity: 0.85; filter: drop-shadow(0 0 14px #f472b6); }}
      }}
      .neon-sign {{ animation: neon-flicker 3s infinite ease-in-out; }}

      @keyframes sparkle-float {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.8; }}
        50% {{ transform: translateY(-5px) rotate(15deg); opacity: 1; }}
      }}
      .sparkle {{ animation: sparkle-float 2.5s infinite ease-in-out; transform-origin: center; }}
    </style>
  </defs>

  <rect width="900" height="240" rx="16" fill="url(#connect-bg)"/>
  <rect width="900" height="240" rx="16" fill="url(#dot-grid)"/>
  <rect width="898" height="238" x="1" y="1" rx="15" fill="none" stroke="url(#aurora-border)" stroke-width="1.5"/>

  <!-- LEFT SIDE: REAL GITHUB AVATAR PHOTO & NEON SIGN -->
  <g transform="translate(30, 20)">
    <!-- Real Avatar Sticker Box -->
    <g transform="translate(20, 20)">
      <rect width="100" height="110" rx="14" fill="#090a12" stroke="#22d3ee" stroke-width="2" filter="url(#neon-glow)"/>
      <image href="{avatar_uri}" x="0" y="0" width="100" height="110" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarConnect)"/>
    </g>

    <!-- Glowing Neon Handwritten Sign -->
    <g transform="translate(145, 45)" class="neon-sign">
      <rect width="260" height="64" rx="12" fill="#0c0d16" stroke="#22d3ee" stroke-opacity="0.6" stroke-width="1.5"/>
      <text x="130" y="38" class="text-mono" font-size="20" font-weight="900" fill="#22d3ee" text-anchor="middle" letter-spacing="1">[tazimcoder]</text>
      <text x="130" y="54" class="text-mono" font-size="9" fill="#f472b6" text-anchor="middle">★ CONNECT &amp; BUILD ★</text>
      <path d="M-10 10 L-5 15 L-10 20 L-15 15 Z" fill="#f472b6" class="sparkle"/>
      <path d="M270 40 L274 44 L270 48 L266 44 Z" fill="#22d3ee" class="sparkle"/>
    </g>
  </g>

  <!-- RIGHT SIDE: LINK CARDS (2x2 GRID WITH NUDGING ARROWS) -->
  <g transform="translate(450, 25)">
    <text x="0" y="0" class="text-mono" font-size="11" font-weight="700" fill="#a78bfa" letter-spacing="1">⚡ GET IN TOUCH / SOCIAL NETWORKS</text>

    <g transform="translate(0, 12)">
      <!-- Card 1: GitHub -->
      <a href="https://github.com/tazimcoder" target="_blank">
        <g transform="translate(0, 0)">
          <rect width="205" height="75" rx="10" fill="#131525" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
          <circle cx="28" cy="37" r="16" fill="#0f172a" stroke="#22d3ee" stroke-width="1"/>
          <path d="M28 27 C22.5 27 18 31.5 18 37 C18 41.4 20.8 45.1 24.7 46.4 C25.2 46.5 25.4 46.2 25.4 45.9 C25.4 45.6 25.4 44.9 25.4 44 C22.7 44.6 22.1 42.7 22.1 42.7 C21.7 41.6 21 41.3 21 41.3 C20.1 40.7 21.1 40.7 21.1 40.7 C22.1 40.8 22.6 41.7 22.6 41.7 C23.5 43.2 24.9 42.8 25.4 42.5 C25.5 41.9 25.7 41.4 26 41.1 C23.8 40.9 21.5 40 21.5 36.2 C21.5 35.1 21.9 34.2 22.5 33.5 C22.4 33.3 22 32.2 22.6 30.8 C22.6 30.8 23.5 30.5 25.4 31.8 C26.2 31.6 27.1 31.5 28 31.5 C28.9 31.5 29.8 31.6 30.6 31.8 C32.5 30.5 33.4 30.8 33.4 30.8 C34 32.2 33.6 33.3 33.5 33.5 C34.1 34.2 34.5 35.1 34.5 36.2 C34.5 40.1 32.2 40.8 30 41.1 C30.4 41.4 30.7 42 30.7 43 C30.7 44.4 30.7 45.5 30.7 45.9 C30.7 46.2 30.9 46.5 31.4 46.4 C35.3 45.1 38 41.4 38 37 C38 31.5 33.5 27 28 27 Z" fill="#ffffff"/>
          <text x="54" y="32" class="text-sans" font-size="14" font-weight="800" fill="#ffffff">GitHub</text>
          <text x="54" y="50" class="text-mono" font-size="10" fill="#94a3b8">@tazimcoder</text>
          <g class="nudge-arrow" transform="translate(170, 32)">
            <path d="M0 5 H14 M9 0 L14 5 L9 10" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round"/>
          </g>
        </g>
      </a>

      <!-- Card 2: IntelliDev -->
      <a href="https://intellidev.dev" target="_blank">
        <g transform="translate(220, 0)">
          <rect width="205" height="75" rx="10" fill="#131525" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1"/>
          <circle cx="28" cy="37" r="16" fill="#0f172a" stroke="#a78bfa" stroke-width="1"/>
          <path d="M28 23 C20.3 23 14 29.3 14 37 C14 44.7 20.3 51 28 51 C35.7 51 42 44.7 42 37 C42 29.3 35.7 23 28 23 Z M28 26 C30 29 31.5 33 31.8 37 C31.5 41 30 45 28 48 C26 45 24.5 41 24.2 37 C24.5 33 26 29 28 26 Z M17 37 C17.5 34.5 20.2 32.5 28 32.5 C35.8 32.5 38.5 34.5 39 37 C38.5 39.5 35.8 41.5 28 41.5 C20.2 41.5 17.5 39.5 17 37 Z" fill="#a78bfa"/>
          <text x="54" y="32" class="text-sans" font-size="14" font-weight="800" fill="#ffffff">IntelliDev Platform</text>
          <text x="54" y="50" class="text-mono" font-size="10" fill="#94a3b8">intellidev.dev</text>
          <g class="nudge-arrow" transform="translate(170, 32)">
            <path d="M0 5 H14 M9 0 L14 5 L9 10" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"/>
          </g>
        </g>
      </a>

      <!-- Card 3: Email -->
      <a href="mailto:tazimcoder@gmail.com" target="_blank">
        <g transform="translate(0, 88)">
          <rect width="205" height="75" rx="10" fill="#131525" stroke="#f472b6" stroke-opacity="0.3" stroke-width="1"/>
          <circle cx="28" cy="37" r="16" fill="#0f172a" stroke="#f472b6" stroke-width="1"/>
          <path d="M18 29 H38 V45 H18 Z M18 29 L28 37 L38 29" fill="none" stroke="#f472b6" stroke-width="2" stroke-linejoin="round"/>
          <text x="54" y="32" class="text-sans" font-size="14" font-weight="800" fill="#ffffff">Email Me</text>
          <text x="54" y="50" class="text-mono" font-size="10" fill="#94a3b8">tazimcoder@gmail.com</text>
          <g class="nudge-arrow" transform="translate(170, 32)">
            <path d="M0 5 H14 M9 0 L14 5 L9 10" fill="none" stroke="#f472b6" stroke-width="2" stroke-linecap="round"/>
          </g>
        </g>
      </a>

      <!-- Card 4: LinkedIn -->
      <a href="https://linkedin.com/in/tazimcoder" target="_blank">
        <g transform="translate(220, 88)">
          <rect width="205" height="75" rx="10" fill="#131525" stroke="#38bdf8" stroke-opacity="0.3" stroke-width="1"/>
          <circle cx="28" cy="37" r="16" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
          <path d="M20 32 H24 V44 H20 Z M22 26 C20.8 26 20 26.8 20 28 C20 29.2 20.8 30 22 30 C23.2 30 24 29.2 22 30 C24 26.8 23.2 26 22 26 Z M26 32 H30 V34 H30.1 C30.7 32.9 32.1 31.8 34.2 31.8 C38.5 31.8 39.3 34.6 39.3 38.3 V44 H35.3 V39 C35.3 37.3 35.3 35.2 33 35.2 C30.7 35.2 30.3 37 30.3 38.9 V44 H26.3 V32 Z" fill="#38bdf8"/>
          <text x="54" y="32" class="text-sans" font-size="14" font-weight="800" fill="#ffffff">LinkedIn</text>
          <text x="54" y="50" class="text-mono" font-size="10" fill="#94a3b8">/in/tazimcoder</text>
          <g class="nudge-arrow" transform="translate(170, 32)">
            <path d="M0 5 H14 M9 0 L14 5 L9 10" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
          </g>
        </g>
      </a>
    </g>
  </g>
</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/connect.svg', 'w') as f:
    f.write(connect_svg)

print("✅ connect.svg updated successfully!")
