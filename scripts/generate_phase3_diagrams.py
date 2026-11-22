"""
Generates 24 custom vector SVG schematics for Phase 3:
- 8 for Criminal Law (BNS & IPC)
- 8 for Criminal Procedure (BNSS & CrPC)
- 8 for Law of Evidence (BSA & IEA)
Output Directory: assets/learning/images/diagrams/
"""

import os

os.makedirs("assets/learning/images/diagrams", exist_ok=True)

def wrap_svg(title, subtitle, badge, content_g):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <linearGradient id="crimGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8c2432"/>
      <stop offset="100%" stop-color="#5a1520"/>
    </linearGradient>
    <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#137d72"/>
      <stop offset="100%" stop-color="#0d5c54"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#142c46" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="500" rx="12" fill="#f8fafc" stroke="#dce3ea" stroke-width="2"/>

  <!-- Top Header Bar -->
  <rect width="800" height="60" rx="12" fill="url(#bgGrad)"/>
  <rect y="48" width="800" height="12" fill="#142c46"/>
  <rect y="58" width="800" height="3" fill="#dfbf80"/>

  <!-- Header Title -->
  <text x="24" y="32" font-family="Georgia, serif" font-size="18" font-weight="bold" fill="#ffffff">{title}</text>
  <text x="24" y="50" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#dfbf80">{subtitle}</text>
  <text x="776" y="36" text-anchor="end" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#a0c0dc">{badge}</text>

  <!-- Body Content -->
  <g transform="translate(0, 70)">
    {content_g}
  </g>
</svg>
"""

# ==============================================================================
# 1. CRIMINAL LAW DIAGRAMS (8)
# ==============================================================================

# 1. Culpable Homicide vs Murder
d1_content = """
  <g transform="translate(40, 20)">
    <!-- Genus Card: Culpable Homicide -->
    <rect x="0" y="0" width="340" height="360" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#dfbf80">CULPABLE HOMICIDE [GENUS]</text>
    <text x="170" y="60" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">BNS Section 100 / IPC Section 299</text>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Three Statutory Limbs:</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">1. Intention of causing death</text>
    <text x="20" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#334155">2. Intention of causing bodily injury likely</text>
    <text x="35" y="150" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">to cause death</text>
    <text x="20" y="175" font-family="system-ui, sans-serif" font-size="11" fill="#334155">3. Knowledge that act is likely to</text>
    <text x="35" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">cause death</text>
    <line x1="20" y1="210" x2="320" y2="210" stroke="#e2e8f0"/>
    <text x="20" y="235" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Key Legal Maxim:</text>
    <text x="20" y="255" font-family="Georgia, serif" font-size="11" font-style="italic" fill="#8c2432">"All murders are culpable homicide,</text>
    <text x="20" y="272" font-family="Georgia, serif" font-size="11" font-style="italic" fill="#8c2432">but all culpable homicides are not murder."</text>
    <text x="20" y="300" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Authority: Reg v. Govinda (1876)</text>
    <text x="20" y="325" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Punishment: S. 105 BNS / S. 304 IPC</text>

    <!-- Arrow / Transition -->
    <path d="M 350 180 L 370 180" stroke="#dfbf80" stroke-width="4" marker-end="url(#arrow)"/>

    <!-- Species Card: Murder -->
    <rect x="380" y="0" width="340" height="360" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="380" y="0" width="340" height="42" rx="8" fill="#8c2432"/>
    <text x="550" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#ffffff">MURDER [SPECIES]</text>
    <text x="550" y="60" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#8c2432">BNS Section 101 / IPC Section 300</text>
    <text x="400" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Four Aggravated Clauses:</text>
    <text x="400" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">1. Act done with intention of causing death</text>
    <text x="400" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#334155">2. Subjective knowledge of special vulnerability</text>
    <text x="400" y="155" font-family="system-ui, sans-serif" font-size="11" fill="#334155">3. Bodily injury sufficient in ordinary course</text>
    <text x="415" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">of nature to cause death (Virsa Singh)</text>
    <text x="400" y="195" font-family="system-ui, sans-serif" font-size="11" fill="#334155">4. Imminently dangerous act (no excuse)</text>
    <line x1="400" y1="210" x2="700" y2="210" stroke="#e2e8f0"/>
    <text x="400" y="235" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#8c2432">The 5 Mitigating Exceptions:</text>
    <text x="400" y="255" font-family="system-ui, sans-serif" font-size="10" fill="#334155">1. Grave & sudden provocation (Nanavati)</text>
    <text x="400" y="272" font-family="system-ui, sans-serif" font-size="10" fill="#334155">2. Private defence excess in good faith</text>
    <text x="400" y="289" font-family="system-ui, sans-serif" font-size="10" fill="#334155">3. Public servant exceeding powers</text>
    <text x="400" y="306" font-family="system-ui, sans-serif" font-size="10" fill="#334155">4. Sudden fight without premeditation</text>
    <text x="400" y="323" font-family="system-ui, sans-serif" font-size="10" fill="#334155">5. Consent of deceased (above 18 years)</text>
  </g>
"""

# 2. Four Stages of Crime & Mens Rea
d2_content = """
  <g transform="translate(40, 30)">
    <!-- Stage 1 -->
    <rect x="0" y="20" width="160" height="260" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="20" width="160" height="35" rx="8" fill="#142c46"/>
    <text x="80" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">1. INTENTION</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Mental Stage</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Mens Rea formulation</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Direction of will</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Purely internal</text>
    <rect x="10" y="180" width="140" height="40" rx="4" fill="#fee2e2"/>
    <text x="80" y="198" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">NOT PUNISHABLE</text>
    <text x="80" y="212" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">(Mere thought is free)</text>

    <!-- Stage 2 -->
    <rect x="180" y="20" width="160" height="260" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="180" y="20" width="160" height="35" rx="8" fill="#142c46"/>
    <text x="260" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">2. PREPARATION</text>
    <text x="195" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Physical Arranging</text>
    <text x="195" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Procuring means</text>
    <text x="195" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Devising plans</text>
    <text x="195" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Locus poenitentiae</text>
    <rect x="190" y="180" width="140" height="40" rx="4" fill="#fef3c7"/>
    <text x="260" y="198" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#92400e">GENERALLY NOT</text>
    <text x="260" y="212" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#92400e">Except: War & Dacoity</text>

    <!-- Stage 3 -->
    <rect x="360" y="20" width="160" height="260" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="360" y="20" width="160" height="35" rx="8" fill="#137d72"/>
    <text x="440" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">3. ATTEMPT</text>
    <text x="375" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Direct Movement</text>
    <text x="375" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Proximity test</text>
    <text x="375" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Beyond repentance</text>
    <text x="375" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Incomplete actus reus</text>
    <rect x="370" y="180" width="140" height="40" rx="4" fill="#d1fae5"/>
    <text x="440" y="198" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">ALWAYS PUNISHABLE</text>
    <text x="440" y="212" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">S. 62 BNS / S. 511 IPC</text>

    <!-- Stage 4 -->
    <rect x="540" y="20" width="180" height="260" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="540" y="20" width="180" height="35" rx="8" fill="#8c2432"/>
    <text x="630" y="44" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">4. COMMISSION</text>
    <text x="555" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#8c2432">Consummation</text>
    <text x="555" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Successful completion</text>
    <text x="555" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Mens Rea + Actus Reus</text>
    <text x="555" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Harm manifested</text>
    <rect x="550" y="180" width="160" height="40" rx="4" fill="#fee2e2"/>
    <text x="630" y="198" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">FULL STATUTORY PENALTY</text>
    <text x="630" y="212" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">Substantive Offence</text>

    <!-- Footer Banner -->
    <rect x="0" y="300" width="720" height="50" rx="6" fill="#142c46"/>
    <text x="360" y="325" text-anchor="middle" font-family="Georgia, serif" font-size="12" fill="#dfbf80">Strict Liability Exception: State of Maharashtra v. M.H. George — Mens rea excluded only by express statutory words or clear implication.</text>
  </g>
