"""
Generates high-resolution academic SVG diagrams for the Indian Constitution Module.
Adheres strictly to the Judicial Design System palette:
- Navy: #142c46, #1b3857
- Teal: #137d72, #0d5c54
- Gold: #dfbf80, #b98a38, #e7c88c
- Ivory/White: #ffffff, #f4f6f9
- Text: #1c2e40, #607387
"""

import os

DIAGRAMS_DIR = "assets/learning/images/diagrams"
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(DIAGRAMS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created {filename}")

# 1. diag-historical-timeline.svg
write_svg("diag-historical-timeline.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="900" height="360" fill="url(#bgGrad)" rx="12"/>
  <text x="450" y="45" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80" letter-spacing="1">CHRONOLOGICAL EVOLUTION OF THE INDIAN CONSTITUTION</text>
  <text x="450" y="70" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">From Company Rule (1773) to Full Enactment and Commencement (1950)</text>
  
  <!-- Central Timeline Axis -->
  <line x1="60" y1="180" x2="840" y2="180" stroke="#dfbf80" stroke-width="4" stroke-dasharray="8 4"/>
  
  <!-- Milestone 1: 1773 -->
  <circle cx="100" cy="180" r="14" fill="#137d72" stroke="#dfbf80" stroke-width="3" filter="url(#shadow)"/>
  <text x="100" y="185" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#fff">1</text>
  <rect x="30" y="90" width="140" height="65" rx="6" fill="#ffffff" filter="url(#shadow)"/>
  <text x="100" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Regulating Act 1773</text>
  <text x="100" y="130" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Gov-Gen of Bengal</text>
  <text x="100" y="145" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">SC at Calcutta 1774</text>
  
  <!-- Milestone 2: 1858 -->
  <circle cx="260" cy="180" r="14" fill="#137d72" stroke="#dfbf80" stroke-width="3" filter="url(#shadow)"/>
  <text x="260" y="185" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#fff">2</text>
  <rect x="190" y="215" width="140" height="65" rx="6" fill="#ffffff" filter="url(#shadow)"/>
  <text x="260" y="237" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">GoI Act 1858</text>
  <text x="260" y="255" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Crown Rule Begins</text>
  <text x="260" y="270" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">Secretary of State</text>

  <!-- Milestone 3: 1919 -->
  <circle cx="420" cy="180" r="14" fill="#137d72" stroke="#dfbf80" stroke-width="3" filter="url(#shadow)"/>
  <text x="420" y="185" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#fff">3</text>
  <rect x="350" y="90" width="140" height="65" rx="6" fill="#ffffff" filter="url(#shadow)"/>
  <text x="420" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">GoI Act 1919</text>
  <text x="420" y="130" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Provincial Dyarchy</text>
  <text x="420" y="145" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">Bicameral Centre</text>

  <!-- Milestone 4: 1935 -->
  <circle cx="580" cy="180" r="14" fill="#b98a38" stroke="#dfbf80" stroke-width="3" filter="url(#shadow)"/>
  <text x="580" y="185" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#fff">4</text>
  <rect x="510" y="215" width="140" height="65" rx="6" fill="#ffffff" filter="url(#shadow)"/>
  <text x="580" y="237" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">GoI Act 1935</text>
  <text x="580" y="255" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Constitutional Blueprint</text>
  <text x="580" y="270" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#b98a38">Provincial Autonomy</text>

  <!-- Milestone 5: 1946-50 -->
  <circle cx="760" cy="180" r="16" fill="#137d72" stroke="#dfbf80" stroke-width="4" filter="url(#shadow)"/>
  <text x="760" y="185" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#dfbf80">★</text>
  <rect x="690" y="85" width="150" height="75" rx="6" fill="#dfbf80" filter="url(#shadow)"/>
  <text x="765" y="107" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">1946–1950</text>
  <text x="765" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Constituent Assembly</text>
  <text x="765" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#1b3857">Adopted: 26 Nov 1949</text>
  <text x="765" y="153" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">Enacted: 26 Jan 1950</text>
</svg>
""")

# 2. diag-sources-features.svg
write_svg("diag-sources-features.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient>
  </defs>
  <rect width="900" height="360" fill="url(#bg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">MAJOR GLOBAL SOURCES OF THE INDIAN CONSTITUTION</text>
  
  <!-- UK -->
  <rect x="40" y="70" width="190" height="120" rx="8" fill="#fff"/>
  <rect x="40" y="70" width="190" height="28" rx="8" fill="#137d72"/>
  <text x="135" y="89" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#fff">United Kingdom (UK)</text>
  <text x="50" y="115" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Parliamentary Form (Cabinet)</text>
  <text x="50" y="132" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Rule of Law &amp; Bicameralism</text>
  <text x="50" y="149" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Single Citizenship</text>
  <text x="50" y="166" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">• Prerogative Writs &amp; Speaker</text>

  <!-- USA -->
  <rect x="255" y="70" width="190" height="120" rx="8" fill="#fff"/>
  <rect x="255" y="70" width="190" height="28" rx="8" fill="#142c46"/>
  <text x="350" y="89" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">United States (USA)</text>
  <text x="265" y="115" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Fundamental Rights (Part III)</text>
  <text x="265" y="132" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Judicial Review (Art. 13/32)</text>
  <text x="265" y="149" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Preamble &amp; Impeachment</text>
  <text x="265" y="166" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• Independence of Judiciary</text>

  <!-- Ireland -->
  <rect x="470" y="70" width="190" height="120" rx="8" fill="#fff"/>
  <rect x="470" y="70" width="190" height="28" rx="8" fill="#137d72"/>
  <text x="565" y="89" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#fff">Ireland (Eire)</text>
  <text x="480" y="115" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Directive Principles (DPSP)</text>
  <text x="480" y="132" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Presidential Election Method</text>
  <text x="480" y="149" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Nomination of 12 Members to</text>
  <text x="480" y="166" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">  Rajya Sabha (Art. 80)</text>

  <!-- Canada -->
  <rect x="685" y="70" width="180" height="120" rx="8" fill="#fff"/>
  <rect x="685" y="70" width="180" height="28" rx="8" fill="#142c46"/>
  <text x="775" y="89" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">Canada</text>
  <text x="695" y="115" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Federation with Strong Centre</text>
  <text x="695" y="132" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Residuary Powers in Centre</text>
  <text x="695" y="149" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Appointment of State Governors</text>
  <text x="695" y="166" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• Advisory Juris. (Art. 143)</text>

  <!-- Row 2: Australia, Germany, USSR, South Africa -->
  <rect x="40" y="210" width="190" height="125" rx="8" fill="#fff"/>
  <text x="135" y="235" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">Australia</text>
  <text x="50" y="258" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Concurrent List (7th Sched)</text>
  <text x="50" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Joint Sitting of Houses (108)</text>
  <text x="50" y="292" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Freedom of Trade/Commerce</text>

  <rect x="255" y="210" width="190" height="125" rx="8" fill="#fff"/>
  <text x="350" y="235" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">Germany (Weimar)</text>
  <text x="265" y="258" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Suspension of Fundamental</text>
  <text x="265" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#607387">  Rights during Emergency</text>
  <text x="265" y="292" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Emergency Financial Orders</text>

  <rect x="470" y="210" width="190" height="125" rx="8" fill="#fff"/>
  <text x="565" y="235" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">USSR (Soviet Union)</text>
  <text x="480" y="258" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Fundamental Duties (51A)</text>
  <text x="480" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Ideals of Justice (Social,</text>
  <text x="480" y="292" font-family="system-ui, sans-serif" font-size="10" fill="#607387">  Economic &amp; Political)</text>

  <rect x="685" y="210" width="180" height="125" rx="8" fill="#fff"/>
  <text x="775" y="235" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">South Africa</text>
  <text x="695" y="258" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Constitutional Amendment</text>
  <text x="695" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#607387">  Procedure (Art. 368)</text>
  <text x="695" y="292" font-family="system-ui, sans-serif" font-size="10" fill="#607387">• Election of Rajya Sabha MPs</text>
</svg>
""")

# 3. diag-preamble-pillars.svg
write_svg("diag-preamble-pillars.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="pbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#pbg)" rx="12"/>
  <text x="450" y="45" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">THE ARCHITECTURAL PILLARS OF THE PREAMBLE</text>
  <text x="450" y="70" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">"We, the People of India..." — Authority, Nature of State, and Grand Objectives</text>
  
  <!-- Left Side: Nature of the Indian State (5 attributes) -->
  <rect x="40" y="95" width="380" height="230" rx="8" fill="#ffffff"/>
  <rect x="40" y="95" width="380" height="35" rx="8" fill="#142c46"/>
  <text x="230" y="118" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">NATURE OF THE POLITY</text>
  
  <text x="60" y="155" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">1. SOVEREIGN</text>
  <text x="180" y="155" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Internally supreme, externally independent</text>
  
  <text x="60" y="190" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">2. SOCIALIST*</text>
  <text x="180" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Democratic socialism; poverty &amp; inequality alleviation</text>
  
  <text x="60" y="225" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">3. SECULAR*</text>
  <text x="180" y="225" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Sarva Dharma Sambhava; equal respect to all faiths</text>
  
  <text x="60" y="260" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">4. DEMOCRATIC</text>
  <text x="180" y="260" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Representative parliamentary democracy</text>
  
  <text x="60" y="295" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">5. REPUBLIC</text>
  <text x="180" y="295" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Elected Head of State (President); no hereditary monarch</text>
  
  <text x="60" y="318" font-family="system-ui, sans-serif" font-size="9" fill="#a63b49">*Added by the 42nd Constitutional Amendment Act, 1976</text>

  <!-- Right Side: Four Objectives of the Constitution -->
  <rect x="480" y="95" width="380" height="230" rx="8" fill="#ffffff"/>
  <rect x="480" y="95" width="380" height="35" rx="8" fill="#137d72"/>
  <text x="670" y="118" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">FOUR CONSTITUTIONAL OBJECTIVES</text>

  <text x="500" y="155" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">1. JUSTICE</text>
  <text x="620" y="155" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Social, Economic, and Political</text>

  <text x="500" y="195" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">2. LIBERTY</text>
  <text x="620" y="195" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Of thought, expression, belief, faith &amp; worship</text>

  <text x="500" y="235" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">3. EQUALITY</text>
  <text x="620" y="235" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Of status and of opportunity</text>

  <text x="500" y="275" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">4. FRATERNITY</text>
  <text x="620" y="275" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Dignity of the individual &amp; Unity/Integrity* of Nation</text>
  
  <text x="500" y="318" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">Legal Status: Integral part of Basic Structure (Kesavananda / LIC of India)</text>
</svg>
""")

# 4. diag-golden-triangle.svg
write_svg("diag-golden-triangle.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="gtbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#gtbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">THE GOLDEN TRIANGLE OF FUNDAMENTAL RIGHTS</text>
  <text x="450" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">Interconnection of Articles 14, 19, and 21 (Maneka Gandhi &amp; Minerva Mills)</text>
  
  <!-- Triangle Graphic -->
  <polygon points="450,95 240,290 660,290" fill="none" stroke="#dfbf80" stroke-width="5" stroke-dasharray="10 5"/>

  <!-- Top Vertex: Article 14 -->
  <circle cx="450" cy="95" r="45" fill="#137d72" stroke="#dfbf80" stroke-width="4"/>
  <text x="450" y="93" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#fff">ARTICLE 14</text>
  <text x="450" y="112" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#dfbf80">EQUALITY</text>
  <rect x="360" y="145" width="180" height="40" rx="4" fill="#ffffff"/>
  <text x="450" y="162" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Anti-Arbitrariness</text>
  <text x="450" y="177" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Royappa / E.P. Royappa (1974)</text>

  <!-- Bottom Left: Article 19 -->
  <circle cx="240" cy="290" r="45" fill="#142c46" stroke="#dfbf80" stroke-width="4"/>
  <text x="240" y="288" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#dfbf80">ARTICLE 19</text>
  <text x="240" y="307" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#fff">FREEDOM</text>
  <rect x="50" y="270" width="135" height="45" rx="4" fill="#ffffff"/>
  <text x="117" y="288" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">6 Democratic Freedoms</text>
  <text x="117" y="303" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Reasonable Restrictions (19(2)-(6))</text>

  <!-- Bottom Right: Article 21 -->
  <circle cx="660" cy="290" r="45" fill="#137d72" stroke="#dfbf80" stroke-width="4"/>
  <text x="660" y="288" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#fff">ARTICLE 21</text>
  <text x="660" y="307" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#dfbf80">LIFE &amp; LIBERTY</text>
  <rect x="715" y="270" width="135" height="45" rx="4" fill="#ffffff"/>
  <text x="782" y="288" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Due Process &amp; Privacy</text>
  <text x="782" y="303" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Just, Fair &amp; Reasonable Law</text>

  <!-- Central Core Rule -->
  <rect x="360" y="220" width="180" height="50" rx="6" fill="#dfbf80"/>
  <text x="450" y="238" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#142c46">MANEKA GANDHI (1978)</text>
  <text x="450" y="253" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#1b3857">Any law depriving liberty under Art. 21</text>
  <text x="450" y="265" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">must also satisfy Arts. 14 and 19!</text>
</svg>
""")

# 5. diag-five-writs.svg
write_svg("diag-five-writs.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="wbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#wbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">THE FIVE HIGH PREROGATIVE WRITS (ARTICLES 32 &amp; 226)</text>
  
  <!-- 1. Habeas Corpus -->
  <rect x="25" y="70" width="160" height="260" rx="8" fill="#ffffff"/>
  <rect x="25" y="70" width="160" height="32" rx="8" fill="#137d72"/>
  <text x="105" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">HABEAS CORPUS</text>
  <text x="105" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">"Have the Body"</text>
  <text x="35" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Remedy against illegal or arbitrary detention</text>
  <text x="35" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Lies against BOTH State and Private individuals</text>
  <text x="35" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Locus Standi is relaxed (relatives/friends can file)</text>
  <text x="35" y="275" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">• Sunil Batra case: protects prisoner rights inside jail</text>

  <!-- 2. Mandamus -->
  <rect x="195" y="70" width="160" height="260" rx="8" fill="#ffffff"/>
  <rect x="195" y="70" width="160" height="32" rx="8" fill="#142c46"/>
  <text x="275" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">MANDAMUS</text>
  <text x="275" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">"We Command"</text>
  <text x="205" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Compels performance of public / statutory duty</text>
  <text x="205" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Requires legal right + corresponding public duty</text>
  <text x="205" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#a63b49">• Does NOT lie against President, Governor, or private body</text>
  <text x="205" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Cannot enforce contract</text>

  <!-- 3. Prohibition -->
  <rect x="365" y="70" width="160" height="260" rx="8" fill="#ffffff"/>
  <rect x="365" y="70" width="160" height="32" rx="8" fill="#137d72"/>
  <text x="445" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">PROHIBITION</text>
  <text x="445" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">"To Forbid"</text>
  <text x="375" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Issued to prevent lower court/tribunal from usurping jurisdiction</text>
  <text x="375" y="195" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">• Purely PREVENTIVE in nature</text>
  <text x="375" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Issued while proceedings are PENDING</text>
  <text x="375" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Lies only against judicial and quasi-judicial bodies</text>

  <!-- 4. Certiorari -->
  <rect x="535" y="70" width="160" height="260" rx="8" fill="#ffffff"/>
  <rect x="535" y="70" width="160" height="32" rx="8" fill="#142c46"/>
  <text x="615" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">CERTIORARI</text>
  <text x="615" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">"To be Certified"</text>
  <text x="545" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Quashes orders passed without jurisdiction, in excess of jurisdiction, or breach of natural justice</text>
  <text x="545" y="200" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• Both PREVENTIVE and CURATIVE in nature</text>
  <text x="545" y="240" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Issued AFTER order is passed</text>
  <text x="545" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">• Extended to admin bodies</text>

  <!-- 5. Quo Warranto -->
  <rect x="705" y="70" width="170" height="260" rx="8" fill="#ffffff"/>
  <rect x="705" y="70" width="170" height="32" rx="8" fill="#137d72"/>
  <text x="790" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">QUO WARRANTO</text>
  <text x="790" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">"By What Warrant?"</text>
  <text x="715" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Inquires into legality of claim to a substantive PUBLIC OFFICE</text>
  <text x="715" y="195" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Prevents usurpation of public office by non-qualified persons</text>
  <text x="715" y="245" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">• Any citizen can move court (no personal grievance required)</text>
</svg>
""")

# 6. diag-two-wheels-chariot.svg
write_svg("diag-two-wheels-chariot.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="cbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#cbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">HARMONIOUS CONSTRUCTION: THE TWO WHEELS OF THE CHARIOT</text>
  <text x="450" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">"Parts III and IV are like two wheels of a chariot, none less important than the other." — Minerva Mills (1980)</text>
  
  <!-- Left Wheel: Part III Fundamental Rights -->
  <circle cx="250" cy="190" r="85" fill="#ffffff" stroke="#dfbf80" stroke-width="6"/>
  <circle cx="250" cy="190" r="30" fill="#137d72"/>
  <text x="250" y="140" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#142c46">PART III</text>
  <text x="250" y="160" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Fundamental Rights</text>
  <text x="250" y="195" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">JUSTICIABLE</text>
  <text x="250" y="235" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Civil &amp; Political Liberties</text>
  <text x="250" y="250" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Negative Obligations on State</text>

  <!-- Axle connecting both wheels -->
  <line x1="335" y1="190" x2="565" y2="190" stroke="#dfbf80" stroke-width="10"/>
  <rect x="380" y="165" width="140" height="50" rx="6" fill="#dfbf80"/>
  <text x="450" y="185" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">THE AXLE</text>
  <text x="450" y="202" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#1b3857">Harmonious Balance</text>

  <!-- Right Wheel: Part IV Directive Principles -->
  <circle cx="650" cy="190" r="85" fill="#ffffff" stroke="#dfbf80" stroke-width="6"/>
  <circle cx="650" cy="190" r="30" fill="#142c46"/>
  <text x="650" y="140" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#142c46">PART IV</text>
  <text x="650" y="160" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Directive Principles</text>
  <text x="650" y="195" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#dfbf80">GOVERNANCE</text>
  <text x="650" y="235" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Socio-Economic Goals</text>
  <text x="650" y="250" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Positive Mandates on State</text>

  <!-- Bottom Evolution Box -->
  <rect x="100" y="295" width="700" height="45" rx="6" fill="#1b3857"/>
  <text x="450" y="313" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#a0b3c6">Jurisprudential Evolution: Champakam Dorairajan (1951) → Kerala Education Bill (1958) → Kesavananda (1973) → Minerva Mills (1980)</text>
  <text x="450" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#dfbf80">Neither has absolute supremacy; both must be harmonized to build a Welfare State.</text>
</svg>
""")

# 7. diag-parliament-bills.svg
write_svg("diag-parliament-bills.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="pbbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#pbbg)" rx="12"/>
  <text x="450" y="38" text-anchor="middle" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#dfbf80">PARLIAMENTARY LEGISLATIVE PROCEDURES &amp; TYPES OF BILLS</text>
  
  <!-- Ordinary Bill -->
  <rect x="30" y="65" width="195" height="275" rx="8" fill="#fff"/>
  <rect x="30" y="65" width="195" height="32" rx="8" fill="#142c46"/>
  <text x="127" y="86" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">Ordinary Bill (Art. 107)</text>
  <text x="40" y="115" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Can be introduced in EITHER House</text>
  <text x="40" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Can be introduced by Minister or Private Member</text>
  <text x="40" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Rajya Sabha can delay for max 6 MONTHS</text>
  <text x="40" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">• Joint Sitting (Art. 108) APPLIES in case of deadlock</text>
  <text x="40" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• President can assent, withhold, or return for reconsideration</text>

  <!-- Money Bill -->
  <rect x="245" y="65" width="195" height="275" rx="8" fill="#fff"/>
  <rect x="245" y="65" width="195" height="32" rx="8" fill="#137d72"/>
  <text x="342" y="86" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">Money Bill (Art. 110)</text>
  <text x="255" y="115" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• ONLY in Lok Sabha (Art. 109)</text>
  <text x="255" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Requires PRIOR recommendation of President</text>
  <text x="255" y="180" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#a63b49">• RS can delay only for 14 DAYS</text>
  <text x="255" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#a63b49">• NO Joint Sitting provision</text>
  <text x="255" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">• Certified solely by Speaker</text>
  <text x="255" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• President cannot return for reconsideration</text>

  <!-- Financial Bills -->
  <rect x="460" y="65" width="195" height="275" rx="8" fill="#fff"/>
  <rect x="460" y="65" width="195" height="32" rx="8" fill="#142c46"/>
  <text x="557" y="86" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">Financial Bills (Art. 117)</text>
  <text x="470" y="115" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• Category I (Art. 117(1)):</text>
  <text x="475" y="132" font-family="system-ui, sans-serif" font-size="8.5" fill="#607387">Contains Art 110 matters + other laws; only in LS; joint sitting applies</text>
  <text x="470" y="170" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• Category II (Art. 117(3)):</text>
  <text x="475" y="187" font-family="system-ui, sans-serif" font-size="8.5" fill="#607387">Expenditure from CFI; can start in either House; needs President recommendation before consideration</text>
  <text x="470" y="240" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">• Treated like Ordinary Bills in passage</text>
  <text x="470" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Joint sitting applies to both categories</text>

  <!-- Amendment Bill -->
  <rect x="675" y="65" width="195" height="275" rx="8" fill="#fff"/>
  <rect x="675" y="65" width="195" height="32" rx="8" fill="#137d72"/>
  <text x="772" y="86" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">Amendment Bill (Art. 368)</text>
  <text x="685" y="115" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Can start in EITHER House</text>
  <text x="685" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• NO prior recommendation needed</text>
  <text x="685" y="175" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• Special Majority in EACH House</text>
  <text x="685" y="210" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#a63b49">• NO Joint Sitting provision</text>
  <text x="685" y="240" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">• Federal clauses: 50% state ratification</text>
  <text x="685" y="280" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• President SHALL give assent (24th Amend)</text>
</svg>
""")

# 8. diag-emergency-comparison.svg
write_svg("diag-emergency-comparison.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="ebg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#ebg)" rx="12"/>
  <text x="450" y="38" text-anchor="middle" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#dfbf80">COMPARATIVE ANALYSIS OF THE THREE TYPES OF EMERGENCY</text>
  
  <!-- Column 1: Feature -->
  <rect x="30" y="60" width="180" height="280" rx="6" fill="#142c46" stroke="#dfbf80" stroke-width="1"/>
  <text x="120" y="90" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">CONSTITUTIONAL FEATURE</text>
  <text x="45" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Grounds of Proclamation</text>
  <text x="45" y="165" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Approval Window</text>
  <text x="45" y="205" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Parliamentary Majority</text>
  <text x="45" y="245" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Maximum Duration</text>
  <text x="45" y="285" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Fundamental Rights Impact</text>
  <text x="45" y="325" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ffffff">Times Declared in India</text>

  <!-- Column 2: Art 352 -->
  <rect x="220" y="60" width="210" height="280" rx="6" fill="#fff"/>
  <text x="325" y="85" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">NATIONAL EMERGENCY</text>
  <text x="325" y="100" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">Article 352</text>
  <text x="230" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">War, External Aggression, or Armed Rebellion (44th Am.)</text>
  <text x="230" y="165" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#a63b49">ONE MONTH (30 Days)</text>
  <text x="230" y="205" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">Special Majority (2/3 + Total)</text>
  <text x="230" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Indefinite (6 months at a time)</text>
  <text x="230" y="285" font-family="system-ui, sans-serif" font-size="9" fill="#a63b49">Art 19 suspended (358); Arts 20 &amp; 21 NEVER suspended</text>
  <text x="230" y="325" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">3 Times (1962, 1971, 1975)</text>

  <!-- Column 3: Art 356 -->
  <rect x="440" y="60" width="210" height="280" rx="6" fill="#fff"/>
  <text x="545" y="85" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">PRESIDENT'S RULE</text>
  <text x="545" y="100" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">Article 356 &amp; 365</text>
  <text x="450" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Failure of constitutional machinery in State</text>
  <text x="450" y="165" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">TWO MONTHS (60 Days)</text>
  <text x="450" y="205" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">Simple Majority</text>
  <text x="450" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Max 3 YEARS (1 yr cap unless EC certifies)</text>
  <text x="450" y="285" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">NO effect on Fundamental Rights of citizens</text>
  <text x="450" y="325" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#a63b49">Over 130 times</text>

  <!-- Column 4: Art 360 -->
  <rect x="660" y="60" width="210" height="280" rx="6" fill="#fff"/>
  <text x="765" y="85" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">FINANCIAL EMERGENCY</text>
  <text x="765" y="100" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">Article 360</text>
  <text x="670" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Threat to financial stability or credit of India</text>
  <text x="670" y="165" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">TWO MONTHS (60 Days)</text>
  <text x="670" y="205" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">Simple Majority</text>
  <text x="670" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Indefinite (no statutory max limit)</text>
  <text x="670" y="285" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">Salary reduction of Union/State staff &amp; SC/HC Judges</text>
  <text x="670" y="325" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">NEVER (0 Times)</text>
</svg>
""")

# 9. diag-federal-distribution.svg
write_svg("diag-federal-distribution.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="fbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#fbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">SEVENTH SCHEDULE: THREE LEGISLATIVE LISTS</text>
  <text x="450" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">Article 246 &amp; The Federal Distribution of Legislative Competence</text>
  
  <!-- List I: Union List -->
  <rect x="40" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="40" y="90" width="250" height="35" rx="8" fill="#142c46"/>
  <text x="165" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">LIST I: UNION LIST</text>
  <text x="165" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Exclusive Parliament Power</text>
  <text x="50" y="165" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Original: 97 Entries | Now: 100 Entries</text>
  <text x="50" y="185" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Defense, Armed Forces &amp; Atomic Energy</text>
  <text x="50" y="205" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Foreign Affairs &amp; Treaties (Art. 253)</text>
  <text x="50" y="225" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Railways, Airways &amp; National Highways</text>
  <text x="50" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Banking, Insurance &amp; Currency</text>
  <text x="50" y="265" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Inter-State Trade and Commerce</text>
  <text x="50" y="295" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#142c46">• Entry 97: RESIDUARY POWERS (Art. 248)</text>

  <!-- List II: State List -->
  <rect x="325" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="325" y="90" width="250" height="35" rx="8" fill="#137d72"/>
  <text x="450" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#fff">LIST II: STATE LIST</text>
  <text x="450" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Exclusive State Legislature Power</text>
  <text x="335" y="165" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Original: 66 Entries | Now: 61 Entries</text>
  <text x="335" y="185" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Public Order &amp; Police</text>
  <text x="335" y="205" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Public Health, Sanitation &amp; Hospitals</text>
  <text x="335" y="225" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Agriculture &amp; Irrigation</text>
  <text x="335" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Local Government (Panchayats/Municipal)</text>
  <text x="335" y="265" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Land &amp; Tenures, Fisheries</text>
  <text x="335" y="295" font-family="system-ui, sans-serif" font-size="9.5" fill="#a63b49">• 5 subjects shifted to Concurrent (42nd Am)</text>

  <!-- List III: Concurrent List -->
  <rect x="610" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="610" y="90" width="250" height="35" rx="8" fill="#142c46"/>
  <text x="735" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">LIST III: CONCURRENT LIST</text>
  <text x="735" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Both Parliament &amp; States Can Legislate</text>
  <text x="620" y="165" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Original: 47 Entries | Now: 52 Entries</text>
  <text x="620" y="185" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Criminal Law (BNS) &amp; CrPC (BNSS)</text>
  <text x="620" y="205" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Civil Procedure &amp; Evidence (BSA)</text>
  <text x="620" y="225" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Marriage, Divorce &amp; Succession</text>
  <text x="620" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Education, Forests &amp; Weights (42nd Am)</text>
  <text x="620" y="265" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Economic &amp; Social Planning</text>
  <text x="620" y="295" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#a63b49">• REPUGNANCY RULE: Art. 254 (Union Prevails)</text>
</svg>
""")

print("All SVG diagrams created successfully!")

# 10. diag-dpsp-classification.svg
write_svg("diag-dpsp-classification.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="dbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#dbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">DIRECTIVE PRINCIPLES OF STATE POLICY: 3-TIER CLASSIFICATION</text>
  <text x="450" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">Part IV (Articles 36–51) — Ideological Framework for Socio-Economic Justice</text>
  
  <!-- Socialistic Principles -->
  <rect x="40" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="40" y="90" width="250" height="35" rx="8" fill="#137d72"/>
  <text x="165" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#fff">SOCIALISTIC PRINCIPLES</text>
  <text x="50" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 38:</tspan> Social order promoting welfare</text>
  <text x="50" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 39(b)&amp;(c):</tspan> Material resources &amp; no concentration of wealth</text>
  <text x="50" y="200" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 39(d):</tspan> Equal pay for equal work</text>
  <text x="50" y="225" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 39A:</tspan> Equal justice &amp; free legal aid</text>
  <text x="50" y="250" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 41:</tspan> Right to work &amp; education</text>
  <text x="50" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 42:</tspan> Just, humane &amp; maternity relief</text>
  <text x="50" y="300" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 43/43A:</tspan> Living wage &amp; worker mgmt</text>

  <!-- Gandhian Principles -->
  <rect x="325" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="325" y="90" width="250" height="35" rx="8" fill="#142c46"/>
  <text x="450" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">GANDHIAN PRINCIPLES</text>
  <text x="335" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 40:</tspan> Organization of Village Panchayats</text>
  <text x="335" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 43:</tspan> Promotion of cottage industries in rural areas</text>
  <text x="335" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 43B:</tspan> Voluntary formation of Co-operative societies (97th Am.)</text>
  <text x="335" y="250" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 46:</tspan> Educational &amp; economic interests of SCs, STs &amp; weaker sections</text>
  <text x="335" y="285" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 47:</tspan> Prohibition of intoxicating drinks</text>
  <text x="335" y="310" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 48:</tspan> Prohibition of slaughter of cows</text>

  <!-- Liberal-Intellectual -->
  <rect x="610" y="90" width="250" height="240" rx="8" fill="#fff"/>
  <rect x="610" y="90" width="250" height="35" rx="8" fill="#137d72"/>
  <text x="735" y="112" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#fff">LIBERAL-INTELLECTUAL</text>
  <text x="620" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 44:</tspan> Uniform Civil Code (UCC) for all citizens</text>
  <text x="620" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 45:</tspan> Early childhood care (0-6 yrs)</text>
  <text x="620" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 48A:</tspan> Protection of environment, forests &amp; wild life (42nd Am.)</text>
  <text x="620" y="250" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 49:</tspan> Protection of monuments &amp; places of national importance</text>
  <text x="620" y="285" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 50:</tspan> Separation of Judiciary from Executive in public services</text>
  <text x="620" y="315" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• <tspan font-weight="bold">Art. 51:</tspan> International peace &amp; security</text>
</svg>
""")

# 11. diag-judicial-hierarchy.svg
write_svg("diag-judicial-hierarchy.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="jbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#jbg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">THE INTEGRATED INDIAN JUDICIAL PYRAMID</text>
  <text x="450" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="12" fill="#a0b3c6">Unified Single System of Courts (Articles 124–147, 214–237)</text>
  
  <!-- Tier 1: Supreme Court of India -->
  <polygon points="450,85 300,165 600,165" fill="#dfbf80" stroke="#fff" stroke-width="2"/>
  <text x="450" y="125" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#142c46">SUPREME COURT OF INDIA</text>
  <text x="450" y="145" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#1b3857">Apex Court • Art. 124 • 34 Judges • Binding Law (Art. 141)</text>

  <!-- Tier 2: High Courts of States -->
  <polygon points="300,170 200,245 700,245 600,170" fill="#137d72" stroke="#fff" stroke-width="2"/>
  <text x="450" y="200" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">HIGH COURTS OF STATES &amp; UTs (25 High Courts)</text>
  <text x="450" y="220" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#dfbf80">Writ Jurisdiction (Art. 226) • Superintendence over all Courts &amp; Tribunals (Art. 227)</text>

  <!-- Tier 3: Subordinate Judiciary -->
  <polygon points="200,250 80,335 820,335 700,250" fill="#ffffff" stroke="#dfbf80" stroke-width="2"/>
  <text x="450" y="275" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">SUBORDINATE JUDICIARY (DISTRICT &amp; SESSIONS COURTS)</text>
  <text x="250" y="305" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">CIVIL SIDE</text>
  <text x="250" y="322" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">District Judge → Civil Judge (Senior Div) → Junior Div</text>
  <line x1="450" y1="285" x2="450" y2="330" stroke="#cdb17d" stroke-width="1.5" stroke-dasharray="4 2"/>
  <text x="650" y="305" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#a63b49">CRIMINAL SIDE</text>
  <text x="650" y="322" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#607387">Sessions Judge → Addl. Sessions → CJM / JMFC / JMIC</text>
</svg>
""")

# 12. diag-amendment-process.svg
write_svg("diag-amendment-process.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs><linearGradient id="abg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142c46"/><stop offset="100%" stop-color="#1b3857"/></linearGradient></defs>
  <rect width="900" height="360" fill="url(#abg)" rx="12"/>
  <text x="450" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#dfbf80">ARTICLE 368: CONSTITUTIONAL AMENDMENT FLOW</text>
  
  <!-- Step 1: Initiation -->
  <rect x="40" y="80" width="160" height="130" rx="8" fill="#fff"/>
  <rect x="40" y="80" width="160" height="28" rx="8" fill="#142c46"/>
  <text x="120" y="99" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">1. INITIATION</text>
  <text x="50" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• In EITHER House of Parliament</text>
  <text x="50" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• By Minister or Private Member</text>
  <text x="50" y="175" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">• NO prior President recommendation</text>

  <!-- Arrow 1 -->
  <line x1="205" y1="145" x2="250" y2="145" stroke="#dfbf80" stroke-width="3"/>
  <polygon points="250,145 240,140 240,150" fill="#dfbf80"/>

  <!-- Step 2: Passage in Parliament -->
  <rect x="255" y="80" width="180" height="130" rx="8" fill="#fff"/>
  <rect x="255" y="80" width="180" height="28" rx="8" fill="#137d72"/>
  <text x="345" y="99" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#fff">2. PARLIAMENT VOTE</text>
  <text x="265" y="125" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#142c46">• Special Majority in EACH House:</text>
  <text x="270" y="145" font-family="system-ui, sans-serif" font-size="8.5" fill="#607387">(a) Majority of total membership</text>
  <text x="270" y="160" font-family="system-ui, sans-serif" font-size="8.5" fill="#607387">(b) 2/3rds present &amp; voting</text>
  <text x="265" y="185" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#a63b49">• NO JOINT SITTING (Art. 108)</text>

  <!-- Arrow 2 -->
  <line x1="440" y1="145" x2="485" y2="145" stroke="#dfbf80" stroke-width="3"/>
  <polygon points="485,145 475,140 475,150" fill="#dfbf80"/>

  <!-- Step 3: State Ratification (if federal) -->
  <rect x="490" y="80" width="170" height="130" rx="8" fill="#fff"/>
  <rect x="490" y="80" width="170" height="28" rx="8" fill="#142c46"/>
  <text x="575" y="99" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">3. STATE RATIFICATION</text>
  <text x="500" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#1c2e40">• Required ONLY for federal matters (Art. 54, 55, 73, 162, 7th Sched, SC/HC, Art 368)</text>
  <text x="500" y="170" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#137d72">• ≥ 50% State Assemblies</text>
  <text x="500" y="190" font-family="system-ui, sans-serif" font-size="9" fill="#607387">• Simple majority in States</text>

  <!-- Arrow 3 -->
  <line x1="665" y1="145" x2="710" y2="145" stroke="#dfbf80" stroke-width="3"/>
  <polygon points="710,145 700,140 700,150" fill="#dfbf80"/>

  <!-- Step 4: Presidential Assent -->
  <rect x="715" y="80" width="155" height="130" rx="8" fill="#dfbf80"/>
  <rect x="715" y="80" width="155" height="28" rx="8" fill="#142c46"/>
  <text x="792" y="99" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">4. ASSENT</text>
  <text x="725" y="125" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#142c46">• President SHALL give assent</text>
  <text x="725" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#1b3857">• Cannot withhold assent</text>
  <text x="725" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#1b3857">• Cannot return for reconsideration</text>
  <text x="725" y="195" font-family="system-ui, sans-serif" font-size="8.5" fill="#a63b49">(24th Amendment Act, 1971)</text>

  <!-- Inviolable Safeguard: Basic Structure -->
  <rect x="150" y="240" width="600" height="90" rx="8" fill="#ffffff" stroke="#a63b49" stroke-width="2"/>
  <text x="450" y="265" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#a63b49">THE INVIOLABLE CONSTITUTIONAL BOUNDARY</text>
  <text x="450" y="288" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">THE BASIC STRUCTURE DOCTRINE (Kesavananda Bharati, 1973)</text>
  <text x="450" y="310" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" fill="#607387">Parliament cannot alter Supremacy of Constitution, Republican &amp; Democratic form, Secularism, Federalism, Separation of Powers, Judicial Review, or Judicial Independence.</text>
</svg>
""")
