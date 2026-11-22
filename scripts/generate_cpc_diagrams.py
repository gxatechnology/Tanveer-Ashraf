import os, xml.etree.ElementTree as ET

os.makedirs('assets/learning/images/diagrams', exist_ok=True)

diagrams = {
    "diag-cpc-jurisdiction-s9.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bgGrad)"/>

  <!-- Title Banner -->
  <rect x="30" y="25" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow)"/>
  <text x="400" y="52" fill="#ffffff" font-family="Georgia, serif" font-size="20" font-weight="bold" text-anchor="middle">SECTION 9 CPC: JURISDICTION OF CIVIL COURTS</text>
  <text x="400" y="70" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">"Courts shall have jurisdiction to try all suits of a civil nature excepting suits barred expressly or impliedly"</text>

  <!-- Left: General Rule -->
  <g transform="translate(40, 105)" filter="url(#shadow)">
    <rect width="225" height="355" rx="8" fill="#fbf8f2"/>
    <rect width="225" height="42" rx="8" fill="#142c46"/>
    <text x="112" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">1. GENERAL MANDATE</text>
    <text x="20" y="70" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Plenary Civil Jurisdiction</text>
    <text x="25" y="90" fill="#4a5568" font-family="sans-serif" font-size="11">Presumption is always IN FAVOR</text>
    <text x="25" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">of civil court jurisdiction.</text>
    <text x="20" y="135" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• What is "Civil Nature"?</text>
    <text x="25" y="155" fill="#4a5568" font-family="sans-serif" font-size="11">Rights to property, office, status,</text>
    <text x="25" y="170" fill="#4a5568" font-family="sans-serif" font-size="11">worship, contract, breach of trust,</text>
    <text x="25" y="185" fill="#4a5568" font-family="sans-serif" font-size="11">franchise, or restitution.</text>
    <text x="20" y="215" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Explanations I &amp; II</text>
    <text x="25" y="235" fill="#4a5568" font-family="sans-serif" font-size="11">Suit for right to property or office</text>
    <text x="25" y="250" fill="#4a5568" font-family="sans-serif" font-size="11">is civil even if dependent on</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">religious rites or ceremonies.</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">Irrelevant whether fees attached.</text>
    <rect x="15" y="310" width="195" height="32" rx="4" fill="#edf7f4"/>
    <text x="112" y="330" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">PMA Metropolitan Case (1995)</text>
  </g>

  <!-- Center: Two Statutory Bars -->
  <g transform="translate(285, 105)" filter="url(#shadow)">
    <rect width="230" height="355" rx="8" fill="#fbf8f2"/>
    <rect width="230" height="42" rx="8" fill="#137d72"/>
    <text x="115" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">2. STATUTORY BARS</text>
    <rect x="15" y="55" width="200" height="135" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="75" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">A. Express Bar</text>
    <text x="25" y="95" fill="#4a5568" font-family="sans-serif" font-size="11">• Barred by direct enactment</text>
    <text x="25" y="110" fill="#4a5568" font-family="sans-serif" font-size="11">• E.g., Industrial Disputes Act,</text>
    <text x="25" y="125" fill="#4a5568" font-family="sans-serif" font-size="11">  Income Tax Act, NGT Act,</text>
    <text x="25" y="140" fill="#4a5568" font-family="sans-serif" font-size="11">  Armed Forces Tribunal.</text>
    <text x="25" y="160" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">Jurisdiction explicitly taken away.</text>

    <rect x="15" y="200" width="200" height="140" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="220" fill="#a63b49" font-family="sans-serif" font-size="12" font-weight="bold">B. Implied Bar</text>
    <text x="25" y="240" fill="#4a5568" font-family="sans-serif" font-size="11">• Barred by general legal principles</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">• Public policy &amp; state sovereignty</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">• Purely political or caste questions</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">• Special statute creates new right</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">  AND provides complete remedy.</text>
    <text x="25" y="325" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">Exclusion must not be readily implied.</text>
  </g>

  <!-- Right: Dhulabhai Principles -->
  <g transform="translate(535, 105)" filter="url(#shadow)">
    <rect width="225" height="355" rx="8" fill="#fbf8f2"/>
    <rect width="225" height="42" rx="8" fill="#a63b49"/>
    <text x="112" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">3. DHULABHAI TESTS (1969)</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">Principles on Exclusion of Jurisdiction:</text>
    <text x="15" y="90" fill="#4a5568" font-family="sans-serif" font-size="10">1. Special tribunal must have power</text>
    <text x="20" y="105" fill="#4a5568" font-family="sans-serif" font-size="10">to decide all questions and grant</text>
    <text x="20" y="120" fill="#4a5568" font-family="sans-serif" font-size="10">adequate remedies.</text>
    <text x="15" y="145" fill="#4a5568" font-family="sans-serif" font-size="10">2. If provisions of special act</text>
    <text x="20" y="160" fill="#4a5568" font-family="sans-serif" font-size="10">are ultra vires or unconstitutional,</text>
    <text x="20" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">civil court ALWAYS has jurisdiction.</text>
    <text x="15" y="200" fill="#4a5568" font-family="sans-serif" font-size="10">3. Civil courts always examine if</text>
    <text x="20" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">fundamental judicial procedure</text>
    <text x="20" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">or natural justice was violated.</text>
    <text x="15" y="255" fill="#4a5568" font-family="sans-serif" font-size="10">4. Exclusion is NOT readily inferred.</text>
    <rect x="15" y="295" width="195" height="45" rx="4" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="112" y="315" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Dhulabhai v. State of MP</text>
    <text x="112" y="330" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">(1968) 3 SCR 662 (Constitution Bench)</text>
  </g>