"""

# 3. Joint Liability: Common Intention vs Common Object
d3_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="320" height="360" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="320" height="40" rx="8" fill="#142c46"/>
    <text x="160" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">COMMON INTENTION</text>
    <text x="160" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">BNS Section 3(5) / IPC Section 34</text>
    
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Distinctions:</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Minimum persons: Two (2) or more</text>
    <text x="20" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Prior meeting of minds (pre-arranged plan)</text>
    <text x="20" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Active physical participation essential</text>
    <text x="20" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Creates rule of evidence, not substantive offence</text>
    <text x="20" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Same intention is NOT common intention</text>
    
    <rect x="15" y="240" width="290" height="90" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="25" y="260" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Landmark Precedents:</text>
    <text x="25" y="280" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Barendra Kumar Ghosh (Post Master Case, 1925)</text>
    <text x="25" y="300" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Mahbub Shah v. Emperor (Indus River, 1945)</text>
    <text x="25" y="320" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Pandurang v. State of Hyderabad (1955)</text>

    <!-- Column 2 -->
    <rect x="360" y="0" width="320" height="360" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="360" y="0" width="320" height="40" rx="8" fill="#137d72"/>
    <text x="520" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">COMMON OBJECT</text>
    <text x="520" y="58" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">BNS Section 190 / IPC Section 149</text>
    
    <text x="380" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Core Distinctions:</text>
    <text x="380" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Minimum persons: Five (5) or more</text>
    <text x="380" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Common object within 5 heads of S. 189</text>
    <text x="380" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Membership of unlawful assembly suffices</text>
    <text x="380" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Creates a specific, substantive penal offence</text>
    <text x="380" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Knowledge of likely offences committed in object</text>
    
    <rect x="375" y="240" width="290" height="90" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="385" y="260" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Landmark Precedents:</text>
    <text x="385" y="280" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Mizaji v. State of UP (AIR 1959 SC 572)</text>
    <text x="385" y="300" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Allauddin Mian v. State of Bihar (1989)</text>
    <text x="385" y="320" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Charan Singh v. State of UP (2004)</text>
  </g>
"""

# 4. Private Defence Spectrum
d4_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="50" rx="6" fill="#142c46"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">RIGHT OF PRIVATE DEFENCE [BNS Sections 34 to 44 / IPC Sections 96 to 106]</text>
    <text x="360" y="42" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#ffffff">Defensive, not punitive or retaliatory • Proportionality rule applies</text>

    <!-- Body Defence -->
    <rect x="0" y="70" width="345" height="280" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="70" width="345" height="35" rx="8" fill="#137d72"/>
    <text x="172" y="93" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">DEFENCE OF BODY [S. 38 BNS / S. 100 IPC]</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">When extends to causing DEATH:</text>
    <text x="15" y="148" font-family="system-ui, sans-serif" font-size="10" fill="#334155">1. Reasonable apprehension of death</text>
    <text x="15" y="168" font-family="system-ui, sans-serif" font-size="10" fill="#334155">2. Reasonable apprehension of grievous hurt</text>
    <text x="15" y="188" font-family="system-ui, sans-serif" font-size="10" fill="#334155">3. Assault with intention of committing rape</text>
    <text x="15" y="208" font-family="system-ui, sans-serif" font-size="10" fill="#334155">4. Assault with intention of gratifying unnatural lust</text>
    <text x="15" y="228" font-family="system-ui, sans-serif" font-size="10" fill="#334155">5. Assault with intention of kidnapping/abducting</text>
    <text x="15" y="248" font-family="system-ui, sans-serif" font-size="10" fill="#334155">6. Wrongful confinement without legal recourse</text>
    <text x="15" y="268" font-family="system-ui, sans-serif" font-size="10" fill="#8c2432">7. Act of throwing or administering acid</text>

    <!-- Property Defence -->
    <rect x="375" y="70" width="345" height="280" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="375" y="70" width="345" height="35" rx="8" fill="#8c2432"/>
    <text x="547" y="93" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">DEFENCE OF PROPERTY [S. 41 BNS / S. 103 IPC]</text>
    <text x="390" y="125" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">When extends to causing DEATH:</text>
    <text x="390" y="148" font-family="system-ui, sans-serif" font-size="10" fill="#334155">1. Robbery (all forms)</text>
    <text x="390" y="172" font-family="system-ui, sans-serif" font-size="10" fill="#334155">2. House-breaking after sunset and before sunrise</text>
    <text x="390" y="196" font-family="system-ui, sans-serif" font-size="10" fill="#334155">3. Mischief by fire/explosives to building, tent,</text>
    <text x="405" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">or vessel used for human dwelling/custody</text>
    <text x="390" y="234" font-family="system-ui, sans-serif" font-size="10" fill="#334155">4. Theft, mischief or house-trespass causing</text>
    <text x="405" y="248" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">reasonable apprehension of death/grievous hurt</text>
    <rect x="390" y="270" width="315" height="60" rx="4" fill="#fef2f2"/>
    <text x="547" y="290" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">ABSOLUTE STATUTORY LIMIT (S. 37 BNS / S. 99 IPC):</text>
    <text x="547" y="306" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">No right where time to seek public authorities' protection,</text>
    <text x="547" y="320" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">or against public servant acting in good faith under color of office.</text>
  </g>
"""

# 5. Property Offences Hierarchy
d5_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="70" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="30" y="30" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#142c46">1. THEFT [BNS S. 303 / IPC S. 378]</text>
    <text x="30" y="52" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">Dishonest taking of movable property out of possession without consent. Community service if under Rs 5,000.</text>

    <text x="350" y="90" text-anchor="middle" font-family="Georgia, serif" font-size="16" fill="#8c2432">▼ + Delivery induced by fear of injury</text>

    <rect x="0" y="105" width="700" height="70" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="30" y="135" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#142c46">2. EXTORTION [BNS S. 308 / IPC S. 383]</text>
    <text x="30" y="157" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">Intentionally putting person in fear of injury and dishonestly inducing delivery of property/valuable security.</text>

    <text x="350" y="195" text-anchor="middle" font-family="Georgia, serif" font-size="16" fill="#8c2432">▼ + Instant death, instant hurt, or instant wrongful restraint</text>

    <rect x="0" y="210" width="700" height="70" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <text x="30" y="240" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#137d72">3. ROBBERY [BNS S. 309 / IPC S. 390]</text>
    <text x="30" y="262" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">In all robbery there is either theft or extortion with immediate violence/presence. S. 390: Aggravated offence.</text>

    <text x="350" y="300" text-anchor="middle" font-family="Georgia, serif" font-size="16" fill="#8c2432">▼ + Five (5) or more persons acting conjointly</text>

    <rect x="0" y="315" width="700" height="60" rx="8" fill="#8c2432" filter="url(#shadow)"/>
    <text x="30" y="342" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#ffffff">4. DACOITY [BNS S. 310 / IPC S. 391]</text>
    <text x="30" y="360" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Conjoint robbery committed or attempted by five or more persons. Preparation is also punishable (S. 312 BNS).</text>
  </g>
"""

# 6. S. 106 Negligent Death & Hit-and-Run Caveat
d6_content = """
  <g transform="translate(50, 20)">
    <!-- Header Banner -->
    <rect x="0" y="0" width="700" height="50" rx="6" fill="#142c46"/>
    <text x="350" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">SECTION 106 BNS: CAUSING DEATH BY NEGLIGENCE &amp; HIT-AND-RUN CAVEAT</text>
    <text x="350" y="42" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#ffffff">Essential Statutory Examination Alert for UP PCS-J 2026–27</text>

    <!-- Sub-section 1 -->
    <rect x="0" y="70" width="335" height="280" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="70" width="335" height="40" rx="8" fill="#137d72"/>
    <text x="167" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">SECTION 106(1) BNS</text>
    <rect x="20" y="125" width="295" height="30" rx="4" fill="#d1fae5"/>
    <text x="167" y="145" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#065f46">STATUS: IN FORCE (1 JULY 2024)</text>
    <text x="20" y="180" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Substantive Provisions:</text>
    <text x="20" y="205" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Causing death by rash or negligent act</text>
    <text x="20" y="225" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Not amounting to culpable homicide</text>
    <text x="20" y="250" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Punishment:</text>
    <text x="20" y="275" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">• General: Up to 5 YEARS imprisonment</text>
    <text x="20" y="295" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">• Registered Doctor: Up to 2 YEARS</text>
    <text x="20" y="325" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Corresponds to historical Section 304A IPC.</text>

    <!-- Sub-section 2 -->
    <rect x="365" y="70" width="335" height="280" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="365" y="70" width="335" height="40" rx="8" fill="#8c2432"/>
    <text x="532" y="95" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">SECTION 106(2) BNS</text>
    <rect x="385" y="125" width="295" height="30" rx="4" fill="#fee2e2"/>
    <text x="532" y="145" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#991b1b">STATUS: NOT IN FORCE / STAYED</text>
    <text x="385" y="180" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Hit-and-Run Provision:</text>
    <text x="385" y="205" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Rash/negligent driving causing death</text>
    <text x="385" y="225" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Escapes without reporting to police</text>
    <text x="385" y="250" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Proposed Punishment:</text>
    <text x="385" y="275" font-family="system-ui, sans-serif" font-size="11" fill="#8c2432">• Imprisonment up to 10 YEARS and fine</text>
    <rect x="385" y="295" width="295" height="45" rx="4" fill="#fef3c7"/>
    <text x="532" y="312" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#92400e">MHA Notification S.O. 850(E):</text>
    <text x="532" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#92400e">Expressly withheld pending transport talks.</text>
  </g>
"""

