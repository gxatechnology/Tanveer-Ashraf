import os

DIAGRAMS_DIR = 'assets/learning/images/diagrams'
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

def create_svg(filename, title, subtitle, content_xml, width=800, height=500):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdfbf7"/>
      <stop offset="100%" stop-color="#f5ede0"/>
    </linearGradient>
    <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#137d72"/>
      <stop offset="100%" stop-color="#0d5c54"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#142c46" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="{width}" height="{height}" rx="12" fill="#f8fafc" stroke="#dce3ea" stroke-width="2"/>

  <!-- Top Decorative Header Bar -->
  <rect width="{width}" height="60" rx="12" fill="url(#bgGrad)"/>
  <rect y="48" width="{width}" height="12" fill="#142c46"/>
  <rect y="58" width="{width}" height="3" fill="#dfbf80"/>

  <!-- Header Title -->
  <text x="24" y="32" font-family="Georgia, serif" font-size="19" font-weight="bold" fill="#ffffff">{title}</text>
  <text x="24" y="50" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#dfbf80">{subtitle}</text>
  <text x="{width - 24}" y="36" text-anchor="end" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#a0c0dc">UP PCS-J ACADEMIC BLUEPRINT</text>

  <!-- Body Content -->
  <g transform="translate(0, 70)">
    {content_xml}
  </g>

  <!-- Footer Watermark -->
  <text x="{width / 2}" y="{height - 12}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" fill="#8899aa">Judicial Learning Academy · Tanveer Ashraf Judicial Prep · Authoritative Subject Schematic</text>
</svg>"""
    filepath = os.path.join(DIAGRAMS_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Created {filename}")

# -------------------------------------------------------------
# JURISPRUDENCE DIAGRAMS (8)
# -------------------------------------------------------------

# 1. Comparative Schools
jur_schools_xml = """
  <!-- 5 Schools Comparison Cards -->
  <g transform="translate(20, 20)">
    <!-- Natural Law -->
    <rect x="0" y="0" width="140" height="360" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="140" height="36" rx="8" fill="#137d72"/>
    <rect x="0" y="28" width="140" height="8" fill="#137d72"/>
    <text x="70" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Natural Law</text>
    <text x="70" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Premise</text>
    <text x="70" y="75" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Universal moral order</text>
    <text x="70" y="90" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Lex injusta non est lex</text>
    <line x1="15" y1="105" x2="125" y2="105" stroke="#edf0f4"/>
    <text x="70" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Proponents</text>
    <text x="70" y="142" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">• Thomas Aquinas</text>
    <text x="70" y="157" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">• John Locke</text>
    <text x="70" y="172" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">• Lon Fuller</text>
    <text x="70" y="187" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">• John Finnis</text>
    <line x1="15" y1="205" x2="125" y2="205" stroke="#edf0f4"/>
    <text x="70" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Central Focus</text>
    <text x="15" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Law derived from reason,</text>
    <text x="15" y="260" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">nature and divine purpose.</text>
    <text x="15" y="275" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Morality is an inherent</text>
    <text x="15" y="290" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">validity condition of law.</text>

    <!-- Analytical Positivist -->
    <rect x="155" y="0" width="140" height="360" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="155" y="0" width="140" height="36" rx="8" fill="#142c46"/>
    <rect x="155" y="28" width="140" height="8" fill="#142c46"/>
    <text x="225" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Analytical</text>
    <text x="225" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Premise</text>
    <text x="225" y="75" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Law as it is (Positum)</text>
    <text x="225" y="90" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Separation thesis</text>
    <line x1="170" y1="105" x2="280" y2="105" stroke="#edf0f4"/>
    <text x="225" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Proponents</text>
    <text x="225" y="142" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• Jeremy Bentham</text>
    <text x="225" y="157" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• John Austin</text>
    <text x="225" y="172" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• H.L.A. Hart</text>
    <text x="225" y="187" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#142c46">• Hans Kelsen</text>
    <line x1="170" y1="205" x2="280" y2="205" stroke="#edf0f4"/>
    <text x="225" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Central Focus</text>
    <text x="170" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Commands of sovereign,</text>
    <text x="170" y="260" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">sanctions, primary/secondary</text>
    <text x="170" y="275" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">rules, and the Grundnorm</text>
    <text x="170" y="290" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">hierarchy of norms.</text>

    <!-- Historical -->
    <rect x="310" y="0" width="140" height="360" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="2" filter="url(#shadow)"/>
    <rect x="310" y="0" width="140" height="36" rx="8" fill="#b98a38"/>
    <rect x="310" y="28" width="140" height="8" fill="#b98a38"/>
    <text x="380" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Historical</text>
    <text x="380" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Premise</text>
    <text x="380" y="75" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Law is found, not made</text>
    <text x="380" y="90" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Volksgeist (National spirit)</text>
    <line x1="325" y1="105" x2="435" y2="105" stroke="#edf0f4"/>
    <text x="380" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Proponents</text>
    <text x="380" y="142" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#74582a">• F.C. von Savigny</text>
    <text x="380" y="157" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#74582a">• Sir Henry Maine</text>
    <text x="380" y="172" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#74582a">• Georg F. Puchta</text>
    <line x1="325" y1="205" x2="435" y2="205" stroke="#edf0f4"/>
    <text x="380" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Central Focus</text>
    <text x="325" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Customary traditions,</text>
    <text x="325" y="260" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">historical evolution,</text>
    <text x="325" y="275" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">movement from Status</text>
    <text x="325" y="290" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">to Contract in societies.</text>

    <!-- Sociological -->
    <rect x="465" y="0" width="140" height="360" rx="8" fill="#ffffff" stroke="#135e48" stroke-width="2" filter="url(#shadow)"/>
    <rect x="465" y="0" width="140" height="36" rx="8" fill="#135e48"/>
    <rect x="465" y="28" width="140" height="8" fill="#135e48"/>
    <text x="535" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Sociological</text>
    <text x="535" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Premise</text>
    <text x="535" y="75" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Law as Social Engineering</text>
    <text x="535" y="90" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Living Law in action</text>
    <line x1="480" y1="105" x2="590" y2="105" stroke="#edf0f4"/>
    <text x="535" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Proponents</text>
    <text x="535" y="142" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#135e48">• Rudolf von Ihering</text>
    <text x="535" y="157" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#135e48">• Eugen Ehrlich</text>
    <text x="535" y="172" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#135e48">• Léon Duguit</text>
    <text x="535" y="187" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#135e48">• Roscoe Pound</text>
    <line x1="480" y1="205" x2="590" y2="205" stroke="#edf0f4"/>
    <text x="535" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Central Focus</text>
    <text x="480" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Balancing competing</text>
    <text x="480" y="260" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">individual, public and</text>
    <text x="480" y="275" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">social interests with least</text>
    <text x="480" y="290" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">friction and waste.</text>

    <!-- Realist -->
    <rect x="620" y="0" width="140" height="360" rx="8" fill="#ffffff" stroke="#a63b49" stroke-width="2" filter="url(#shadow)"/>
    <rect x="620" y="0" width="140" height="36" rx="8" fill="#a63b49"/>
    <rect x="620" y="28" width="140" height="8" fill="#a63b49"/>
    <text x="690" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Realist</text>
    <text x="690" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Premise</text>
    <text x="690" y="75" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Law is what judges do</text>
    <text x="690" y="90" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Skepticism of rules</text>
    <line x1="635" y1="105" x2="745" y2="105" stroke="#edf0f4"/>
    <text x="690" y="125" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Proponents</text>
    <text x="690" y="142" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#a63b49">• O.W. Holmes Jr.</text>
    <text x="690" y="157" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#a63b49">• Karl Llewellyn</text>
    <text x="690" y="172" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#a63b49">• Jerome Frank</text>
    <text x="690" y="187" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#a63b49">• Alf Ross</text>
    <line x1="635" y1="205" x2="745" y2="205" stroke="#edf0f4"/>
    <text x="690" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Central Focus</text>
    <text x="635" y="245" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">Courtroom realities,</text>
    <text x="635" y="260" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">psychological biases,</text>
    <text x="635" y="275" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">bad man perspective,</text>
    <text x="635" y="290" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">and prophecy of courts.</text>
  </g>
