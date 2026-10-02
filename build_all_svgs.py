import base64
import os

avatar_b64_path = '/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/avatar.b64'
with open(avatar_b64_path, 'r') as f:
    avatar_b64 = f.read().strip()

avatar_uri = f"data:image/png;base64,{avatar_b64}"

print("Building all 5 NEXT-LEVEL SVGs matching Megha Mittal's profile layout for Tazim Kassar...")

# ================= 1. HERO.SVG (Width: 1280, Height: 680) =================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 680" width="100%" height="100%" role="img" aria-label="Tazim Kassar - Full-Stack Architect &amp; Software Developer">
<title>Tazim Kassar — Full-Stack Architect &amp; Software Developer</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }}
.name-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
@keyframes popIn {{ 0% {{ opacity:0; transform:translateY(14px) scale(.7); }} 70% {{ opacity:1; transform:translateY(-3px) scale(1.06); }} 100% {{ opacity:1; transform:translateY(0) scale(1); }} }}
@keyframes blink {{ 0%,49% {{ opacity:1; }} 50%,100% {{ opacity:0; }} }}
@keyframes floaty {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-8px); }} }}
@keyframes floaty2 {{ 0%,100% {{ transform:translateY(0) rotate(0deg); }} 50% {{ transform:translateY(-10px) rotate(2deg); }} }}
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
.fl {{ animation:floaty 5s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }}
.fl2 {{ animation:floaty2 4.2s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }}
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

<!-- Avatar Clip Paths -->
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

<!-- ================= LEFT COLUMN: INFO & TYPOGRAPHY ================= -->
<g transform="translate(0, 0)">
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
  <text clip-path="url(#r2)" x="48" y="224" font-size="16" fill="#a78bfa" filter="url(#glow)">&lt; React.js &amp; Node.js Engineer /&gt;</text>
  <text clip-path="url(#r3)" x="48" y="224" font-size="16" fill="#f472b6" filter="url(#glow)">&lt; C++ &amp; Python Systems Dev /&gt;</text>
  <text clip-path="url(#r4)" x="48" y="224" font-size="16" fill="#38bdf8" filter="url(#glow)">&lt; SQL &amp; Database Architect /&gt;</text>
  <rect x="48" y="211" width="2.5" height="16" fill="#22d3ee" opacity="0"><animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="2.7s"/></rect>

  <!-- Quote Box -->
  <g style="animation:fadeIn .5s ease 3.2s forwards">
    <rect x="48" y="248" width="410" height="66" rx="8" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
    <rect x="48" y="252" width="3.5" height="58" rx="1.5" fill="#22d3ee"/>
  </g>
  <text clip-path="url(#q1)" x="74" y="275" font-size="14" fill="#e6edf3">I don't just write code,</text>
  <text clip-path="url(#q2)" x="74" y="299" font-size="14"><tspan fill="#e6edf3">I </tspan><tspan fill="#22d3ee" font-weight="bold">architect</tspan><tspan fill="#e6edf3"> full-stack &amp; AI systems.</tspan></text>

  <!-- TECH I KNOW PILLS -->
  <text class="ii" x="48" y="348" font-size="14" fill="#a78bfa" font-weight="bold" style="animation:fadeIn .4s ease 4.2s forwards">🧩 Tech I Know</text>
  <g transform="translate(48, 360)">
    <g class="pill" style="animation:fadeIn .3s ease 4.4s forwards"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"><rect x="0" y="0" width="60" height="24" rx="12" fill="rgba(227,79,38,.14)" stroke="#e34f26" stroke-width="1"/><text x="30" y="16" text-anchor="middle" font-size="11" fill="#ff8a65" font-weight="bold">HTML</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.5s forwards"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><rect x="68" y="0" width="54" height="24" rx="12" fill="rgba(38,119,189,.14)" stroke="#38bdf8" stroke-width="1"/><text x="95" y="16" text-anchor="middle" font-size="11" fill="#7dd3fc" font-weight="bold">CSS</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.6s forwards"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"><rect x="130" y="0" width="46" height="24" rx="12" fill="rgba(247,223,30,.14)" stroke="#f7df1e" stroke-width="1"/><text x="153" y="16" text-anchor="middle" font-size="11" fill="#fde047" font-weight="bold">JS</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.7s forwards"><a xlink:href="https://react.dev/" target="_blank"><rect x="184" y="0" width="82" height="24" rx="12" fill="rgba(34,211,238,.14)" stroke="#22d3ee" stroke-width="1"/><text x="225" y="16" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold">REACT.JS</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><a xlink:href="https://nodejs.org/" target="_blank"><rect x="274" y="0" width="76" height="24" rx="12" fill="rgba(167,139,250,.14)" stroke="#a78bfa" stroke-width="1"/><text x="312" y="16" text-anchor="middle" font-size="11" fill="#c084fc" font-weight="bold">NODE.JS</text></a></g>

    <g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><a xlink:href="https://www.postgresql.org/" target="_blank"><rect x="0" y="30" width="52" height="24" rx="12" fill="rgba(244,114,182,.14)" stroke="#f472b6" stroke-width="1"/><text x="26" y="46" text-anchor="middle" font-size="11" fill="#f9a8d4" font-weight="bold">SQL</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><a xlink:href="https://isocpp.org/" target="_blank"><rect x="60" y="30" width="54" height="24" rx="12" fill="rgba(59,130,246,.14)" stroke="#3b82f6" stroke-width="1"/><text x="87" y="46" text-anchor="middle" font-size="11" fill="#93c5fd" font-weight="bold">C++</text></a></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><a xlink:href="https://python.org" target="_blank"><rect x="122" y="30" width="76" height="24" rx="12" fill="rgba(74,222,128,.14)" stroke="#4ade80" stroke-width="1"/><text x="160" y="46" text-anchor="middle" font-size="11" fill="#86efac" font-weight="bold">PYTHON</text></a></g>
  </g>

  <!-- About Me Bullet Points -->
  <text class="ii" x="48" y="450" font-size="14" fill="#f472b6" font-weight="bold" style="animation:fadeIn .4s ease 5.3s forwards">💗 About Me</text>
  <text class="ii" x="48" y="472" font-size="12.5" style="animation:fadeIn .4s ease 5.5s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">Building IntelliDev — AI code intelligence &amp; Web IDE platform.</tspan></text>
  <text class="ii" x="48" y="494" font-size="12.5" style="animation:fadeIn .4s ease 5.7s forwards"><tspan fill="#fde047">💡 </tspan><tspan fill="#cdd3dd">Proficient in C++, Python, SQL, React.js &amp; Node.js architecture.</tspan></text>
  <text class="ii" x="48" y="516" font-size="12.5" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#22d3ee">🚀 </tspan><tspan fill="#cdd3dd">Turning complex logic into high-performance software applications.</tspan></text>

  <!-- Telemetry Stats Card -->
  <g style="animation:fadeIn .5s ease 6.1s forwards">
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
</g>

