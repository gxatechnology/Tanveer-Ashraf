"""
Generate 18 Academic SVG Diagrams for Social Legislation (Paper I - General Knowledge)
Two diagrams per Act:
1. RPwD: diag-soc-disab-rights-framework.svg, diag-soc-disab-accessibility.svg
2. Senior Citizens: diag-soc-parent-tribunal-flow.svg, diag-soc-parent-maintenance-comparison.svg
3. Dowry: diag-soc-dowry-offences-elements.svg, diag-soc-dowry-vs-gifts.svg
4. DV: diag-soc-dv-remedies-hierarchy.svg, diag-soc-dv-domestic-relationship.svg
5. POSH: diag-soc-posh-complaint-inquiry.svg, diag-soc-posh-ic-vs-lc.svg
6. PCPNDT: diag-soc-pcpndt-regulatory-architecture.svg, diag-soc-pcpndt-prohibited-conduct.svg
7. MTP: diag-soc-mtp-gestational-framework.svg, diag-soc-mtp-consent-medical-board.svg
8. IRWA: diag-soc-irwa-prohibitions-exceptions.svg, diag-soc-irwa-enforcement-powers.svg
9. POCSO: diag-soc-pocso-protection-framework.svg, diag-soc-pocso-special-court-trial.svg
"""

import os