"""
create_svg('diag-jur-schools-comparison.svg', 'Comparative Schools of Jurisprudence', 'Foundational philosophical paradigms, core doctrines and leading jurists', jur_schools_xml)

# 2. Jurists & Theories
jur_jurists_xml = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="20" y="26" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">John Austin (1790–1859)</text>
    <text x="20" y="46" font-family="system-ui, sans-serif" font-size="12" fill="#607387">"Law is the command of a sovereign backed by the threat of sanction, habitual obedience."</text>
    <rect x="580" y="14" width="120" height="32" rx="4" fill="#edf7f4"/>
    <text x="640" y="34" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Command Theory</text>

    <rect x="0" y="75" width="720" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="20" y="101" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">Hans Kelsen (1881–1973)</text>
    <text x="20" y="121" font-family="system-ui, sans-serif" font-size="12" fill="#607387">"Law is a hierarchy of ought-propositions validated by an apex Grundnorm (Basic Norm)."</text>
    <rect x="580" y="89" width="120" height="32" rx="4" fill="#fff8ee"/>
    <text x="640" y="109" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#b98a38">Pure Theory</text>

    <rect x="0" y="150" width="720" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="20" y="176" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">H.L.A. Hart (1907–1992)</text>
    <text x="20" y="196" font-family="system-ui, sans-serif" font-size="12" fill="#607387">"Law is the union of primary rules of obligation and secondary rules of recognition, change &amp; adjudication."</text>
    <rect x="580" y="164" width="120" height="32" rx="4" fill="#edf7f4"/>
    <text x="640" y="184" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Rule of Recognition</text>

    <rect x="0" y="225" width="720" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="20" y="251" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">Friedrich Carl von Savigny (1779–1861)</text>
    <text x="20" y="271" font-family="system-ui, sans-serif" font-size="12" fill="#607387">"Law grows with the growth and strengthens with the strength of the people (Volksgeist)."</text>
    <rect x="580" y="239" width="120" height="32" rx="4" fill="#fff8ee"/>
    <text x="640" y="259" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#b98a38">Volksgeist Doctrine</text>

    <rect x="0" y="300" width="720" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="20" y="326" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">Roscoe Pound (1870–1964)</text>
    <text x="20" y="346" font-family="system-ui, sans-serif" font-size="12" fill="#607387">"Law is social engineering to satisfy maximum human wants with minimum friction and waste."</text>
    <rect x="580" y="314" width="120" height="32" rx="4" fill="#edf7f4"/>
    <text x="640" y="334" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Social Engineering</text>
  </g>
"""
create_svg('diag-jur-jurists-theories.svg', 'Master Jurists & Core Jurisprudential Doctrines', 'Authoritative synthesis of prominent analytical, historical and sociological scholars', jur_jurists_xml)