<!-- ================= RIGHT COLUMN: CODE WINDOW & REAL GITHUB AVATAR CARD ================= -->
<g transform="translate(710, 42)">
  <g class="fl2">
    <rect width="520" height="195" rx="10" fill="#111322" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.2"/>
    <circle cx="16" cy="14" r="4.5" fill="#ef4444"/>
    <circle cx="29" cy="14" r="4.5" fill="#f59e0b"/>
    <circle cx="42" cy="14" r="4.5" fill="#10b981"/>
    <text x="260" y="17" text-anchor="middle" font-size="11" fill="#94a3b8">intellidev.jsx</text>
    <line x1="0" y1="28" x2="520" y2="28" stroke="#ffffff" stroke-opacity="0.08"/>

    <g transform="translate(16, 46)" font-size="11">
      <text y="0"><tspan fill="#f472b6">function </tspan><tspan fill="#38bdf8">buildIntelliDev</tspan><tspan fill="#cbd5e1">() {{</tspan></text>
      <text y="18" x="12"><tspan fill="#f472b6">return </tspan><tspan fill="#cbd5e1">(</tspan></text>
      <text y="36" x="24"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#22d3ee">Workspace </tspan><tspan fill="#fbbf24">skills</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"C++, Python, React, Node"</tspan><tspan fill="#a78bfa">&gt;</tspan></text>
      <text y="54" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#38bdf8">AICopilot </tspan><tspan fill="#fbbf24">model</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"gpt-4o"</tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
      <text y="72" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#f472b6">MonacoEditor </tspan><tspan fill="#fbbf24">theme</tspan><tspan fill="#cbd5e1">=</tspan><tspan fill="#4ade80">"vs-dark"</tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
      <text y="90" x="36"><tspan fill="#a78bfa">&lt;</tspan><tspan fill="#10b981">SQLDatabaseEngine </tspan><tspan fill="#a78bfa">/&gt;</tspan></text>
      <text y="108" x="24"><tspan fill="#a78bfa">&lt;/</tspan><tspan fill="#22d3ee">Workspace</tspan><tspan fill="#a78bfa">&gt;</tspan></text>
      <text y="126"><tspan fill="#cbd5e1">}} </tspan><tspan fill="#64748b">// export default intellidev</tspan></text>
    </g>
  </g>
</g>

<!-- Real GitHub Profile Photo Card (Bottom Right) -->
<g transform="translate(710, 255)">
  <g class="fl">
    <rect width="520" height="340" rx="14" fill="#0d0f1c" stroke="url(#borderg)" stroke-width="1.5"/>
    <rect width="520" height="340" rx="14" fill="url(#dots)"/>

    <!-- Left: Real Profile Photo Frame with Traveling Neon Light -->
    <g transform="translate(25, 30)">
      <rect width="180" height="195" rx="14" fill="#070810" stroke="#1e293b" stroke-width="2"/>
      <rect width="180" height="195" rx="14" fill="none" stroke="#22d3ee" stroke-width="2.5" class="frame-light" filter="url(#glow)"/>
      <g transform="translate(15, 15)">
        <image href="{avatar_uri}" width="150" height="165" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarSquare)"/>
      </g>
      <g transform="translate(145, 160)">
        <circle cx="12" cy="12" r="14" fill="#090a12" stroke="#22d3ee" stroke-width="1.5"/>
        <path d="M7 12 L11 16 L17 8" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/>
      </g>
    </g>

    <!-- Right: Identity Details & Neon Sign -->
    <g transform="translate(230, 30)">
      <rect width="265" height="32" rx="6" fill="#16192c" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
      <text x="14" y="21" font-size="11" font-weight="700" fill="#22d3ee">VERIFIED DEVELOPER // #TZ-9042</text>

      <text x="0" y="62" class="name-text" font-size="24" font-weight="900" fill="#ffffff">Tazim Kassar</text>
      <text x="0" y="82" font-size="12" font-weight="700" fill="#a78bfa">@tazimcoder • San Francisco / Remote</text>

      <!-- Neon Sign Box -->
      <g transform="translate(0, 102)" class="neon-on">
        <rect width="265" height="110" rx="12" fill="#090a14" stroke="#f472b6" stroke-opacity="0.7" stroke-width="1.5" filter="url(#glowBig)"/>
        <g transform="translate(132, 35)">
          <text font-size="22" font-weight="bold" fill="#f472b6" text-anchor="middle" filter="url(#glow)">&lt;/&gt;</text>
          <text y="28" font-size="12" font-weight="bold" fill="#22d3ee" text-anchor="middle" letter-spacing="1" class="np">KEEP CODING</text>
          <text y="46" font-size="12" font-weight="bold" fill="#a78bfa" text-anchor="middle" letter-spacing="1" class="np">KEEP GROWING</text>
        </g>
      </g>
    </g>

    <!-- Bottom Badge Row -->
    <g transform="translate(25, 255)">
      <rect width="470" height="55" rx="8" fill="#131628" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
      <text x="20" y="24" font-size="12" font-weight="700" fill="#38bdf8">⚡ Creator of IntelliDev SaaS &amp; Web IDE</text>
      <text x="20" y="42" font-size="11" fill="#94a3b8">★ Core Stack: C++, Python, SQL, React.js, Node.js, HTML &amp; CSS</text>
    </g>
  </g>
</g>