</svg>''',

    "diag-cpc-res-sub-judice-judicata.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg2)"/>

  <!-- Title -->
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow2)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">RES SUB JUDICE (S. 10) vs RES JUDICATA (S. 11)</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Stay of Pending Suit vs Final Bar of Decided Litigation</text>

  <!-- Left: Section 10 -->
  <g transform="translate(40, 95)" filter="url(#shadow2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">SECTION 10: RES SUB JUDICE</text>
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Meaning: "Matter under judicial consideration"</text>
    <text x="20" y="90" fill="#4a5568" font-family="sans-serif" font-size="11">• Object: Prevents two courts of concurrent</text>
    <text x="25" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">jurisdiction from trying parallel identical suits.</text>
    <text x="20" y="135" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• 4 Essential Conditions:</text>
    <text x="25" y="155" fill="#4a5568" font-family="sans-serif" font-size="11">1. Two suits (previous &amp; subsequent)</text>
    <text x="25" y="170" fill="#4a5568" font-family="sans-serif" font-size="11">2. Matter directly &amp; substantially in issue same</text>
    <text x="25" y="185" fill="#4a5568" font-family="sans-serif" font-size="11">3. Same parties or litigating under same title</text>
    <text x="25" y="200" fill="#4a5568" font-family="sans-serif" font-size="11">4. Former court competent to grant relief</text>
    <rect x="20" y="225" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="245" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">CRITICAL DISTINCTIONS:</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Bars the TRIAL of subsequent suit, NOT institution.</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">• Does NOT apply if previous suit is in a FOREIGN court.</text>
    <text x="30" y="295" fill="#4a5568" font-family="sans-serif" font-size="10">• Does not bar interim/injunction applications.</text>
    <rect x="20" y="320" width="300" height="40" rx="4" fill="#edf7f4"/>
    <text x="170" y="337" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Legal Effect: Order Staying Trial</text>
    <text x="170" y="352" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">(Suit remains alive on docket awaiting former decision)</text>
  </g>

  <!-- Right: Section 11 -->
  <g transform="translate(420, 95)" filter="url(#shadow2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">SECTION 11: RES JUDICATA</text>
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Meaning: "A matter already judged"</text>
    <text x="20" y="90" fill="#4a5568" font-family="sans-serif" font-size="11">• Object: Finality in litigation (Nemo debet bis vexari)</text>
    <text x="25" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">and state interest in ending suits (Interest reipublicae).</text>
    <text x="20" y="135" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• 4 Essential Conditions:</text>
    <text x="25" y="155" fill="#4a5568" font-family="sans-serif" font-size="11">1. Former suit heard and finally decided</text>
    <text x="25" y="170" fill="#4a5568" font-family="sans-serif" font-size="11">2. Directly and substantially in issue</text>
    <text x="25" y="185" fill="#4a5568" font-family="sans-serif" font-size="11">3. Between same parties under same title</text>
    <text x="25" y="200" fill="#4a5568" font-family="sans-serif" font-size="11">4. Former court competent to try subsequent suit</text>
    <rect x="20" y="225" width="300" height="75" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="245" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">THE 8 STATUTORY EXPLANATIONS:</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Expl. IV: CONSTRUCTIVE RES JUDICATA (Might &amp; Ought)</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">• Expl. VI: Representative suits bind all represented</text>
    <text x="30" y="295" fill="#4a5568" font-family="sans-serif" font-size="10">• Expl. VIII: Limited jurisdiction court decision binds</text>
    <rect x="20" y="320" width="300" height="40" rx="4" fill="#fff5f5"/>
    <text x="170" y="337" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Legal Effect: Complete Dismissal of Suit</text>
    <text x="170" y="352" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">(Operates as an absolute bar on trial of issue/suit)</text>
  </g>
</svg>''',

    "diag-cpc-parties-suits.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg3)"/>

  <!-- Title -->
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow3)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">ORDER I CPC: PARTIES TO SUITS &amp; DEFECTS</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Necessary vs Proper Parties, Joinder Rules, and Non-Joinder Proviso</text>

  <!-- Left: Necessary vs Proper -->
  <g transform="translate(40, 95)" filter="url(#shadow3)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">NECESSARY vs PROPER PARTIES</text>
    
    <rect x="15" y="55" width="310" height="135" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="75" fill="#a63b49" font-family="sans-serif" font-size="12" font-weight="bold">1. NECESSARY PARTY (Substantive Right)</text>
    <text x="25" y="95" fill="#4a5568" font-family="sans-serif" font-size="11">• A party against whom relief is sought,</text>
    <text x="30" y="110" fill="#4a5568" font-family="sans-serif" font-size="11">AND in whose absence NO effective decree</text>
    <text x="30" y="125" fill="#4a5568" font-family="sans-serif" font-size="11">can be passed at all.</text>
    <text x="25" y="145" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">• Non-Joinder is FATAL to the suit!</text>
    <text x="25" y="165" fill="#607387" font-family="sans-serif" font-size="10">E.g., Co-sharer in partition, mortgagor in foreclosure.</text>

    <rect x="15" y="205" width="310" height="150" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="225" fill="#137d72" font-family="sans-serif" font-size="12" font-weight="bold">2. PROPER PARTY (Convenience of Court)</text>
    <text x="25" y="245" fill="#4a5568" font-family="sans-serif" font-size="11">• A party against whom no direct relief is claimed,</text>
    <text x="30" y="260" fill="#4a5568" font-family="sans-serif" font-size="11">but whose presence enables court to completely</text>
    <text x="30" y="275" fill="#4a5568" font-family="sans-serif" font-size="11">and effectually adjudicate all questions.</text>
    <text x="25" y="295" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">• Non-Joinder is NOT fatal.</text>
    <text x="25" y="315" fill="#607387" font-family="sans-serif" font-size="10">Court can proceed and decide rights of parties before it.</text>
    <text x="25" y="335" fill="#607387" font-family="sans-serif" font-size="10">E.g., Sub-tenant in eviction against tenant.</text>
  </g>

  <!-- Right: Rules & Defects -->
  <g transform="translate(420, 95)" filter="url(#shadow3)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">DEFECTS &amp; PROCEDURAL RULES</text>
    
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Order I Rule 9 (Suit Not Defeated by Misjoinder):</text>
    <text x="20" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">"No suit shall be defeated by reason of misjoinder</text>
    <text x="20" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">or non-joinder of parties..."</text>
    <rect x="15" y="115" width="310" height="50" rx="4" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="135" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">PROVISO (CRITICAL EXCEPTION):</text>
    <text x="25" y="150" fill="#4a5568" font-family="sans-serif" font-size="10">Does NOT apply to non-joinder of a NECESSARY party!</text>

    <text x="15" y="190" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Order I Rule 8 (Representative Suits):</text>
    <text x="20" y="210" fill="#4a5568" font-family="sans-serif" font-size="11">1. Numerous persons with same interest</text>
    <text x="20" y="225" fill="#4a5568" font-family="sans-serif" font-size="11">2. Permission of court or direction by court</text>
    <text x="20" y="240" fill="#4a5568" font-family="sans-serif" font-size="11">3. Mandatory notice to all interested parties</text>
    <text x="20" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">4. Compromise requires leave of court (R. 8(4))</text>

    <text x="15" y="285" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Order I Rule 10 (Striking/Adding Parties):</text>
    <text x="20" y="305" fill="#4a5568" font-family="sans-serif" font-size="11">Court may at ANY STAGE strike out improper parties</text>
    <text x="20" y="320" fill="#4a5568" font-family="sans-serif" font-size="11">or add necessary/proper parties suo motu.</text>
    <rect x="15" y="335" width="310" height="25" rx="4" fill="#edf7f4"/>
    <text x="170" y="352" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Objections must be taken at earliest opportunity (Rule 13)</text>
  </g>