# 3. Law vs Morality
jur_morality_xml = """
  <g transform="translate(60, 40)">
    <!-- Law Circle -->
    <circle cx="240" cy="160" r="140" fill="#142c46" fill-opacity="0.15" stroke="#142c46" stroke-width="3"/>
    <!-- Morality Circle -->
    <circle cx="440" cy="160" r="140" fill="#137d72" fill-opacity="0.15" stroke="#137d72" stroke-width="3"/>

    <!-- Left: Law Exclusive -->
    <text x="170" y="130" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#142c46">Law Alone</text>
    <text x="170" y="155" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Traffic rules (drive on left)</text>
    <text x="170" y="175" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Company filing formalities</text>
    <text x="170" y="195" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Procedural stamp duty</text>

    <!-- Center Intersection: Confluence -->
    <text x="340" y="115" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#b98a38">Confluence</text>
    <text x="340" y="135" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#142c46">(Law + Morals)</text>
    <text x="340" y="160" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Prohibition of Murder</text>
    <text x="340" y="178" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Theft &amp; Robbery</text>
    <text x="340" y="196" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Fraud &amp; Perjury</text>
    <text x="340" y="214" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Rape &amp; Assault</text>

    <!-- Right: Morality Exclusive -->
    <text x="510" y="130" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#137d72">Morality Alone</text>
    <text x="510" y="155" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Telling petty lies</text>
    <text x="510" y="175" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Ingratitude to parents</text>
    <text x="510" y="195" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Failing to help stranger</text>
    <text x="510" y="215" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Coveting another's wealth</text>
  </g>
"""
create_svg('diag-jur-law-morality.svg', 'Jurisprudential Intersections: Law versus Morality', 'Hart-Fuller & Hart-Devlin perspectives on the distinct boundaries of legal and ethical enforcement', jur_morality_xml)

# 4. Hohfeld's Table
jur_hohfeld_xml = """
  <g transform="translate(50, 20)">
    <!-- Correlatives Table -->
    <rect x="0" y="0" width="700" height="160" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2"/>
    <rect x="0" y="0" width="700" height="32" rx="8" fill="#142c46"/>
    <text x="350" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">TABLE 1: JURAL CORRELATIVES (Vertical Presence: One Entails the Other)</text>
    <line x1="175" y1="32" x2="175" y2="160" stroke="#dce3ea"/>
    <line x1="350" y1="32" x2="350" y2="160" stroke="#dce3ea"/>
    <line x1="525" y1="32" x2="525" y2="160" stroke="#dce3ea"/>
    <line x1="0" y1="96" x2="700" y2="96" stroke="#dce3ea"/>

    <text x="87" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#137d72">RIGHT (Claim)</text>
    <text x="87" y="80" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">A demands B not trespass</text>
    <text x="87" y="126" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">DUTY</text>
    <text x="87" y="144" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">B must not trespass</text>

    <text x="262" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#137d72">PRIVILEGE (Liberty)</text>
    <text x="262" y="80" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">A walks on public road</text>
    <text x="262" y="126" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">NO-RIGHT</text>
    <text x="262" y="144" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">B cannot stop A</text>

    <text x="437" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#137d72">POWER</text>
    <text x="437" y="80" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">A makes a valid will</text>
    <text x="437" y="126" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">LIABILITY</text>
    <text x="437" y="144" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">B's position altered</text>

    <text x="612" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#137d72">IMMUNITY</text>
    <text x="612" y="80" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">President cannot be sued</text>
    <text x="612" y="126" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">DISABILITY</text>
    <text x="612" y="144" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#607387">Citizen lacks power to sue</text>

    <!-- Opposites Table -->
    <rect x="0" y="190" width="700" height="160" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="2"/>
    <rect x="0" y="190" width="700" height="32" rx="8" fill="#b98a38"/>
    <text x="350" y="212" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">TABLE 2: JURAL OPPOSITES (In One Person: Contradictory States)</text>
    <line x1="175" y1="222" x2="175" y2="350" stroke="#dce3ea"/>
    <line x1="350" y1="222" x2="350" y2="350" stroke="#dce3ea"/>
    <line x1="525" y1="222" x2="525" y2="350" stroke="#dce3ea"/>
    <line x1="0" y1="286" x2="700" y2="286" stroke="#dce3ea"/>

    <text x="87" y="252" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">RIGHT</text>
    <text x="87" y="322" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#a63b49">NO-RIGHT</text>

    <text x="262" y="252" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">PRIVILEGE</text>
    <text x="262" y="322" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#a63b49">DUTY</text>

    <text x="437" y="252" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">POWER</text>
    <text x="437" y="322" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#a63b49">DISABILITY</text>

    <text x="612" y="252" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#142c46">IMMUNITY</text>
    <text x="612" y="322" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#a63b49">LIABILITY</text>
  </g>
"""
create_svg('diag-jur-hohfeld-table.svg', "Hohfeld's Fundamental Legal Conceptions Matrix", 'Comprehensive representation of Jural Correlatives and Jural Opposites', jur_hohfeld_xml)