<!-- ================= FOOTER BAR ================= -->
<g transform="translate(0, 622)">
  <rect x="1" y="0" width="1278" height="57" rx="0" fill="#080911" fill-opacity="0.8"/>
  <line x1="0" y1="0" x2="1280" y2="0" stroke="#ffffff" stroke-opacity="0.08"/>

  <g transform="translate(48, 22)">
    <a xlink:href="https://github.com/tazimcoder" target="_blank">
      <circle cx="10" cy="10" r="9" fill="#0f172a" stroke="#22d3ee" stroke-width="1"/>
      <path d="M10 4 C6.7 4 4 6.7 4 10 C4 12.6 5.7 14.8 8.1 15.6 C8.4 15.7 8.5 15.5 8.5 15.3 C8.5 15.1 8.5 14.7 8.5 14.2 C6.8 14.6 6.5 13.4 6.5 13.4 C6.2 12.7 5.8 12.5 5.8 12.5 C5.3 12.1 5.9 12.1 5.9 12.1 C6.5 12.2 6.8 12.7 6.8 12.7 C7.3 13.6 8.2 13.4 8.5 13.2 C8.6 12.8 8.7 12.5 8.9 12.3 C7.6 12.2 6.2 11.7 6.2 9.4 C6.2 8.7 6.4 8.2 6.8 7.8 C6.7 7.6 6.5 7 6.9 6.1 C6.9 6.1 7.4 5.9 8.5 6.7 C9 6.6 9.5 6.5 10 6.5 C10.5 6.5 11 6.6 11.5 6.7 C12.6 5.9 13.1 6.1 13.1 6.1 C13.5 7 13.3 7.6 13.2 7.8 C13.6 8.2 13.8 8.7 13.8 9.4 C13.8 11.7 12.4 12.2 11.1 12.3 C11.3 12.5 11.5 12.9 11.5 13.5 C11.5 14.4 11.5 15.1 11.5 15.3 C11.5 15.5 11.6 15.7 11.9 15.6 C14.3 14.8 16 12.6 16 10 C16 6.7 13.3 4 10 4 Z" fill="#22d3ee"/>
      <text x="26" y="14" font-size="12" fill="#cbd5e1" font-weight="bold">tazimcoder</text>
    </a>
  </g>

  <g transform="translate(200, 22)">
    <a xlink:href="mailto:tazimcoder@gmail.com" target="_blank">
      <rect x="0" y="2" width="16" height="12" rx="2" fill="none" stroke="#f472b6" stroke-width="1.2"/>
      <path d="M0 4 L8 10 L16 4" fill="none" stroke="#f472b6" stroke-width="1.2"/>
      <text x="24" y="14" font-size="12" fill="#cbd5e1">tazimcoder@gmail.com</text>
    </a>
  </g>

  <g transform="translate(450, 22)">
    <a xlink:href="https://intellidev.dev" target="_blank">
      <circle cx="8" cy="10" r="7" fill="none" stroke="#a78bfa" stroke-width="1.2"/>
      <text x="22" y="14" font-size="12" fill="#cbd5e1">intellidev.dev</text>
    </a>
  </g>

  <g transform="translate(630, 22)">
    <circle cx="8" cy="10" r="4" fill="#4ade80"/>
    <text x="18" y="14" font-size="12" fill="#86efac" font-weight="bold">open to collaborate</text>
  </g>

  <g transform="translate(1232, 36)">
    <text text-anchor="end" font-size="12" fill="#94a3b8" font-style="italic">"Code is my art, AI is my superpower. ♥"</text>
  </g>
</g>

</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/hero.svg', 'w') as f:
    f.write(hero_svg)


# ================= 2. STACK.SVG (Width: 900, Height: 480) - MATCHING IMAGE 1 =================
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 480" width="100%" height="100%" role="img" aria-label="Tools I build with - Tech Stack Ecosystem">
<title>Tools I build with — Tech Stack Ecosystem</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, monospace; }}
.title-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes spin1 {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
@keyframes spin2 {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(-360deg); }} }}
@keyframes pulseCore {{ 0%,100% {{ transform: scale(1); filter: drop-shadow(0 0 15px rgba(167,139,250,.6)); }} 50% {{ transform: scale(1.06); filter: drop-shadow(0 0 25px rgba(34,211,238,.9)); }} }}
@keyframes floatBadge {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-4px); }} }}

.orbit1 {{ transform-box: fill-box; transform-origin: center; animation: spin1 20s linear infinite; }}
.orbit2 {{ transform-box: fill-box; transform-origin: center; animation: spin2 25s linear infinite; }}
.orbit3 {{ transform-box: fill-box; transform-origin: center; animation: spin1 18s linear infinite; }}
.core-pulse {{ transform-box: fill-box; transform-origin: center; animation: pulseCore 4s ease-in-out infinite; }}
.tech-chip {{ transition: transform .2s ease, filter .2s ease; cursor: pointer; }}
.tech-chip:hover {{ transform: scale(1.06); filter: brightness(1.3); }}
]]></style>

<linearGradient id="bgS" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0b0d19"/><stop offset="100%" stop-color="#070811"/>
</linearGradient>
<linearGradient id="coreG" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#a78bfa"/><stop offset="50%" stop-color="#f472b6"/><stop offset="100%" stop-color="#22d3ee"/>
</linearGradient>
<radialGradient id="glowR"><stop offset="0%" stop-color="#a78bfa" stop-opacity=".4"/><stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/></radialGradient>

<filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dotsS" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r=".5" fill="rgba(255,255,255,.08)"/></pattern>

<clipPath id="avatarCircleS"><circle cx="40" cy="40" r="38"/></clipPath>
</defs>

<!-- Background -->
<rect width="900" height="480" rx="18" fill="url(#bgS)" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1.5"/>
<rect width="900" height="480" rx="18" fill="url(#dotsS)"/>

<!-- Header -->
<g transform="translate(45, 45)">
  <text font-size="12" font-weight="700" fill="#22d3ee" letter-spacing="1.5">// TECH STACK</text>
  <text class="title-text" x="0" y="32" font-size="28" font-weight="800" fill="#ffffff">Tools I build with</text>
</g>