# 7. Kidnapping vs Abduction
d7_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="330" height="360" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="0" width="330" height="40" rx="8" fill="#142c46"/>
    <text x="165" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">KIDNAPPING [S. 137 BNS / S. 359 IPC]</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Characteristics:</text>
    <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Two forms: From India or Guardianship</text>
    <text x="20" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Age threshold: Under 18 years (BNS equalized)</text>
    <text x="20" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Person of unsound mind included</text>
    <text x="20" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Means used: Taking or enticing away</text>
    <text x="20" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Consent of minor is completely immaterial</text>
    <text x="20" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Substantive, punishable offence in itself</text>
    <rect x="15" y="245" width="300" height="95" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="25" y="265" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Precedent & Rule:</text>
    <text x="25" y="285" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• S. Varadarajan v. State of Madras (1965)</text>
    <text x="25" y="305" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Taking requires active solicitation</text>
    <text x="25" y="325" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Not a continuing offence (ends upon removal)</text>

    <!-- Column 2 -->
    <rect x="370" y="0" width="330" height="360" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="370" y="0" width="330" height="40" rx="8" fill="#137d72"/>
    <text x="535" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#ffffff">ABDUCTION [S. 138 BNS / S. 362 IPC]</text>
    <text x="390" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Characteristics:</text>
    <text x="390" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Any person of ANY age (adult or child)</text>
    <text x="390" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• No reference to lawful guardianship</text>
    <text x="390" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Means used: Force compelled or deceit induced</text>
    <text x="390" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Free, uncoerced consent condones abduction</text>
    <text x="390" y="190" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Auxiliary act: NOT punishable per se</text>
    <text x="390" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Must be accompanied by criminal intent (murder/ransom)</text>
    <rect x="385" y="245" width="300" height="95" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="395" y="265" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Precedent & Rule:</text>
    <text x="395" y="285" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Bahadur Ali v. King Emperor (1923)</text>
    <text x="395" y="305" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Is a CONTINUING offence as person moves</text>
    <text x="395" y="325" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">• Punishable only with intention (e.g. S. 140 BNS)</text>
  </g>
"""

# 8. Punishments in BNS
d8_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="40" rx="6" fill="#142c46"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">THE SIX STATUTORY PUNISHMENTS [SECTION 4 BNS 2023]</text>

    <!-- Grid of 6 items -->
    <rect x="0" y="55" width="225" height="135" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <text x="15" y="80" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#8c2432">1. DEATH</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Capital punishment</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Rarest of rare cases</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Bachan Singh doctrine</text>

    <rect x="245" y="55" width="230" height="135" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="260" y="80" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">2. LIFE IMPRISONMENT</text>
    <text x="260" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Imprisonment for remainder</text>
    <text x="260" y="122" font-family="system-ui, sans-serif" font-size="10" fill="#334155">of natural life</text>
    <text x="260" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Gopal Vinayak Godse (1961)</text>

    <rect x="495" y="55" width="225" height="135" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="510" y="80" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">3. IMPRISONMENT</text>
    <text x="510" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Rigorous (hard labor)</text>
    <text x="510" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Simple (no hard labor)</text>
    <text x="510" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Includes Solitary (S. 11 BNS)</text>

    <rect x="0" y="205" width="225" height="145" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="15" y="230" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">4. FORFEITURE</text>
    <text x="15" y="255" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Forfeiture of property</text>
    <text x="15" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Offences against state</text>
    <text x="15" y="295" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Exceptional circumstances</text>

    <rect x="245" y="205" width="230" height="145" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="260" y="230" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">5. FINE</text>
    <text x="260" y="255" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Monetary penalty</text>
    <text x="260" y="275" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Default imprisonment rules</text>
    <text x="260" y="295" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Proportional to offender means</text>

    <!-- NEW 6th Punishment: Community Service -->
    <rect x="495" y="205" width="225" height="145" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="495" y="205" width="225" height="30" rx="6" fill="#137d72"/>
    <text x="607" y="225" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">6. COMMUNITY SERVICE</text>
    <text x="510" y="255" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">★ NEW REFORM IN BNS ★</text>
    <text x="510" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Petty theft under Rs 5,000</text>
    <text x="510" y="292" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Defamation (S. 356)</text>
    <text x="510" y="309" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Public drunkenness misconduct</text>
    <text x="510" y="326" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Failure to appear on proclamation</text>
  </g>
"""

# ==============================================================================
# 2. CRIMINAL PROCEDURE DIAGRAMS (8)
# ==============================================================================

# 9. Courts Hierarchy & Sentences
d9_content = """
  <g transform="translate(50, 20)">
    <!-- High Court -->
    <rect x="150" y="0" width="400" height="45" rx="6" fill="#142c46" filter="url(#shadow)"/>
    <text x="350" y="22" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">HIGH COURT &amp; SESSIONS JUDGE</text>
    <text x="350" y="38" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff">Death (Sessions requires HC confirmation S. 407 BNSS), Life, Any authorized sentence</text>

    <text x="350" y="62" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" fill="#8c2432">▼</text>

    <!-- Additional Sessions -->
    <rect x="150" y="70" width="400" height="45" rx="6" fill="#1b3857" filter="url(#shadow)"/>
    <text x="350" y="92" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">ADDITIONAL SESSIONS JUDGE</text>
    <text x="350" y="108" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#dfbf80">Equivalent powers to Sessions Judge (Death sentence subject to confirmation)</text>

    <text x="350" y="132" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" fill="#8c2432">▼</text>

    <!-- CJM -->
    <rect x="150" y="140" width="400" height="45" rx="6" fill="#137d72" filter="url(#shadow)"/>
    <text x="350" y="162" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">CHIEF JUDICIAL MAGISTRATE (CJM)</text>
    <text x="350" y="178" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff">Imprisonment up to 7 YEARS • Any fine authorized by law</text>

    <text x="350" y="202" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" fill="#8c2432">▼</text>

    <!-- JMFC -->
    <rect x="150" y="210" width="400" height="45" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <text x="350" y="232" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">JUDICIAL MAGISTRATE FIRST CLASS (JMFC)</text>
    <text x="350" y="248" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#137d72">Imprisonment up to 3 YEARS • Fine up to Rs 50,000 (BNSS increased from Rs 10k)</text>

    <text x="350" y="272" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" fill="#8c2432">▼</text>

    <!-- JMSC -->
    <rect x="150" y="280" width="400" height="45" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="350" y="302" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">JUDICIAL MAGISTRATE SECOND CLASS</text>
    <text x="350" y="318" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Imprisonment up to 1 YEAR • Fine up to Rs 10,000 (BNSS increased from Rs 5k)</text>

    <!-- Metropolitan Magistrates note -->
    <rect x="80" y="340" width="540" height="25" rx="4" fill="#fee2e2"/>
    <text x="350" y="357" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">BNSS Reform: Separate Metropolitan Magistrates abolished; integrated with JMFCs.</text>
  </g>
"""

# 10. Investigation Flowchart
d10_content = """
  <g transform="translate(40, 20)">
    <!-- Step 1 -->
    <rect x="0" y="20" width="160" height="140" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="20" width="160" height="30" rx="6" fill="#142c46"/>
    <text x="80" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">1. FIR / INTIMATION</text>
    <text x="10" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">S. 173 BNSS / S. 154 CrPC</text>
    <text x="10" y="90" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Zero FIR (any station)</text>
    <text x="10" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• E-FIR (signed in 3 days)</text>
    <text x="10" y="120" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Prelim inquiry (14 days)</text>
    <text x="10" y="135" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Lalita Kumari ruling</text>

    <text x="175" y="95" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Step 2 -->
    <rect x="190" y="20" width="160" height="140" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="190" y="20" width="160" height="30" rx="6" fill="#142c46"/>
    <text x="270" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">2. INVESTIGATION</text>
    <text x="200" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">S. 176–181 BNSS</text>
    <text x="200" y="90" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Spot inspection</text>
    <text x="200" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Search & seizure (S. 105)</text>
    <text x="200" y="120" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Witness exam (S. 180)</text>
    <text x="200" y="135" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Audio-video recording</text>

    <text x="365" y="95" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Step 3 -->
    <rect x="380" y="20" width="160" height="140" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="380" y="20" width="160" height="30" rx="6" fill="#137d72"/>
    <text x="460" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">3. ARREST &amp; REMAND</text>
    <text x="390" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">S. 187 BNSS / S. 167 CrPC</text>
    <text x="390" y="90" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• 24-hr Magistrate production</text>
    <text x="390" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Police custody: 15 days in</text>
    <text x="400" y="118" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">parts across 40/60 days</text>
    <text x="390" y="135" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Judicial remand up to 60/90</text>

    <text x="555" y="95" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Step 4 -->
    <rect x="570" y="20" width="150" height="140" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="570" y="20" width="150" height="30" rx="6" fill="#8c2432"/>
    <text x="645" y="40" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">4. FINAL REPORT</text>
    <text x="580" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">S. 193 BNSS / S. 173 CrPC</text>
    <text x="580" y="90" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Charge-sheet / Closure</text>
    <text x="580" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Rape cases: 2 months</text>
    <text x="580" y="120" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Progress update in 90 days</text>
    <text x="580" y="135" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Cognizance by Court</text>

    <!-- Bottom statutory box -->
    <rect x="0" y="190" width="720" height="160" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="20" y="215" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">CRITICAL STATUTORY MILESTONES &amp; TIMELINES</text>
    <text x="20" y="240" font-family="system-ui, sans-serif" font-size="11" fill="#334155">1. S. 173(3) BNSS Preliminary Inquiry: In offences punishable with 3-7 years, preliminary inquiry within 14 days before FIR.</text>
    <text x="20" y="265" font-family="system-ui, sans-serif" font-size="11" fill="#334155">2. S. 187(2) BNSS Remand: Police remand allowed in parts during first 40 or 60 days (overcoming CBI v. Anupam Kulkarni).</text>
    <text x="20" y="290" font-family="system-ui, sans-serif" font-size="11" fill="#334155">3. S. 187(5) BNSS Default Bail: Accused entitled to bail on expiry of 90 days (death/life/10yr) or 60 days (other offences).</text>
    <text x="20" y="315" font-family="system-ui, sans-serif" font-size="11" fill="#334155">4. S. 193(3) BNSS Electronic Filing: Police reports and documents can be submitted to Magistrate electronically.</text>
  </g>
"""

