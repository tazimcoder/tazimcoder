import base64
import os

with open('/Users/macbook/.gemini/antigravity-ide/scratch/tazimcoder/avatar.b64', 'r') as f:
    avatar_b64 = f.read().strip()

avatar_uri = f"data:image/png;base64,{avatar_b64}"
github_avatar_url = "https://avatars.githubusercontent.com/u/148122455?v=4"

print("Building all 5 NEXT-LEVEL SVGs with fixed transform hierarchy & perfect alignment...")

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

<!-- ================= LEFT COLUMN: INFO & TYPOGRAPHY (Width <= 640px) ================= -->
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
  <g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
    <rect x="48" y="248" width="410" height="66" rx="8" fill="#131627" stroke="#22d3ee" stroke-opacity="0.3" stroke-width="1"/>
    <rect x="48" y="252" width="3.5" height="58" rx="1.5" fill="#22d3ee"/>
  </g>
  <text clip-path="url(#q1)" x="74" y="275" font-size="14" fill="#e6edf3">I don't just write code,</text>
  <text clip-path="url(#q2)" x="74" y="299" font-size="14"><tspan fill="#e6edf3">I </tspan><tspan fill="#22d3ee" font-weight="bold">architect</tspan><tspan fill="#e6edf3"> full-stack &amp; AI systems.</tspan></text>

  <!-- TECH I KNOW PILLS -->
  <text class="ii" x="48" y="348" font-size="14" fill="#a78bfa" font-weight="bold" style="animation:fadeIn .4s ease 4.2s forwards">🧩 Tech I Know</text>
  <g transform="translate(48, 360)">
    <g class="pill" style="animation:fadeIn .3s ease 4.4s forwards"><rect x="0" y="0" width="60" height="24" rx="12" fill="rgba(227,79,38,.14)" stroke="#e34f26" stroke-width="1"/><text x="30" y="16" text-anchor="middle" font-size="11" fill="#ff8a65" font-weight="bold">HTML</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.5s forwards"><rect x="68" y="0" width="54" height="24" rx="12" fill="rgba(38,119,189,.14)" stroke="#38bdf8" stroke-width="1"/><text x="95" y="16" text-anchor="middle" font-size="11" fill="#7dd3fc" font-weight="bold">CSS</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.6s forwards"><rect x="130" y="0" width="46" height="24" rx="12" fill="rgba(247,223,30,.14)" stroke="#f7df1e" stroke-width="1"/><text x="153" y="16" text-anchor="middle" font-size="11" fill="#fde047" font-weight="bold">JS</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.7s forwards"><rect x="184" y="0" width="82" height="24" rx="12" fill="rgba(34,211,238,.14)" stroke="#22d3ee" stroke-width="1"/><text x="225" y="16" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold">REACT.JS</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="274" y="0" width="76" height="24" rx="12" fill="rgba(167,139,250,.14)" stroke="#a78bfa" stroke-width="1"/><text x="312" y="16" text-anchor="middle" font-size="11" fill="#c084fc" font-weight="bold">NODE.JS</text></g>

    <g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="0" y="30" width="52" height="24" rx="12" fill="rgba(244,114,182,.14)" stroke="#f472b6" stroke-width="1"/><text x="26" y="46" text-anchor="middle" font-size="11" fill="#f9a8d4" font-weight="bold">SQL</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="60" y="30" width="54" height="24" rx="12" fill="rgba(59,130,246,.14)" stroke="#3b82f6" stroke-width="1"/><text x="87" y="46" text-anchor="middle" font-size="11" fill="#93c5fd" font-weight="bold">C++</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="122" y="30" width="76" height="24" rx="12" fill="rgba(74,222,128,.14)" stroke="#4ade80" stroke-width="1"/><text x="160" y="46" text-anchor="middle" font-size="11" fill="#86efac" font-weight="bold">PYTHON</text></g>
  </g>

  <!-- About Me Bullet Points -->
  <text class="ii" x="48" y="450" font-size="14" fill="#f472b6" font-weight="bold" style="animation:fadeIn .4s ease 5.3s forwards">💗 About Me</text>
  <text class="ii" x="48" y="472" font-size="12.5" style="animation:fadeIn .4s ease 5.5s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">Building IntelliDev — AI code intelligence &amp; Web IDE platform.</tspan></text>
  <text class="ii" x="48" y="494" font-size="12.5" style="animation:fadeIn .4s ease 5.7s forwards"><tspan fill="#fde047">💡 </tspan><tspan fill="#cdd3dd">Proficient in C++, Python, SQL, React.js &amp; Node.js architecture.</tspan></text>
  <text class="ii" x="48" y="516" font-size="12.5" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#22d3ee">🚀 </tspan><tspan fill="#cdd3dd">Turning complex logic into high-performance software applications.</tspan></text>

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
</g>

<!-- ================= RIGHT COLUMN: CODE WINDOW & REAL GITHUB AVATAR CARD (Locked at x=710, y=42) ================= -->

<!-- 1. IDE Code Window (Top Right) -->
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

<!-- 2. Real GitHub Profile Photo Card (Bottom Right, Locked at x=710, y=255) -->
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
    <circle cx="10" cy="10" r="9" fill="#0f172a" stroke="#22d3ee" stroke-width="1"/>
    <path d="M10 4 C6.7 4 4 6.7 4 10 C4 12.6 5.7 14.8 8.1 15.6 C8.4 15.7 8.5 15.5 8.5 15.3 C8.5 15.1 8.5 14.7 8.5 14.2 C6.8 14.6 6.5 13.4 6.5 13.4 C6.2 12.7 5.8 12.5 5.8 12.5 C5.3 12.1 5.9 12.1 5.9 12.1 C6.5 12.2 6.8 12.7 6.8 12.7 C7.3 13.6 8.2 13.4 8.5 13.2 C8.6 12.8 8.7 12.5 8.9 12.3 C7.6 12.2 6.2 11.7 6.2 9.4 C6.2 8.7 6.4 8.2 6.8 7.8 C6.7 7.6 6.5 7 6.9 6.1 C6.9 6.1 7.4 5.9 8.5 6.7 C9 6.6 9.5 6.5 10 6.5 C10.5 6.5 11 6.6 11.5 6.7 C12.6 5.9 13.1 6.1 13.1 6.1 C13.5 7 13.3 7.6 13.2 7.8 C13.6 8.2 13.8 8.7 13.8 9.4 C13.8 11.7 12.4 12.2 11.1 12.3 C11.3 12.5 11.5 12.9 11.5 13.5 C11.5 14.4 11.5 15.1 11.5 15.3 C11.5 15.5 11.6 15.7 11.9 15.6 C14.3 14.8 16 12.6 16 10 C16 6.7 13.3 4 10 4 Z" fill="#22d3ee"/>
    <text x="26" y="14" font-size="12" fill="#cbd5e1" font-weight="bold">tazimcoder</text>
  </g>

  <g transform="translate(200, 22)">
    <rect x="0" y="2" width="16" height="12" rx="2" fill="none" stroke="#f472b6" stroke-width="1.2"/>
    <path d="M0 4 L8 10 L16 4" fill="none" stroke="#f472b6" stroke-width="1.2"/>
    <text x="24" y="14" font-size="12" fill="#cbd5e1">tazimcoder@gmail.com</text>
  </g>

  <g transform="translate(450, 22)">
    <circle cx="8" cy="10" r="7" fill="none" stroke="#a78bfa" stroke-width="1.2"/>
    <text x="22" y="14" font-size="12" fill="#cbd5e1">intellidev.dev</text>
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

print("✅ hero.svg alignment & transform hierarchy updated successfully!")