<!-- LEFT SIDE: 3D ATOM NUCLEUS WITH REAL AVATAR CORE (x=210, y=280) -->
<g transform="translate(210, 280)">
  <!-- Glow backdrop -->
  <circle cx="0" cy="0" r="140" fill="url(#glowR)"/>

  <!-- Tilted Orbits -->
  <g class="orbit1">
    <ellipse cx="0" cy="0" rx="145" ry="55" fill="none" stroke="#22d3ee" stroke-dasharray="6,6" stroke-width="1.5" opacity=".7"/>
    <!-- Electron badge HTML5 -->
    <g transform="translate(145, 0)">
      <circle cx="0" cy="0" r="14" fill="#e34f26" stroke="#ffffff" stroke-width="1"/>
      <text y="4" text-anchor="middle" font-size="9" fill="#ffffff" font-weight="bold">H5</text>
    </g>
    <g transform="translate(-145, 0)">
      <circle cx="0" cy="0" r="14" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
      <text y="4" text-anchor="middle" font-size="9" fill="#ffffff" font-weight="bold">CSS</text>
    </g>
  </g>

  <g class="orbit2">
    <ellipse cx="0" cy="0" rx="150" ry="60" transform="rotate(60)" fill="none" stroke="#a78bfa" stroke-dasharray="6,6" stroke-width="1.5" opacity=".7"/>
    <g transform="translate(0, 150)">
      <circle cx="0" cy="0" r="14" fill="#f7df1e" stroke="#000000" stroke-width="1"/>
      <text y="4" text-anchor="middle" font-size="9" fill="#000000" font-weight="bold">JS</text>
    </g>
    <g transform="translate(0, -150)">
      <circle cx="0" cy="0" r="14" fill="#3178c6" stroke="#ffffff" stroke-width="1"/>
      <text y="4" text-anchor="middle" font-size="9" fill="#ffffff" font-weight="bold">TS</text>
    </g>
  </g>

  <g class="orbit3">
    <ellipse cx="0" cy="0" rx="140" ry="55" transform="rotate(-60)" fill="none" stroke="#f472b6" stroke-dasharray="6,6" stroke-width="1.5" opacity=".7"/>
    <g transform="translate(140, 0)">
      <circle cx="0" cy="0" r="14" fill="#61dafb" stroke="#000000" stroke-width="1"/>
      <text y="4" text-anchor="middle" font-size="9" fill="#000000" font-weight="bold">R</text>
    </g>
  </g>

  <!-- Core Nucleus with Real Avatar Photo -->
  <g class="core-pulse">
    <circle cx="0" cy="0" r="48" fill="url(#coreG)"/>
    <circle cx="0" cy="0" r="44" fill="#090a12"/>
    <g transform="translate(-40, -40)">
      <image href="{avatar_uri}" width="80" height="80" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarCircleS)"/>
    </g>
  </g>
</g>


<!-- RIGHT SIDE: CATEGORIZED TECH PILLS (x=410, y=110) -->
<g transform="translate(410, 110)">

  <!-- 1. FRONTEND -->
  <g transform="translate(0, 0)">
    <line x1="0" y1="6" x2="14" y2="6" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>
    <text x="22" y="10" font-size="11" font-weight="700" fill="#22d3ee" letter-spacing="1">FRONTEND</text>

    <g transform="translate(0, 22)">
      <!-- HTML5 -->
      <g class="tech-chip" transform="translate(0,0)"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"><rect width="82" height="32" rx="8" fill="#131627" stroke="#e34f26" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">HTML5</text></a></g>
      <!-- CSS -->
      <g class="tech-chip" transform="translate(90,0)"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><rect width="68" height="32" rx="8" fill="#131627" stroke="#38bdf8" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">CSS</text></a></g>
      <!-- JS -->
      <g class="tech-chip" transform="translate(166,0)"><a xlink:href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"><rect width="112" height="32" rx="8" fill="#131627" stroke="#f7df1e" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">JavaScript</text></a></g>
      <!-- TS -->
      <g class="tech-chip" transform="translate(286,0)"><a xlink:href="https://www.typescriptlang.org/" target="_blank"><rect width="112" height="32" rx="8" fill="#131627" stroke="#3178c6" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">TypeScript</text></a></g>
      <!-- React -->
      <g class="tech-chip" transform="translate(406,0)"><a xlink:href="https://react.dev/" target="_blank"><rect width="76" height="32" rx="8" fill="#131627" stroke="#61dafb" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">React</text></a></g>
    </g>
  </g>

  <!-- 2. MOTION & 3D -->
  <g transform="translate(0, 85)">
    <line x1="0" y1="6" x2="14" y2="6" stroke="#a78bfa" stroke-width="3" stroke-linecap="round"/>
    <text x="22" y="10" font-size="11" font-weight="700" fill="#a78bfa" letter-spacing="1">MOTION &amp; 3D</text>

    <g transform="translate(0, 22)">
      <g class="tech-chip" transform="translate(0,0)"><a xlink:href="https://gsap.com/" target="_blank"><rect width="78" height="32" rx="8" fill="#131627" stroke="#00ef63" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">GSAP</text></a></g>
      <g class="tech-chip" transform="translate(86,0)"><a xlink:href="https://framer.com/" target="_blank"><rect width="84" height="32" rx="8" fill="#131627" stroke="#0055ff" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Framer</text></a></g>
      <g class="tech-chip" transform="translate(178,0)"><a xlink:href="https://threejs.org/" target="_blank"><rect width="96" height="32" rx="8" fill="#131627" stroke="#ffffff" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Three.js</text></a></g>
    </g>
  </g>

  <!-- 3. DATA & ENTERPRISE -->
  <g transform="translate(0, 170)">
    <line x1="0" y1="6" x2="14" y2="6" stroke="#fde047" stroke-width="3" stroke-linecap="round"/>
    <text x="22" y="10" font-size="11" font-weight="700" fill="#fde047" letter-spacing="1">DATA &amp; ENTERPRISE</text>

    <g transform="translate(0, 22)">
      <g class="tech-chip" transform="translate(0,0)"><a xlink:href="https://www.postgresql.org/" target="_blank"><rect width="68" height="32" rx="8" fill="#131627" stroke="#f472b6" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">SQL</text></a></g>
      <g class="tech-chip" transform="translate(76,0)"><a xlink:href="https://isocpp.org/" target="_blank"><rect width="68" height="32" rx="8" fill="#131627" stroke="#3b82f6" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">C++</text></a></g>
      <g class="tech-chip" transform="translate(152,0)"><a xlink:href="https://python.org" target="_blank"><rect width="84" height="32" rx="8" fill="#131627" stroke="#4ade80" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Python</text></a></g>
      <g class="tech-chip" transform="translate(244,0)"><a xlink:href="https://nodejs.org/" target="_blank"><rect width="92" height="32" rx="8" fill="#131627" stroke="#a78bfa" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Node.js</text></a></g>
    </g>
  </g>

  <!-- 4. AI & WORKFLOW -->
  <g transform="translate(0, 255)">
    <line x1="0" y1="6" x2="14" y2="6" stroke="#f472b6" stroke-width="3" stroke-linecap="round"/>
    <text x="22" y="10" font-size="11" font-weight="700" fill="#f472b6" letter-spacing="1">AI &amp; WORKFLOW</text>

    <g transform="translate(0, 22)">
      <g class="tech-chip" transform="translate(0,0)"><a xlink:href="https://anthropic.com" target="_blank"><rect width="84" height="32" rx="8" fill="#131627" stroke="#d97706" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Claude</text></a></g>
      <g class="tech-chip" transform="translate(92,0)"><a xlink:href="https://github.com/features/copilot" target="_blank"><rect width="138" height="32" rx="8" fill="#131627" stroke="#a78bfa" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">GitHub Copilot</text></a></g>
      <g class="tech-chip" transform="translate(238,0)"><a xlink:href="https://git-scm.com/" target="_blank"><rect width="60" height="32" rx="8" fill="#131627" stroke="#f05032" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">Git</text></a></g>
      <g class="tech-chip" transform="translate(306,0)"><a xlink:href="https://github.com/tazimcoder" target="_blank"><rect width="84" height="32" rx="8" fill="#131627" stroke="#22d3ee" stroke-width="1"/><text x="14" y="20" font-size="12" fill="#ffffff" font-weight="bold">GitHub</text></a></g>
    </g>
  </g>