# 11. Arrest Safeguards & 24hr Production
d11_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="40" rx="6" fill="#142c46"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">ARREST SAFEGUARDS &amp; RIGHTS OF ARRESTED PERSONS</text>

    <!-- Box 1 -->
    <rect x="0" y="55" width="345" height="140" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <text x="20" y="80" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#137d72">1. Notice of Appearance (S. 35 BNSS / S. 41A)</text>
    <text x="20" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• In offences punishable with up to 7 years</text>
    <text x="20" y="122" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Notice of appearance mandatory; arrest only if reasons recorded</text>
    <text x="20" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• For offences under 3 years: DSP prior approval required if</text>
    <text x="30" y="155" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">accused is aged over 60 years or infirm (BNSS S. 35(7))</text>
    <text x="20" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#065f46">Arnesh Kumar v. State of Bihar (2014) guidelines codified.</text>

    <!-- Box 2 -->
    <rect x="375" y="55" width="345" height="140" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <text x="395" y="80" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#8c2432">2. Handcuff Regulation (S. 43(3) BNSS)</text>
    <text x="395" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Handcuffs allowed ONLY for habitual offenders or</text>
    <text x="395" y="122" font-family="system-ui, sans-serif" font-size="10" fill="#334155">heinous crimes (Terrorism, Murder, Rape, Acid attack,</text>
    <text x="395" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Organised crime, Counterfeiting, or Escaping custody)</text>
    <text x="395" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#991b1b">Prem Shankar Shukla & Citizens for Democracy precedent</text>
    <text x="395" y="175" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Codified with statutory exceptions in Section 43(3) BNSS.</text>

    <!-- Box 3 -->
    <rect x="0" y="210" width="345" height="140" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="20" y="235" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">3. The 24-Hour Rule (S. 58 BNSS / S. 57 CrPC)</text>
    <text x="20" y="260" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• No police officer shall detain arrestee > 24 hours</text>
    <text x="20" y="278" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Exclusive of journey time to nearest Magistrate</text>
    <text x="20" y="296" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Inviolable constitutional guarantee under Art 22(2)</text>
    <text x="20" y="316" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Continued detention requires judicial order (S. 187)</text>
    <text x="20" y="335" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Non-compliance renders detention illegal.</text>

    <!-- Box 4 -->
    <rect x="375" y="210" width="345" height="140" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="395" y="235" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">4. Mandatory Rights (D.K. Basu Guidelines)</text>
    <text x="395" y="260" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Right to know grounds of arrest & bailability (S. 47)</text>
    <text x="395" y="278" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Right to inform friend/relative immediately (S. 48)</text>
    <text x="395" y="296" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Mandatory medical exam by medical officer (S. 53)</text>
    <text x="395" y="316" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Right to consult advocate during interrogation (S. 38)</text>
    <text x="395" y="335" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">Designated Police Officer in every district (S. 37 BNSS).</text>
  </g>
"""

# 12. Remand Architecture
d12_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">SECTION 187 BNSS: REMAND ARCHITECTURE &amp; POLICE CUSTODY IN PARTS</text>

    <!-- Diagram comparison -->
    <rect x="0" y="60" width="330" height="230" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="60" width="330" height="35" rx="8" fill="#8c2432"/>
    <text x="165" y="83" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">OLD CrPC S. 167 (Anupam Kulkarni)</text>
    <text x="15" y="120" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Police custody strictly limited to FIRST 15 DAYS</text>
    <text x="25" y="136" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">from the initial date of Magistrate remand.</text>
    <text x="15" y="160" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• After 15 days, ONLY judicial custody allowed.</text>
    <text x="15" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• If accused fell sick in first 15 days, police</text>
    <text x="25" y="201" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">lost all opportunity for police interrogation.</text>
    <text x="15" y="230" font-family="system-ui, sans-serif" font-size="10" fill="#991b1b">CBI v. Anupam J. Kulkarni (1992) 3 SCC 141</text>
    <text x="15" y="255" font-family="system-ui, sans-serif" font-size="10" fill="#991b1b">Rigid cutoff caused investigation bottlenecks.</text>

    <!-- New BNSS S. 187 -->
    <rect x="370" y="60" width="330" height="230" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="370" y="60" width="330" height="35" rx="8" fill="#137d72"/>
    <text x="535" y="83" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">NEW BNSS S. 187(2) FRAMEWORK</text>
    <text x="385" y="120" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">• 15 DAYS POLICE CUSTODY IN WHOLE OR IN PARTS</text>
    <text x="395" y="136" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Spread across first 40 days (for 60-day offences)</text>
    <text x="395" y="152" font-family="system-ui, sans-serif" font-size="10" fill="#334155">or first 60 days (for 90-day offences).</text>
    <text x="385" y="180" font-family="system-ui, sans-serif" font-size="11" fill="#334155">• Police can seek intermittent police remand</text>
    <text x="395" y="196" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">subject to total aggregate cap of 15 days.</text>
    <text x="385" y="225" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">V. Senthil Balaji v. State (2023) confirmed need;</text>
    <text x="385" y="245" font-family="system-ui, sans-serif" font-size="10" fill="#065f46">Now statutorily codified in Section 187(2) BNSS.</text>

    <!-- Footer Banner on Default Bail -->
    <rect x="0" y="305" width="700" height="55" rx="6" fill="#142c46"/>
    <text x="350" y="327" text-anchor="middle" font-family="Georgia, serif" font-size="12" fill="#dfbf80">DEFAULT BAIL PRESERVED: If investigation not completed within 90 days (death/life/10+ yrs)</text>
    <text x="350" y="345" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#ffffff">or 60 days (any other offence), accused is entitled to indefeasible default bail (S. 187(5) BNSS).</text>
  </g>
"""

# 13. Trials Comparison Matrix
d13_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="350" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    
    <!-- Table Header -->
    <rect x="0" y="0" width="720" height="40" rx="8" fill="#142c46"/>
    <text x="90" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">TRIAL TYPE</text>
    <text x="240" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">SECTIONS (BNSS / CrPC)</text>
    <text x="430" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">APPLICABLE OFFENCES</text>
    <text x="630" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">KEY PROCEDURE</text>

    <!-- Row 1: Sessions -->
    <line x1="0" y1="40" x2="720" y2="40" stroke="#cbd5e1"/>
    <text x="90" y="70" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#8c2432">Sessions Trial</text>
    <text x="240" y="70" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">BNSS S. 248–260</text>
    <text x="240" y="85" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">(CrPC S. 225–237)</text>
    <text x="430" y="70" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Exclusively triable by Sessions</text>
    <text x="430" y="85" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">(Murder, Rape, Dacoity)</text>
    <text x="630" y="65" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Opened by PP; Discharge</text>
    <text x="630" y="80" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">app within 60 days of committal;</text>
    <text x="630" y="95" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Formal charge framing mandatory</text>

    <!-- Row 2: Warrant Cases -->
    <line x1="0" y1="110" x2="720" y2="110" stroke="#cbd5e1"/>
    <text x="90" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Warrant Cases</text>
    <text x="90" y="155" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">by Magistrates</text>
    <text x="240" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">BNSS S. 261–273</text>
    <text x="240" y="155" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">(CrPC S. 238–250)</text>
    <text x="430" y="140" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Punishable with death, life,</text>
    <text x="430" y="155" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">or imprisonment > 2 years</text>
    <text x="630" y="135" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Bifurcated: Police report vs</text>
    <text x="630" y="150" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Private complaint; Pre-charge</text>
    <text x="630" y="165" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">evidence in complaint cases</text>

    <!-- Row 3: Summons Cases -->
    <line x1="0" y1="180" x2="720" y2="180" stroke="#cbd5e1"/>
    <text x="90" y="210" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#137d72">Summons Cases</text>
    <text x="90" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">by Magistrates</text>
    <text x="240" y="210" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">BNSS S. 274–282</text>
    <text x="240" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">(CrPC S. 251–259)</text>
    <text x="430" y="210" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Relating to offence not being</text>
    <text x="430" y="225" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">a warrant case (≤ 2 years)</text>
    <text x="630" y="205" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">NO formal charge framed;</text>
    <text x="630" y="220" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Substance of accusation stated;</text>
    <text x="630" y="235" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">No discharge (straight acquittal/convict)</text>

    <!-- Row 4: Summary Trial -->
    <line x1="0" y1="250" x2="720" y2="250" stroke="#cbd5e1"/>
    <text x="90" y="280" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Summary Trial</text>
    <text x="240" y="280" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">BNSS S. 283–288</text>
    <text x="240" y="295" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">(CrPC S. 260–265)</text>
    <text x="430" y="280" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Offences not punishable with</text>
    <text x="430" y="295" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">imprisonment > 3 years (BNSS)</text>
    <text x="630" y="275" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Summons procedure followed;</text>
    <text x="630" y="290" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Max sentence: 3 MONTHS;</text>
    <text x="630" y="305" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Abridged record & judgment</text>

    <!-- Footer Note -->
    <rect x="0" y="325" width="720" height="25" rx="4" fill="#f8fafc"/>
    <text x="360" y="342" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">BNSS S. 283(2) raises summary trial threshold to offences punishable with imprisonment up to 3 years (formerly 2 years in CrPC).</text>
  </g>