# 5. Ownership vs Possession
jur_own_pos_xml = """
  <g transform="translate(40, 20)">
    <!-- Ownership Card -->
    <rect x="0" y="0" width="340" height="350" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#dfbf80">OWNERSHIP (De Jure Right)</text>
    <text x="20" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Definition (Salmond):</text>
    <text x="20" y="86" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">The relation between a person and any right that is vested in him.</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Bundle of Rights (Incidents):</text>
    <text x="20" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">1. Right to possess (Jus Possidendi)</text>
    <text x="20" y="153" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">2. Right to use &amp; enjoy (Jus Utendi)</text>
    <text x="20" y="171" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">3. Right to consume or destroy (Jus Abutendi)</text>
    <text x="20" y="189" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">4. Right to alienate or transfer (Jus Disponendi)</text>
    <text x="20" y="207" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">5. Indeterminate duration &amp; residuary character</text>
    <line x1="20" y1="225" x2="320" y2="225" stroke="#edf0f4"/>
    <text x="20" y="250" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#137d72">Legal Characteristic:</text>
    <text x="20" y="270" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">Absolute and ultimate title recognized by the legal order, independent of physical control.</text>

    <!-- Possession Card -->
    <rect x="380" y="0" width="340" height="350" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="380" y="0" width="340" height="42" rx="8" fill="#137d72"/>
    <text x="550" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#ffffff">POSSESSION (De Facto Control)</text>
    <text x="400" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Definition (Salmond):</text>
    <text x="400" y="86" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Continuing exercise of a claim to the exclusive physical use of a thing.</text>
    <text x="400" y="115" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Two Essential Elements (Savigny):</text>
    <text x="400" y="135" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">1. Corpus Possessionis:</text>
    <text x="415" y="153" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">Physical control &amp; power to exclude others.</text>
    <text x="400" y="175" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">2. Animus Possidendi:</text>
    <text x="415" y="193" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">Mental intention to hold as owner / for self.</text>
    <line x1="400" y1="225" x2="700" y2="225" stroke="#edf0f4"/>
    <text x="400" y="250" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#137d72">Legal Axiom:</text>
    <text x="400" y="270" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">"Possession is nine points of the law."</text>
    <text x="400" y="288" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">Protected by law against all except true owner.</text>
  </g>
"""
create_svg('diag-jur-ownership-possession.svg', 'Ownership versus Possession: The De Jure & De Facto Nexus', 'Comparative analysis of the bundle of rights and corpus-animus dualism', jur_own_pos_xml)

# 6. Legal Personality
jur_personality_xml = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="340" height="160" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="30" rx="8" fill="#142c46"/>
    <text x="170" y="20" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">Natural Persons</text>
    <text x="20" y="55" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Living human beings with legal capacity</text>
    <text x="20" y="75" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Unborn child (Nasciturus pro iam nato habetur)</text>
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Dead persons: Reputation, body, will protected</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Animals: Objects of legal duty, not rights holders</text>

    <rect x="380" y="0" width="340" height="160" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="1.5"/>
    <rect x="380" y="0" width="340" height="30" rx="8" fill="#137d72"/>
    <text x="550" y="20" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">Juristic / Artificial Persons</text>
    <text x="400" y="55" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Incorporated Companies (Salomon v Salomon)</text>
    <text x="400" y="75" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Hindu Deity / Idol (Pramatha Nath Mullick)</text>
    <text x="400" y="95" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Guru Granth Sahib (Shiromani Gurdwara case)</text>
    <text x="400" y="115" font-family="system-ui, sans-serif" font-size="11.5" fill="#1c2e40">• Corporations sole and Corporations aggregate</text>

    <!-- Theories of Corporate Personality -->
    <rect x="0" y="180" width="720" height="180" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="1.5"/>
    <rect x="0" y="180" width="720" height="30" rx="8" fill="#b98a38"/>
    <text x="360" y="200" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">THEORIES OF CORPORATE PERSONALITY</text>
    
    <text x="20" y="235" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">1. Fiction Theory (Savigny &amp; Salmond):</text>
    <text x="20" y="252" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Personality is a pure legal fiction created solely by the authority of the state.</text>

    <text x="20" y="280" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">2. Realist Theory (Gierke):</text>
    <text x="20" y="297" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Corporation is an organic, living reality with a genuine collective will, not a fiction.</text>

    <text x="380" y="235" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">3. Bracket / Symbolist Theory (Jhering):</text>
    <text x="380" y="252" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Corporation is a convenient bracket enclosing natural human members.</text>

    <text x="380" y="280" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">4. Purpose Theory (Brinz):</text>
    <text x="380" y="297" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Legal person is simply dedicated property (Zweckvermögen) tied to a purpose.</text>
  </g>