</g>
</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/stack.svg', 'w') as f:
    f.write(stack_svg)


# ================= 3. CONNECT.SVG (Width: 900, Height: 260) - MATCHING IMAGE 3 =================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 260" width="100%" height="100%" role="img" aria-label="Let's build something together - Connect with Tazim Kassar">
<title>Let's build something together — Connect with Tazim Kassar</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, monospace; }}
.title-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes floaty {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-6px); }} }}
@keyframes neonGlow {{ 0%,100% {{ filter: drop-shadow(0 0 8px rgba(244,114,182,.4)); }} 50% {{ filter: drop-shadow(0 0 16px rgba(34,211,238,.7)); }} }}

.fl {{ animation: floaty 4.5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.card-hover {{ transition: transform .2s ease, filter .2s ease; cursor: pointer; }}
.card-hover:hover {{ transform: translateY(-3px); filter: brightness(1.25); }}
]]></style>

<linearGradient id="bgC" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0c0e1a"/><stop offset="100%" stop-color="#070810"/>
</linearGradient>
<linearGradient id="borderC" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#f472b6"/><stop offset="50%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#22d3ee"/>
</linearGradient>
<pattern id="dotsC" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r=".5" fill="rgba(244,114,182,.1)"/></pattern>

<clipPath id="avatarRoundedC"><rect width="130" height="145" rx="14"/></clipPath>
</defs>

<!-- Outer Container -->
<rect width="900" height="260" rx="18" fill="url(#bgC)" stroke="url(#borderC)" stroke-width="1.5"/>
<rect width="900" height="260" rx="18" fill="url(#dotsC)"/>

<!-- LEFT SIDE: STICKER IMAGE CARD WITH REAL AVATAR PHOTO (x=30, y=25) -->
<g transform="translate(30, 25)">
  <g class="fl">
    <!-- Outer Card Frame -->
    <rect width="200" height="210" rx="14" fill="#090a14" stroke="#f472b6" stroke-opacity="0.6" stroke-width="1.5"/>
    <g transform="translate(35, 15)">
      <image href="{avatar_uri}" width="130" height="145" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarRoundedC)"/>
    </g>
    <!-- Sticker Signature Tag -->
    <g transform="translate(15, 168)">
      <rect width="170" height="28" rx="6" fill="#131628" stroke="#22d3ee" stroke-width="1"/>
      <text x="85" y="19" text-anchor="middle" font-size="11" font-weight="bold" fill="#22d3ee">coder.tazim ⚡</text>
    </g>
  </g>
</g>