"""

# 14. Bail Framework
d14_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="40" rx="6" fill="#142c46"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">THE COMPREHENSIVE BAIL SPECTRUM IN CRIMINAL PROCEDURE</text>

    <!-- Bailable -->
    <rect x="0" y="55" width="170" height="280" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="55" width="170" height="35" rx="6" fill="#137d72"/>
    <text x="85" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">BAILABLE OFFENCES</text>
    <text x="10" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">S. 478 BNSS / S. 436</text>
    <text x="10" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Bail is an ABSOLUTE</text>
    <text x="18" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">statutory right</text>
    <text x="10" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Police officer or court</text>
    <text x="18" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#334155">MUST release on bail</text>
    <text x="10" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Indigent person released</text>
    <text x="18" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#334155">on personal bond without</text>
    <text x="18" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#334155">sureties after 1 week</text>
    <text x="10" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Rasiklal v. Kishore (2009)</text>

    <!-- Non-Bailable -->
    <rect x="180" y="55" width="175" height="280" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="180" y="55" width="175" height="35" rx="6" fill="#142c46"/>
    <text x="267" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#dfbf80">NON-BAILABLE OFFENCE</text>
    <text x="190" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">S. 480 BNSS / S. 437</text>
    <text x="190" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Judicial discretion</text>
    <text x="190" y="148" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Barred if reasonable</text>
    <text x="198" y="162" font-family="system-ui, sans-serif" font-size="9" fill="#334155">ground for death/life</text>
    <text x="190" y="180" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#8c2432">Proviso Exceptions:</text>
    <text x="190" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Under 16 years of age</text>
    <text x="190" y="218" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Woman</text>
    <text x="190" y="236" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Sick or infirm person</text>
    <text x="190" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Satender Kumar Antil (2022)</text>

    <!-- Undertrials -->
    <rect x="365" y="55" width="175" height="280" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="365" y="55" width="175" height="35" rx="6" fill="#137d72"/>
    <text x="452" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">UNDERTRIAL BAIL</text>
    <text x="375" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">S. 479 BNSS / S. 436A</text>
    <text x="375" y="130" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#065f46">★ MAJOR BNSS REFORM:</text>
    <text x="375" y="148" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• First-time offender: released</text>
    <text x="385" y="162" font-family="system-ui, sans-serif" font-size="9" fill="#137d72">after ONE-THIRD period</text>
    <text x="375" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• General undertrials: released</text>
    <text x="385" y="195" font-family="system-ui, sans-serif" font-size="9" fill="#334155">after ONE-HALF period</text>
    <text x="375" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• In no case detained > max</text>
    <text x="375" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Jailer duty to file app</text>
    <text x="375" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Bhim Singh v. UOI (2015)</text>

    <!-- Anticipatory -->
    <rect x="550" y="55" width="170" height="280" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="550" y="55" width="170" height="35" rx="6" fill="#8c2432"/>
    <text x="635" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">ANTICIPATORY BAIL</text>
    <text x="560" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">S. 482 BNSS / S. 438</text>
    <text x="560" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Direction for bail in</text>
    <text x="568" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">anticipation of arrest</text>
    <text x="560" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• High Court or Sessions</text>
    <text x="560" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Non-bailable offences</text>
    <text x="560" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• No time-limit (Sushila</text>
    <text x="568" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Aggarwal 5-judge bench)</text>
    <text x="560" y="240" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">• Barred in SC/ST Act &</text>
    <text x="568" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">certain aggravated rapes</text>
    <text x="560" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Gurbaksh Sibbia (1980)</text>
  </g>
"""

# 15. Trial in Absentia (S. 356 BNSS)
d15_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">TRIAL IN ABSENTIA OF PROCLAIMED OFFENDERS [SECTION 356 BNSS]</text>

    <!-- Stage 1 -->
    <rect x="0" y="60" width="160" height="240" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="60" width="160" height="30" rx="6" fill="#142c46"/>
    <text x="80" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#dfbf80">1. ABSCONDING</text>
    <text x="10" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Statutory Trigger</text>
    <text x="10" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Person declared as</text>
    <text x="18" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">proclaimed offender (S. 84)</text>
    <text x="10" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Absconded to evade trial</text>
    <text x="10" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• No immediate prospect</text>
    <text x="18" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#334155">of arrest</text>
    <text x="10" y="225" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Warrant unexecuted</text>

    <text x="175" y="170" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Stage 2 -->
    <rect x="190" y="60" width="160" height="240" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="190" y="60" width="160" height="30" rx="6" fill="#142c46"/>
    <text x="270" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#dfbf80">2. CHARGE FRAMING</text>
    <text x="200" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Court Procedure</text>
    <text x="200" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Charges framed against</text>
    <text x="208" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">absconding accused</text>
    <text x="200" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Mandatory 90 DAYS</text>
    <text x="208" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#334155">cooling period begins</text>
    <text x="200" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Public notice published in</text>
    <text x="208" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#334155">national newspapers</text>

    <text x="365" y="170" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Stage 3 -->
    <rect x="380" y="60" width="160" height="240" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="380" y="60" width="160" height="30" rx="6" fill="#137d72"/>
    <text x="460" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">3. LEGAL AID COUNSEL</text>
    <text x="390" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Fair Trial Safeguard</text>
    <text x="390" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Court appoints advocate</text>
    <text x="398" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">at State expense</text>
    <text x="390" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Evidence of prosecution</text>
    <text x="398" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#334155">witnesses recorded</text>
    <text x="390" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Defence cross-examines</text>
    <text x="398" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#334155">witnesses</text>

    <text x="555" y="170" text-anchor="middle" font-family="system-ui, sans-serif" font-size="16" fill="#8c2432">➔</text>

    <!-- Stage 4 -->
    <rect x="570" y="60" width="130" height="240" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="570" y="60" width="130" height="30" rx="6" fill="#8c2432"/>
    <text x="635" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">4. JUDGMENT</text>
    <text x="580" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">Pronouncement</text>
    <text x="580" y="130" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Court delivers verdict</text>
    <text x="580" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Conviction/Acquittal</text>
    <text x="580" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• If convicted, sentence</text>
    <text x="588" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#334155">passed in absentia</text>
    <text x="580" y="210" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Appeal rights: 3 yrs</text>

    <!-- Bottom Banner -->
    <rect x="0" y="315" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="338" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Section 356 BNSS marks an unprecedented break from ancient English common law trial presence requirements.</text>
  </g>