</svg>''',

    "diag-cpc-plaint-ws-setoff.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg4)"/>

  <!-- Title -->
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow4)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">PLEADINGS, SET-OFF &amp; COUNTER-CLAIM</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Plaint (Order VII), Written Statement (Order VIII), Set-Off (Rule 6) vs Counter-Claim (Rule 6A)</text>

  <!-- Left: Legal Set-off -->
  <g transform="translate(40, 95)" filter="url(#shadow4)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">LEGAL SET-OFF (Order VIII Rule 6)</text>
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Nature: Shield / Ground of Defence</text>
    <text x="20" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Applies ONLY in money recovery suits.</text>
    <text x="20" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">• Sum claimed must be an ASCERTAINED sum.</text>
    <text x="20" y="125" fill="#4a5568" font-family="sans-serif" font-size="11">• Sum must be LEGALLY RECOVERABLE</text>
    <text x="25" y="140" fill="#4a5568" font-family="sans-serif" font-size="11">(cannot be barred by limitation on suit date).</text>
    <text x="20" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Must not exceed court's pecuniary limits.</text>
    <text x="20" y="180" fill="#4a5568" font-family="sans-serif" font-size="11">• Both parties must fill same character.</text>
    
    <rect x="20" y="210" width="300" height="85" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="230" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LEGAL SET-OFF vs EQUITABLE SET-OFF:</text>
    <text x="30" y="250" fill="#4a5568" font-family="sans-serif" font-size="10">• Legal Set-off: Ascertained sum, statutory right.</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Equitable Set-off: Unascertained sum arising</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">  from SAME transaction; judicial discretion.</text>

    <rect x="20" y="315" width="300" height="45" rx="4" fill="#fff5f5"/>
    <text x="170" y="333" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Effect: Extinguishes plaintiff's claim pro tanto</text>
    <text x="170" y="348" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">(Falls with suit if suit dismissed on preliminary ground)</text>
  </g>

  <!-- Right: Counter-Claim -->
  <g transform="translate(420, 95)" filter="url(#shadow4)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">COUNTER-CLAIM (Rules 6A to 6G)</text>
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Nature: Sword / Cross-Action (Cross-Suit)</text>
    <text x="20" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Not restricted to money suits; can be for any relief.</text>
    <text x="20" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">• Sum claimed can be unascertained damages.</text>
    <text x="20" y="125" fill="#4a5568" font-family="sans-serif" font-size="11">• Cause of action must accrue before or after</text>
    <text x="25" y="140" fill="#4a5568" font-family="sans-serif" font-size="11">suit filed, BUT BEFORE defence delivered.</text>
    <text x="20" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Must be within pecuniary jurisdiction of court.</text>
    <text x="20" y="180" fill="#4a5568" font-family="sans-serif" font-size="11">• Treated as a PLAINT in a cross-suit.</text>

    <rect x="20" y="210" width="300" height="85" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="230" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">INDEPENDENT VIABILITY (Rule 6D):</text>
    <text x="30" y="250" fill="#4a5568" font-family="sans-serif" font-size="10">• If plaintiff's suit is stayed, discontinued or</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">  dismissed, counter-claim MAY NEVERTHELESS</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">  BE PROCEEDED WITH and decreed!</text>

    <rect x="20" y="315" width="300" height="45" rx="4" fill="#edf7f4"/>
    <text x="170" y="333" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Effect: Independent cross-decree against plaintiff</text>
    <text x="170" y="348" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">(Plaintiff can file written statement in answer: Rule 6G)</text>
  </g>
</svg>''',

    "diag-cpc-return-vs-rejection.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg5)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow5)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">RETURN OF PLAINT vs REJECTION OF PLAINT</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Order VII Rule 10 (Lack of Jurisdiction) vs Order VII Rule 11 (Fatal Defect / Bar)</text>

  <!-- Left: Return of Plaint -->
  <g transform="translate(40, 95)" filter="url(#shadow5)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">RETURN OF PLAINT (O. VII R. 10)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Ground for Return:</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Court lacks PECUNIARY or TERRITORIAL</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">jurisdiction to entertain the suit.</text>

    <text x="20" y="130" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Stage: At ANY STAGE of suit</text>
    <text x="25" y="150" fill="#4a5568" font-family="sans-serif" font-size="11">(including in appeal or revision court).</text>

    <text x="20" y="180" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Judge's Endorsement:</text>
    <text x="25" y="200" fill="#4a5568" font-family="sans-serif" font-size="11">Date of presentation, return, party name,</text>
    <text x="25" y="215" fill="#4a5568" font-family="sans-serif" font-size="11">and brief statement of reasons.</text>

    <rect x="20" y="240" width="300" height="70" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="260" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LEGAL CHARACTER &amp; REMEDY:</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">• NOT a Decree (only an Order).</text>
    <text x="30" y="295" fill="#4a5568" font-family="sans-serif" font-size="10">• Appealable under Order XLIII Rule 1(a).</text>

    <rect x="20" y="325" width="300" height="35" rx="4" fill="#edf7f4"/>
    <text x="170" y="347" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Plaint is presented de novo in competent court</text>
  </g>

  <!-- Right: Rejection of Plaint -->
  <g transform="translate(420, 95)" filter="url(#shadow5)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#a63b49"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">REJECTION OF PLAINT (O. VII R. 11)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• 6 Statutory Grounds:</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">(a) Does not disclose cause of action</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">(b) Undervalued &amp; plaintiff fails to correct</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">(c) Insufficiently stamped &amp; not corrected</text>
    <text x="25" y="130" fill="#4a5568" font-family="sans-serif" font-size="11">(d) Barred by any law (limitation, res judicata)</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">(e) Not filed in duplicate</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">(f) Non-compliance with Rule 9 (copies)</text>

    <rect x="20" y="180" width="300" height="60" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="200" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">DEMURRER PRINCIPLE:</text>
    <text x="30" y="218" fill="#4a5568" font-family="sans-serif" font-size="10">Court looks ONLY at plaint averments as true.</text>
    <text x="30" y="232" fill="#4a5568" font-family="sans-serif" font-size="10">Defence / WS cannot be considered!</text>

    <rect x="20" y="250" width="300" height="60" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="270" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LEGAL CHARACTER &amp; REMEDY:</text>
    <text x="30" y="288" fill="#4a5568" font-family="sans-serif" font-size="10">• It is a DEEMED DECREE under Section 2(2).</text>
    <text x="30" y="302" fill="#4a5568" font-family="sans-serif" font-size="10">• First Appeal lies under Section 96.</text>

    <rect x="20" y="325" width="300" height="35" rx="4" fill="#fff5f5"/>
    <text x="170" y="347" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Rule 13: Fresh plaint permitted on same cause of action</text>
  </g>