<!-- RIGHT SIDE: HEADER + 2x2 CONTACT GRID (x=260, y=30) -->
<g transform="translate(260, 30)">
  <!-- Header -->
  <text font-size="12" font-weight="700" fill="#f472b6" letter-spacing="1.5">// LET'S CONNECT</text>
  <text class="title-text" x="0" y="30" font-size="24" font-weight="800" fill="#ffffff">Let's build something together</text>
  <text x="0" y="48" font-size="11.5" fill="#94a3b8">Open to collabs, freelance work and high-performance software projects.</text>

  <!-- 2x2 Grid -->
  <g transform="translate(0, 64)">
    <!-- 1. GitHub Card -->
    <g class="card-hover" transform="translate(0, 0)">
      <a xlink:href="https://github.com/tazimcoder" target="_blank">
        <rect width="290" height="52" rx="10" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
        <circle cx="26" cy="26" r="14" fill="#0f172a" stroke="#22d3ee" stroke-width="1"/>
        <path d="M26 18 C22.7 18 20 20.7 20 24 C20 26.6 21.7 28.8 24.1 29.6 C24.4 29.7 24.5 29.5 24.5 29.3 C24.5 29.1 24.5 28.7 24.5 28.2 C22.8 28.6 22.5 27.4 22.5 27.4 C22.2 26.7 21.8 26.5 21.8 26.5 C21.3 26.1 21.9 26.1 21.9 26.1 C22.5 26.2 22.8 26.7 22.8 26.7 C23.3 27.6 24.2 27.4 24.5 27.2 C24.6 26.8 24.7 26.5 24.9 26.3 C23.6 26.2 22.2 25.7 22.2 23.4 C22.2 22.7 22.4 22.2 22.8 21.8 C22.7 21.6 22.5 21 22.9 20.1 C22.9 20.1 23.4 19.9 24.5 20.7 C25 20.6 25.5 20.5 26 20.5 C26.5 20.5 27 20.6 27.5 20.7 C28.6 19.9 29.1 20.1 29.1 20.1 C29.5 21 29.3 21.6 29.2 21.8 C29.6 22.2 29.8 22.7 29.8 23.4 C29.8 25.7 28.4 26.2 27.1 26.3 C27.3 26.5 27.5 26.9 27.5 27.5 C27.5 28.4 27.5 29.1 27.5 29.3 C27.5 29.5 27.6 29.7 27.9 29.6 C30.3 28.8 32 26.6 32 24 C32 20.7 29.3 18 26 18 Z" fill="#22d3ee"/>
        <text x="50" y="24" font-size="12" font-weight="bold" fill="#ffffff">GitHub</text>
        <text x="50" y="38" font-size="11" fill="#94a3b8">tazimcoder</text>
      </a>
    </g>

    <!-- 2. Email Card -->
    <g class="card-hover" transform="translate(306, 0)">
      <a xlink:href="mailto:tazimcoder@gmail.com" target="_blank">
        <rect width="290" height="52" rx="10" fill="#131627" stroke="#f472b6" stroke-opacity="0.3" stroke-width="1"/>
        <circle cx="26" cy="26" r="14" fill="#0f172a" stroke="#f472b6" stroke-width="1"/>
        <path d="M18 20 L34 20 L34 32 L18 32 Z" fill="none" stroke="#f472b6" stroke-width="1.2"/>
        <path d="M18 20 L26 26 L34 20" fill="none" stroke="#f472b6" stroke-width="1.2"/>
        <text x="50" y="24" font-size="12" font-weight="bold" fill="#ffffff">Email</text>
        <text x="50" y="38" font-size="11" fill="#94a3b8">tazimcoder@gmail.com</text>
      </a>
    </g>

    <!-- 3. LinkedIn Card -->
    <g class="card-hover" transform="translate(0, 60)">
      <a xlink:href="https://linkedin.com/in/tazimcoder" target="_blank">
        <rect width="290" height="52" rx="10" fill="#131627" stroke="#38bdf8" stroke-opacity="0.3" stroke-width="1"/>
        <circle cx="26" cy="26" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="26" y="31" text-anchor="middle" font-size="13" font-weight="bold" fill="#38bdf8">in</text>
        <text x="50" y="24" font-size="12" font-weight="bold" fill="#ffffff">LinkedIn</text>
        <text x="50" y="38" font-size="11" fill="#94a3b8">Tazim Kassar</text>
      </a>
    </g>

    <!-- 4. Website Card -->
    <g class="card-hover" transform="translate(306, 60)">
      <a xlink:href="https://intellidev.dev" target="_blank">
        <rect width="290" height="52" rx="10" fill="#131627" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1"/>
        <circle cx="26" cy="26" r="14" fill="#0f172a" stroke="#a78bfa" stroke-width="1"/>
        <circle cx="26" cy="26" r="7" fill="none" stroke="#a78bfa" stroke-width="1.2"/>
        <text x="50" y="24" font-size="12" font-weight="bold" fill="#ffffff">Website</text>
        <text x="50" y="38" font-size="11" fill="#94a3b8">intellidev.dev</text>
      </a>
    </g>
  </g>

  <!-- Quote at Bottom -->
  <text x="0" y="200" font-size="11" fill="#f472b6" font-style="italic">"Code is my art, logic is my superpower."</text>
</g>

</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/connect.svg', 'w') as f:
    f.write(connect_svg)


# ================= 4. ABOUT-LIFE.SVG (Width: 900, Height: 440) =================
about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 440" width="100%" height="100%" role="img" aria-label="Capabilities &amp; Lifestyle - Tazim Kassar">
<title>Capabilities &amp; Lifestyle — Tazim Kassar</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, monospace; }}
.title-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes spinRing {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
.ring-spin {{ transform-box: fill-box; transform-origin: center; animation: spinRing 12s linear infinite; }}
]]></style>

<linearGradient id="bgA" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0a0c18"/><stop offset="100%" stop-color="#060710"/>
</linearGradient>
<pattern id="dotsA" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r=".5" fill="rgba(34,211,238,.1)"/></pattern>

<clipPath id="avatarSquareA"><rect width="60" height="60" rx="8"/></clipPath>
</defs>

<rect width="900" height="440" rx="18" fill="url(#bgA)" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1.5"/>
<rect width="900" height="440" rx="18" fill="url(#dotsA)"/>

<!-- LEFT SIDE: IDE CODE CAPABILITIES (x=30, y=30) -->
<g transform="translate(30, 30)">
  <rect width="460" height="380" rx="12" fill="#0e101f" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
  <circle cx="16" cy="16" r="4" fill="#ef4444"/>
  <circle cx="28" cy="16" r="4" fill="#f59e0b"/>
  <circle cx="40" cy="16" r="4" fill="#10b981"/>
  <text x="230" y="20" text-anchor="middle" font-size="11" fill="#94a3b8">capabilities.config.json</text>
  <line x1="0" y1="32" x2="460" y2="32" stroke="#ffffff" stroke-opacity="0.08"/>

  <g transform="translate(20, 56)" font-size="11.5">
    <text y="0"><tspan fill="#cbd5e1">{{</tspan></text>
    <text y="20" x="14"><tspan fill="#22d3ee">"developer"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#4ade80">"Tazim Kassar"</tspan><tspan fill="#cbd5e1">,</tspan></text>
    <text y="40" x="14"><tspan fill="#22d3ee">"handle"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#4ade80">"@tazimcoder"</tspan><tspan fill="#cbd5e1">,</tspan></text>
    <text y="60" x="14"><tspan fill="#22d3ee">"role"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#4ade80">"Full-Stack &amp; Systems Architect"</tspan><tspan fill="#cbd5e1">,</tspan></text>
    <text y="80" x="14"><tspan fill="#22d3ee">"languages"</tspan><tspan fill="#cbd5e1">: [</tspan><tspan fill="#f472b6">"C++"</tspan><tspan fill="#cbd5e1">, </tspan><tspan fill="#f472b6">"Python"</tspan><tspan fill="#cbd5e1">, </tspan><tspan fill="#f472b6">"SQL"</tspan><tspan fill="#cbd5e1">, </tspan><tspan fill="#f472b6">"JS"</tspan><tspan fill="#cbd5e1">],</tspan></text>
    <text y="100" x="14"><tspan fill="#22d3ee">"frameworks"</tspan><tspan fill="#cbd5e1">: [</tspan><tspan fill="#fde047">"React.js"</tspan><tspan fill="#cbd5e1">, </tspan><tspan fill="#fde047">"Node.js"</tspan><tspan fill="#cbd5e1">],</tspan></text>
    <text y="120" x="14"><tspan fill="#22d3ee">"flagship_saas"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#a78bfa">"IntelliDev Web IDE"</tspan><tspan fill="#cbd5e1">,</tspan></text>
    <text y="140" x="14"><tspan fill="#22d3ee">"focus"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#4ade80">"AI Code Intelligence &amp; Low-Latency Logic"</tspan><tspan fill="#cbd5e1">,</tspan></text>
    <text y="160" x="14"><tspan fill="#22d3ee">"status"</tspan><tspan fill="#cbd5e1">: </tspan><tspan fill="#38bdf8">"Available for High-Impact Projects"</tspan></text>
    <text y="180"><tspan fill="#cbd5e1">}}</tspan></text>
  </g>

  <g transform="translate(20, 275)">
    <rect width="420" height="80" rx="8" fill="#131527" stroke="#ffffff" stroke-opacity="0.08"/>
    <g transform="translate(15, 10)">
      <image href="{avatar_uri}" width="60" height="60" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarSquareA)"/>
    </g>
    <text x="90" y="32" font-size="13" font-weight="bold" fill="#ffffff">Tazim Kassar</text>
    <text x="90" y="50" font-size="11" fill="#22d3ee">Building next-gen AI &amp; developer tools 🚀</text>
  </g>