"""

# 16. Maintenance S. 144 BNSS / S. 125 CrPC
d16_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">ORDER FOR MAINTENANCE [S. 144 BNSS / S. 125 CrPC]</text>

    <!-- Requisites -->
    <rect x="0" y="55" width="330" height="230" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="55" width="330" height="35" rx="8" fill="#137d72"/>
    <text x="165" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">STATUTORY ESSENTIALS</text>
    <text x="15" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Person Having Sufficient Means:</text>
    <text x="15" y="135" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Neglects or refuses to maintain</text>
    <text x="15" y="155" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Eligible Claimants:</text>
    <text x="15" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">1. Wife unable to maintain herself (includes divorcee)</text>
    <text x="15" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">2. Legitimate or illegitimate minor child</text>
    <text x="15" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">3. Major child with physical/mental abnormality</text>
    <text x="15" y="235" font-family="system-ui, sans-serif" font-size="10" fill="#334155">4. Father or mother unable to maintain themselves</text>
    <text x="15" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Secular remedy: applies irrespective of personal religion.</text>

    <!-- Disqualifications & Timelines -->
    <rect x="370" y="55" width="330" height="230" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="370" y="55" width="330" height="35" rx="8" fill="#8c2432"/>
    <text x="535" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">BARS &amp; STATUTORY TIMELINES</text>
    <text x="385" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#8c2432">Disqualifications for Wife (S. 144(4)):</text>
    <text x="385" y="135" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Living in adultery</text>
    <text x="385" y="155" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Refuses to live with husband without sufficient reason</text>
    <text x="385" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Living separately by mutual consent</text>
    <text x="385" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Interim Maintenance Timeline:</text>
    <rect x="385" y="215" width="300" height="35" rx="4" fill="#fee2e2"/>
    <text x="535" y="236" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">Disposed of within 60 DAYS of notice service.</text>
    <text x="385" y="270" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Shah Bano (1985) & Rajnesh v. Neha (2020) guidelines.</text>

    <!-- Bottom note -->
    <rect x="0" y="300" width="700" height="45" rx="6" fill="#142c46"/>
    <text x="350" y="325" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Enforcement (S. 147 BNSS): Default in payment without sufficient cause punishable with imprisonment up to 1 month.</text>
  </g>
"""

# ==============================================================================
# 3. LAW OF EVIDENCE DIAGRAMS (8)
# ==============================================================================

# 17. Relevancy vs Admissibility
d17_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">RELEVANCY VERSUS ADMISSIBILITY IN LAW OF EVIDENCE</text>

    <!-- Venn Visualization -->
    <circle cx="260" cy="190" r="130" fill="#e0f2fe" fill-opacity="0.7" stroke="#0284c7" stroke-width="2"/>
    <circle cx="440" cy="190" r="100" fill="#d1fae5" fill-opacity="0.7" stroke="#059669" stroke-width="2"/>

    <text x="200" y="140" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#0369a1">RELEVANCY</text>
    <text x="160" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Logical connection</text>
    <text x="160" y="185" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Defined by BSA S. 4–50</text>
    <text x="160" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Rules of logic & cause</text>
    <text x="160" y="225" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Genus (wider)</text>

    <!-- Overlap -->
    <text x="350" y="170" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#142c46">ADMISSIBLE</text>
    <text x="350" y="188" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#142c46">Relevant facts</text>
    <text x="350" y="202" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#142c46">NOT barred by</text>
    <text x="350" y="216" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#142c46">exclusion rules</text>

    <text x="480" y="150" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#047857">ADMISSIBILITY</text>
    <text x="450" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Legal consequence</text>
    <text x="450" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Based on strict law</text>
    <text x="450" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Excludes hearsay,</text>
    <text x="460" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">police confessions</text>

    <!-- Bottom summary banner -->
    <rect x="0" y="325" width="700" height="35" rx="6" fill="#142c46"/>
    <text x="350" y="347" text-anchor="middle" font-family="Georgia, serif" font-size="12" fill="#dfbf80">CARDINAL RULE: All admissible evidence is relevant, but all relevant evidence is not admissible.</text>
  </g>
"""

# 18. Res Gestae Flowchart
d18_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">DOCTRINE OF RES GESTAE [BSA SECTION 4 / IEA SECTION 6]</text>

    <rect x="50" y="60" width="600" height="60" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="350" y="85" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">THE STATUTORY RULE</text>
    <text x="350" y="105" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">Facts so connected with a fact in issue as to form PART OF THE SAME TRANSACTION are relevant,</text>
    <text x="350" y="120" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">whether they occurred at the same time and place or at different times and places.</text>

    <!-- Two tests -->
    <rect x="50" y="145" width="285" height="150" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="50" y="145" width="285" height="30" rx="8" fill="#137d72"/>
    <text x="192" y="165" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">SPONTANEITY &amp; CONTEMPORANEITY</text>
    <text x="65" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Must be spontaneous statement</text>
    <text x="65" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• No time interval to fabricate/concoct</text>
    <text x="65" y="235" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">Ratten v. The Queen (1972) AC 378:</text>
    <text x="65" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Distressed telephone call before murder held</text>
    <text x="65" y="270" font-family="system-ui, sans-serif" font-size="9" fill="#334155">admissible as res gestae.</text>

    <rect x="365" y="145" width="285" height="150" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="365" y="145" width="285" height="30" rx="8" fill="#8c2432"/>
    <text x="507" y="165" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">THE EXCLUSIONARY THRESHOLD</text>
    <text x="380" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Past narrative is NOT res gestae</text>
    <text x="380" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Interval creates opportunity for design</text>
    <text x="380" y="235" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">R. v. Bedingfield (1879) 14 Cox CC 341:</text>
    <text x="380" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#334155">"See what Harry has done!" excluded as act</text>
    <text x="380" y="270" font-family="system-ui, sans-serif" font-size="9" fill="#334155">was complete (strict historic view).</text>

    <rect x="50" y="310" width="600" height="40" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="350" y="332" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#142c46">Sukhar v. State of UP (1999) 9 SCC 507 — Bystander statements admissible only if simultaneous with act.</text>
  </g>
"""

# 19. Confessions Landscape
d19_content = """
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="720" height="40" rx="6" fill="#142c46"/>
    <text x="360" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">CONFESSIONS ARCHITECTURE UNDER BHARATIYA SAKSHYA ADHINIYAM (BSA)</text>

    <!-- General Involuntary -->
    <rect x="0" y="55" width="225" height="230" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="55" width="225" height="30" rx="6" fill="#8c2432"/>
    <text x="112" y="75" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">INVOLUNTARY CONFESSION</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">S. 22 BSA / S. 24 IEA</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Caused by inducement,</text>
    <text x="25" y="140" font-family="system-ui, sans-serif" font-size="9" fill="#334155">threat, or promise</text>
    <text x="15" y="160" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• From person in authority</text>
    <text x="15" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Regarding charge</text>
    <rect x="15" y="205" width="195" height="30" rx="4" fill="#fee2e2"/>
    <text x="112" y="224" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">IRRELEVANT IN LAW</text>
    <text x="15" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Free & voluntary test</text>

    <!-- Police Confession -->
    <rect x="245" y="55" width="230" height="230" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="245" y="55" width="230" height="30" rx="6" fill="#8c2432"/>
    <text x="360" y="75" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">CONFESSION TO POLICE</text>
    <text x="260" y="105" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">S. 23(1) BSA / S. 25, 26 IEA</text>
    <text x="260" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Confession to police officer</text>
    <text x="270" y="140" font-family="system-ui, sans-serif" font-size="9" fill="#334155">cannot be proved</text>
    <text x="260" y="160" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Made in police custody</text>
    <text x="270" y="175" font-family="system-ui, sans-serif" font-size="9" fill="#334155">barred unless before Mag.</text>
    <rect x="260" y="205" width="200" height="30" rx="4" fill="#fee2e2"/>
    <text x="360" y="224" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#991b1b">ABSOLUTE BAR ON PROOF</text>
    <text x="260" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Protection against torture</text>

    <!-- S. 23(2) Discovery Exception -->
    <rect x="495" y="55" width="225" height="230" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="495" y="55" width="225" height="30" rx="6" fill="#137d72"/>
    <text x="607" y="75" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">DISCOVERY EXCEPTION</text>
    <text x="510" y="105" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">S. 23(2) BSA / S. 27 IEA</text>
    <text x="510" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Information leading distinctly</text>
    <text x="520" y="140" font-family="system-ui, sans-serif" font-size="9" fill="#334155">to discovery of fact</text>
    <text x="510" y="160" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Confirmatory test</text>
    <rect x="510" y="205" width="195" height="30" rx="4" fill="#d1fae5"/>
    <text x="607" y="224" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">ADMISSIBLE IN EVIDENCE</text>
    <text x="510" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Pulukuri Kottaya (1947) PC</text>

    <!-- Bottom note -->
    <rect x="0" y="300" width="720" height="40" rx="6" fill="#142c46"/>
    <text x="360" y="324" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Kashmira Singh v. State of MP (1952) — Co-accused confession under S. 24 BSA cannot be substantive evidence.</text>
  </g>
"""