</svg>''',

    "diag-cpc-exparte-default-remedies.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg6)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow6)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">ORDER IX CPC: APPEARANCE, DISMISSAL &amp; EX PARTE DECREE</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Procedural Scenarios when Parties Fail to Appear &amp; Respective Legal Remedies</text>

  <!-- Left: Plaintiff Default (Rule 8 & 9) -->
  <g transform="translate(40, 95)" filter="url(#shadow6)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PLAINTIFF ABSENT, DEFENDANT PRESENT</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Order IX Rule 8:</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Where defendant appears and plaintiff absent,</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">court MUST DISMISS suit for default,</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">unless defendant admits the claim.</text>

    <rect x="20" y="135" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="155" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">BAR ON FRESH SUIT (Order IX Rule 9):</text>
    <text x="30" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">• Plaintiff is PRECLUDED from filing a fresh suit</text>
    <text x="30" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">  on the same cause of action.</text>
    <text x="30" y="210" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• ONLY REMEDY: Application under O. IX R. 9</text>
    <text x="35" y="223" fill="#607387" font-family="sans-serif" font-size="9">  to set aside dismissal on showing sufficient cause.</text>

    <text x="20" y="255" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• If BOTH Parties Absent (Rule 3):</text>
    <text x="25" y="275" fill="#4a5568" font-family="sans-serif" font-size="11">Court dismisses suit under Rule 3.</text>
    <text x="25" y="295" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">• Under Rule 4: Plaintiff may either:</text>
    <text x="30" y="315" fill="#4a5568" font-family="sans-serif" font-size="10">(a) File a fresh suit; OR</text>
    <text x="30" y="330" fill="#4a5568" font-family="sans-serif" font-size="10">(b) Apply to set aside dismissal order.</text>
  </g>

  <!-- Right: Defendant Default & Ex Parte (Rule 6 & 13) -->
  <g transform="translate(420, 95)" filter="url(#shadow6)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#a63b49"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PLAINTIFF PRESENT, DEFENDANT ABSENT</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Order IX Rule 6(1)(a):</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">If summons duly served, court may proceed</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">EX PARTE and pass an Ex Parte Decree.</text>

    <rect x="20" y="120" width="300" height="150" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="140" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">DEFENDANT'S 3 CONCURRENT REMEDIES:</text>
    <text x="30" y="160" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">1. Order IX Rule 13 Application</text>
    <text x="35" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">Apply to SAME court to set aside ex parte decree</text>
    <text x="35" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">(Summons not served OR sufficient cause for absence).</text>
    <text x="30" y="210" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">2. Regular First Appeal under Section 96(2)</text>
    <text x="35" y="225" fill="#4a5568" font-family="sans-serif" font-size="10">Appeal to higher court against ex parte decree on merits.</text>
    <text x="30" y="245" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">3. Review under Section 114 / Order XLVII</text>
    <text x="35" y="260" fill="#4a5568" font-family="sans-serif" font-size="10">Or file separate suit IF decree obtained by fraud.</text>

    <rect x="20" y="285" width="300" height="70" rx="4" fill="#fff5f5"/>
    <text x="30" y="305" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">O. IX R. 13 LIMITATION: 30 DAYS</text>
    <text x="30" y="322" fill="#4a5568" font-family="sans-serif" font-size="10">Article 123 Limitation Act: From decree date,</text>
    <text x="30" y="337" fill="#4a5568" font-family="sans-serif" font-size="10">or from knowledge date if summons not duly served.</text>
  </g>
</svg>''',

    "diag-cpc-civil-trial-sequence.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow7" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg7)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow7)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">CIVIL TRIAL SEQUENCE: FROM INSTITUTION TO DECREE</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Step-by-Step Statutory Progression of a Regular Civil Suit under CPC</text>

  <!-- 5 Horizontal Stages -->
  <!-- Stage 1 -->
  <g transform="translate(40, 100)" filter="url(#shadow7)">
    <rect width="130" height="150" rx="6" fill="#fbf8f2"/>
    <rect width="130" height="28" rx="6" fill="#142c46"/>
    <text x="65" y="19" fill="#dfbf80" font-family="Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">1. FILING</text>
    <text x="10" y="48" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Plaint in Duplicate</text>
    <text x="15" y="63" fill="#607387" font-family="sans-serif" font-size="9">Order IV Rule 1</text>
    <text x="10" y="83" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Verification</text>
    <text x="15" y="98" fill="#607387" font-family="sans-serif" font-size="9">Section 26(2) Affidavit</text>
    <text x="10" y="118" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Court Fee &amp; Value</text>
    <text x="15" y="133" fill="#607387" font-family="sans-serif" font-size="9">Suit Valuation Act</text>
  </g>

  <!-- Stage 2 -->
  <g transform="translate(185, 100)" filter="url(#shadow7)">
    <rect width="130" height="150" rx="6" fill="#fbf8f2"/>
    <rect width="130" height="28" rx="6" fill="#137d72"/>
    <text x="65" y="19" fill="#ffffff" font-family="Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">2. SUMMONS</text>
    <text x="10" y="48" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Service within 30d</text>
    <text x="15" y="63" fill="#607387" font-family="sans-serif" font-size="9">Order V Rule 1</text>
    <text x="10" y="83" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Copy of Plaint</text>
    <text x="15" y="98" fill="#607387" font-family="sans-serif" font-size="9">Order V Rule 2</text>
    <text x="10" y="118" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Substituted Service</text>
    <text x="15" y="133" fill="#607387" font-family="sans-serif" font-size="9">Order V Rule 20</text>
  </g>

  <!-- Stage 3 -->
  <g transform="translate(330, 100)" filter="url(#shadow7)">
    <rect width="130" height="150" rx="6" fill="#fbf8f2"/>
    <rect width="130" height="28" rx="6" fill="#142c46"/>
    <text x="65" y="19" fill="#dfbf80" font-family="Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">3. DEFENCE</text>
    <text x="10" y="48" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Written Statement</text>
    <text x="15" y="63" fill="#607387" font-family="sans-serif" font-size="9">30 to 90 Days (O. 8)</text>
    <text x="10" y="83" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Set-off</text>
    <text x="15" y="98" fill="#607387" font-family="sans-serif" font-size="9">Order VIII Rule 6</text>
    <text x="10" y="118" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Counter-Claim</text>
    <text x="15" y="133" fill="#607387" font-family="sans-serif" font-size="9">Order VIII Rule 6A</text>
  </g>

  <!-- Stage 4 -->
  <g transform="translate(475, 100)" filter="url(#shadow7)">
    <rect width="130" height="150" rx="6" fill="#fbf8f2"/>
    <rect width="130" height="28" rx="6" fill="#137d72"/>
    <text x="65" y="19" fill="#ffffff" font-family="Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">4. ISSUES &amp; ADR</text>
    <text x="10" y="48" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Framing Issues</text>
    <text x="15" y="63" fill="#607387" font-family="sans-serif" font-size="9">Order XIV Rules 1-5</text>
    <text x="10" y="83" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• ADR Referral</text>
    <text x="15" y="98" fill="#607387" font-family="sans-serif" font-size="9">Section 89 / O. 10 R. 1A</text>
    <text x="10" y="118" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• 1st Hearing Disposal</text>
    <text x="15" y="133" fill="#607387" font-family="sans-serif" font-size="9">Order XV (No dispute)</text>
  </g>

  <!-- Stage 5 -->
  <g transform="translate(620, 100)" filter="url(#shadow7)">
    <rect width="140" height="150" rx="6" fill="#fbf8f2"/>
    <rect width="140" height="28" rx="6" fill="#a63b49"/>
    <text x="70" y="19" fill="#ffffff" font-family="Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">5. TRIAL &amp; DECREE</text>
    <text x="10" y="48" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Witness Evidence</text>
    <text x="15" y="63" fill="#607387" font-family="sans-serif" font-size="9">Order XVIII Rule 4 (Affidavit)</text>
    <text x="10" y="83" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Max 3 Adjournments</text>
    <text x="15" y="98" fill="#607387" font-family="sans-serif" font-size="9">Order XVII Rule 1</text>
    <text x="10" y="118" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">• Judgment in 30d</text>
    <text x="15" y="133" fill="#607387" font-family="sans-serif" font-size="9">Section 33 &amp; Order XX</text>
  </g>

  <!-- Lower Panel: Post-Decree Remedies -->
  <g transform="translate(40, 275)" filter="url(#shadow7)">
    <rect width="720" height="195" rx="8" fill="#fbf8f2"/>
    <rect width="720" height="35" rx="8" fill="#142c46"/>
    <text x="360" y="23" fill="#dfbf80" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">POST-DECREE PROCEDURAL AVENUES</text>

    <!-- Box 1: Execution -->
    <rect x="20" y="50" width="215" height="130" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="72" fill="#137d72" font-family="sans-serif" font-size="12" font-weight="bold">EXECUTION (Order XXI)</text>
    <text x="30" y="92" fill="#4a5568" font-family="sans-serif" font-size="10">• Realization of fruits of decree</text>
    <text x="30" y="107" fill="#4a5568" font-family="sans-serif" font-size="10">• Attachment &amp; Sale of Property</text>
    <text x="30" y="122" fill="#4a5568" font-family="sans-serif" font-size="10">• Arrest &amp; Detention (S. 51 &amp; 58)</text>
    <text x="30" y="137" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 56: No arrest of women for money</text>
    <text x="30" y="152" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 60: Exempt assets protected</text>
    <text x="30" y="167" fill="#137d72" font-family="sans-serif" font-size="9" font-weight="bold">S. 47: All questions decided in execution.</text>

    <!-- Box 2: Appeals -->
    <rect x="250" y="50" width="220" height="130" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="260" y="72" fill="#a63b49" font-family="sans-serif" font-size="12" font-weight="bold">APPEALS (Order XLI &amp; XLII)</text>
    <text x="260" y="92" fill="#4a5568" font-family="sans-serif" font-size="10">• First Appeal: S. 96 &amp; Order XLI</text>
    <text x="265" y="107" fill="#4a5568" font-family="sans-serif" font-size="9">  (Facts &amp; Law; barred against consent)</text>
    <text x="260" y="122" fill="#4a5568" font-family="sans-serif" font-size="10">• Second Appeal: S. 100 &amp; Order XLII</text>
    <text x="265" y="137" fill="#4a5568" font-family="sans-serif" font-size="9">  (Substantial Question of Law only)</text>
    <text x="260" y="152" fill="#4a5568" font-family="sans-serif" font-size="10">• Appeals from Orders: S. 104 &amp; O. XLIII</text>
    <text x="260" y="167" fill="#a63b49" font-family="sans-serif" font-size="9" font-weight="bold">S. 100A: No intra-court single judge appeal.</text>

    <!-- Box 3: Supervisory Remedies -->
    <rect x="485" y="50" width="215" height="130" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="495" y="72" fill="#137d72" font-family="sans-serif" font-size="12" font-weight="bold">SUPERVISORY TRIAD</text>
    <text x="495" y="92" fill="#4a5568" font-family="sans-serif" font-size="10">• Reference: S. 113 &amp; Order XLVI</text>
    <text x="500" y="107" fill="#4a5568" font-family="sans-serif" font-size="9">  (Pending doubt on law / validity of Act)</text>
    <text x="495" y="122" fill="#4a5568" font-family="sans-serif" font-size="10">• Review: S. 114 &amp; Order XLVII</text>
    <text x="500" y="137" fill="#4a5568" font-family="sans-serif" font-size="9">  (Same court; error apparent on record)</text>
    <text x="495" y="152" fill="#4a5568" font-family="sans-serif" font-size="10">• Revision: S. 115 (Jurisdictional error)</text>
    <text x="495" y="167" fill="#137d72" font-family="sans-serif" font-size="9" font-weight="bold">UP Amendment: District Court vs HC.</text>
  </g>