</g>

<!-- RIGHT SIDE: LIFESTYLE & PROGRESS RINGS (x=510, y=30) -->
<g transform="translate(510, 30)">
  <rect width="360" height="380" rx="12" fill="#0e101f" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1"/>
  <text class="title-text" x="24" y="32" font-size="18" font-weight="700" fill="#ffffff">Engineering Discipline</text>

  <!-- Carousel / Hobbies -->
  <g transform="translate(24, 50)">
    <rect width="312" height="60" rx="8" fill="#14172b" stroke="#38bdf8" stroke-width="1"/>
    <text x="16" y="26" font-size="12" font-weight="bold" fill="#38bdf8">💻 SaaS &amp; Web IDE Platforms</text>
    <text x="16" y="44" font-size="11" fill="#94a3b8">Architecting IntelliDev SaaS Ecosystem</text>
  </g>

  <!-- Daily Progress Rings -->
  <g transform="translate(24, 135)">
    <text font-size="12" font-weight="bold" fill="#a78bfa">Daily Capability Index</text>

    <!-- Ring 1: Coding 95% -->
    <g transform="translate(50, 80)">
      <circle cx="0" cy="0" r="34" fill="none" stroke="#1f243d" stroke-width="6"/>
      <circle cx="0" cy="0" r="34" fill="none" stroke="#22d3ee" stroke-width="6" stroke-dasharray="213" stroke-dashoffset="15" class="ring-spin"/>
      <text y="4" text-anchor="middle" font-size="12" font-weight="bold" fill="#22d3ee">95%</text>
      <text y="48" text-anchor="middle" font-size="11" fill="#cbd5e1">Coding</text>
    </g>

    <!-- Ring 2: System Design 90% -->
    <g transform="translate(156, 80)">
      <circle cx="0" cy="0" r="34" fill="none" stroke="#1f243d" stroke-width="6"/>
      <circle cx="0" cy="0" r="34" fill="none" stroke="#a78bfa" stroke-width="6" stroke-dasharray="213" stroke-dashoffset="25" class="ring-spin"/>
      <text y="4" text-anchor="middle" font-size="12" font-weight="bold" fill="#a78bfa">90%</text>
      <text y="48" text-anchor="middle" font-size="11" fill="#cbd5e1">Architecture</text>
    </g>

    <!-- Ring 3: Problem Solving 98% -->
    <g transform="translate(262, 80)">
      <circle cx="0" cy="0" r="34" fill="none" stroke="#1f243d" stroke-width="6"/>
      <circle cx="0" cy="0" r="34" fill="none" stroke="#f472b6" stroke-width="6" stroke-dasharray="213" stroke-dashoffset="6" class="ring-spin"/>
      <text y="4" text-anchor="middle" font-size="12" font-weight="bold" fill="#f472b6">98%</text>
      <text y="48" text-anchor="middle" font-size="11" fill="#cbd5e1">Algorithms</text>
    </g>
  </g>

  <!-- Quote -->
  <g transform="translate(24, 305)">
    <rect width="312" height="50" rx="8" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3"/>
    <text x="156" y="30" text-anchor="middle" font-size="11" fill="#22d3ee">"Consistency creates software mastery."</text>
  </g>
</g>

</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/about-life.svg', 'w') as f:
    f.write(about_life_svg)


# ================= 5. ID-DASHBOARD.SVG (Width: 900, Height: 460) =================
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 460" width="100%" height="100%" role="img" aria-label="Developer ID Badge &amp; Live Telemetry">
<title>Developer ID Badge &amp; Live Telemetry — Tazim Kassar</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&display=swap');
text {{ font-family: 'Fira Code', 'SFMono-Regular', Consolas, monospace; }}
.title-text {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}

@keyframes swingBadge {{ 0%,100% {{ transform: rotate(-1.5deg); }} 50% {{ transform: rotate(1.5deg); }} }}
.swing {{ transform-box: fill-box; transform-origin: top center; animation: swingBadge 4s ease-in-out infinite; }}
]]></style>

<linearGradient id="bgID" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0b0d18"/><stop offset="100%" stop-color="#070810"/>
</linearGradient>
<pattern id="dotsID" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r=".5" fill="rgba(167,139,250,.1)"/></pattern>

<clipPath id="avatarBadgeCircle"><circle cx="45" cy="45" r="42"/></clipPath>
</defs>

<rect width="900" height="460" rx="18" fill="url(#bgID)" stroke="#f472b6" stroke-opacity="0.3" stroke-width="1.5"/>
<rect width="900" height="460" rx="18" fill="url(#dotsID)"/>