"""
create_svg('diag-jur-legal-personality.svg', 'Theories and Taxonomy of Legal Personality', 'Natural vs Juristic persons and the five major theories of corporate entity', jur_personality_xml)

# 7. Sources of Law
jur_sources_xml = """
  <g transform="translate(60, 20)">
    <!-- Central Node -->
    <rect x="240" y="10" width="200" height="50" rx="8" fill="#142c46" stroke="#dfbf80" stroke-width="2"/>
    <text x="340" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#dfbf80">SOURCES OF LAW</text>

    <!-- Branch 1: Custom -->
    <rect x="0" y="110" width="200" height="240" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2"/>
    <rect x="0" y="110" width="200" height="32" rx="8" fill="#137d72"/>
    <text x="100" y="131" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">CUSTOM (Consuetudo)</text>
    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Mandatory Requisites:</text>
    <text x="15" y="185" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Immemorial Antiquity</text>
    <text x="15" y="205" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Continuous Observance</text>
    <text x="15" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Reasonableness</text>
    <text x="15" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Conformity with Statute</text>
    <text x="15" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Opinio Juris Necessitatis</text>

    <!-- Branch 2: Judicial Precedent -->
    <rect x="240" y="110" width="200" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2"/>
    <rect x="240" y="110" width="200" height="32" rx="8" fill="#142c46"/>
    <text x="340" y="131" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">JUDICIAL PRECEDENT</text>
    <text x="255" y="165" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Stare Decisis Principles:</text>
    <text x="255" y="185" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Ratio Decidendi (Binding)</text>
    <text x="255" y="205" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Obiter Dicta (Persuasive)</text>
    <text x="255" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Declaratory Theory (Carter)</text>
    <text x="255" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Creative Theory (Austin)</text>
    <text x="255" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Art. 141 Binding Precedent</text>

    <!-- Branch 3: Legislation -->
    <rect x="480" y="110" width="200" height="240" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="2"/>
    <rect x="480" y="110" width="200" height="32" rx="8" fill="#b98a38"/>
    <text x="580" y="131" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">LEGISLATION</text>
    <text x="495" y="165" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Direct State Enactment:</text>
    <text x="495" y="185" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Supreme Legislation (Acts)</text>
    <text x="495" y="205" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Subordinate / Delegated</text>
    <text x="495" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Executive Ordinances</text>
    <text x="495" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Municipal Bye-laws</text>
    <text x="495" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Overrides Custom &amp; Ruling</text>
  </g>
"""
create_svg('diag-jur-sources-of-law.svg', 'Tripartite Classification of Sources of Law', 'Analytical hierarchy between Custom, Judicial Precedent and Statutory Legislation', jur_sources_xml)

# 8. Types of Liability
jur_liability_xml = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="220" height="340" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="8" fill="#142c46"/>
    <text x="110" y="24" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">Civil vs Penal Liability</text>
    <text x="20" y="60" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Remedial Liability:</text>
    <text x="20" y="78" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">Enforcement of plaintiff's right via compensation, specific performance or restitution.</text>
    <text x="20" y="130" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#a63b49">Penal Liability:</text>
    <text x="20" y="148" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">Infliction of punishment for breach of public duty to deter and reform.</text>

    <rect x="250" y="0" width="220" height="340" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2"/>
    <rect x="250" y="0" width="220" height="36" rx="8" fill="#137d72"/>
    <text x="360" y="24" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">Strict vs Absolute</text>
    <text x="270" y="60" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Strict Liability (Rylands):</text>
    <text x="270" y="78" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">Non-natural user + Escape of dangerous thing. Subject to 5 exceptions (Act of God, Consent, etc.).</text>
    <text x="270" y="140" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Absolute Liability (M.C. Mehta):</text>
    <text x="270" y="158" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">Hazardous enterprise. Zero exceptions. Strict duty to community.</text>

    <rect x="500" y="0" width="220" height="340" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="2"/>
    <rect x="500" y="0" width="220" height="36" rx="8" fill="#b98a38"/>
    <text x="610" y="24" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">Vicarious Liability</text>
    <text x="520" y="60" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Foundational Maxims:</text>
    <text x="520" y="80" font-family="system-ui, sans-serif" font-size="10.5" fill="#74582a">• Qui facit per alium facit per se</text>
    <text x="520" y="100" font-family="system-ui, sans-serif" font-size="10.5" fill="#74582a">• Respondeat Superior</text>
    <text x="520" y="130" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Conditions:</text>
    <text x="520" y="148" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">1. Master-Servant relation.</text>
    <text x="520" y="168" font-family="system-ui, sans-serif" font-size="10.5" fill="#607387">2. Act in the course of employment.</text>
  </g>
"""
create_svg('diag-jur-liability-types.svg', 'Taxonomy of Legal Liability in Jurisprudence', 'Civil, criminal, strict, absolute and vicarious liability doctrines', jur_liability_xml)

print("Jurisprudence diagrams generated!")

# -------------------------------------------------------------
# CONTRACT LAW DIAGRAMS (8)
# -------------------------------------------------------------