</svg>''',

    "diag-cpc-execution-framework.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow8" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg8)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow8)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">EXECUTION OF DECREES: SECTIONS 36–74 &amp; ORDER XXI</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Modes of Execution, Statutory Safeguards, Section 60 Exemptions &amp; Objections</text>

  <!-- Left: Modes of Execution -->
  <g transform="translate(40, 95)" filter="url(#shadow8)">
    <rect width="230" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="230" height="42" rx="8" fill="#142c46"/>
    <text x="115" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">1. MODES (SECTION 51)</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Delivery of Property</text>
    <text x="20" y="80" fill="#4a5568" font-family="sans-serif" font-size="10">Movable (R. 31) or Immovable (R. 35)</text>
    <text x="15" y="105" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Attachment and Sale</text>
    <text x="20" y="120" fill="#4a5568" font-family="sans-serif" font-size="10">Sale of movable or immovable assets</text>
    <text x="15" y="145" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Arrest and Detention</text>
    <text x="20" y="160" fill="#4a5568" font-family="sans-serif" font-size="10">Civil prison subject to S. 58 limits</text>
    <text x="15" y="185" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Appointment of Receiver</text>
    <text x="20" y="200" fill="#4a5568" font-family="sans-serif" font-size="10">To collect rents, profits &amp; manage</text>
    <text x="15" y="225" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Garnishee Proceedings</text>
    <text x="20" y="240" fill="#4a5568" font-family="sans-serif" font-size="10">Order XXI Rules 46A to 46I</text>
    <rect x="15" y="265" width="200" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="285" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">ARREST SAFEGUARDS:</text>
    <text x="25" y="303" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 56: NO arrest of women</text>
    <text x="25" y="318" fill="#4a5568" font-family="sans-serif" font-size="10">  for execution of money decrees.</text>
    <text x="25" y="333" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 58: Under Rs 2000: NO arrest.</text>
    <text x="25" y="348" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 55: No night arrest; subsistence.</text>
  </g>

  <!-- Center: Section 60 Exemptions -->
  <g transform="translate(285, 95)" filter="url(#shadow8)">
    <rect width="230" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="230" height="42" rx="8" fill="#137d72"/>
    <text x="115" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">2. SECTION 60 EXEMPTIONS</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">Properties IMMUNE from Attachment:</text>
    <text x="15" y="85" fill="#4a5568" font-family="sans-serif" font-size="10">1. Necessary wearing apparel, beds</text>
    <text x="20" y="100" fill="#4a5568" font-family="sans-serif" font-size="10">and cooking vessels.</text>
    <text x="15" y="120" fill="#4a5568" font-family="sans-serif" font-size="10">2. Tools of artisans, agricultural</text>
    <text x="20" y="135" fill="#4a5568" font-family="sans-serif" font-size="10">implements and cattle.</text>
    <text x="15" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">3. Houses of agriculturists &amp; labourers.</text>
    <text x="15" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">4. Books of accounts.</text>
    <text x="15" y="195" fill="#4a5568" font-family="sans-serif" font-size="10">5. Mere right to sue for damages.</text>
    <text x="15" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">6. Stipends and political pensions.</text>
    <rect x="15" y="240" width="200" height="120" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="260" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SALARY ATTACHMENT RULES:</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">• Non-Maintenance Decrees:</text>
    <text x="30" y="295" fill="#4a5568" font-family="sans-serif" font-size="9">First Rs 1,000 + 2/3 remainder</text>
    <text x="30" y="308" fill="#4a5568" font-family="sans-serif" font-size="9">EXEMPT. Max 24 months limit.</text>
    <text x="25" y="328" fill="#4a5568" font-family="sans-serif" font-size="10">• Maintenance Decrees:</text>
    <text x="30" y="343" fill="#4a5568" font-family="sans-serif" font-size="9">1/3 exempt; 2/3 attachable.</text>
  </g>

  <!-- Right: Objections & Claims -->
  <g transform="translate(530, 95)" filter="url(#shadow8)">
    <rect width="230" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="230" height="42" rx="8" fill="#a63b49"/>
    <text x="115" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">3. OBJECTIONS &amp; CLAIMS</text>
    
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Order XXI Rule 58:</text>
    <text x="15" y="82" fill="#4a5568" font-family="sans-serif" font-size="10">Third-party claim to attached property.</text>
    <text x="15" y="97" fill="#4a5568" font-family="sans-serif" font-size="10">Adjudicated by EXECUTING court as a suit.</text>
    <text x="15" y="112" fill="#a63b49" font-family="sans-serif" font-size="9" font-weight="bold">No separate suit lies! Appealable as decree.</text>

    <text x="15" y="137" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Setting Aside Auction Sale:</text>
    <text x="15" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">1. Rule 89: On deposit of decree debt</text>
    <text x="20" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">+ 5% penalty to purchaser in 60 days.</text>
    <text x="15" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">2. Rule 90: Material irregularity or</text>
    <text x="20" y="205" fill="#4a5568" font-family="sans-serif" font-size="10">fraud causing substantial injury.</text>

    <text x="15" y="230" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Resistance to Possession:</text>
    <text x="15" y="248" fill="#4a5568" font-family="sans-serif" font-size="10">Order XXI Rules 97 to 106:</text>
    <text x="15" y="263" fill="#4a5568" font-family="sans-serif" font-size="10">Obstruction by debtor or third party.</text>
    <text x="15" y="278" fill="#4a5568" font-family="sans-serif" font-size="10">All questions decided under Rule 101;</text>
    <text x="15" y="293" fill="#4a5568" font-family="sans-serif" font-size="10">separate suit strictly barred.</text>

    <rect x="15" y="315" width="200" height="45" rx="4" fill="#edf7f4"/>
    <text x="115" y="333" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Order XXI Rule 103:</text>
    <text x="115" y="348" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">Order has same force as a decree.</text>
  </g>
</svg>''',

    "diag-cpc-interim-relief-injunctions.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow9" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg9)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow9)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">INTERIM RELIEFS &amp; INJUNCTIONS IN CPC</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Temporary Injunctions (O. XXXIX), Attachment Before Judgment (O. XXXVIII) &amp; Receivers (O. XL)</text>

  <!-- Left: The Injunction Triple Test -->
  <g transform="translate(40, 95)" filter="url(#shadow9)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">TEMPORARY INJUNCTION: TRIPLE TEST</text>
    
    <rect x="15" y="55" width="310" height="70" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="75" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">1. PRIMA FACIE CASE</text>
    <text x="25" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• Serious question to be tried on merits.</text>
    <text x="25" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">• Probability of plaintiff succeeding (not 100% certainty).</text>

    <rect x="15" y="135" width="310" height="70" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="155" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">2. IRREPARABLE INJURY</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">• Injury that cannot be adequately compensated</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">  by damages or financial restitution.</text>

    <rect x="15" y="215" width="310" height="70" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="235" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">3. BALANCE OF CONVENIENCE</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="10">• Mischief or inconvenience to plaintiff if withheld</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="10">  is GREATER than that to defendant if granted.</text>

    <rect x="15" y="295" width="310" height="65" rx="4" fill="#fff5f5"/>
    <text x="25" y="315" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">BREACH PENALTY (Rule 2A):</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="10">• Attachment of property up to 1 year; AND/OR</text>
    <text x="25" y="345" fill="#4a5568" font-family="sans-serif" font-size="10">• Detention in civil prison up to 3 MONTHS.</text>
  </g>

  <!-- Right: Other Interim Remedies -->
  <g transform="translate(420, 95)" filter="url(#shadow9)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">OTHER INTERLOCUTORY REMEDIES</text>
    
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Attachment Before Judgment (Order XXXVIII R. 5):</text>
    <text x="20" y="82" fill="#4a5568" font-family="sans-serif" font-size="10">Extraordinary remedy where defendant is about to</text>
    <text x="20" y="97" fill="#4a5568" font-family="sans-serif" font-size="10">remove or dispose of property with intent to obstruct decree.</text>
    <text x="20" y="112" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">Rule 5(4): Attachment without hearing is VOID.</text>

    <text x="15" y="140" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Arrest Before Judgment (Order XXXVIII R. 1):</text>
    <text x="20" y="157" fill="#4a5568" font-family="sans-serif" font-size="10">Where defendant has absconded or is about to leave</text>
    <text x="20" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">local limits of jurisdiction to delay suit.</text>

    <text x="15" y="200" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Receivers (Order XL Rule 1):</text>
    <text x="20" y="217" fill="#4a5568" font-family="sans-serif" font-size="10">Court appoints receiver when "just and convenient".</text>
    <text x="20" y="232" fill="#4a5568" font-family="sans-serif" font-size="10">Officer of court; property in custodia legis.</text>

    <text x="15" y="260" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Caveat Petitions (Section 148A):</text>
    <text x="20" y="277" fill="#4a5568" font-family="sans-serif" font-size="10">Precautionary notice to hear party before interim order.</text>
    <text x="20" y="292" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">Remains in force for exactly 90 DAYS.</text>

    <rect x="15" y="310" width="310" height="50" rx="4" fill="#edf7f4"/>
    <text x="25" y="328" fill="#142c46" font-family="sans-serif" font-size="10" font-weight="bold">Section 151 Inherent Powers:</text>
    <text x="25" y="343" fill="#607387" font-family="sans-serif" font-size="9">Can grant injunction in situations not covered by O. 39 (Manohar Lal).</text>
  </g>