DIAGRAMS = {
    # 1. RPwD 1
    "diag-soc-disab-rights-framework.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_rpwd1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_rpwd1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_rpwd1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_rpwd1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">RIGHTS OF PERSONS WITH DISABILITIES (RPwD ACT, 2016)</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Statutory Rights Architecture • UNCRPD Harmonization • Benchmark Disabilities (40%)</text>

  <!-- Left: Core Statutory Rights -->
  <g transform="translate(40, 95)" filter="url(#shadow_rpwd1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SUBSTANTIVE RIGHTS (CHAPTER II)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 3: Equality &amp; Non-Discrimination</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">No person with disability shall be discriminated on ground</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">of disability; duty to provide Reasonable Accommodation.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5: Community Living &amp; Home</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">Right to live in community; not to be segregated.</text>

    <text x="20" y="170" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 12: Equal Legal Capacity</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="11">Right to own and inherit property, control financial affairs</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">and access bank loans/mortgages equally with others.</text>

    <rect x="20" y="225" width="300" height="75" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="245" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LEGAL GUARDIANSHIP (SECTION 14):</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Limited Guardianship: specific period &amp; decision.</text>
    <text x="30" y="282" fill="#4a5568" font-family="sans-serif" font-size="10">• Plenary Guardianship granted only exceptionally.</text>

    <text x="20" y="325" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 16 &amp; 17: Inclusive Education</text>
    <text x="25" y="345" fill="#4a5568" font-family="sans-serif" font-size="11">Admission without discrimination; free education up to</text>
    <text x="25" y="360" fill="#4a5568" font-family="sans-serif" font-size="11">18 years for benchmark disabilities (Section 31).</text>
  </g>

  <!-- Right: Affirmative Action & Reservations -->
  <g transform="translate(420, 95)" filter="url(#shadow_rpwd1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">BENCHMARK DISABILITY &amp; RESERVATIONS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 2(r): Benchmark Disability</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Not less than 40% of a specified disability certified</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">by competent certifying medical authority.</text>

    <rect x="20" y="115" width="300" height="115" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="135" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 34: 4% EMPLOYMENT RESERVATION:</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">(a) 1% Blindness and low vision</text>
    <text x="30" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">(b) 1% Deaf and hard of hearing</text>
    <text x="30" y="189" fill="#4a5568" font-family="sans-serif" font-size="10">(c) 1% Locomotor disability including cerebral palsy,</text>
    <text x="45" y="204" fill="#4a5568" font-family="sans-serif" font-size="10">leprosy cured, dwarfism, acid attack victims</text>
    <text x="30" y="221" fill="#4a5568" font-family="sans-serif" font-size="10">(d) 1% Autism, intellectual disability &amp; multiple</text>

    <text x="20" y="250" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 32: 5% Higher Education Quota</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">Minimum 5% seats reserved in government and aided</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">higher educational institutions with 5-year age relaxation.</text>

    <rect x="20" y="305" width="300" height="55" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="325" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SCHEDULE: 21 SPECIFIED DISABILITIES</text>
    <text x="30" y="345" fill="#4a5568" font-family="sans-serif" font-size="10">Expanded from 7 (1995 Act) to 21 categories including</text>
    <text x="30" y="358" fill="#4a5568" font-family="sans-serif" font-size="10">Parkinson's, Acid Attack, Thalassemia, Sickle Cell.</text>
  </g>
</svg>""",

    # 1. RPwD 2
    "diag-soc-disab-accessibility.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_rpwd2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_rpwd2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_rpwd2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_rpwd2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">RPwD ACT 2016: ENFORCEMENT &amp; ACCESSIBILITY</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Institutional Redressal Machinery • Accessibility Mandates • Special Courts &amp; Penalties</text>

  <!-- Left: Institutional Machinery -->
  <g transform="translate(40, 95)" filter="url(#shadow_rpwd2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">INSTITUTIONAL COMMISSIONERS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Central &amp; State Advisory Boards (S. 60 &amp; 66)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Apex policy-making and advisory bodies at Union</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">and State levels; 3-year tenure for nominated members.</text>

    <rect x="20" y="120" width="300" height="90" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="140" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">CHIEF &amp; STATE COMMISSIONERS (S. 74 &amp; 79):</text>
    <text x="30" y="160" fill="#4a5568" font-family="sans-serif" font-size="10">• Inquire into deprivation of rights &amp; safeguards.</text>
    <text x="30" y="177" fill="#4a5568" font-family="sans-serif" font-size="10">• Civil Court powers under CPC: summoning witnesses,</text>
    <text x="30" y="194" fill="#4a5568" font-family="sans-serif" font-size="10">discovery of documents, requisitioning public records.</text>

    <text x="20" y="235" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 84: Special Courts</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">State Government, with concurrence of High Court</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">Chief Justice, designates Court of Session as Special Court.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 85: Special Public Prosecutor</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Advocate with minimum 7 YEARS practice designated</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">for conducting trials in Special Courts.</text>

    <rect x="20" y="342" width="300" height="24" rx="4" fill="#fff9ec"/>
    <text x="170" y="358" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: 7 Years Standing Required (S. 85)</text>
  </g>

  <!-- Right: Accessibility & Penalties -->
  <g transform="translate(420, 95)" filter="url(#shadow_rpwd2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">ACCESSIBILITY &amp; OFFENCES</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Accessibility Framework (Sections 40–46)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Section 41: Accessible transport (buses, rail, air).</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">• Section 42: Accessible ICT (websites, electronic media).</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">• Section 45: 5-year timeline for retrofitting buildings.</text>

    <rect x="20" y="130" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="150" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">OFFENCES &amp; PENALTIES (SECTIONS 89–95):</text>
    <text x="30" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 89 General Penalty: First offence fine up to Rs 10,000;</text>
    <text x="35" y="185" fill="#4a5568" font-family="sans-serif" font-size="10">subsequent offence fine Rs 50,000 to Rs 5,00,000.</text>
    <text x="30" y="202" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 92 Atrocities: Insult/humiliation, assault, denial</text>
    <text x="35" y="217" fill="#4a5568" font-family="sans-serif" font-size="10">of food = 6 months to 5 years imprisonment + fine.</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 93: Penalty for Failure to Furnish Info</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Fine up to Rs 25,000 for each failure; Rs 1,000/day fine.</text>

    <text x="20" y="290" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 94: Corporate Liability</text>
    <text x="25" y="310" fill="#4a5568" font-family="sans-serif" font-size="11">Company as well as officer-in-charge liable unless</text>
    <text x="25" y="325" fill="#4a5568" font-family="sans-serif" font-size="11">offence committed without knowledge/due diligence.</text>

    <rect x="20" y="340" width="300" height="25" rx="4" fill="#edf7f4"/>
    <text x="170" y="357" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Focus: S. 92 Atrocities 6 Mo to 5 Yrs</text>
  </g>
</svg>""",

    # 2. Senior Citizens 1
    "diag-soc-parent-tribunal-flow.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_par1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_par1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_par1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_par1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">MAINTENANCE &amp; WELFARE OF PARENTS ACT, 2007</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Tribunal Adjudication Architecture • Summary Proceedings • SDO &amp; DM Jurisdiction</text>

  <!-- Left: Application & Adjudication -->
  <g transform="translate(40, 95)" filter="url(#shadow_par1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">MAINTENANCE TRIBUNAL (SDO)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 4: Eligibility &amp; Entitlement</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Senior citizen (60+ years) or parent unable to maintain</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">themselves from own earning or property.</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">• Against children (major) or childless relative inheriting.</text>

    <text x="20" y="140" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5: Application Procedure</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Filed by senior citizen/parent, authorized NGO, or suo motu.</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• Interim maintenance permissible during inquiry.</text>

    <rect x="20" y="195" width="300" height="75" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="215" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">CONSTITUTION &amp; PROCEDURE (S. 7 &amp; 8):</text>
    <text x="30" y="235" fill="#4a5568" font-family="sans-serif" font-size="10">• Presided by Sub-Divisional Officer (SDO).</text>
    <text x="30" y="250" fill="#4a5568" font-family="sans-serif" font-size="10">• Summary procedure under CrPC; Civil Court powers.</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Conciliation referral to Conciliation Officer (S. 6).</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 9: Maintenance Order</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Monthly allowance determined based on standard of living</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">(Statutory cap of Rs 10,000 originally in Section 9(2)).</text>
    <rect x="20" y="342" width="300" height="24" rx="4" fill="#fff9ec"/>
    <text x="170" y="358" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Point: SDO is Tribunal, DM is Appellate</text>
  </g>

  <!-- Right: Appeals & Bar of Advocates -->
  <g transform="translate(420, 95)" filter="url(#shadow_par1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">APPELLATE TRIBUNAL &amp; SPECIAL BARS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 15: Appellate Tribunal (DM)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Constituted in each district, presided over by</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">the DISTRICT MAGISTRATE (DM / Collector).</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 16: Right to Appeal</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">• Period of limitation: 60 DAYS from date of order.</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Statute gives right of appeal to senior citizen/parent.</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• High Courts have read in children's appeal rights.</text>

    <rect x="20" y="195" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="215" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 17: BAR ON LEGAL PRACTITIONERS:</text>
    <text x="30" y="235" fill="#4a5568" font-family="sans-serif" font-size="10">• Advocates CANNOT represent any party as of right.</text>
    <text x="30" y="250" fill="#4a5568" font-family="sans-serif" font-size="10">• Senior citizen may be assisted by Maintenance Officer.</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Paramjit Kumar Saroya v. UOI read down bar for complex cases.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 14: Enforcement of Order</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Enforced in same manner as CrPC Section 125;</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">warrant for levying amount + 1 month imprisonment.</text>
    <rect x="20" y="342" width="300" height="24" rx="4" fill="#edf7f4"/>
    <text x="170" y="358" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Limitation for Appeal is 60 Days (S. 16)</text>
  </g>
</svg>""",

    # 2. Senior Citizens 2
    "diag-soc-parent-maintenance-comparison.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_par2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_par2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_par2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_par2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">SECTION 23: PROPERTY VOIDANCE &amp; S. 24 OFFENCES</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Deemed Fraud Transfers • Sudesh Chhikara Doctrine • Abandonment Penalties</text>

  <!-- Left: Section 23 Property Transfer -->
  <g transform="translate(40, 95)" filter="url(#shadow_par2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SECTION 23: PROPERTY TRANSFER VOID</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Statutory Deemed Fraud Provision</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Where senior citizen transfers property by gift or otherwise,</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">subject to condition of basic amenities &amp; physical needs.</text>

    <rect x="20" y="115" width="300" height="100" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="135" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">ESSENTIAL CONDITIONS FOR S. 23 VOIDANCE:</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">1. Transfer must be made after Act commencement (2007).</text>
    <text x="30" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">2. Transferee undertook to provide basic amenities/needs.</text>
    <text x="30" y="189" fill="#4a5568" font-family="sans-serif" font-size="10">3. Transferee failed or refused to provide amenities.</text>
    <text x="30" y="206" fill="#4a5568" font-family="sans-serif" font-size="10">-> Transfer deemed made by FRAUD, COERCION or UNDUE INFLUENCE.</text>

    <text x="20" y="235" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Landmark: Sudesh Chhikara v. Ramti Devi (2022)</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">Supreme Court held: Condition to maintain MUST be stated</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">in the document or clearly discernible from circumstances.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Power of Maintenance Tribunal</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Tribunal can declare transfer VOID at senior citizen's option.</text>
    <rect x="20" y="335" width="300" height="28" rx="4" fill="#fff9ec"/>
    <text x="170" y="353" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Point: Transfer Void at Option of Senior Citizen</text>
  </g>

  <!-- Right: Section 24 Offences & Welfare -->
  <g transform="translate(420, 95)" filter="url(#shadow_par2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">S. 24 OFFENCE &amp; STATE WELFARE</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 24: Abandonment of Senior Citizen</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Whoever, having the care or protection of senior citizen,</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">leaves such senior citizen in any place with intention of</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">wholly abandoning them commits a cognizable offence.</text>

    <rect x="20" y="130" width="300" height="80" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="150" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">PUNISHMENT UNDER SECTION 24:</text>
    <text x="30" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">• Imprisonment up to THREE (3) MONTHS, or</text>
    <text x="30" y="187" fill="#4a5568" font-family="sans-serif" font-size="10">• Fine up to FIVE THOUSAND (Rs 5,000) RUPEES, or BOTH.</text>
    <text x="30" y="202" fill="#4a5568" font-family="sans-serif" font-size="10">• Section 25: Cognizable &amp; Bailable offence tried summarily.</text>

    <text x="20" y="235" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 19: Old Age Homes</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">State Government may establish old age homes accessible</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">to at least 150 indigent senior citizens per district.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 20: Medical Support Mandates</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Government hospitals to provide beds, separate queues,</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">and specialized geriatric treatment facilities.</text>
    <rect x="20" y="342" width="300" height="24" rx="4" fill="#edf7f4"/>
    <text x="170" y="358" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Penalty S. 24 is 3 Months / Rs 5,000</text>
  </g>
</svg>""",

    # 3. Dowry 1
    "diag-soc-dowry-offences-elements.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_dow1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_dow1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_dow1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_dow1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">DOWRY PROHIBITION ACT, 1961: OFFENCES &amp; PENALTIES</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 2 Dowry Definition • Mandatory Minimum Sentences • S. 6 Benefit of Wife</text>

  <!-- Left: Section 3 & 4 Offences -->
  <g transform="translate(40, 95)" filter="url(#shadow_dow1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">GIVING, TAKING &amp; DEMANDING</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 3: Giving or Taking Dowry</text>
    <rect x="20" y="75" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="95" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">MANDATORY PUNISHMENT (S. 3(1)):</text>
    <text x="30" y="115" fill="#4a5568" font-family="sans-serif" font-size="10">• Imprisonment: Minimum FIVE (5) YEARS.</text>
    <text x="30" y="132" fill="#4a5568" font-family="sans-serif" font-size="10">• Fine: Minimum Rs 15,000 OR amount of dowry (higher).</text>
    <text x="30" y="145" fill="#4a5568" font-family="sans-serif" font-size="9">(Court may record reasons for lower imprisonment).</text>

    <text x="20" y="175" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 4: Demanding Dowry</text>
    <rect x="20" y="185" width="300" height="65" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="205" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">PUNISHMENT FOR DEMAND (S. 4):</text>
    <text x="30" y="225" fill="#4a5568" font-family="sans-serif" font-size="10">• Imprisonment: Minimum 6 MONTHS up to 2 YEARS.</text>
    <text x="30" y="240" fill="#4a5568" font-family="sans-serif" font-size="10">• Fine: Up to TEN THOUSAND (Rs 10,000) RUPEES.</text>

    <text x="20" y="275" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 4A: Advertisement Ban</text>
    <text x="25" y="295" fill="#4a5568" font-family="sans-serif" font-size="11">Printing, publishing or circulating offers of share in</text>
    <text x="25" y="310" fill="#4a5568" font-family="sans-serif" font-size="11">property/money in consideration of marriage = 6 Mo to 5 Yrs.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Giving and Taking Dowry Equal Penalty (S. 3)</text>
  </g>

  <!-- Right: Agreements & Stridhan Trust -->
  <g transform="translate(420, 95)" filter="url(#shadow_dow1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">AGREEMENT VOID &amp; TRUST (S. 5 &amp; 6)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5: Dowry Agreement Void</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Any agreement for the giving or taking of dowry shall be</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">VOID AB INITIO and completely unenforceable at law.</text>

    <rect x="20" y="115" width="300" height="110" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="135" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 6: DOWRY FOR BENEFIT OF WIFE:</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">• If received by any person other than wife, must transfer</text>
    <text x="35" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">to woman within THREE (3) MONTHS:</text>
    <text x="40" y="185" fill="#4a5568" font-family="sans-serif" font-size="10">(a) From date of marriage (if received before marriage)</text>
    <text x="40" y="200" fill="#4a5568" font-family="sans-serif" font-size="10">(b) From date of receipt (if received at/after marriage)</text>
    <text x="40" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">(c) From date she attains 18 years (if minor when married)</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 6(2) Penalty for Failure to Transfer</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Imprisonment minimum 6 MONTHS up to 2 YEARS,</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="11">or fine Rs 5,000 to Rs 10,000, or both.</text>

    <text x="20" y="305" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 6(3): Deceased Woman's Heirs</text>
    <text x="25" y="325" fill="#4a5568" font-family="sans-serif" font-size="11">If woman dies before receiving, property transfers to children,</text>
    <text x="25" y="340" fill="#4a5568" font-family="sans-serif" font-size="11">or parents if she died within 7 years of marriage childless.</text>
    <rect x="20" y="350" width="300" height="18" rx="4" fill="#fff5f5"/>
    <text x="170" y="363" fill="#a63b49" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Transfer Period is Exactly 3 Months</text>
  </g>
</svg>""",

    # 3. Dowry 2
    "diag-soc-dowry-vs-gifts.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_dow2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_dow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_dow2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_dow2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">DOWRY VS GIFTS &amp; STATUTORY PRESUMPTIONS</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 3(2) Presents Exemption • Section 8A Reverse Burden • Section 8B DPO</text>

  <!-- Left: Dowry vs Customary Presents -->
  <g transform="translate(40, 95)" filter="url(#shadow_dow2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">DOWRY VS PRESENTS (SECTION 3(2))</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 2: Definition of 'Dowry'</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Any property or valuable security given/agreed to be given</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">directly or indirectly in connection with marriage.</text>

    <rect x="20" y="115" width="300" height="110" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="135" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 3(2) STATUTORY EXEMPTION (PRESENTS):</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">Presents given to bride or bridegroom exempt ONLY IF:</text>
    <text x="35" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">1. Given at the time of marriage WITHOUT DEMAND.</text>
    <text x="35" y="189" fill="#4a5568" font-family="sans-serif" font-size="10">2. Entered in a signed LIST (Dowry Rules 1985).</text>
    <text x="35" y="206" fill="#4a5568" font-family="sans-serif" font-size="10">3. Customary in nature and NOT EXCESSIVE in value</text>
    <text x="40" y="219" fill="#4a5568" font-family="sans-serif" font-size="10">having regard to financial status of giver.</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Stridhan Distinction (Pratibha Rani Doctrine)</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Stridhan is absolute property of woman; in-laws hold it as</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="11">trustees. Refusal to return = Criminal Breach of Trust.</text>

    <rect x="20" y="305" width="300" height="55" rx="4" fill="#fff9ec"/>
    <text x="170" y="325" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Maintenance of Lists of Presents Rules, 1985</text>
    <text x="170" y="342" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">List must be in writing, describe articles, value, relationship &amp; signed</text>
  </g>

  <!-- Right: Evidentiary Burden & Officers -->
  <g transform="translate(420, 95)" filter="url(#shadow_dow2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">BURDEN OF PROOF &amp; ENFORCEMENT</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 8A: Reverse Burden of Proof</text>
    <rect x="20" y="75" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="95" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">STATUTORY PRESUMPTION (S. 8A):</text>
    <text x="30" y="115" fill="#4a5568" font-family="sans-serif" font-size="10">Where any person is prosecuted for taking or abetting</text>
    <text x="30" y="130" fill="#4a5568" font-family="sans-serif" font-size="10">the taking of dowry under S. 3 or demanding dowry under</text>
    <text x="30" y="145" fill="#4a5568" font-family="sans-serif" font-size="10">S. 4, BURDEN OF PROVING INNOCENCE IS ON HIM.</text>

    <text x="20" y="175" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 8: Classification of Offences</text>
    <text x="25" y="195" fill="#4a5568" font-family="sans-serif" font-size="11">• COGNIZABLE for purpose of investigation.</text>
    <text x="25" y="210" fill="#4a5568" font-family="sans-serif" font-size="11">• NON-BAILABLE and NON-COMPOUNDABLE.</text>

    <text x="20" y="235" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 8B: Dowry Prohibition Officers (DPO)</text>
    <text x="25" y="255" fill="#4a5568" font-family="sans-serif" font-size="11">• Appointed by State Govt with powers of police officer.</text>
    <text x="25" y="270" fill="#4a5568" font-family="sans-serif" font-size="11">• State Govt may associate Advisory Board of 5 social workers.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 7: Cognizance of Offences</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Only MM or JMFC; upon police report or private complaint.</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">Limitation under CrPC S. 468 DOES NOT APPLY.</text>
    <rect x="20" y="342" width="300" height="24" rx="4" fill="#edf7f4"/>
    <text x="170" y="358" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: CrPC S. 468 Limitation Excluded (S. 7(2))</text>
  </g>
</svg>""",

    # 4. DV 1
    "diag-soc-dv-remedies-hierarchy.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_dv1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_dv1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_dv1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_dv1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">DOMESTIC VIOLENCE ACT, 2005: REMEDIES MATRIX</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Civil Law Relief Spectrum • Magistrate Powers • Section 31 Criminal Sanction</text>

  <!-- Left: Civil Reliefs -->
  <g transform="translate(40, 95)" filter="url(#shadow_dv1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">STATUTORY CIVIL RELIEFS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 18: Protection Orders</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Restraining respondent from committing DV, entering</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">place of employment, communicating, disposing assets.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 19: Residence Orders</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">Restraining dispossession from shared household, directing</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">respondent to remove himself, securing alternate housing.</text>

    <text x="20" y="185" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 20: Monetary Reliefs</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">Medical expenses, loss of earnings, destruction of property,</text>
    <text x="25" y="220" fill="#4a5568" font-family="sans-serif" font-size="11">and maintenance under or in addition to CrPC S. 125.</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 21 &amp; 22: Custody &amp; Compensation</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Temporary custody of children to aggrieved woman;</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="11">compensation for injuries, emotional distress &amp; trauma.</text>

    <rect x="20" y="300" width="300" height="60" rx="4" fill="#edf7f4"/>
    <text x="170" y="320" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">SECTION 23: EX PARTE &amp; INTERIM RELIEFS</text>
    <text x="170" y="338" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">Magistrate may grant interim and ex-parte orders on affidavit</text>
    <text x="170" y="350" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">without waiting for response if prima facie case established</text>
  </g>

  <!-- Right: Procedure & Section 31 Criminal Sanction -->
  <g transform="translate(420, 95)" filter="url(#shadow_dv1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PROCEDURE &amp; PENALTIES</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 12: Application to Magistrate</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Presented to Judicial Magistrate First Class or MM;</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">Magistrate MUST consider Domestic Incident Report (DIR).</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 12(5): 60-Day Disposal Mandate</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">Magistrate shall endeavor to dispose of every application</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">within SIXTY (60) DAYS from date of first hearing.</text>

    <rect x="20" y="175" width="300" height="85" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="195" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 31: BREACH OF PROTECTION ORDER:</text>
    <text x="30" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">• Breach of protection/interim protection order is an offence.</text>
    <text x="30" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">• Imprisonment up to ONE (1) YEAR, or fine up to Rs 20,000.</text>
    <text x="30" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">• Section 32: Offence is COGNIZABLE and NON-BAILABLE.</text>

    <text x="20" y="280" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 29: Appeal</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">Appeal lies to COURT OF SESSION within 30 DAYS</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">from the date order is served on aggrieved person/respondent.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#fff9ec"/>
    <text x="170" y="353" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Appeal Lies to Sessions Court (30 Days)</text>
  </g>
</svg>""",

    # 4. DV 2
    "diag-soc-dv-domestic-relationship.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_dv2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_dv2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_dv2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_dv2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">SHARED HOUSEHOLD &amp; DOMESTIC RELATIONSHIP</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 2(s) • Section 17 Right of Residence • Overruling of S.R. Batra</text>

  <!-- Left: Definitions & Judicial Evolution -->
  <g transform="translate(40, 95)" filter="url(#shadow_dv2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SECTION 2(s) &amp; SECTION 17</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 2(f): Domestic Relationship</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Relationship between two persons who live or have, at any</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">point of time, lived together in a shared household through</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">consanguinity, marriage, adoption or relationships in nature of marriage.</text>

    <text x="20" y="140" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 17: Right to Reside</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">Every woman in a domestic relationship has the right to</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">reside in the shared household, whether or not she has</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="11">any right, title or beneficial interest in the property.</text>

    <rect x="20" y="205" width="300" height="100" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="225" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SATISH CHANDER AHUJA V. SNEHA AHUJA (2020):</text>
    <text x="30" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">• 3-Judge Bench OVERRULED S.R. Batra v. Taruna Batra.</text>
    <text x="30" y="260" fill="#4a5568" font-family="sans-serif" font-size="10">• Held: Shared household is NOT restricted to property</text>
    <text x="35" y="275" fill="#4a5568" font-family="sans-serif" font-size="10">owned/rented by husband; includes property of in-laws</text>
    <text x="35" y="290" fill="#4a5568" font-family="sans-serif" font-size="10">where woman lived in domestic relationship.</text>

    <rect x="20" y="320" width="300" height="40" rx="4" fill="#fff9ec"/>
    <text x="170" y="337" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Prabha Tyagi v. Kamlesh Devi (2022)</text>
    <text x="170" y="352" fill="#4a5568" font-family="sans-serif" font-size="9" text-anchor="middle">Subsequent past residence suffices; subsisting cohabitation not required</text>
  </g>

  <!-- Right: Protection Officers & Machinery -->
  <g transform="translate(420, 95)" filter="url(#shadow_dv2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">ENFORCEMENT MACHINERY</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 8: Protection Officers (PO)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Appointed by State Govt; preferably WOMEN.</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">• Shall be under control and supervision of Magistrate.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 9: Duties of Protection Officers</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">• Assist Magistrate in discharge of functions.</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Make Domestic Incident Report (DIR) to Magistrate.</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• Ensure legal aid, medical examination &amp; safe shelter.</text>

    <text x="20" y="200" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 10: Service Providers</text>
    <text x="25" y="220" fill="#4a5568" font-family="sans-serif" font-size="11">Voluntary associations/NGOs registered with State Govt;</text>
    <text x="25" y="235" fill="#4a5568" font-family="sans-serif" font-size="11">empowered to record DIR, get medical aid &amp; shelter.</text>

    <rect x="20" y="250" width="300" height="60" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="270" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">FEMALE RELATIVES AS RESPONDENTS:</text>
    <text x="30" y="290" fill="#4a5568" font-family="sans-serif" font-size="10">• Hiralal P. Harsora v. Kusum Narottamdas Harsora (2016):</text>
    <text x="35" y="303" fill="#4a5568" font-family="sans-serif" font-size="10">SC struck down "adult male person"; female relatives can</text>
    <text x="35" y="316" fill="#4a5568" font-family="sans-serif" font-size="10">also be named as respondents (mother-in-law, sister-in-law).</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Landmark: Hiralal Harsora (Female Respondents)</text>
  </g>
</svg>""",

    # 5. POSH 1
    "diag-soc-posh-complaint-inquiry.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_posh1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_posh1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_posh1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_posh1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">POSH ACT, 2013: COMPLAINT &amp; INQUIRY TIMELINE</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Internal &amp; Local Committee Inquiry Architecture • Strict Statutory Deadlines</text>

  <!-- Left: Complaint & Conciliation -->
  <g transform="translate(40, 95)" filter="url(#shadow_posh1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">COMPLAINT &amp; CONCILIATION</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 9: Filing of Complaint</text>
    <rect x="20" y="75" width="300" height="65" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="95" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LIMITATION PERIOD (S. 9(1)):</text>
    <text x="30" y="115" fill="#4a5568" font-family="sans-serif" font-size="10">• Within THREE (3) MONTHS from incident date.</text>
    <text x="30" y="130" fill="#4a5568" font-family="sans-serif" font-size="10">• IC/LC may extend by 3 MONTHS for sufficient cause.</text>

    <text x="20" y="160" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 10: Conciliation Mandate</text>
    <text x="25" y="180" fill="#4a5568" font-family="sans-serif" font-size="11">• At the request of aggrieved woman, IC/LC may take</text>
    <text x="25" y="195" fill="#4a5568" font-family="sans-serif" font-size="11">steps to settle matter through conciliation before inquiry.</text>
    <rect x="20" y="205" width="300" height="45" rx="4" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="223" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">ABSOLUTE BAR (SECTION 10(1) PROVISO):</text>
    <text x="30" y="238" fill="#4a5568" font-family="sans-serif" font-size="9.5">NO MONETARY SETTLEMENT shall be made basis of conciliation!</text>

    <text x="20" y="270" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 12: Interim Measures during Inquiry</text>
    <text x="25" y="290" fill="#4a5568" font-family="sans-serif" font-size="11">Transfer woman/respondent, grant leave up to 3 MONTHS</text>
    <text x="25" y="305" fill="#4a5568" font-family="sans-serif" font-size="11">(in addition to regular leaves), restrain reporting appraisal.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#fff9ec"/>
    <text x="170" y="353" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: No Money in Conciliation (S. 10(1))</text>
  </g>

  <!-- Right: Inquiry, Report & Penalties -->
  <g transform="translate(420, 95)" filter="url(#shadow_posh1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">INQUIRY, REPORT &amp; SECRECY</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 11: Inquiry Procedure</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Conducted under service rules; IC/LC possesses Civil Court</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">powers under CPC (summoning, discovery, oath).</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">• Inquiring period: MUST BE COMPLETED IN 90 DAYS.</text>

    <text x="20" y="135" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 13: Inquiry Report &amp; Action</text>
    <text x="25" y="155" fill="#4a5568" font-family="sans-serif" font-size="11">• Report to employer/District Officer within 10 DAYS.</text>
    <text x="25" y="170" fill="#4a5568" font-family="sans-serif" font-size="11">• Employer must act on recommendations within 60 DAYS.</text>

    <rect x="20" y="185" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="205" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 16: STRICT CONFIDENTIALITY:</text>
    <text x="30" y="225" fill="#4a5568" font-family="sans-serif" font-size="10">• Prohibition on publishing complaint, inquiry &amp; identity.</text>
    <text x="30" y="240" fill="#4a5568" font-family="sans-serif" font-size="10">• RTI Act 2005 EXCLUDED from disclosure.</text>
    <text x="30" y="253" fill="#4a5568" font-family="sans-serif" font-size="9.5">• Penalty under S. 17: Rs 5,000 fine for disclosure.</text>

    <text x="20" y="280" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 26: Penalties on Employer</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">Failure to constitute IC = Fine up to Rs 50,000.</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Repeat offence = Double fine &amp; cancellation of license.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Inquiry = 90 Days; Report = 10 Days</text>
  </g>
</svg>""",

    # 5. POSH 2
    "diag-soc-posh-ic-vs-lc.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_posh2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_posh2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_posh2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_posh2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">INTERNAL COMMITTEE (IC) VS LOCAL COMMITTEE (LC)</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 4 vs Section 6 • 10-Worker Threshold • 50% Women Representation Mandate</text>

  <!-- Left: Internal Committee -->
  <g transform="translate(40, 95)" filter="url(#shadow_posh2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">INTERNAL COMMITTEE (S. 4)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Threshold for Mandatory Constitution</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Every workplace employing TEN (10) OR MORE workers</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">must constitute an Internal Committee (IC) by order in writing.</text>

    <rect x="20" y="115" width="300" height="130" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="135" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">IC COMPOSITION (4 MEMBERS MINIMUM):</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">1. Presiding Officer: Senior level woman employee.</text>
    <text x="30" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">2. Employee Members: At least 2 employees committed</text>
    <text x="40" y="187" fill="#4a5568" font-family="sans-serif" font-size="10">to cause of women or having legal knowledge.</text>
    <text x="30" y="204" fill="#4a5568" font-family="sans-serif" font-size="10">3. External Member: From NGO or associations committed</text>
    <text x="40" y="219" fill="#4a5568" font-family="sans-serif" font-size="10">to women's cause or familiar with sexual harassment.</text>
    <text x="30" y="236" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">-> At least 50% of total members MUST BE WOMEN!</text>

    <text x="20" y="265" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Tenure &amp; Branches</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">Tenure: Up to 3 YEARS. Constituted at all administrative</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">units or offices where 10 or more workers employed.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#fff9ec"/>
    <text x="170" y="343" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Point: 50% Women + 1 External Member</text>
  </g>

  <!-- Right: Local Committee -->
  <g transform="translate(420, 95)" filter="url(#shadow_posh2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">LOCAL COMMITTEE (S. 6 &amp; 7)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Jurisdiction &amp; Purpose</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• For establishments with FEWER THAN 10 WORKERS.</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">• Where complaint is AGAINST THE EMPLOYER himself.</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">• Covers unorganized sector, domestic workers, daily wage.</text>

    <rect x="20" y="130" width="300" height="120" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="150" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">LC CONSTITUTION BY DISTRICT OFFICER (S. 7):</text>
    <text x="30" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">1. Chairperson: Eminent woman in social work.</text>
    <text x="30" y="187" fill="#4a5568" font-family="sans-serif" font-size="10">2. Local Woman: Working in block/taluk/ward.</text>
    <text x="30" y="204" fill="#4a5568" font-family="sans-serif" font-size="10">3. Two NGO Members (at least one SC/ST/OBC woman).</text>
    <text x="30" y="221" fill="#4a5568" font-family="sans-serif" font-size="10">4. Ex-Officio: Officer dealing with women/child dev.</text>
    <text x="30" y="238" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">-> District Officer is DM/ADM/Collector (Section 5).</text>

    <text x="20" y="265" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Nodal Officers (Section 6(2))</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">Designated in every rural/tribal block, tehsil, and ward</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">to receive complaints and forward to LC within 7 DAYS.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#edf7f4"/>
    <text x="170" y="343" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: If Complaint against Employer -> Goes to LC</text>
  </g>
</svg>""",

    # 6. PCPNDT 1
    "diag-soc-pcpndt-regulatory-architecture.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_pcp1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_pcp1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_pcp1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_pcp1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">PCPNDT ACT, 1994: REGULATORY ARCHITECTURE</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Supervisory Boards • Appropriate Authorities (S. 17) • Mandatory Registration (S. 18)</text>

  <!-- Left: Supervisory Boards & Policy -->
  <g transform="translate(40, 95)" filter="url(#shadow_pcp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">POLICY &amp; SUPERVISORY BOARDS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Central Supervisory Board (CSB, S. 7)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">• Chaired by Union Minister for Health &amp; Family Welfare.</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">• Meets at least once every SIX (6) MONTHS.</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">• Advises Central Govt on policy matters.</text>

    <text x="20" y="140" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• State Supervisory Boards (SSB, S. 16A)</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Chaired by State Minister for Health &amp; Family Welfare.</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• Meets at least once every FOUR (4) MONTHS.</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="11">• Oversees implementation by Appropriate Authorities.</text>

    <rect x="20" y="205" width="300" height="100" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="225" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 4 PERMISSIBLE TEST CONDITIONS:</text>
    <text x="30" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">Diagnostic techniques permitted ONLY for detecting:</text>
    <text x="30" y="260" fill="#4a5568" font-family="sans-serif" font-size="10">(i) Chromosomal abnormalities (ii) Genetic metabolic</text>
    <text x="30" y="275" fill="#4a5568" font-family="sans-serif" font-size="10">diseases (iii) Haemoglobinopathies (iv) Sex-linked disorders.</text>
    <text x="30" y="290" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">-> NEVER FOR DETERMINATION OF SEX!</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#fff9ec"/>
    <text x="170" y="343" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: CSB meets 6 months; SSB meets 4 months</text>
  </g>

  <!-- Right: Appropriate Authority & Enforcement -->
  <g transform="translate(420, 95)" filter="url(#shadow_pcp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">APPROPRIATE AUTHORITY (S. 17)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Constitution &amp; Levels (S. 17)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">State Govt appoints Appropriate Authority for whole State,</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">District (DM/CMO), or Sub-district levels.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Advisory Committee (Section 17(5))</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">3 medical experts, 1 legal expert, 1 social worker / NGO.</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">Aids Appropriate Authority in grant/cancellation of licenses.</text>

    <rect x="20" y="175" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="195" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SEARCH &amp; SEIZURE POWERS (SECTION 30):</text>
    <text x="30" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">• Enter and search any clinic, genetic lab, or vehicle.</text>
    <text x="30" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">• SEIZE ultrasound machines, records, registers, Form F.</text>
    <text x="30" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">• SEAL machines immediately upon detection of violation.</text>
    <text x="30" y="258" fill="#4a5568" font-family="sans-serif" font-size="9.5">• Civil Court powers under CPC under Section 17A.</text>

    <text x="20" y="285" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 28: Cognizance Safeguard</text>
    <text x="25" y="305" fill="#4a5568" font-family="sans-serif" font-size="11">Court takes cognizance ONLY on complaint by Appropriate</text>
    <text x="25" y="320" fill="#4a5568" font-family="sans-serif" font-size="11">Authority, or citizen giving 15 DAYS NOTICE to Authority.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Citizen Notice Period is 15 Days (S. 28)</text>
  </g>
</svg>""",

    # 6. PCPNDT 2
    "diag-soc-pcpndt-prohibited-conduct.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_pcp2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_pcp2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_pcp2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_pcp2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">PROHIBITED CONDUCT, PRESUMPTIONS &amp; PENALTIES</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 5 &amp; 6 Absolute Prohibitions • Section 23 Penalties • Section 24 Presumption</text>

  <!-- Left: Prohibitions & Form F -->
  <g transform="translate(40, 95)" filter="url(#shadow_pcp2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PROHIBITIONS &amp; MANDATORY FORM F</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5(2): Communication of Sex Ban</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">No person conducting pre-natal diagnostic procedures shall</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">communicate to pregnant woman or relatives the SEX OF FOETUS</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">by words, signs or in any other manner whatsoever.</text>

    <text x="20" y="140" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 6: Pre-Conception Sex Selection</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">Total prohibition on sex selection before or after conception.</text>

    <rect x="20" y="180" width="300" height="95" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="200" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">MANDATORY STATUTORY FORM F (S. 29):</text>
    <text x="30" y="220" fill="#4a5568" font-family="sans-serif" font-size="10">• Every ultrasound scan must be recorded in Form F.</text>
    <text x="30" y="235" fill="#4a5568" font-family="sans-serif" font-size="10">• Incomplete or inaccurate Form F creates presumption of guilt!</text>
    <text x="30" y="250" fill="#4a5568" font-family="sans-serif" font-size="10">• All records must be preserved for minimum TWO (2) YEARS.</text>
    <text x="30" y="265" fill="#4a5568" font-family="sans-serif" font-size="10">• Voluntary Health Association v. UOI strict compliance.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 22: Ban on Advertisements</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Any advertisement relating to sex determination facilities =</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">Imprisonment up to 3 years and fine up to Rs 10,000.</text>

    <rect x="20" y="342" width="300" height="24" rx="4" fill="#fff9ec"/>
    <text x="170" y="358" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Record Retention is Exactly 2 Years</text>
  </g>

  <!-- Right: Penalties & Section 24 Presumption -->
  <g transform="translate(420, 95)" filter="url(#shadow_pcp2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PENALTIES &amp; REVERSE BURDEN</text>
    
    <rect x="20" y="55" width="300" height="110" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="75" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 23: GRADED PENALTIES (DOCTOR):</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• First Conviction: Imprisonment up to THREE (3) YEARS,</text>
    <text x="35" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">and fine up to TEN THOUSAND (Rs 10,000) RUPEES.</text>
    <text x="30" y="127" fill="#4a5568" font-family="sans-serif" font-size="10">• Subsequent Conviction: Imprisonment up to FIVE (5) YEARS,</text>
    <text x="35" y="142" fill="#4a5568" font-family="sans-serif" font-size="10">and fine up to FIFTY THOUSAND (Rs 50,000) RUPEES.</text>
    <text x="30" y="157" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">• Medical Council strikes off name (5 yrs / permanent).</text>

    <text x="20" y="185" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Penalty on Husband / Relatives (S. 23(3))</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">Husband or relative seeking sex selection = Imprisonment up to</text>
    <text x="25" y="220" fill="#4a5568" font-family="sans-serif" font-size="11">3 years &amp; fine up to Rs 50,000 (subsequent: 5 yrs &amp; 1 Lakh).</text>

    <rect x="20" y="235" width="300" height="90" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="255" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 24: STATUTORY PRESUMPTION:</text>
    <text x="30" y="275" fill="#4a5568" font-family="sans-serif" font-size="10">• Court SHALL PRESUME that pregnant woman was compelled</text>
    <text x="35" y="290" fill="#4a5568" font-family="sans-serif" font-size="10">by her husband or relatives to undergo sex selection!</text>
    <text x="30" y="307" fill="#4a5568" font-family="sans-serif" font-size="10">• Woman is presumed innocent unless contrary proved.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Pregnant Woman Presumed Compelled (S. 24)</text>
  </g>
</svg>""",

    # 7. MTP 1
    "diag-soc-mtp-gestational-framework.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_mtp1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_mtp1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_mtp1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_mtp1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">MEDICAL TERMINATION OF PREGNANCY ACT (MTP ACT)</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">2021 Gestational Tier Paradigm • RMP Opinions • State Medical Board Certification</text>

  <!-- Left: Gestational Tiers -->
  <g transform="translate(40, 95)" filter="url(#shadow_mtp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">STATUTORY GESTATIONAL TIERS</text>
    
    <rect x="20" y="55" width="300" height="70" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="75" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">TIER 1: UP TO 20 WEEKS (S. 3(2)(a)):</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• Requires opinion of ONE (1) Registered Medical Practitioner.</text>
    <text x="30" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">• Grounds: Risk to life, grave injury to physical/mental health,</text>
    <text x="35" y="122" fill="#4a5568" font-family="sans-serif" font-size="9.5">or contraceptive failure (married or unmarried woman).</text>

    <rect x="20" y="135" width="300" height="95" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="155" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">TIER 2: 20 TO 24 WEEKS (S. 3(2)(b)):</text>
    <text x="30" y="175" fill="#4a5568" font-family="sans-serif" font-size="10">• Requires opinion of TWO (2) Medical Practitioners.</text>
    <text x="30" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">• Applicable ONLY to prescribed vulnerable categories:</text>
    <text x="35" y="205" fill="#4a5568" font-family="sans-serif" font-size="9.5">Survivors of rape/incest, minors, change of marital status</text>
    <text x="35" y="218" fill="#4a5568" font-family="sans-serif" font-size="9.5">during pregnancy, women with disabilities, emergencies.</text>

    <rect x="20" y="240" width="300" height="80" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="260" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">TIER 3: BEYOND 24 WEEKS (S. 3(2B)):</text>
    <text x="30" y="280" fill="#4a5568" font-family="sans-serif" font-size="10">• NO GESTATIONAL CEILING if substantial foetal abnormalities!</text>
    <text x="30" y="295" fill="#4a5568" font-family="sans-serif" font-size="10">• Mandatory permission by STATE MEDICAL BOARD</text>
    <text x="35" y="310" fill="#4a5568" font-family="sans-serif" font-size="9.5">(Gynaecologist, Paediatrician, Radiologist/Sonologist).</text>

    <rect x="20" y="330" width="300" height="32" rx="4" fill="#edf7f4"/>
    <text x="170" y="350" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: 20 Wks = 1 RMP; 24 Wks = 2 RMPs</text>
  </g>

  <!-- Right: Emergency & Landmark Law -->
  <g transform="translate(420, 95)" filter="url(#shadow_mtp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">EMERGENCY &amp; REPRODUCTIVE RIGHTS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5: Emergency Life-Saving Exception</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Where termination is immediately necessary to save the</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">LIFE OF THE PREGNANT WOMAN:</text>
    <text x="30" y="117" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">• Section 3 gestational limits DO NOT APPLY.</text>
    <text x="30" y="132" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">• Section 4 approved place requirement DOES NOT APPLY.</text>
    <text x="30" y="147" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold">• Single RMP can perform termination at ANY place.</text>

    <rect x="20" y="160" width="300" height="95" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="180" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">LANDMARK: X V. PRINCIPAL SECRETARY (2022):</text>
    <text x="30" y="200" fill="#4a5568" font-family="sans-serif" font-size="10">• Supreme Court Bench led by CJI D.Y. Chandrachud.</text>
    <text x="30" y="215" fill="#4a5568" font-family="sans-serif" font-size="10">• Held: Distinguishing between married and UNMARRIED</text>
    <text x="35" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">women violates Article 14. Unmarried women included</text>
    <text x="35" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">in 20-24 week window for contraceptive failure.</text>

    <text x="20" y="275" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 4: Approved Places</text>
    <text x="25" y="295" fill="#4a5568" font-family="sans-serif" font-size="11">Termination allowed only at government hospitals or places</text>
    <text x="25" y="310" fill="#4a5568" font-family="sans-serif" font-size="11">approved by District Level Committee under CMO.</text>

    <rect x="20" y="330" width="300" height="32" rx="4" fill="#fff9ec"/>
    <text x="170" y="350" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Landmark: X v. Principal Secy (Unmarried Equality)</text>
  </g>
</svg>""",

    # 7. MTP 2
    "diag-soc-mtp-consent-medical-board.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_mtp2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_mtp2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_mtp2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_mtp2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">MTP ACT: CONSENT REGIME &amp; PRIVACY SAFEGUARDS</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 3(4) Sole Consent • Guardian Exceptions • Section 5A Identity Protection</text>

  <!-- Left: Consent Architecture -->
  <g transform="translate(40, 95)" filter="url(#shadow_mtp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SECTION 3(4) CONSENT ARCHITECTURE</text>
    
    <rect x="20" y="55" width="300" height="85" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="75" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">GENERAL RULE (SECTION 3(4)(b)):</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• SOLE CONSENT of pregnant woman (adult) is mandatory.</text>
    <text x="30" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">• NO SPOUSAL CONSENT required under law!</text>
    <text x="30" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">• Husband/in-laws CANNOT veto or force termination.</text>

    <rect x="20" y="150" width="300" height="95" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="170" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">EXCEPTIONS (SECTION 3(4)(a)):</text>
    <text x="30" y="190" fill="#4a5568" font-family="sans-serif" font-size="10">Written consent of GUARDIAN is required ONLY IF:</text>
    <text x="35" y="207" fill="#4a5568" font-family="sans-serif" font-size="10">1. Pregnant woman has NOT attained age of 18 YEARS (Minor).</text>
    <text x="35" y="224" fill="#4a5568" font-family="sans-serif" font-size="10">2. Pregnant woman is a MENTALLY ILL PERSON</text>
    <text x="40" y="238" fill="#4a5568" font-family="sans-serif" font-size="9.5">(mental illness as defined in Mental Healthcare Act, 2017).</text>

    <text x="20" y="265" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Suchita Srivastava v. Chandigarh Admn (2009)</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">Reproductive autonomy is an integral part of personal liberty</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">under Article 21; State cannot force termination on woman.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#edf7f4"/>
    <text x="170" y="343" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: No Husband Consent Required for Adult Wife</text>
  </g>

  <!-- Right: Confidentiality & Penalties -->
  <g transform="translate(420, 95)" filter="url(#shadow_mtp1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">CONFIDENTIALITY &amp; PENALTIES</text>
    
    <rect x="20" y="55" width="300" height="110" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="75" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 5A: PRIVACY OF WOMAN PROTECTED:</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• NO registered medical practitioner shall reveal name</text>
    <text x="35" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">and other particulars of a woman whose pregnancy has</text>
    <text x="35" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">been terminated, except to authorized person by law.</text>
    <text x="30" y="142" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">• PENALTY: Imprisonment up to ONE (1) YEAR, or fine, or both.</text>

    <text x="20" y="185" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5(2) Unlawful Termination</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">Termination by person who is NOT an RMP = Punishable</text>
    <text x="25" y="220" fill="#4a5568" font-family="sans-serif" font-size="11">with Rigorous Imprisonment 2 to 7 YEARS under IPC/BNS.</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 5(3) Unapproved Place</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Termination at unapproved place = Rigorous Imprisonment</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="11">for 2 to 7 YEARS for doctor / owner of clinic.</text>

    <text x="20" y="305" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 7: Regulations &amp; Admission Register</text>
    <text x="25" y="325" fill="#4a5568" font-family="sans-serif" font-size="11">Admission register kept under strict lock and key in hospital.</text>

    <rect x="20" y="335" width="300" height="28" rx="4" fill="#edf7f4"/>
    <text x="170" y="353" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Section 5A Breach = 1 Year Imprisonment</text>
  </g>
</svg>""",

    # 8. IRWA 1
    "diag-soc-irwa-prohibitions-exceptions.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_irwa1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_irwa1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_irwa1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_irwa1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">INDECENT REPRESENTATION OF WOMEN ACT, 1986</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 3 &amp; 4 Core Prohibitions • Section 4 Statutory Exceptions • Digital Convergence</text>

  <!-- Left: Core Prohibitions -->
  <g transform="translate(40, 95)" filter="url(#shadow_irwa1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">CORE PROHIBITIONS (S. 3 &amp; 4)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 2(c): Indecent Representation</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Depiction in any manner of the figure of a woman, her form</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">or body which has effect of being INDECENT, DEROGATORY,</text>
    <text x="25" y="115" fill="#4a5568" font-family="sans-serif" font-size="11">or is likely to deprave, corrupt or injure public morality.</text>

    <rect x="20" y="130" width="300" height="75" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="150" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 3: ADVERTISEMENTS BAN:</text>
    <text x="30" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">• Absolute ban on publishing or causing to be published</text>
    <text x="35" y="185" fill="#4a5568" font-family="sans-serif" font-size="10">any advertisement containing indecent representation.</text>
    <text x="30" y="198" fill="#4a5568" font-family="sans-serif" font-size="9.5">• Applies to notice, circular, label, wrapper, or visual.</text>

    <text x="20" y="225" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 4: Publications &amp; Distribution Ban</text>
    <text x="25" y="245" fill="#4a5568" font-family="sans-serif" font-size="11">No person shall produce or cause to be produced, sell,</text>
    <text x="25" y="260" fill="#4a5568" font-family="sans-serif" font-size="11">let to hire, distribute, circulate, or send by post any</text>
    <text x="25" y="275" fill="#4a5568" font-family="sans-serif" font-size="11">book, pamphlet, paper, slide, film, writing, drawing or figure.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#edf7f4"/>
    <text x="170" y="343" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Focus: S. 3 Advertisements vs S. 4 Books/Films</text>
  </g>

  <!-- Right: Statutory Exceptions -->
  <g transform="translate(420, 95)" filter="url(#shadow_irwa1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">STATUTORY EXCEPTIONS (S. 4)</text>
    
    <rect x="20" y="55" width="300" height="135" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="75" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 4 PROVISO: EXEMPTED CATEGORIES:</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">Nothing in Section 4 shall apply to:</text>
    <text x="30" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">(a) Any book, pamphlet, etc. justified in the PUBLIC GOOD</text>
    <text x="40" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">as being in interest of science, literature, art or learning.</text>
    <text x="30" y="142" fill="#4a5568" font-family="sans-serif" font-size="10">(b) Any publication kept or used bona fide for RELIGIOUS purposes.</text>
    <text x="30" y="159" fill="#4a5568" font-family="sans-serif" font-size="10">(c) Any sculpture, engraving or painting in any TEMPLE or car</text>
    <text x="40" y="174" fill="#4a5568" font-family="sans-serif" font-size="10">used for conveyance of idols, or ANCIENT MONUMENT.</text>

    <text x="20" y="205" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Certified Films Exception (S. 4 Proviso (ii))</text>
    <text x="25" y="225" fill="#4a5568" font-family="sans-serif" font-size="11">Films certified under Part II of CINEMATOGRAPH ACT, 1952</text>
    <text x="25" y="240" fill="#4a5568" font-family="sans-serif" font-size="11">are completely exempted from prosecution under Section 4.</text>

    <text x="20" y="265" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Digital Convergence (IT Act 2000 Interface)</text>
    <text x="25" y="285" fill="#4a5568" font-family="sans-serif" font-size="11">Applies concurrently with Section 67 (Obscenity in electronic</text>
    <text x="25" y="300" fill="#4a5568" font-family="sans-serif" font-size="11">form) and Section 67A of the Information Technology Act.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#fff9ec"/>
    <text x="170" y="343" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Point: Ancient Monuments &amp; Temples Exempt</text>
  </g>
</svg>""",

    # 8. IRWA 2
    "diag-soc-irwa-enforcement-powers.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_irwa2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_irwa2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_irwa2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_irwa2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">IRWA 1986: ENFORCEMENT, POWERS &amp; PENALTIES</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 5 Search &amp; Seizure • Section 6 Graded Penalties • Section 8 Cognizable &amp; Bailable</text>

  <!-- Left: Section 5 Search & Seizure -->
  <g transform="translate(40, 95)" filter="url(#shadow_irwa2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SEARCH &amp; SEIZURE (SECTION 5)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Authorized Officer (Section 5(1))</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Any GAZETTED OFFICER authorized by the State Govt</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">may exercise powers within local limits of his jurisdiction.</text>

    <rect x="20" y="115" width="300" height="110" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="135" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">POWERS OF GAZETTED OFFICER (S. 5):</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">1. Enter &amp; search any place where offence suspected.</text>
    <text x="30" y="172" fill="#4a5568" font-family="sans-serif" font-size="10">2. Seize any advertisement or book/pamphlet/film.</text>
    <text x="30" y="189" fill="#4a5568" font-family="sans-serif" font-size="10">3. Examine any record, register or document.</text>
    <text x="30" y="206" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">-> PRIVATE DWELLING: Search requires WARRANT!</text>

    <text x="20" y="245" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Seizure Intimation to Magistrate</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">Officer seizing any article MUST inform the nearest</text>
    <text x="25" y="280" fill="#4a5568" font-family="sans-serif" font-size="11">Magistrate and take his orders as to custody.</text>

    <text x="20" y="305" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• CrPC Search Provisions Apply (S. 5(2))</text>
    <text x="25" y="325" fill="#4a5568" font-family="sans-serif" font-size="11">Provisions of CrPC relating to search &amp; seizure apply.</text>

    <rect x="20" y="342" width="300" height="24" rx="4" fill="#fff9ec"/>
    <text x="170" y="358" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Private Dwelling Search Needs Warrant</text>
  </g>

  <!-- Right: Section 6 Penalties & Section 8 -->
  <g transform="translate(420, 95)" filter="url(#shadow_irwa2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SECTION 6 GRADED PENALTIES</text>
    
    <rect x="20" y="55" width="300" height="115" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="75" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">STATUTORY PENALTIES (SECTION 6):</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• FIRST CONVICTION:</text>
    <text x="35" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">Imprisonment up to TWO (2) YEARS,</text>
    <text x="35" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">and fine up to TWO THOUSAND (Rs 2,000) RUPEES.</text>
    <text x="30" y="142" fill="#4a5568" font-family="sans-serif" font-size="10">• SECOND OR SUBSEQUENT CONVICTION:</text>
    <text x="35" y="157" fill="#4a5568" font-family="sans-serif" font-size="10">Imprisonment MINIMUM 6 MONTHS up to 5 YEARS,</text>
    <text x="35" y="169" fill="#4a5568" font-family="sans-serif" font-size="9.5">and fine Rs 10,000 to Rs 1,00,000.</text>

    <text x="20" y="185" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 7: Offences by Companies</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">Company as well as every person in charge and responsible</text>
    <text x="25" y="220" fill="#4a5568" font-family="sans-serif" font-size="11">to the company deemed guilty unless lack of knowledge proved.</text>

    <rect x="20" y="235" width="300" height="65" rx="6" fill="#edf7f4" stroke="#137d72" stroke-width="1"/>
    <text x="30" y="255" fill="#137d72" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 8: CLASSIFICATION OF OFFENCES:</text>
    <text x="30" y="275" fill="#4a5568" font-family="sans-serif" font-size="10">• Offence under this Act is COGNIZABLE.</text>
    <text x="30" y="290" fill="#4a5568" font-family="sans-serif" font-size="10">• Offence under this Act is BAILABLE.</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#fff9ec"/>
    <text x="170" y="343" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: IRWA Offences are Cognizable but BAILABLE</text>
  </g>
</svg>""",

    # 9. POCSO 1
    "diag-soc-pocso-protection-framework.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_poc1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_poc1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_poc1)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_poc1)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">POCSO ACT, 2012: SUBSTANTIVE OFFENCES &amp; PENALTIES</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Gender-Neutral Child Definition (S. 2(1)(d)) • Graded Punishments • 2019 Capital Punishment</text>

  <!-- Left: Penetrative Offences -->
  <g transform="translate(40, 95)" filter="url(#shadow_poc1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">PENETRATIVE OFFENCES (S. 3–6)</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 2(1)(d): Definition of 'Child'</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Any person below EIGHTEEN (18) YEARS of age.</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">Act is completely GENDER-NEUTRAL as to victim child.</text>

    <rect x="20" y="115" width="300" height="65" rx="6" fill="#fff9ec" stroke="#dfbf80" stroke-width="1"/>
    <text x="30" y="135" fill="#b98a38" font-family="sans-serif" font-size="11" font-weight="bold">PENETRATIVE SEXUAL ASSAULT (S. 3 &amp; 4):</text>
    <text x="30" y="155" fill="#4a5568" font-family="sans-serif" font-size="10">• Rigorous Imprisonment: MINIMUM 10 YEARS up to LIFE.</text>
    <text x="30" y="170" fill="#4a5568" font-family="sans-serif" font-size="10">• Liable to fine (paid to victim child as relief).</text>

    <rect x="20" y="190" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="210" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">AGGRAVATED PENETRATIVE ASSAULT (S. 5 &amp; 6):</text>
    <text x="30" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">• By police, armed forces, doctor, teacher, guardian,</text>
    <text x="35" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">or on child under 12/16 years, or causing grievous hurt.</text>
    <text x="30" y="260" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">• PUNISHMENT (Post-2019): MINIMUM 20 YEARS</text>
    <text x="35" y="275" fill="#a63b49" font-family="sans-serif" font-size="10" font-weight="bold">up to IMPRISONMENT FOR LIFE (natural life) OR DEATH!</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#edf7f4"/>
    <text x="170" y="343" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Point: Death Penalty Added via 2019 Amendment</text>
  </g>

  <!-- Right: Sexual Assault, Harassment & Pornography -->
  <g transform="translate(420, 95)" filter="url(#shadow_poc1)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">ASSAULT, HARASSMENT &amp; DIGITAL</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Sexual Assault (Sections 7 &amp; 8)</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Touching private parts with sexual intent (non-penetrative).</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">Punishment: Imprisonment MINIMUM 3 YEARS up to 5 YEARS + fine.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Aggravated Sexual Assault (Sections 9 &amp; 10)</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">Punishment: Imprisonment MINIMUM 5 YEARS up to 7 YEARS + fine.</text>

    <text x="20" y="170" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Sexual Harassment (Sections 11 &amp; 12)</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="11">Uttering sexually explicit words, gestures, stalking, flashes.</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">Punishment: Imprisonment up to THREE (3) YEARS + fine.</text>

    <rect x="20" y="220" width="300" height="95" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="240" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">CHILD PORNOGRAPHY (SECTIONS 13–15):</text>
    <text x="30" y="260" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 14 Using child for porn: Min 5 yrs up to 7 yrs + fine.</text>
    <text x="30" y="275" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 15 Storage of pornographic material involving child:</text>
    <text x="35" y="290" fill="#4a5568" font-family="sans-serif" font-size="10">Fine; if stored for commercial purpose = 3 to 5 yrs.</text>
    <text x="30" y="305" fill="#a63b49" font-family="sans-serif" font-size="9.5">• Failure to delete/report child porn is an offence (2019).</text>

    <rect x="20" y="325" width="300" height="38" rx="4" fill="#fff9ec"/>
    <text x="170" y="343" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Skin-to-Skin Overruled in Attorney General (2021)</text>
  </g>
</svg>""",

    # 9. POCSO 2
    "diag-soc-pocso-special-court-trial.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_poc2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c46"/>
      <stop offset="100%" stop-color="#1b3857"/>
    </linearGradient>
    <filter id="shadow_poc2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="12" fill="url(#bg_poc2)"/>
  <rect x="30" y="20" width="740" height="55" rx="8" fill="#137d72" filter="url(#shadow_poc2)"/>
  <text x="400" y="46" fill="#ffffff" font-family="Georgia, serif" font-size="18" font-weight="bold" text-anchor="middle">POCSO ACT: REPORTING, SPECIAL COURTS &amp; PRESUMPTIONS</text>
  <text x="400" y="64" fill="#dfbf80" font-family="sans-serif" font-size="11" text-anchor="middle">Section 19 Mandatory Reporting • Section 35 Timelines • S. 29 &amp; 30 Reverse Burdens</text>

  <!-- Left: Reporting & Investigation -->
  <g transform="translate(40, 95)" filter="url(#shadow_poc2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#142c46"/>
    <text x="170" y="27" fill="#dfbf80" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">MANDATORY REPORTING &amp; SJPU</text>
    
    <rect x="20" y="55" width="300" height="85" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="75" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">SECTION 19: MANDATORY REPORTING:</text>
    <text x="30" y="95" fill="#4a5568" font-family="sans-serif" font-size="10">• ANY person having apprehension/knowledge must report.</text>
    <text x="30" y="110" fill="#4a5568" font-family="sans-serif" font-size="10">• Section 21 Penalty for failure to report: Up to 6 MONTHS</text>
    <text x="35" y="125" fill="#4a5568" font-family="sans-serif" font-size="10">imprisonment/fine; In-charge of institution up to 1 YEAR.</text>
    <text x="30" y="137" fill="#137d72" font-family="sans-serif" font-size="9.5" font-weight="bold">• S. 19(7): Person reporting in good faith incurs NO liability.</text>

    <text x="20" y="155" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 24: Child-Friendly Investigation</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• Special Juvenile Police Unit (SJPU) or Women Police.</text>
    <text x="25" y="190" fill="#4a5568" font-family="sans-serif" font-size="11">• Statement recorded at child's residence; NO POLICE UNIFORM.</text>
    <text x="25" y="205" fill="#4a5568" font-family="sans-serif" font-size="11">• Child shall NEVER be detained at police station at night.</text>

    <text x="20" y="230" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 27: Medical Examination</text>
    <text x="25" y="250" fill="#4a5568" font-family="sans-serif" font-size="11">Conducted in presence of parent; if victim girl child,</text>
    <text x="25" y="265" fill="#4a5568" font-family="sans-serif" font-size="11">conducted EXCLUSIVELY BY WOMAN DOCTOR.</text>

    <rect x="20" y="285" width="300" height="75" rx="4" fill="#edf7f4"/>
    <text x="170" y="305" fill="#137d72" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">SECTION 35 STATUTORY TIMELINES</text>
    <text x="170" y="325" fill="#4a5568" font-family="sans-serif" font-size="10" text-anchor="middle">• Evidence of child recorded within THIRTY (30) DAYS.</text>
    <text x="170" y="342" fill="#4a5568" font-family="sans-serif" font-size="10" text-anchor="middle">• Trial completed within ONE (1) YEAR of taking cognizance.</text>
  </g>

  <!-- Right: Special Court & Presumptions -->
  <g transform="translate(420, 95)" filter="url(#shadow_poc2)">
    <rect width="340" height="375" rx="8" fill="#fbf8f2"/>
    <rect width="340" height="42" rx="8" fill="#137d72"/>
    <text x="170" y="27" fill="#ffffff" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">SPECIAL COURT &amp; PRESUMPTIONS</text>
    
    <text x="20" y="65" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 28 &amp; 33: Special Court</text>
    <text x="25" y="85" fill="#4a5568" font-family="sans-serif" font-size="11">Court of Session designated as Special Court;</text>
    <text x="25" y="100" fill="#4a5568" font-family="sans-serif" font-size="11">can take cognizance WITHOUT committal by Magistrate.</text>

    <text x="20" y="125" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 33 &amp; 36: Trial Environment</text>
    <text x="25" y="145" fill="#4a5568" font-family="sans-serif" font-size="11">• Child not exposed to accused (video link / single-way mirror).</text>
    <text x="25" y="160" fill="#4a5568" font-family="sans-serif" font-size="11">• Questions put to child ONLY through the Special Judge.</text>
    <text x="25" y="175" fill="#4a5568" font-family="sans-serif" font-size="11">• Frequent breaks allowed; in-camera trial (Section 37).</text>

    <rect x="20" y="190" width="300" height="85" rx="6" fill="#fff5f5" stroke="#a63b49" stroke-width="1"/>
    <text x="30" y="210" fill="#a63b49" font-family="sans-serif" font-size="11" font-weight="bold">STATUTORY REVERSE BURDENS (S. 29 &amp; 30):</text>
    <text x="30" y="230" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 29: Special Court SHALL PRESUME that accused</text>
    <text x="35" y="245" fill="#4a5568" font-family="sans-serif" font-size="10">committed offence under S. 3, 5, 7 or 9 unless contrary proved.</text>
    <text x="30" y="260" fill="#4a5568" font-family="sans-serif" font-size="10">• S. 30: Presumption of CULPABLE MENTAL STATE.</text>

    <text x="20" y="295" fill="#142c46" font-family="sans-serif" font-size="12" font-weight="bold">• Section 42A: Overriding Effect</text>
    <text x="25" y="315" fill="#4a5568" font-family="sans-serif" font-size="11">Provisions of POCSO Act shall have effect notwithstanding</text>
    <text x="25" y="330" fill="#4a5568" font-family="sans-serif" font-size="11">anything inconsistent contained in any other law.</text>

    <rect x="20" y="342" width="300" height="24" rx="4" fill="#fff9ec"/>
    <text x="170" y="358" fill="#b98a38" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">UP PCS-J Trap: Special Court Takes Direct Cognizance (S. 33)</text>
  </g>
</svg>"""
}

def main():
    target_dir = "assets/learning/images/diagrams"
    os.makedirs(target_dir, exist_ok=True)
    created = 0
    for filename, content in DIAGRAMS.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created {filename}")
        created += 1
    print(f"SUCCESS: Created exactly {created} SVG diagrams in {target_dir}!")

if __name__ == "__main__":
    main()