# 1. Agreement vs Contract
cnt_agr_vs_cont_xml = """
  <g transform="translate(60, 30)">
    <rect x="0" y="0" width="300" height="320" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="300" height="40" rx="8" fill="#142c46"/>
    <text x="150" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#dfbf80">AGREEMENT [Section 2(e)]</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Statutory Formula:</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">Offer + Acceptance = Promise</text>
    <text x="20" y="103" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">Promise + Consideration = Agreement</text>
    <line x1="20" y1="120" x2="280" y2="120" stroke="#edf0f4"/>
    <text x="20" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Key Characteristics:</text>
    <text x="20" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Wider genus (social, domestic, legal)</text>
    <text x="20" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• May or may not create legal obligation</text>
    <text x="20" y="205" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• Not necessarily enforceable by court</text>
    <text x="20" y="225" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">• All contracts are agreements</text>

    <!-- Plus Enforceability -->
    <circle cx="340" cy="160" r="24" fill="#dfbf80"/>
    <text x="340" y="166" text-anchor="middle" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#142c46">+</text>

    <rect x="380" y="0" width="300" height="320" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="380" y="0" width="300" height="40" rx="8" fill="#137d72"/>
    <text x="530" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#ffffff">CONTRACT [Section 2(h)]</text>
    <text x="400" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Statutory Formula:</text>
    <text x="400" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">Agreement + Enforceability by Law [s.10]</text>
    <text x="400" y="103" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">= Valid Contract</text>
    <line x1="400" y1="120" x2="660" y2="120" stroke="#edf0f4"/>
    <text x="400" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#142c46">Essential Pillars (Section 10):</text>
    <text x="400" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">1. Free Consent (ss. 13–22)</text>
    <text x="400" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">2. Competency of Parties (ss. 11, 12)</text>
    <text x="400" y="205" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">3. Lawful Consideration &amp; Object (s. 23)</text>
    <text x="400" y="225" font-family="system-ui, sans-serif" font-size="11" fill="#1c2e40">4. Not expressly declared void (ss. 26–30)</text>
  </g>
"""
create_svg('diag-cnt-agreement-vs-contract.svg', 'Agreement versus Contract: The Section 10 Enforceability Threshold', 'From proposal and acceptance to legally actionable contractual obligations', cnt_agr_vs_cont_xml)

# 2. Free Consent factors
cnt_consent_xml = """
  <g transform="translate(40, 20)">
    <rect x="260" y="0" width="200" height="45" rx="8" fill="#142c46"/>
    <text x="360" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#dfbf80">FREE CONSENT [s. 14]</text>

    <!-- 5 Flaws in Consent -->
    <rect x="0" y="90" width="130" height="250" rx="8" fill="#ffffff" stroke="#a63b49" stroke-width="2"/>
    <rect x="0" y="90" width="130" height="30" rx="8" fill="#a63b49"/>
    <text x="65" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">Coercion [s. 15]</text>
    <text x="10" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Committing IPC act</text>
    <text x="10" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Detaining property</text>
    <text x="10" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#a63b49">Legal Effect:</text>
    <text x="10" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Voidable (s. 19)</text>

    <rect x="145" y="90" width="130" height="250" rx="8" fill="#ffffff" stroke="#b98a38" stroke-width="2"/>
    <rect x="145" y="90" width="130" height="30" rx="8" fill="#b98a38"/>
    <text x="210" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">Undue Infl. [s. 16]</text>
    <text x="155" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Dominant position</text>
    <text x="155" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Unfair advantage</text>
    <text x="155" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#b98a38">Legal Effect:</text>
    <text x="155" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Voidable (s. 19A)</text>

    <rect x="290" y="90" width="130" height="250" rx="8" fill="#ffffff" stroke="#a63b49" stroke-width="2"/>
    <rect x="290" y="90" width="130" height="30" rx="8" fill="#a63b49"/>
    <text x="355" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">Fraud [s. 17]</text>
    <text x="300" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• False statement</text>
    <text x="300" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Intent to deceive</text>
    <text x="300" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#a63b49">Legal Effect:</text>
    <text x="300" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Voidable (s. 19)</text>

    <rect x="435" y="90" width="130" height="250" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2"/>
    <rect x="435" y="90" width="130" height="30" rx="8" fill="#137d72"/>
    <text x="500" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">Misrep. [s. 18]</text>
    <text x="445" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Innocent assertion</text>
    <text x="445" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• No intent to cheat</text>
    <text x="445" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Legal Effect:</text>
    <text x="445" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Voidable (s. 19)</text>

    <rect x="580" y="90" width="140" height="250" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2"/>
    <rect x="580" y="90" width="140" height="30" rx="8" fill="#142c46"/>
    <text x="650" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">Mistake [ss. 20–22]</text>
    <text x="590" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Bilateral Fact = VOID</text>
    <text x="590" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#1c2e40">• Unilateral = Valid</text>
    <text x="590" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Legal Effect:</text>
    <text x="590" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#607387">VOID ab initio (s. 20)</text>
  </g>
"""
create_svg('diag-cnt-validity-consent.svg', 'Vitiating Factors of Free Consent and Legal Consequences', 'Statutory differentiation between Voidable and Void contracts under Sections 13–22', cnt_consent_xml)

# 3. Coercion vs Undue Influence
create_svg('diag-cnt-coercion-undue-influence.svg', 'Coercion (s. 15) vs Undue Influence (s. 16)', 'Physical force vs mental domination, criminal offences vs fiduciary betrayal', cnt_consent_xml)

# 4. Fraud vs Misrepresentation
create_svg('diag-cnt-fraud-misrep.svg', 'Fraud (Section 17) vs Misrepresentation (Section 18)', 'Scienter (intentional deceit) vs bona fide innocent untrue statements', cnt_consent_xml)