</svg>''',

    "diag-cpc-appeals-hierarchy.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg10" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow10" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg10)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow10)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">APPELLATE HIERARCHY IN CIVIL PROCEDURE</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">First Appeal (S. 96 &amp; O. XLI) vs Second Appeal (S. 100 &amp; O. XLII) vs Appeals from Orders (S. 104)</text>

  <!-- Left: First Appeal -->
  <g transform="translate(40, 95)" filter="url(#shadow10)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">FIRST APPEAL (Section 96 &amp; Order XLI)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Right of Appeal: Statutory creation</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Lies on questions of FACT as well as LAW.</text>
    <text x="25" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">• First appellate court is the FINAL court of fact.</text>
    <text x="25" y="125" fill="#4a5568" font-family="sans-serif" font-size="11">• Can re-appreciate entire oral and documentary</text>
    <text x="25" y="140" fill="#4a5568" font-family="sans-serif" font-size="11">  evidence and reach independent conclusions.</text>

    <rect x="20" y="160" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="180" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">STATUTORY BARS TO FIRST APPEAL:</text>
    <text x="30" y="200" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 96(3): NO appeal from decree passed with</text>
    <text x="35" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">CONSENT OF PARTIES (Compromise decree).</text>
    <text x="30" y="235" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 96(4): In Small Cause suits under Rs 10,000,</text>
    <text x="35" y="248" fill="#4a5568" font-family="sans-serif" font-size="10">appeal lies ONLY on question of law.</text>

    <text x="20" y="280" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Powers of Appellate Court (S. 107):</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="10">Determine case finally, remand case (R. 23/23A),</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="10">frame issues &amp; refer (R. 25), take additional evidence (R. 27).</text>
    <rect x="20" y="330" width="300" height="30" rx="4" fill="#edf7f4"/>
    <text x="170" y="350" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Lies against Ex Parte Decree: Section 96(2)</text>
  </g>

  <!-- Right: Second Appeal -->
  <g transform="translate(420, 95)" filter="url(#shadow10)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SECOND APPEAL (Section 100 &amp; Order XLII)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Forum: Exclusively to the HIGH COURT</text>
    <text x="20" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Confined strictly to SUBSTANTIAL QUESTION OF LAW.</text>
    <text x="20" y="105" fill="#4a5568" font-family="sans-serif" font-size="11">• High Court CANNOT interfere on pure questions</text>
    <text x="25" y="120" fill="#4a5568" font-family="sans-serif" font-size="11">  of fact, even if findings are erroneous.</text>

    <rect x="20" y="135" width="300" height="90" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="155" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">WHAT IS A SUBSTANTIAL QUESTION?</text>
    <text x="30" y="173" fill="#4a5568" font-family="sans-serif" font-size="10">• Directly affects rights of parties;</text>
    <text x="30" y="188" fill="#4a5568" font-family="sans-serif" font-size="10">• Open question not settled by SC or statute;</text>
    <text x="30" y="203" fill="#4a5568" font-family="sans-serif" font-size="10">• Sir Chunilal Mehta v. Century Spg (1962 SC).</text>
    <text x="30" y="218" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">HC MUST formally formulate the question!</text>

    <text x="20" y="250" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Statutory Bars to Second Appeal:</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 102: No 2nd appeal in money suits &lt;= Rs 25,000.</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 100A: No intra-court appeal from Single Judge.</text>

    <rect x="20" y="305" width="300" height="55" rx="4" fill="#fff5f5"/>
    <text x="30" y="325" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">APPEALS FROM ORDERS (S. 104 &amp; O. XLIII):</text>
    <text x="30" y="340" fill="#4a5568" font-family="sans-serif" font-size="10">• Only specified orders are appealable.</text>
    <text x="30" y="353" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 104(2): NO second appeal from orders ever!</text>
  </g>
</svg>''',

    "diag-cpc-reference-review-revision.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg11" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow11" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg11)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow11)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">THE SUPERVISORY TRIAD: S. 113, S. 114 &amp; S. 115</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">Reference (High Court Consult) vs Review (Same Court Reconsideration) vs Revision (Jurisdictional Oversight)</text>

  <!-- 3 Columns -->
  <!-- Col 1: Reference -->
  <g transform="translate(40, 95)" filter="url(#shadow11)">
    <rect width="225" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="225" height="42" rx="8" fill="#142c46"/>
    <text x="112" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">1. REFERENCE (S. 113)</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Made BY Court, not party</text>
    <text x="15" y="85" fill="#4a5568" font-family="sans-serif" font-size="10">• Made to HIGH COURT.</text>
    <text x="15" y="105" fill="#4a5568" font-family="sans-serif" font-size="10">• During PENDING suit/appeal.</text>
    <text x="15" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">• Reasonable doubt on law.</text>
    <rect x="15" y="145" width="195" height="95" rx="4" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="25" y="165" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">MANDATORY REFERENCE:</text>
    <text x="25" y="180" fill="#4a5568" font-family="sans-serif" font-size="9">• Question regarding validity</text>
    <text x="25" y="195" fill="#4a5568" font-family="sans-serif" font-size="9">  of any Act, Ordinance or Reg;</text>
    <text x="25" y="210" fill="#4a5568" font-family="sans-serif" font-size="9">• Necessary for disposal;</text>
    <text x="25" y="225" fill="#4a5568" font-family="sans-serif" font-size="9">• Court considers it invalid.</text>
    <text x="15" y="260" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">Order XLVI Procedure:</text>
    <text x="15" y="275" fill="#4a5568" font-family="sans-serif" font-size="9">Court states case and opinion,</text>
    <text x="15" y="290" fill="#4a5568" font-family="sans-serif" font-size="9">awaits High Court decision.</text>
    <rect x="15" y="315" width="195" height="45" rx="4" fill="#edf7f4"/>
    <text x="112" y="333" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Consultative Nature</text>
    <text x="112" y="348" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">Guidance before final decision</text>
  </g>

  <!-- Col 2: Review -->
  <g transform="translate(285, 95)" filter="url(#shadow11)">
    <rect width="230" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="230" height="42" rx="8" fill="#137d72"/>
    <text x="115" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">2. REVIEW (S. 114)</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Made to SAME Court</text>
    <text x="15" y="85" fill="#4a5568" font-family="sans-serif" font-size="10">• By aggrieved person.</text>
    <text x="15" y="105" fill="#4a5568" font-family="sans-serif" font-size="10">• Where NO appeal preferred.</text>
    <text x="15" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">• Order XLVII Rule 1 grounds:</text>
    <rect x="15" y="145" width="200" height="95" rx="4" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="165" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">3 EXCLUSIVE GROUNDS:</text>
    <text x="25" y="180" fill="#4a5568" font-family="sans-serif" font-size="9">1. Discovery of new matter/evidence</text>
    <text x="30" y="193" fill="#4a5568" font-family="sans-serif" font-size="9">   after due diligence.</text>
    <text x="25" y="208" fill="#4a5568" font-family="sans-serif" font-size="9">2. Mistake or error apparent on face.</text>
    <text x="25" y="223" fill="#4a5568" font-family="sans-serif" font-size="9">3. Any other sufficient reason.</text>
    <text x="15" y="260" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">Cannot Re-hear on Merits:</text>
    <text x="15" y="275" fill="#4a5568" font-family="sans-serif" font-size="9">Not an appeal in disguise</text>
    <text x="15" y="290" fill="#4a5568" font-family="sans-serif" font-size="9">(Parsion Devi v. Sumitri Devi).</text>
    <rect x="15" y="315" width="200" height="45" rx="4" fill="#fff5f5"/>
    <text x="115" y="333" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Order Rejecting Review:</text>
    <text x="115" y="348" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">NOT appealable (Order XLVII Rule 7)</text>
  </g>

  <!-- Col 3: Revision -->
  <g transform="translate(535, 95)" filter="url(#shadow11)">
    <rect width="225" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="225" height="42" rx="8" fill="#a63b49"/>
    <text x="112" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">3. REVISION (S. 115)</text>
    <text x="15" y="65" fill="#142c46" font-family="sans-serif" font-size="11" font-weight="bold">• Supervisory Power</text>
    <text x="15" y="85" fill="#4a5568" font-family="sans-serif" font-size="10">• High Court (or District Court in UP).</text>
    <text x="15" y="105" fill="#4a5568" font-family="sans-serif" font-size="10">• "Case decided" by subordinate court.</text>
    <text x="15" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">• NO APPEAL lies to High Court.</text>
    <rect x="15" y="145" width="195" height="95" rx="4" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="25" y="165" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">3 JURISDICTIONAL GROUNDS:</text>
    <text x="25" y="180" fill="#4a5568" font-family="sans-serif" font-size="9">1. Exercised jurisdiction not vested.</text>
    <text x="25" y="195" fill="#4a5568" font-family="sans-serif" font-size="9">2. Failed to exercise jurisdiction.</text>
    <text x="25" y="210" fill="#4a5568" font-family="sans-serif" font-size="9">3. Acted illegally or with</text>
    <text x="30" y="225" fill="#4a5568" font-family="sans-serif" font-size="9">   material irregularity.</text>
    <text x="15" y="260" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">UP State Amendment:</text>
    <text x="15" y="275" fill="#4a5568" font-family="sans-serif" font-size="9">Jurisdiction divided between</text>
    <text x="15" y="290" fill="#4a5568" font-family="sans-serif" font-size="9">District Court &amp; High Court.</text>
    <rect x="15" y="315" width="195" height="45" rx="4" fill="#edf7f4"/>
    <text x="112" y="333" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Revision vs Art. 227</text>
    <text x="112" y="348" fill="#607387" font-family="sans-serif" font-size="9" text-anchor="middle">Art 227 is constitutional supervision</text>
  </g>