# 20. Dying Declarations Rules
d20_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">DYING DECLARATION [BSA S. 26(a) / IEA S. 32(1)]</text>

    <!-- Principles -->
    <rect x="0" y="55" width="330" height="235" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="55" width="330" height="35" rx="8" fill="#137d72"/>
    <text x="165" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">CARDINAL LEGAL PRINCIPLES</text>
    <text x="15" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Nemo Moriturus Praesumitur Mentire:</text>
    <text x="15" y="132" font-family="Georgia, serif" font-size="10" font-style="italic" fill="#64748b">"A man will not meet his maker with a lie in his mouth."</text>
    <text x="15" y="155" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Relates to CAUSE OF DEATH or</text>
    <text x="25" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#334155">circumstances of transaction resulting in death</text>
    <text x="15" y="190" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Expectation of death NOT required (Indian Law)</text>
    <text x="15" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Admissible in BOTH criminal & civil proceedings</text>
    <text x="15" y="235" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">Pakala Narayana Swami v. Emperor (1939):</text>
    <text x="15" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Transaction must have proximate relation to the death.</text>

    <!-- Evidentiary Value & Tests -->
    <rect x="370" y="55" width="330" height="235" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="370" y="55" width="330" height="35" rx="8" fill="#142c46"/>
    <text x="535" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">EVIDENTIARY VALUE &amp; JUDICIAL TESTS</text>
    <text x="385" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Sole Basis of Conviction:</text>
    <text x="385" y="132" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Can form sole basis if voluntary & truthful</text>
    <text x="385" y="155" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">Required Safeguards:</text>
    <text x="385" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Fit state of mind certified by medical officer</text>
    <text x="385" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Free from tutoring, prompting, or coercion</text>
    <text x="385" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Recorded preferably by Magistrate (Q&A form)</text>
    <text x="385" y="240" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">Kushal Rao (1958) & Sharad Sarda (1984):</text>
    <text x="385" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Inconsistent dying declarations require corroboration.</text>

    <!-- Bottom note -->
    <rect x="0" y="305" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Signs and gestures by injured person unable to speak constitute valid dying declaration (Queen Empress v. Abdullah).</text>
  </g>
"""

# 21. Electronic Evidence Certification (S. 63 BSA / S. 65B IEA)
d21_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">ELECTRONIC EVIDENCE ADMISSIBILITY [BSA S. 61 &amp; S. 63 / IEA S. 65B]</text>

    <!-- Section 61 BSA Equivalence -->
    <rect x="0" y="55" width="700" height="50" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <text x="20" y="78" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#137d72">SECTION 61 BSA: EQUAL LEGAL STATUS</text>
    <text x="20" y="94" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Electronic or digital records shall have the same legal effect, validity, and enforceability as any paper document.</text>

    <!-- S. 63 Certificate Requirements -->
    <rect x="0" y="120" width="335" height="175" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="120" width="335" height="30" rx="8" fill="#142c46"/>
    <text x="167" y="140" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#dfbf80">SECTION 63 CERTIFICATE CONDITIONS</text>
    <text x="15" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#334155">1. Identifying the electronic record</text>
    <text x="15" y="190" font-family="system-ui, sans-serif" font-size="10" fill="#334155">2. Describing the device producing it</text>
    <text x="15" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#334155">3. Computer operating in lawful custody</text>
    <text x="15" y="230" font-family="system-ui, sans-serif" font-size="10" fill="#334155">4. Device operating properly at all times</text>
    <text x="15" y="250" font-family="system-ui, sans-serif" font-size="10" fill="#334155">5. Signed by person in official custody</text>

    <!-- Judicial Interpretation -->
    <rect x="365" y="120" width="335" height="175" rx="8" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <rect x="365" y="120" width="335" height="30" rx="8" fill="#8c2432"/>
    <text x="532" y="140" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#ffffff">LANDMARK SUPREME COURT RULINGS</text>
    <text x="380" y="170" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">Anvar P.V. v. P.K. Basheer (2014):</text>
    <text x="380" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Certificate is a condition precedent for secondary electronic evidence.</text>
    <text x="380" y="210" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Arjun Panditrao Khotkar (2020) 3-Judge Bench:</text>
    <text x="380" y="225" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Certificate mandatory for secondary copy; if original device produced in court, no certificate needed.</text>
    <text x="380" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">BSA provides standard schedule form for certificate.</text>

    <!-- Bottom note -->
    <rect x="0" y="310" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="333" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Section 63(4) BSA schedule format codifies standard certificate requirements into statutory law.</text>
  </g>
"""

# 22. Burden of Proof Spectrum
d22_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">BURDEN OF PROOF VS ONUS OF PROOF</text>

    <rect x="0" y="55" width="330" height="235" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="55" width="330" height="35" rx="8" fill="#142c46"/>
    <text x="165" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#dfbf80">LEGAL BURDEN [BSA S. 104 / IEA S. 101]</text>
    <text x="15" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Burden of Establishing Case:</text>
    <text x="15" y="135" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Lies on party asserting affirmative of issue</text>
    <text x="15" y="155" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">• NEVER SHIFTS throughout the trial</text>
    <text x="15" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• In criminal cases: on prosecution to prove</text>
    <text x="25" y="190" font-family="system-ui, sans-serif" font-size="10" fill="#334155">guilt beyond all reasonable doubt</text>
    <text x="15" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• If neither side adduces evidence, person</text>
    <text x="25" y="230" font-family="system-ui, sans-serif" font-size="10" fill="#334155">bearing legal burden loses (S. 105 BSA)</text>
    <text x="15" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Fixed by substantive law and pleadings.</text>

    <!-- Column 2 -->
    <rect x="370" y="55" width="330" height="235" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="370" y="55" width="330" height="35" rx="8" fill="#137d72"/>
    <text x="535" y="78" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#ffffff">ONUS OF PROOF [BSA S. 105 / IEA S. 102]</text>
    <text x="385" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#142c46">Evidential Burden of Adducing Evidence:</text>
    <text x="385" y="135" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Burden of introducing evidence</text>
    <text x="385" y="155" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">• CONTINUOUSLY SHIFTS back and forth</text>
    <text x="385" y="175" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Shifts like a pendulum as evidence is led</text>
    <text x="385" y="200" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">Special Knowledge Exception (S. 109 BSA):</text>
    <text x="385" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#334155">When fact especially within knowledge of a person,</text>
    <text x="385" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#334155">burden of proving it lies upon him (Shambhu Nath Mehra).</text>
    <text x="385" y="260" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">General Exceptions burden: on accused (S. 108 BSA / S. 105 IEA).</text>

    <!-- Bottom note -->
    <rect x="0" y="305" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Raghavamma v. Chenchamma (AIR 1964 SC 136) — Landmark Constitution Bench distinguishing burden vs onus.</text>
  </g>
"""

# 23. Estoppel Types
d23_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">DOCTRINE OF ESTOPPEL [BSA S. 121 / IEA S. 115]</text>

    <rect x="50" y="55" width="600" height="70" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="350" y="80" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#142c46">STATUTORY DEFINITION</text>
    <text x="350" y="100" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#137d72">When one person has, by declaration, act or omission, intentionally caused another to believe a thing</text>
    <text x="350" y="115" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">to be true and act upon such belief, neither he nor representative can deny truth of that thing.</text>

    <!-- 3 columns -->
    <rect x="50" y="140" width="180" height="150" rx="6" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <text x="140" y="165" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#137d72">PROMISSORY</text>
    <text x="65" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Unequivocal promise</text>
    <text x="65" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Alteration of position</text>
    <text x="65" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Motilal Padampat</text>
    <text x="65" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Sugar Mills (1979)</text>

    <rect x="260" y="140" width="180" height="150" rx="6" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <text x="350" y="165" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#142c46">TENANT ESTOPPEL</text>
    <text x="275" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• S. 122 BSA / S. 116</text>
    <text x="275" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Tenant cannot deny</text>
    <text x="285" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#334155">landlord's title at start</text>
    <text x="275" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Licensee estoppel</text>

    <rect x="470" y="140" width="180" height="150" rx="6" fill="#ffffff" stroke="#8c2432" stroke-width="2" filter="url(#shadow)"/>
    <text x="560" y="165" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#8c2432">EXCEPTIONS</text>
    <text x="485" y="195" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• NO estoppel vs STATUTE</text>
    <text x="485" y="215" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• NO estoppel vs MINOR</text>
    <text x="485" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">Mohori Bibee (1903)</text>
    <text x="485" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#991b1b">No estoppel on law</text>

    <!-- Bottom note -->
    <rect x="50" y="305" width="600" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Estoppel is a rule of civil evidence; it cannot be invoked to validate an illegal or void act.</text>
  </g>
"""