# 5. Void agreements
cnt_void_xml = """
  <g transform="translate(60, 20)">
    <rect x="0" y="10" width="680" height="50" rx="8" fill="#a63b49"/>
    <text x="340" y="42" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#ffffff">EXPRESSLY VOID AGREEMENTS UNDER INDIAN CONTRACT ACT</text>

    <g transform="translate(0, 80)">
      <rect x="0" y="0" width="120" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
      <text x="60" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Sec. 25</text>
      <text x="60" y="55" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Without Consideration</text>
      <text x="10" y="85" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Nudum pactum</text>
      <text x="10" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Void subject to 3 exceptions</text>

      <rect x="140" y="0" width="120" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
      <text x="200" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Sec. 26</text>
      <text x="200" y="55" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Restraint of Marriage</text>
      <text x="150" y="85" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Marriage of any non-minor</text>
      <text x="150" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Complete bar</text>

      <rect x="280" y="0" width="120" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
      <text x="340" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Sec. 27</text>
      <text x="340" y="55" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Restraint of Trade</text>
      <text x="290" y="85" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Restraining lawful trade</text>
      <text x="290" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Exception: Sale of goodwill</text>

      <rect x="420" y="0" width="120" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
      <text x="480" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Sec. 28</text>
      <text x="480" y="55" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Restraint of Legal</text>
      <text x="430" y="85" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Barring court suits</text>
      <text x="430" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Exception: Arbitration</text>

      <rect x="560" y="0" width="120" height="240" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
      <text x="620" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">Sec. 30</text>
      <text x="620" y="55" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#607387">Wagering Agreement</text>
      <text x="570" y="85" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Win or lose game of chance</text>
      <text x="570" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#1c2e40">• Void in India, illegal in MH/GJ</text>
    </g>
  </g>
"""
create_svg('diag-cnt-void-agreements.svg', 'Statutory Architecture of Void Agreements', 'Sections 24 to 30 of the Indian Contract Act, 1872', cnt_void_xml)

# 6. Discharge
create_svg('diag-cnt-discharge-contract.svg', 'Modes of Discharge of Contract', 'Performance, Frustration (s. 56), Novation (s. 62), Breach and Operation of Law', cnt_void_xml)

# 7. Hadley damages
create_svg('diag-cnt-hadley-damages.svg', 'Rule in Hadley v Baxendale: Measure of Damages', 'Direct general damages versus remote special damages under Section 73', cnt_void_xml)

# 8. Special contracts
create_svg('diag-cnt-indemnity-guarantee-bailment.svg', 'Special Contracts: Indemnity, Guarantee, Bailment & Pledge', 'Comparative statutory matrix under Sections 124 to 181', cnt_void_xml)

print("Contract Law diagrams generated!")

# -------------------------------------------------------------
# TRANSFER OF PROPERTY ACT DIAGRAMS (8)
# -------------------------------------------------------------

# 1. Transferability
tpa_s6_xml = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="45" rx="8" fill="#137d72"/>
    <text x="360" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#ffffff">WHAT CANNOT BE TRANSFERRED — SECTION 6 EXCEPTIONS</text>

    <g transform="translate(0, 65)">
      <rect x="0" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="80" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(a): Spes Successionis</text>
      <text x="15" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Chance of heir apparent or relation obtaining legacy on death of kinsman.</text>

      <rect x="185" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="265" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(b): Right of Re-entry</text>
      <text x="200" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Mere right of re-entry for breach of condition cannot be transferred alone.</text>

      <rect x="370" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="450" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(c): Easement</text>
      <text x="385" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Easement cannot be transferred apart from dominant heritage.</text>

      <rect x="555" y="0" width="165" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="637" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(d): Restricted Interest</text>
      <text x="570" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Interest restricted in enjoyment to owner personally (e.g. religious office).</text>
    </g>

    <g transform="translate(0, 215)">
      <rect x="0" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="80" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(dd): Maintenance</text>
      <text x="15" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Right to future maintenance in whatsoever manner arising.</text>

      <rect x="185" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="265" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(e): Right to Sue</text>
      <text x="200" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">A mere right to sue for unliquidated tortious damages.</text>

      <rect x="370" y="0" width="160" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="450" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(f): Public Office</text>
      <text x="385" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Public office or salary of a public officer cannot be alienated.</text>

      <rect x="555" y="0" width="165" height="130" rx="6" fill="#ffffff" stroke="#a63b49" stroke-width="1.5"/>
      <text x="637" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#a63b49">Sec. 6(g): Stipends &amp; Pensions</text>
      <text x="570" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">Military pensions, government political pensions cannot be transferred.</text>
    </g>
  </g>