</svg>''',

    "diag-cpc-civil-suit-journey.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg12" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow12" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg12)"/>

  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow12)"/>
  <text x="400" y="47" fill="#ffffff" font-family="Georgia, serif" font-size="19" font-weight="bold" text-anchor="middle">THE CIVIL SUIT JOURNEY: 14 PROCEDURAL STAGES</text>
  <text x="400" y="65" fill="#dfbf80" font-family="sans-serif" font-size="12" text-anchor="middle">"From Plaint to Decree. Understand Every Stage." — Comprehensive Roadmap</text>

  <!-- 14 Interactive Pipeline Blocks in 2 Rows of 7 -->
  <!-- Row 1: Stages 1 to 7 -->
  <g transform="translate(35, 95)">
    <!-- Stage 1 -->
    <g transform="translate(0, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">1. CAUSE</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Right infringed</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Bundle of facts</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Accrual date</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Order II R. 2</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Limitation Act</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Foundation</text>
    </g>

    <!-- Stage 2 -->
    <g transform="translate(105, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">2. JURISDICTION</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Section 9</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Pecuniary S. 15</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Territorial S. 16-20</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Objections S. 21</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Lowest grade</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Competence</text>
    </g>

    <!-- Stage 3 -->
    <g transform="translate(210, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">3. INSTITUTION</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Section 26</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Order IV Rule 1</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Duplicate copy</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• S. 26(2) Affidavit</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Court fees paid</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Register of Suits</text>
    </g>

    <!-- Stage 4 -->
    <g transform="translate(315, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">4. PLAINT SCRUTINY</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order VII</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Return: R. 10</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Rejection: R. 11</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Deemed decree</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Fresh suit allowed</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Gatekeeper</text>
    </g>

    <!-- Stage 5 -->
    <g transform="translate(420, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">5. SUMMONS</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order V</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Issue within 30d</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Courier / Speed</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Substituted R. 20</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Personal service</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Process Notice</text>
    </g>

    <!-- Stage 6 -->
    <g transform="translate(525, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">6. DEFENCE</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Written Statement</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• 30 to 90 Days</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Set-off (R. 6)</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Counter-claim 6A</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Kailash v Nanhku</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#edf7f4"/>
      <text x="47" y="139" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Order VIII</text>
    </g>

    <!-- Stage 7 -->
    <g transform="translate(630, 0)" filter="url(#shadow12)">
      <rect width="95" height="155" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#a63b49"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">7. APPEARANCE</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order IX</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Default dismissal</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Ex parte decree</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Setting aside R.13</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">30 days limitation</text>
      <rect x="5" y="125" width="85" height="20" rx="3" fill="#fff5f5"/>
      <text x="47" y="139" fill="#a63b49" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Court Hearing</text>
    </g>
  </g>

  <!-- Row 2: Stages 8 to 14 -->
  <g transform="translate(35, 275)">
    <!-- Stage 8 -->
    <g transform="translate(0, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">8. DISCOVERY</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order X Exam</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Interrogatories</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Order XI</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Admissions (O. 12)</text>
      <text x="8" y="105" fill="#4a5568" font-family="sans-serif" font-size="8">• Production (O. 13)</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Evidentiary Prep</text>
    </g>

    <!-- Stage 9 -->
    <g transform="translate(105, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">9. ISSUES</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order XIV</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Issues of fact</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Issues of law</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• ADR referral S. 89</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Disposal if agreed</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Framing Contest</text>
    </g>

    <!-- Stage 10 -->
    <g transform="translate(210, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">10. TRIAL</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Witness Lists</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">Order XVI (15 days)</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Affidavit Evidence</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">Order XVIII Rule 4</text>
      <text x="8" y="105" fill="#4a5568" font-family="sans-serif" font-size="8">• Cross-examination</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Open Court Trial</text>
    </g>

    <!-- Stage 11 -->
    <g transform="translate(315, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">11. ARGUMENTS</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Order XVIII R. 2</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Right to begin</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Reply arguments</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Written arguments</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Order XVIII R. 2(3A)</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Final Submissions</text>
    </g>

    <!-- Stage 12 -->
    <g transform="translate(420, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#a63b49"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">12. JUDGMENT</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Section 33</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Within 30 to 60d</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Order XX Rule 1</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Findings on issues</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Reasoning &amp; ratio</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#fff5f5"/>
      <text x="47" y="160" fill="#a63b49" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Adjudication</text>
    </g>

    <!-- Stage 13 -->
    <g transform="translate(525, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#142c46"/>
      <text x="47" y="18" fill="#dfbf80" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">13. DECREE</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Section 2(2)</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">• Formal expression</text>
      <text x="8" y="75" fill="#4a5568" font-family="sans-serif" font-size="8">• Preliminary / Final</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">• Interest S. 34</text>
      <text x="8" y="105" fill="#607387" font-family="sans-serif" font-size="7">Costs S. 35, 35A</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Enforceable Act</text>
    </g>

    <!-- Stage 14 -->
    <g transform="translate(630, 0)" filter="url(#shadow12)">
      <rect width="95" height="180" rx="6" fill="#fbf8f2"/>
      <rect width="95" height="26" rx="6" fill="#137d72"/>
      <text x="47" y="18" fill="#ffffff" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">14. ENFORCEMENT</text>
      <text x="8" y="45" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Execution</text>
      <text x="8" y="60" fill="#4a5568" font-family="sans-serif" font-size="8">Order XXI</text>
      <text x="8" y="75" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Appeals</text>
      <text x="8" y="90" fill="#4a5568" font-family="sans-serif" font-size="8">S. 96 &amp; S. 100</text>
      <text x="8" y="105" fill="#142c46" font-family="sans-serif" font-size="8" font-weight="bold">• Revision</text>
      <text x="8" y="120" fill="#4a5568" font-family="sans-serif" font-size="8">Section 115</text>
      <rect x="5" y="145" width="85" height="22" rx="3" fill="#edf7f4"/>
      <text x="47" y="160" fill="#137d72" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle">Finality</text>
    </g>
  </g>
</svg>'''
}

# Verify XML and write to disk
for filename, content in diagrams.items():
    try:
        ET.fromstring(content)
        path = os.path.join('assets/learning/images/diagrams', filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Verified & wrote: {filename}")
    except ET.ParseError as e:
        print(f"XML Error in {filename}: {e}")

print(f"Total CPC diagrams generated: {len(diagrams)}")