<!-- LEFT SIDE: SWINGING LANYARD ID BADGE (x=30, y=20) -->
<g transform="translate(30, 20)">
  <!-- Lanyard String -->
  <line x1="130" y1="0" x2="130" y2="35" stroke="#a78bfa" stroke-width="3"/>
  <circle cx="130" cy="35" r="6" fill="#131627" stroke="#22d3ee" stroke-width="2"/>

  <!-- Swinging Card Body -->
  <g transform="translate(0, 35)" class="swing">
    <rect width="260" height="370" rx="14" fill="#0e101f" stroke="#22d3ee" stroke-width="1.5"/>

    <!-- Top Badge Header -->
    <rect width="260" height="45" rx="14" fill="#15182e"/>
    <text x="130" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#22d3ee">INTELLIDEV ARCHITECT</text>
    <line x1="0" y1="45" x2="260" y2="45" stroke="#22d3ee" stroke-opacity="0.4"/>

    <!-- Avatar Circle -->
    <g transform="translate(85, 65)">
      <circle cx="45" cy="45" r="45" fill="#22d3ee" opacity=".3"/>
      <circle cx="45" cy="45" r="42" fill="#090a12"/>
      <image href="{avatar_uri}" width="90" height="90" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarBadgeCircle)"/>
    </g>

    <!-- Name & Info -->
    <text x="130" y="180" text-anchor="middle" class="title-text" font-size="18" font-weight="800" fill="#ffffff">Tazim Kassar</text>
    <text x="130" y="198" text-anchor="middle" font-size="11" font-weight="bold" fill="#a78bfa">@tazimcoder</text>
    <text x="130" y="216" text-anchor="middle" font-size="10" fill="#94a3b8">ID: #TZ-9042-FULLSTACK</text>

    <!-- QR Code / Barcode Simulation -->
    <g transform="translate(30, 235)">
      <rect width="200" height="50" rx="6" fill="#131627" stroke="#ffffff" stroke-opacity="0.1"/>
      <g transform="translate(10, 10)" fill="#22d3ee">
        <rect x="0" y="0" width="4" height="30"/><rect x="8" y="0" width="8" height="30"/><rect x="20" y="0" width="2" height="30"/>
        <rect x="26" y="0" width="6" height="30"/><rect x="36" y="0" width="10" height="30"/><rect x="50" y="0" width="4" height="30"/>
        <rect x="58" y="0" width="8" height="30"/><rect x="70" y="0" width="4" height="30"/><rect x="78" y="0" width="12" height="30"/>
        <rect x="94" y="0" width="6" height="30"/><rect x="104" y="0" width="4" height="30"/><rect x="112" y="0" width="10" height="30"/>
        <rect x="126" y="0" width="4" height="30"/><rect x="134" y="0" width="8" height="30"/><rect x="146" y="0" width="6" height="30"/>
        <rect x="156" y="0" width="10" height="30"/><rect x="170" y="0" width="4" height="30"/>
      </g>
    </g>

    <!-- Status Chip -->
    <g transform="translate(30, 305)">
      <rect width="200" height="36" rx="18" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/>
      <circle cx="20" cy="18" r="4" fill="#4ade80"/>
      <text x="32" y="22" font-size="11" font-weight="bold" fill="#86efac">STATUS: ACTIVE &amp; BUILDING</text>
    </g>
  </g>
</g>

<!-- RIGHT SIDE: LIVE TELEMETRY KPI & REPO ACTIVITY (x=320, y=30) -->
<g transform="translate(320, 30)">
  <rect width="550" height="400" rx="14" fill="#0e101f" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1"/>
  <text class="title-text" x="24" y="36" font-size="18" font-weight="700" fill="#ffffff">Live Telemetry &amp; System Stats</text>

  <!-- 4 KPI Cards -->
  <g transform="translate(24, 55)">
    <!-- KPI 1 -->
    <g transform="translate(0, 0)">
      <rect width="240" height="70" rx="10" fill="#131627" stroke="#22d3ee" stroke-opacity="0.4"/>
      <text x="16" y="24" font-size="11" fill="#94a3b8">Flagship SaaS</text>
      <text x="16" y="48" font-size="14" font-weight="bold" fill="#22d3ee">IntelliDev Platform</text>
    </g>

    <!-- KPI 2 -->
    <g transform="translate(260, 0)">
      <rect width="240" height="70" rx="10" fill="#131627" stroke="#a78bfa" stroke-opacity="0.4"/>
      <text x="16" y="24" font-size="11" fill="#94a3b8">System Speed</text>
      <text x="16" y="48" font-size="14" font-weight="bold" fill="#a78bfa">C++ Ultra-Low Latency</text>
    </g>

    <!-- KPI 3 -->
    <g transform="translate(0, 85)">
      <rect width="240" height="70" rx="10" fill="#131627" stroke="#f472b6" stroke-opacity="0.4"/>
      <text x="16" y="24" font-size="11" fill="#94a3b8">Security Scanner</text>
      <text x="16" y="48" font-size="14" font-weight="bold" fill="#f472b6">Cloud SAST Audit</text>
    </g>

    <!-- KPI 4 -->
    <g transform="translate(260, 85)">
      <rect width="240" height="70" rx="10" fill="#131627" stroke="#fde047" stroke-opacity="0.4"/>
      <text x="16" y="24" font-size="11" fill="#94a3b8">Full-Stack Tech</text>
      <text x="16" y="48" font-size="14" font-weight="bold" fill="#fde047">React &amp; Node Suite</text>
    </g>
  </g>

  <!-- Repo Velocity Chart -->
  <g transform="translate(24, 230)">
    <text font-size="12" font-weight="bold" fill="#22d3ee">Repository Commit Velocity (2026)</text>
    <rect x="0" y="15" width="500" height="130" rx="8" fill="#131527" stroke="#ffffff" stroke-opacity="0.08"/>

    <!-- Simulated Wave Path -->
    <path d="M10 120 Q 60 40, 120 80 T 240 50 T 360 90 T 490 30" fill="none" stroke="#22d3ee" stroke-width="2.5"/>
    <path d="M10 120 Q 60 40, 120 80 T 240 50 T 360 90 T 490 30 L 490 135 L 10 135 Z" fill="url(#bgID)" opacity=".4"/>

    <!-- Points -->
    <circle cx="120" cy="80" r="4" fill="#a78bfa"/>
    <circle cx="240" cy="50" r="4" fill="#f472b6"/>
    <circle cx="490" cy="30" r="5" fill="#4ade80"/>

    <text x="480" y="22" text-anchor="end" font-size="10" fill="#86efac">PEAK PERFORMANCE ⚡</text>
  </g>
</g>

</svg>'''

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/id-dashboard.svg', 'w') as f:
    f.write(id_dashboard_svg)

print("✅ All 5 SVGs generated successfully!")