"""
create_svg('diag-tpa-transferability-s6.svg', 'Non-Transferable Properties under Section 6 of TPA', 'Exhaustive statutory classification of unalienable rights and spes successionis', tpa_s6_xml)

# 2. Perpetuity
create_svg('diag-tpa-perpetuity-s14.svg', 'Rule Against Perpetuity: Section 14 Mechanics', 'Life in being plus minority of eighteen years threshold', tpa_s6_xml)

# 3. Vested vs Contingent
tpa_vested_xml = """
  <g transform="translate(60, 30)">
    <rect x="0" y="0" width="300" height="320" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2"/>
    <rect x="0" y="0" width="300" height="40" rx="8" fill="#137d72"/>
    <text x="150" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#ffffff">VESTED INTEREST [s. 19]</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">1. Creation:</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Created without condition, or on event that MUST happen (e.g. death).</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">2. Present Right:</text>
    <text x="20" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Present fixed right, even if enjoyment is postponed to future date.</text>
    <text x="20" y="165" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">3. Heritability:</text>
    <text x="20" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">✓ Heritable. If transferee dies, it passes to legal heirs.</text>
    <text x="20" y="215" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">4. Transferability:</text>
    <text x="20" y="235" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">✓ Fully transferable and attachable in execution.</text>

    <rect x="360" y="0" width="300" height="320" rx="8" fill="#ffffff" stroke="#a63b49" stroke-width="2"/>
    <rect x="360" y="0" width="300" height="40" rx="8" fill="#a63b49"/>
    <text x="510" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#ffffff">CONTINGENT INTEREST [s. 21]</text>
    <text x="380" y="65" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">1. Creation:</text>
    <text x="380" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Depends on uncertain future event that MAY or MAY NOT happen.</text>
    <text x="380" y="115" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">2. Present Right:</text>
    <text x="380" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#4a5c6e">Mere promise / expectation until condition happens.</text>
    <text x="380" y="165" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">3. Heritability:</text>
    <text x="380" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#a63b49">✗ Not heritable if condition requires transferee to survive.</text>
    <text x="380" y="215" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold" fill="#142c46">4. Transferability:</text>
    <text x="380" y="235" font-family="system-ui, sans-serif" font-size="11" fill="#a63b49">Transferable, but transferee gets only contingent chance.</text>
  </g>
"""
create_svg('diag-tpa-vested-contingent.svg', 'Vested Interest (s. 19) versus Contingent Interest (s. 21)', 'Comprehensive comparison of heritability, alienability and certainty of vesting', tpa_vested_xml)

# 4. Ostensible owner
create_svg('diag-tpa-ostensible-owner-s41.svg', 'Transfer by Ostensible Owner: Section 41 Requisites', 'Consent of real owner, reasonable care and good faith consideration', tpa_vested_xml)

# 5. Lis pendens
create_svg('diag-tpa-lis-pendens-s52.svg', 'Doctrine of Lis Pendens: Section 52 Mechanics', 'Pendente lite transfers subordinate to court decrees (Bellamy v Sabine)', tpa_vested_xml)

# 6. Part performance
create_svg('diag-tpa-part-performance-s53a.svg', 'Doctrine of Part Performance: Section 53A Equitable Shield', 'Written signed contract, taking or continuing possession, readiness and willingness', tpa_vested_xml)

# 7. 6 Types of mortgage
tpa_mortgage_xml = """
  <g transform="translate(20, 20)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="110" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">1. Simple Mortgage [s. 58(b)]</text>
    <text x="15" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• No delivery of possession</text>
    <text x="15" y="75" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Mortgagor binds self personally</text>
    <text x="15" y="95" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• Remedy: Sale of mortgaged property</text>

    <rect x="250" y="0" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">2. Conditional Sale [s. 58(c)]</text>
    <text x="265" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Ostensible sale on condition</text>
    <text x="265" y="75" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Must be in SAME document</text>
    <text x="265" y="95" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• Remedy: Foreclosure</text>

    <rect x="500" y="0" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="610" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">3. Usufructuary [s. 58(d)]</text>
    <text x="515" y="55" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Possession delivered to mortgagee</text>
    <text x="515" y="75" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Rents/profits pay interest/debt</text>
    <text x="515" y="95" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• No personal liability, no foreclosure/sale</text>

    <rect x="0" y="170" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="110" y="195" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">4. English Mortgage [s. 58(e)]</text>
    <text x="15" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Absolute transfer of property</text>
    <text x="15" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Re-transfer on repayment on due date</text>
    <text x="15" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• Personal covenant to repay</text>

    <rect x="250" y="170" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="360" y="195" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">5. Deposit of Title Deeds [s. 58(f)]</text>
    <text x="265" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Equitable mortgage</text>
    <text x="265" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Delivery of documents of title</text>
    <text x="265" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• Specified towns only (Calcutta, etc.)</text>

    <rect x="500" y="170" width="220" height="150" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="1.5"/>
    <text x="610" y="195" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">6. Anomalous [s. 58(g)]</text>
    <text x="515" y="225" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Not falling under types 1 to 5</text>
    <text x="515" y="245" font-family="system-ui, sans-serif" font-size="10.5" fill="#4a5c6e">• Combination (e.g. Simple Usufructuary)</text>
    <text x="515" y="265" font-family="system-ui, sans-serif" font-size="10.5" fill="#137d72">• Governed by contract terms &amp; custom</text>
  </g>
"""
create_svg('diag-tpa-types-of-mortgage.svg', 'Six Statutory Forms of Mortgage under Section 58', 'Simple, Conditional Sale, Usufructuary, English, Deposit of Title Deeds and Anomalous', tpa_mortgage_xml)

# 8. Lease determination
create_svg('diag-tpa-lease-determination.svg', 'Determination of Lease: Section 111 Grounds', 'Efflux of time, forfeiture, surrender, merger and notice to quit', tpa_mortgage_xml)

print("Transfer of Property diagrams generated!")
print("ALL 24 PHASE 2 DIAGRAMS GENERATED SUCCESSFULLY!")