# 24. Stages of Witness Examination
d24_content = """
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="25" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#dfbf80">THE THREE STAGES OF WITNESS EXAMINATION [BSA S. 142 &amp; 143 / IEA S. 137 &amp; 138]</text>

    <!-- Stage 1: Chief -->
    <rect x="0" y="60" width="215" height="235" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="0" y="60" width="215" height="35" rx="8" fill="#142c46"/>
    <text x="107" y="83" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">1. EXAMINATION-IN-CHIEF</text>
    <text x="15" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">By party who calls witness</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Purpose: to elicit facts</text>
    <text x="25" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#334155">supporting party's case</text>
    <text x="15" y="185" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#8c2432">Leading Questions Barred:</text>
    <text x="15" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Must NOT be asked without</text>
    <text x="15" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#334155">permission of court (S. 147 BSA)</text>
    <text x="15" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">Except introductory/uncontested.</text>

    <text x="230" y="175" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" fill="#8c2432">➔</text>

    <!-- Stage 2: Cross -->
    <rect x="245" y="60" width="215" height="235" rx="8" fill="#ffffff" stroke="#137d72" stroke-width="2" filter="url(#shadow)"/>
    <rect x="245" y="60" width="215" height="35" rx="8" fill="#137d72"/>
    <text x="352" y="83" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#ffffff">2. CROSS-EXAMINATION</text>
    <text x="260" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#137d72">By the adverse party</text>
    <text x="260" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Test veracity & credibility</text>
    <text x="260" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Discover who witness is</text>
    <text x="260" y="185" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Shake credit (S. 149 BSA)</text>
    <rect x="255" y="205" width="195" height="30" rx="4" fill="#d1fae5"/>
    <text x="352" y="224" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#065f46">LEADING QUESTIONS ALLOWED</text>
    <text x="260" y="255" font-family="system-ui, sans-serif" font-size="9" fill="#065f46">Section 148 BSA / S. 143 IEA</text>

    <text x="475" y="175" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" fill="#8c2432">➔</text>

    <!-- Stage 3: Re-exam -->
    <rect x="490" y="60" width="210" height="235" rx="8" fill="#ffffff" stroke="#142c46" stroke-width="2" filter="url(#shadow)"/>
    <rect x="490" y="60" width="210" height="35" rx="8" fill="#142c46"/>
    <text x="595" y="83" text-anchor="middle" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#dfbf80">3. RE-EXAMINATION</text>
    <text x="505" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#142c46">By party who called witness</text>
    <text x="505" y="145" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Explain matters referred</text>
    <text x="515" y="160" font-family="system-ui, sans-serif" font-size="10" fill="#334155">to in cross-examination</text>
    <text x="505" y="185" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• NO new matter without</text>
    <text x="515" y="200" font-family="system-ui, sans-serif" font-size="10" fill="#334155">permission of court</text>
    <text x="505" y="225" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• If new matter introduced,</text>
    <text x="515" y="240" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">adverse party may cross-examine</text>

    <!-- Bottom note -->
    <rect x="0" y="305" width="700" height="40" rx="6" fill="#142c46"/>
    <text x="350" y="328" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" fill="#dfbf80">Hostile Witness (S. 157 BSA / S. 154 IEA): Court may permit party to put cross-examination questions to his own witness.</text>
  </g>
"""

DIAGRAMS = [
    # Criminal Law (8)
    ("diag-crim-culpable-homicide-murder.svg", "Culpable Homicide vs Murder: The S. 100/101 BNS Distinction", "Statutory elements, Reg v. Govinda formula & The 5 Exceptions", "CRIMINAL LAW BLUEPRINT", d1_content),
    ("diag-crim-mens-rea-liability.svg", "The Four Stages of Crime & Mens Rea Principles", "From criminal intention to commission and strict liability", "CRIMINAL LAW BLUEPRINT", d2_content),
    ("diag-crim-joint-liability-common-intention.svg", "Joint Liability: Common Intention vs Common Object", "Section 3(5) BNS (S. 34 IPC) versus Section 190 BNS (S. 149 IPC)", "CRIMINAL LAW BLUEPRINT", d3_content),
    ("diag-crim-private-defence-spectrum.svg", "Right of Private Defence of Body & Property", "BNS Sections 34 to 44 / IPC Sections 96 to 106 & Causing Death", "CRIMINAL LAW BLUEPRINT", d4_content),
    ("diag-crim-property-offences-gradation.svg", "Property Offences: The Theft to Dacoity Escalation Spectrum", "From simple possession transfer to organized violent extortion", "CRIMINAL LAW BLUEPRINT", d5_content),
    ("diag-crim-hit-and-run-caveat.svg", "Causing Death by Rash/Negligent Act: Section 106 BNS", "Section 106(1) in force vs Section 106(2) hit-and-run stay notification", "STATUTORY CAVEAT ALERT", d6_content),
    ("diag-crim-kidnapping-vs-abduction.svg", "Kidnapping versus Abduction: Statutory Comparison", "Guardianship vs forceful compulsion & BNS age equalization", "CRIMINAL LAW BLUEPRINT", d7_content),
    ("diag-crim-punishments-bns.svg", "The Six Punishments & Community Service in BNS", "Capital punishment, life imprisonment, and the new 6th reform", "BNS 2023 SENTENCING", d8_content),

    # Criminal Procedure (8)
    ("diag-crpc-courts-hierarchy.svg", "Hierarchy of Criminal Courts & Sentencing Jurisdictions", "Sessions, CJM, JMFC & Abolition of Metropolitan Magistrates in BNSS", "CRIMINAL PROCEDURE BLUEPRINT", d9_content),
    ("diag-crpc-investigation-flowchart.svg", "Criminal Investigation Timeline: FIR to Police Report", "S. 173 FIR, Zero FIR, Witness Examination & S. 193 Charge-Sheet", "CRIMINAL PROCEDURE BLUEPRINT", d10_content),
    ("diag-crpc-arrest-safeguards.svg", "Arrest Safeguards, Handcuff Rules & The 24-Hour Rule", "Notice of appearance, D.K. Basu guidelines, and Section 43(3) limits", "PROCEDURAL SAFEGUARDS", d11_content),
    ("diag-crpc-remand-custody-timeline.svg", "Remand & Police Custody in Parts under Section 187 BNSS", "15-day custody spread across 40/60 days & Default Bail Rights", "PROCEDURAL REFORMS", d12_content),
    ("diag-crpc-trials-comparison.svg", "Comparative Matrix of Four Criminal Trials", "Sessions, Warrant, Summons, and Summary Trials under BNSS & CrPC", "CRIMINAL PROCEDURE BLUEPRINT", d13_content),
    ("diag-crpc-bail-framework.svg", "The Criminal Bail Spectrum: Regular, Undertrial & Anticipatory", "Bailable right, Section 479 undertrial release, and Section 482", "BAIL JURISPRUDENCE", d14_content),
    ("diag-crpc-trial-in-absentia.svg", "Trial in Absentia of Proclaimed Offenders: Section 356 BNSS", "Groundbreaking procedure for absconders evading trial", "BNSS 2023 INNOVATION", d15_content),
    ("diag-crpc-maintenance-s144.svg", "Statutory Maintenance Framework: Section 144 BNSS", "Essential conditions, 60-day interim disposal & secular coverage", "CRIMINAL PROCEDURE BLUEPRINT", d16_content),

    # Law of Evidence (8)
    ("diag-evi-relevancy-vs-admissibility.svg", "Relevancy versus Admissibility in Evidence Law", "Logical connection versus legal admissibility & Exclusionary rules", "EVIDENCE LAW BLUEPRINT", d17_content),
    ("diag-evi-res-gestae-flowchart.svg", "Doctrine of Res Gestae: Facts Forming Part of Same Transaction", "Section 4 BSA / Section 6 IEA, Spontaneity, and Ratten v. R", "EVIDENCE LAW BLUEPRINT", d18_content),
    ("diag-evi-confessions-landscape.svg", "Confessions Architecture: Involuntary, Police Bar & Discovery", "Sections 22, 23(1) and the Section 23(2) Pulukuri Kottaya Exception", "EVIDENCE LAW BLUEPRINT", d19_content),
    ("diag-evi-dying-declaration-rules.svg", "Dying Declarations: Section 26(a) BSA / Section 32(1) IEA", "Pakala Narayana Swami, Sharad Sarda, and Evidentiary Weight", "EVIDENCE LAW BLUEPRINT", d20_content),
    ("diag-evi-electronic-evidence-cert.svg", "Electronic Evidence Admissibility & Section 63 BSA Certificate", "Digital equivalence under S. 61 & Mandatory Section 63 Conditions", "MODERN EVIDENCE BLUEPRINT", d21_content),
    ("diag-evi-burden-of-proof-spectrum.svg", "Burden of Proof vs Onus of Proof & Statutory Presumptions", "Legal burden (S. 104) versus Evidential onus (S. 105) & S. 109", "EVIDENCE LAW BLUEPRINT", d22_content),
    ("diag-evi-estoppel-types.svg", "Doctrine of Estoppel: Section 121 BSA / Section 115 IEA", "Representation, Promissory Estoppel, Tenant Estoppel & Exceptions", "EVIDENCE LAW BLUEPRINT", d23_content),
    ("diag-evi-witness-examination-stages.svg", "Three Stages of Witness Examination & Leading Questions", "Examination-in-Chief, Cross-Examination & Re-Examination", "TRIAL ADVOCACY BLUEPRINT", d24_content)
]

for filename, title, subtitle, badge, content_g in DIAGRAMS:
    svg_code = wrap_svg(title, subtitle, badge, content_g)
    filepath = os.path.join("assets/learning/images/diagrams", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"Generated: {filename}")

print(f"All {len(DIAGRAMS)} custom vector SVG schematics successfully generated.")
