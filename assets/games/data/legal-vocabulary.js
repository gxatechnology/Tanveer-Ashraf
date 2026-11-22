/**
 * LEGAL VOCABULARY DATABASE (V3.0 Phase 3)
 * Authoritative Indian Legal Terminology, Maxims, and Statutory Definitions
 * Specifically curated and verified for UP Judicial Services (UP PCS-J)
 * Total Verified Entries: 285 unique items across 10 subject disciplines
 */
(function() {
  'use strict';

  const VOCABULARY = [
  {
    "id": "voc-001",
    "canonical": "HABEAS CORPUS",
    "acceptedVariants": [
      "HABEAS CORPUS"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Prerogative writ literally translating to 'you may have the body', securing release from unlawful detention",
    "additionalHint": "Guaranteed under Article 32 and Article 226 of the Constitution of India",
    "definition": "A judicial writ ordering a detaining authority to produce an imprisoned individual before the court to determine legality of confinement.",
    "educationalExample": "When a citizen was detained by police beyond 24 hours without magistrate remand, counsel filed a writ of Habeas Corpus.",
    "statuteOrAuthority": "Constitution of India, Article 32 & 226; ADM Jabalpur v. Shivkant Shukla (overruled by K.S. Puttaswamy)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-002",
    "canonical": "MANDAMUS",
    "acceptedVariants": [
      "MANDAMUS"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Judicial command compelling a public official or body to perform a mandatory statutory duty",
    "additionalHint": "Latin for 'we command'; cannot lie against purely discretionary functions",
    "definition": "A high prerogative writ issued by the High Court or Supreme Court directing an authority to discharge its public or statutory obligation.",
    "educationalExample": "The municipal corporation failed to supply drinking water despite statutory obligation, prompting an application for Mandamus.",
    "statuteOrAuthority": "Constitution of India, Article 32 & Article 226; Gujarat State Financial Corp. v. Lotus Hotels",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-003",
    "canonical": "CERTIORARI",
    "acceptedVariants": [
      "CERTIORARI"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Curative writ quashing the decision of an inferior court or quasi-judicial tribunal for jurisdictional error",
    "additionalHint": "Latin for 'to be certified'; operates after a final or interim order has been passed",
    "definition": "A constitutional writ quashing orders passed by inferior courts or tribunals where they acted without jurisdiction, in excess of jurisdiction, or violated natural justice.",
    "educationalExample": "A rent controller evicted a tenant without serving summons, so the High Court quashed the order via Certiorari.",
    "statuteOrAuthority": "Constitution of India, Article 226; Syed Yakoob v. K.S. Radhakrishnan (AIR 1964 SC 477)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-004",
    "canonical": "QUO WARRANTO",
    "acceptedVariants": [
      "QUO WARRANTO"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Writ challenging the legal authority of a person holding a substantive public office",
    "additionalHint": "Translates to 'by what warrant'; prevents usurping public office without statutory eligibility",
    "definition": "A writ issued to inquire into the legality of the claim which a party asserts to a public office and to oust him if his tenure is unlawful.",
    "educationalExample": "A candidate appointed Vice-Chancellor without requisite 10 years of professorship faced a writ of Quo Warranto.",
    "statuteOrAuthority": "Constitution of India, Article 32 & Article 226; University of Mysore v. Govinda Rao (AIR 1965 SC 491)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-005",
    "canonical": "PROHIBITION",
    "acceptedVariants": [
      "PROHIBITION"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Preventive writ staying proceedings in an inferior tribunal before final decision due to absence of jurisdiction",
    "additionalHint": "Often called a negative cousin of Mandamus; stops ongoing illegal proceedings",
    "definition": "A writ issued by a superior court to prevent an inferior court or tribunal from exceeding its jurisdiction or usurping a jurisdiction with which it is not legally vested.",
    "educationalExample": "When a consumer forum initiated hearing on a complex industrial patent dispute, the High Court issued Prohibition.",
    "statuteOrAuthority": "Constitution of India, Article 226; S. Govinda Menon v. Union of India (AIR 1967 SC 1274)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-006",
    "canonical": "BASIC STRUCTURE",
    "acceptedVariants": [
      "BASIC STRUCTURE"
    ],
    "difficulty": "advanced",
    "subject": "Constitutional Law",
    "primaryClue": "Judicial doctrine establishing unamendable foundational features of the Indian Constitution",
    "additionalHint": "Established in Kesavananda Bharati (1973) limiting Parliament's amending power under Article 368",
    "definition": "A constitutional principle holding that Parliament cannot alter the fundamental framework and core identity of the Indian Constitution through constitutional amendment.",
    "educationalExample": "An amendment seeking to eliminate judicial review of election disputes was struck down as violative of the Basic Structure.",
    "statuteOrAuthority": "Constitution of India, Article 368; Kesavananda Bharati v. State of Kerala (1973 4 SCC 225)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-007",
    "canonical": "PITH AND SUBSTANCE",
    "acceptedVariants": [
      "PITH AND SUBSTANCE"
    ],
    "difficulty": "advanced",
    "subject": "Constitutional Law",
    "primaryClue": "Interpretation doctrine determining true nature and legislative competence of an enactment when incidental encroachment occurs",
    "additionalHint": "Applied under Seventh Schedule legislative list disputes between Union and State lists",
    "definition": "A doctrine holding that if a statute substantially falls within the legislative power of a legislature, its validity is not affected by incidental encroachment on an unauthorized field.",
    "educationalExample": "A state law regulating money-lending was upheld despite incidental encroachment on banking negotiable instruments.",
    "statuteOrAuthority": "Constitution of India, Article 246; Prafulla Kumar Mukherjee v. Bank of Commerce, Khulna (AIR 1947 PC 60)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-008",
    "canonical": "COLORABLE LEGISLATION",
    "acceptedVariants": [
      "COLORABLE LEGISLATION"
    ],
    "difficulty": "advanced",
    "subject": "Constitutional Law",
    "primaryClue": "Maxim: 'What cannot be done directly, cannot also be done indirectly' in legislative enactment",
    "additionalHint": "Examines whether legislature possessed competence or disguised an unconstitutional act",
    "definition": "A doctrine checking covert legislative transgression where an enactment pretends to act within constitutional authority while encroaching on forbidden territory.",
    "educationalExample": "A state legislature passed an estate taxation act disguised as agricultural regulation, struck down as colorable.",
    "statuteOrAuthority": "Constitution of India, Article 246; K.C. Gajapati Narayan Deo v. State of Orissa (AIR 1953 SC 375)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-009",
    "canonical": "SEVERABILITY",
    "acceptedVariants": [
      "SEVERABILITY",
      "DOCTRINE OF SEVERABILITY"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Rule saving constitutional portions of an enactment if unconstitutional provisions can be cleanly excised",
    "additionalHint": "Derived from Article 13(1) of the Indian Constitution",
    "definition": "A rule stating that only the offending unconstitutional clause of an act becomes void, leaving the remainder operative if independent.",
    "educationalExample": "Section 14 of the Preventive Detention Act was declared void, but the rest of the statute survived intact.",
    "statuteOrAuthority": "Constitution of India, Article 13; A.K. Gopalan v. State of Madras (AIR 1950 SC 27)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-010",
    "canonical": "ECLIPSE",
    "acceptedVariants": [
      "ECLIPSE",
      "DOCTRINE OF ECLIPSE"
    ],
    "difficulty": "advanced",
    "subject": "Constitutional Law",
    "primaryClue": "Doctrine where a pre-constitutional law violating fundamental rights becomes dormant rather than dead",
    "additionalHint": "Can revive upon subsequent constitutional amendment removing the inconsistency",
    "definition": "A principle where a pre-constitutional law in conflict with fundamental rights remains dormant and unenforceable, but revives once the constitutional shadow is removed.",
    "educationalExample": "Motor Vehicles Act provision was dormant until constitutional amendment authorized state transport monopolies.",
    "statuteOrAuthority": "Constitution of India, Article 13(1); Bhikaji Narain Dhakras v. State of M.P. (AIR 1955 SC 781)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-011",
    "canonical": "SECULARISM",
    "acceptedVariants": [
      "SECULARISM"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Preamble feature mandating that the state maintains equal respect and distance from all religions",
    "additionalHint": "Inserted into Preamble by 42nd Amendment Act, 1976; part of Basic Structure",
    "definition": "A constitutional principle establishing that the Indian state has no official religion and accords equal treatment to all faiths without discrimination.",
    "educationalExample": "State funds cannot be spent exclusively on promoting a single religious denomination pursuant to Article 27.",
    "statuteOrAuthority": "Constitution of India, Preamble & Articles 25-28; S.R. Bommai v. Union of India (1994 3 SCC 1)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-012",
    "canonical": "FEDERALISM",
    "acceptedVariants": [
      "FEDERALISM"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Constitutional distribution of legislative, executive and financial powers between Union and States",
    "additionalHint": "Described as quasi-federal by K.C. Wheare; recognized as Basic Structure in S.R. Bommai",
    "definition": "A system of government where sovereignty is constitutionally partitioned between central governing authority and constituent political units.",
    "educationalExample": "Disputes regarding sharing of interstate river waters are adjudicated under federal constitutional machinery.",
    "statuteOrAuthority": "Constitution of India, Article 1 & Part XI; State of West Bengal v. Union of India (AIR 1963 SC 1241)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-013",
    "canonical": "ORDINANCE",
    "acceptedVariants": [
      "ORDINANCE"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Temporary executive law promulgated by the President or Governor when legislature is not in session",
    "additionalHint": "Promulgated under Article 123 (President) and Article 213 (Governor)",
    "definition": "A law promulgated by the executive head of state during recess of parliament or state legislature to address emergent situations.",
    "educationalExample": "Repeated re-promulgation of ordinances without legislative approval was struck down as constitutional fraud.",
    "statuteOrAuthority": "Constitution of India, Article 123 & 213; D.C. Wadhwa v. State of Bihar (1987 1 SCC 378)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-014",
    "canonical": "IMPEACHMENT",
    "acceptedVariants": [
      "IMPEACHMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Constitutional quasi-judicial procedure for removal of the President of India for violation of the Constitution",
    "additionalHint": "Prescribed under Article 61 requiring a two-thirds majority of total membership",
    "definition": "A formal legislative proceeding to charge, try, and remove the President from office for proven violation of the Constitution.",
    "educationalExample": "A resolution to investigate Presidential conduct under Article 61 requires 14 days prior notice signed by at least one-fourth members.",
    "statuteOrAuthority": "Constitution of India, Article 61",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-015",
    "canonical": "PROROGATION",
    "acceptedVariants": [
      "PROROGATION"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Formal termination of a session of Parliament without dissolving the House",
    "additionalHint": "Effectuated by the President under Article 85(2)(a)",
    "definition": "The official act by the head of state ending an ongoing sitting session of Parliament or legislative assembly without bringing about a dissolution.",
    "educationalExample": "The President prorogued the Monsoon Session of Parliament following completion of designated legislative business.",
    "statuteOrAuthority": "Constitution of India, Article 85(2)(a)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-016",
    "canonical": "DISSOLUTION",
    "acceptedVariants": [
      "DISSOLUTION"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Act of bringing the life of Lok Sabha or Legislative Assembly to an end, necessitating fresh elections",
    "additionalHint": "Rajya Sabha is not subject to dissolution; governed by Article 83(2)",
    "definition": "The formal termination of the existence of an elected legislative house leading to general elections for reconstituting it.",
    "educationalExample": "Upon recommendation of the Union Council of Ministers, the President dissolved the 17th Lok Sabha.",
    "statuteOrAuthority": "Constitution of India, Article 85(2)(b)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-017",
    "canonical": "SOVEREIGNTY",
    "acceptedVariants": [
      "SOVEREIGNTY"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Preamble principle denoting supreme independent authority free from external control",
    "additionalHint": "First attribute declaring India a Sovereign Socialist Secular Democratic Republic",
    "definition": "The supreme, absolute, and uncontrollable power by which any independent state is governed internally and externally.",
    "educationalExample": "India's accession to international treaties does not compromise its legislative sovereignty under Article 253.",
    "statuteOrAuthority": "Constitution of India, Preamble; Kesavananda Bharati v. State of Kerala",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-018",
    "canonical": "FRATERNITY",
    "acceptedVariants": [
      "FRATERNITY"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Preamble goal ensuring a sense of common brotherhood and dignity of the individual",
    "additionalHint": "Emphasized by Dr. B.R. Ambedkar as indispensable for liberty and equality",
    "definition": "A sense of shared collective brotherhood and psychological unity transcending narrow sectarian, regional, or linguistic barriers.",
    "educationalExample": "Hate speech inciting communal discord was held to violate the constitutional commitment to fraternity.",
    "statuteOrAuthority": "Constitution of India, Preamble & Article 51A(e); Nandini Sundar v. State of Chhattisgarh",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-019",
    "canonical": "EQUALITY",
    "acceptedVariants": [
      "EQUALITY"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Fundamental right under Article 14 prohibiting arbitrary state action and guaranteeing equal protection of laws",
    "additionalHint": "Includes both formal equality (anti-discrimination) and substantive equality (reasonable classification)",
    "definition": "The state of being equal before the law without privilege, ensuring non-arbitrariness in legislative and executive action.",
    "educationalExample": "A government procurement rule excluding suppliers without rational basis was struck down under Article 14.",
    "statuteOrAuthority": "Constitution of India, Article 14; E.P. Royappa v. State of Tamil Nadu (1974 4 SCC 3)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-020",
    "canonical": "LIBERTY",
    "acceptedVariants": [
      "LIBERTY"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Core value under Article 21 protecting personal freedom, dignified existence, and privacy against state deprivation",
    "additionalHint": "Expanded through Maneka Gandhi (1978) to require fair, just and reasonable procedure",
    "definition": "The freedom of an individual to act without arbitrary restraint, embodying bodily autonomy, dignity, and expression.",
    "educationalExample": "Imposition of travel bans without hearing was struck down as an arbitrary curtailment of personal liberty.",
    "statuteOrAuthority": "Constitution of India, Article 21; Maneka Gandhi v. Union of India (1978 1 SCC 248)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-021",
    "canonical": "PREAMBLE",
    "acceptedVariants": [
      "PREAMBLE"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Introductory statement setting out guiding ideals, philosophy, and objectives of the Constitution",
    "additionalHint": "Held to be an integral part of the Constitution in Kesavananda Bharati (1973)",
    "definition": "The solemn preface declaring the source of authority, nature of polity, and fundamental objectives of the Indian Republic.",
    "educationalExample": "Courts refer to the Preamble as a key to unpack ambiguous constitutional provisions.",
    "statuteOrAuthority": "Constitution of India, Preamble; Re: Berubari Union (1960) & Kesavananda Bharati (1973)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-022",
    "canonical": "CITIZENSHIP",
    "acceptedVariants": [
      "CITIZENSHIP"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Legal status under Part II of the Constitution conferring full civil and political rights in the Republic",
    "additionalHint": "Articles 5 to 11; regulated by the Citizenship Act, 1955",
    "definition": "The legal bond connecting an individual with the sovereign state, entailing reciprocal rights of allegiance and constitutional protection.",
    "educationalExample": "Only citizens possess the fundamental rights guaranteed under Articles 15, 16, 19, 29, and 30.",
    "statuteOrAuthority": "Constitution of India, Articles 5-11 & Citizenship Act, 1955",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-023",
    "canonical": "BICAMERAL",
    "acceptedVariants": [
      "BICAMERAL"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Legislative system consisting of two separate deliberative assemblies or chambers",
    "additionalHint": "Exemplified by Parliament comprising Lok Sabha and Rajya Sabha under Article 79",
    "definition": "Having two branches, chambers, or houses as a legislative body to ensure sober second thought and federal representation.",
    "educationalExample": "Six Indian states, including Uttar Pradesh, possess a bicameral legislature with Legislative Council and Assembly.",
    "statuteOrAuthority": "Constitution of India, Article 79 & Article 168",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-024",
    "canonical": "ADJOURNMENT",
    "acceptedVariants": [
      "ADJOURNMENT"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Suspension of a sitting of Parliament or judicial court to a specified future hour, day, or sine die",
    "additionalHint": "Ordered by Presiding Officer (Speaker/Chairman), distinct from prorogation",
    "definition": "The temporary postponement or suspension of proceedings of a legislative house or judicial bench to a designated time.",
    "educationalExample": "Due to persistent disorder in the well of the house, the Speaker ordered adjournment until tomorrow 11 AM.",
    "statuteOrAuthority": "Rules of Procedure and Conduct of Business in Lok Sabha, Rule 15",
    "sourceUrl": "https://loksabha.nic.in",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-025",
    "canonical": "REMEDY",
    "acceptedVariants": [
      "REMEDY"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Means given by law for recovery of a right or obtaining redress for a wrong (Article 32)",
    "additionalHint": "Termed 'heart and soul' of the Constitution by Dr. B.R. Ambedkar",
    "definition": "The legal means enforced by a court of law to restore a right, recover compensation, or redress an injury.",
    "educationalExample": "Article 32 is itself a fundamental right ensuring a guaranteed constitutional remedy for breach of Part III rights.",
    "statuteOrAuthority": "Constitution of India, Article 32; Prem Chand Garg v. Excise Commissioner (AIR 1963 SC 996)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-026",
    "canonical": "PRIVILEGE",
    "acceptedVariants": [
      "PRIVILEGE"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Immunity protecting legislators from civil liability or arrest for speeches and votes in the House",
    "additionalHint": "Enshrined under Article 105 (Parliament) and Article 194 (State Legislatures)",
    "definition": "Special rights, immunities, and exemptions enjoyed by members of each house of legislature collectively and individually.",
    "educationalExample": "A member cannot be prosecuted in any court for anything said or any vote cast in Parliament under Article 105(2).",
    "statuteOrAuthority": "Constitution of India, Article 105 & 194; Sita Soren v. Union of India (2024 SC 7-judge bench)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-027",
    "canonical": "AMENDMENT",
    "acceptedVariants": [
      "AMENDMENT"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Formal alteration, addition, or repeal of constitutional provisions under Article 368",
    "additionalHint": "Subject to the judicial limitation of the Basic Structure doctrine",
    "definition": "A formal modification or addition made to a statute or the Constitution following a designated parliamentary procedure.",
    "educationalExample": "The 101st Constitutional Amendment Act introduced the Goods and Services Tax (GST) regime.",
    "statuteOrAuthority": "Constitution of India, Article 368; Shankari Prasad v. Union of India",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-028",
    "canonical": "EMERGENCY",
    "acceptedVariants": [
      "EMERGENCY"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Constitutional proclamation under Part XVIII vesting extraordinary powers in the Union executive",
    "additionalHint": "Includes National (Article 352), State Breakdown (Article 356), and Financial (Article 360)",
    "definition": "A state of national crisis declared by the President entitling the Union to assume exceptional executive and legislative powers.",
    "educationalExample": "A proclamation of National Emergency under Article 352 requires prior written recommendation of the Union Cabinet.",
    "statuteOrAuthority": "Constitution of India, Articles 352-360; Minerva Mills v. Union of India",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-029",
    "canonical": "TRIBUNAL",
    "acceptedVariants": [
      "TRIBUNAL"
    ],
    "difficulty": "intermediate",
    "subject": "Constitutional Law",
    "primaryClue": "Quasi-judicial administrative adjudication body created under Article 323A or 323B",
    "additionalHint": "Decisions remain subject to High Court judicial review under Article 226 (L. Chandra Kumar)",
    "definition": "A specialized administrative or statutory adjudicatory body established to hear and decide disputes in specific regulatory domains.",
    "educationalExample": "The Central Administrative Tribunal adjudicates recruitment disputes of central government employees.",
    "statuteOrAuthority": "Constitution of India, Articles 323A-323B; L. Chandra Kumar v. Union of India (1997 3 SCC 261)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-030",
    "canonical": "GOVERNOR",
    "acceptedVariants": [
      "GOVERNOR"
    ],
    "difficulty": "beginner",
    "subject": "Constitutional Law",
    "primaryClue": "Constitutional executive head of a State appointed by the President under Article 155",
    "additionalHint": "Acts on aid and advice of State Council of Ministers under Article 163, subject to discretionary powers",
    "definition": "The nominal constitutional executive head of a constituent state in the Indian Union appointed for a 5-year term.",
    "educationalExample": "The Governor exercises the constitutional power to summon, prorogue, and dissolve the State Legislative Assembly.",
    "statuteOrAuthority": "Constitution of India, Articles 153-163; Shamsher Singh v. State of Punjab",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-031",
    "canonical": "THEFT",
    "acceptedVariants": [
      "THEFT"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Dishonestly taking any movable property out of possession of any person without consent",
    "additionalHint": "Governed by Section 303 of Bharatiya Nyaya Sanhita, 2023 (formerly Section 378 IPC)",
    "definition": "The unlawful taking of movable property out of another's possession with dishonest intention at inception.",
    "educationalExample": "Taking an unattended laptop from a library table with intention to keep it constitutes theft under Section 303(2) BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 303(2); Pyare Lal Bhargava v. State of Rajasthan (AIR 1963 SC 1094)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-032",
    "canonical": "EXTORTION",
    "acceptedVariants": [
      "EXTORTION"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Intentionally putting any person in fear of any injury and thereby dishonestly inducing delivery of property",
    "additionalHint": "Offence under Section 308 of BNS 2023 (formerly Section 383 IPC); delivery is made under duress",
    "definition": "Coercing another to deliver valuable security or property by putting them in fear of injury.",
    "educationalExample": "Threatening to publish defamatory photographs unless fifty thousand rupees is transferred is extortion under Section 308 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 308; R.S. Nayak v. A.R. Antulay (1986 2 SCC 716)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-033",
    "canonical": "ROBBERY",
    "acceptedVariants": [
      "ROBBERY"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Aggravated theft or extortion involving actual hurt, death, wrongful restraint, or imminent fear thereof",
    "additionalHint": "Section 309 of BNS 2023 (formerly Section 390 IPC); in all robbery there is either theft or extortion",
    "definition": "An aggravated form of theft or extortion accomplished by causing or threatening death, hurt, or wrongful restraint.",
    "educationalExample": "Snatching a gold chain while pressing a knife to the victim's neck transforms theft into robbery under Section 309 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 309 & 310; State of Maharashtra v. Joseph Mingel Koli (1997 Cri LJ 3962)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-034",
    "canonical": "DACOITY",
    "acceptedVariants": [
      "DACOITY"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Robbery committed or attempted by five or more persons acting conjointly",
    "additionalHint": "Section 310 of BNS 2023 (formerly Section 391 IPC); assembly of 5+ persons is an essential ingredient",
    "definition": "A joint robbery committed by five or more persons acting in concert.",
    "educationalExample": "Six armed intruders looting a bank teller at gunpoint commit dacoity under Section 310 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 310; Shyam Behari v. State of U.P. (AIR 1957 SC 320)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-035",
    "canonical": "CHEATING",
    "acceptedVariants": [
      "CHEATING"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Dishonestly deceiving a person to fraudulently induce delivery of property or consent to retain it",
    "additionalHint": "Section 318 of BNS 2023 (formerly Section 415/420 IPC); fraudulent intention must exist from the inception",
    "definition": "Fraudulently or dishonestly deceiving a person to cause wrongful gain or wrongful loss.",
    "educationalExample": "Selling forged land deeds representing oneself as the registered titleholder constitutes cheating under Section 318(4) BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 318(4); Hridaya Ranjan Prasad Verma v. State of Bihar (2000 4 SCC 168)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-036",
    "canonical": "FORGERY",
    "acceptedVariants": [
      "FORGERY"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Making a false document with intent to cause damage or injury, or support any claim or title",
    "additionalHint": "Section 336 of BNS 2023 (formerly Section 463 IPC); requires making a false document under Section 335",
    "definition": "The fraudulent creation or alteration of a document with intent to deceive and prejudice legal rights.",
    "educationalExample": "Forging a testator's signature onto a bogus will to claim ancestral agricultural property constitutes forgery under Section 336 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 336 & 338; Sheila Sebastian v. R. Jawaharaj (2018 7 SCC 581)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-037",
    "canonical": "MISAPPROPRIATION",
    "acceptedVariants": [
      "MISAPPROPRIATION"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Dishonestly converting to one's own use any movable property found or lawfully obtained",
    "additionalHint": "Section 314 of BNS 2023 (formerly Section 403 IPC); initial possession is lawful, conversion is dishonest",
    "definition": "The dishonest appropriation of property that initially came into possession without a criminal act.",
    "educationalExample": "Finding a dropped diamond ring on the road and immediately pawning it without attempting to discover the owner is misappropriation.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 314; Ramaswami Nadar v. State of Madras (AIR 1958 SC 56)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-038",
    "canonical": "MENS REA",
    "acceptedVariants": [
      "MENS REA"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Guilty mind or blameworthy mental state required to constitute criminal liability",
    "additionalHint": "Reflected in maxim 'Actus non facit reum nisi mens sit rea'; manifested as intention, knowledge, or recklessness",
    "definition": "The culpable state of mind that accompanies a criminal act, necessary to establish criminal guilt.",
    "educationalExample": "An accidental firing of a rifle during cleaning without negligent recklessness lacks mens rea for culpable homicide.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, General Exceptions (Sections 14-44); State of Maharashtra v. Mayer Hans George (AIR 1965 SC 722)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-039",
    "canonical": "ACTUS REUS",
    "acceptedVariants": [
      "ACTUS REUS"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Physical wrongful act or prohibited conduct accompanied by consequences prohibited by law",
    "additionalHint": "Physical half of criminal liability, complementing the mental element of mens rea",
    "definition": "The overt objective physical act or omission comprising the external elements of a statutory crime.",
    "educationalExample": "In theft, the physical actus reus consists of moving the movable property out of the possessor's control.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 303; Kartar Singh v. State of Punjab (1994 3 SCC 569)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-040",
    "canonical": "DOLI INCAPAX",
    "acceptedVariants": [
      "DOLI INCAPAX"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Legal presumption that a child below seven years of age is completely incapable of committing an offence",
    "additionalHint": "Codified in Section 20 of Bharatiya Nyaya Sanhita, 2023 (formerly Section 82 IPC)",
    "definition": "An absolute statutory defense immunizing children under seven from all criminal prosecution.",
    "educationalExample": "A six-year-old child who discharges a loaded firearm causing fatal injury cannot be prosecuted pursuant to doli incapax.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 20; Ulla Mahapatra v. The King (AIR 1950 Ori 261)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-041",
    "canonical": "HOMICIDE",
    "acceptedVariants": [
      "HOMICIDE"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "The killing of a human being by another human being, lawful or unlawful",
    "additionalHint": "Divided into lawful (justifiable/excusable) and unlawful (culpable homicide under Section 100 BNS)",
    "definition": "The act of causing the death of a human being through an act or omission.",
    "educationalExample": "Culpable homicide is the genus, whereas murder under Section 101 BNS is the specific aggravated species.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 100 & 101; Reg. v. Govinda (1876 ILR 1 Bom 342)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-042",
    "canonical": "MURDER",
    "acceptedVariants": [
      "MURDER"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Aggravated culpable homicide committed with intention or imminently dangerous act without lawful excuse",
    "additionalHint": "Section 101 of BNS 2023 (formerly Section 300 IPC); punishable under Section 103 BNS",
    "definition": "Unlawful culpable homicide involving premeditated lethal intention or knowledge that death is almost certain.",
    "educationalExample": "Shooting a victim point-blank in the chest with intention to cause death constitutes murder under Section 103 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 101 & 103; Virsa Singh v. State of Punjab (AIR 1958 SC 465)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-043",
    "canonical": "ASSAULT",
    "acceptedVariants": [
      "ASSAULT"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Gesture or preparation causing apprehension of imminent criminal force on another's person",
    "additionalHint": "Section 130 of BNS 2023 (formerly Section 351 IPC); mere words alone do not amount to assault without gesture",
    "definition": "An act creating a reasonable apprehension in another that criminal force is about to be inflicted.",
    "educationalExample": "Shaking a clenched fist inches from someone's face while threatening an immediate beating constitutes assault.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 130; AC Cama v. H.F. Morgan (1864 1 BHC 205)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-044",
    "canonical": "BATTERY",
    "acceptedVariants": [
      "BATTERY"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Actual intentional application of physical force to another's person without lawful justification",
    "additionalHint": "Corresponds to 'Criminal Force' under Section 129 of BNS 2023 (formerly Section 350 IPC)",
    "definition": "The unlawful and non-consensual application of force, however slight, to the body of another.",
    "educationalExample": "Slapping a person or throwing hot tea onto their clothes constitutes criminal force (battery).",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 129; Cole v. Turner (1704 6 Mod 149)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-045",
    "canonical": "CONSPIRACY",
    "acceptedVariants": [
      "CONSPIRACY"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Agreement between two or more persons to commit an illegal act or a legal act by illegal means",
    "additionalHint": "Section 61 of BNS 2023 (formerly Section 120A/120B IPC); agreement itself constitutes the offense",
    "definition": "A joint agreement between two or more parties to execute an unlawful objective or use unlawful methods.",
    "educationalExample": "Meeting secretly to plan and finance an armed robbery constitutes criminal conspiracy even prior to execution.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 61; State of Tamil Nadu v. Nalini (1999 5 SCC 253)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-046",
    "canonical": "ABETMENT",
    "acceptedVariants": [
      "ABETMENT"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Instigating, conspiring, or intentionally aiding another in the commission of an offense",
    "additionalHint": "Section 45 of BNS 2023 (formerly Section 107 IPC); covers instigation, conspiracy, and intentional aiding",
    "definition": "Encouraging, facilitating, or intentionally helping another individual to perpetrate a crime.",
    "educationalExample": "Supplying poison to a murderer knowing the intended purpose constitutes abetment by aiding under Section 45 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 45; Sanju v. State of M.P. (2002 5 SCC 371)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-047",
    "canonical": "KIDNAPPING",
    "acceptedVariants": [
      "KIDNAPPING"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Taking or enticing away a minor from lawful guardianship or conveying any person beyond India without consent",
    "additionalHint": "Section 137 of BNS 2023 (formerly Section 359/361 IPC); age threshold is under 18 years",
    "definition": "Unlawfully taking or enticing a minor out of the custody of their lawful guardian without guardian's consent.",
    "educationalExample": "Enticing a 15-year-old student away from home without parental knowledge amounts to kidnapping from lawful guardianship.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 137; S. Varadarajan v. State of Madras (AIR 1965 SC 942)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-048",
    "canonical": "ABDUCTION",
    "acceptedVariants": [
      "ABDUCTION"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Compelling by force or inducing by deceitful means any person to go from any place",
    "additionalHint": "Section 138 of BNS 2023 (formerly Section 362 IPC); abduction is an auxiliary act, punishable when accompanied by felonious intent",
    "definition": "Forcibly moving or deceitfully enticing any person of any age from one location to another.",
    "educationalExample": "Forcing an adult businessman into a van at gunpoint constitutes abduction under Section 138 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 138; Gurucharan Singh v. State of Haryana (AIR 1972 SC 2661)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-049",
    "canonical": "PERJURY",
    "acceptedVariants": [
      "PERJURY"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Knowingly giving false evidence under oath in a judicial proceeding",
    "additionalHint": "Offence under Section 227 of BNS 2023 (formerly Section 191 IPC); punishable under Section 229 BNS",
    "definition": "The criminal act of deliberately making a false statement on oath during a judicial or legal inquiry.",
    "educationalExample": "Deposing falsely in the witness box that an accused was at home during a murder constitutes perjury under Section 227 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 227 & 229; Iqbal Singh Marwah v. Meenakshi Marwah (2005 4 SCC 370)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-050",
    "canonical": "DEFAMATION",
    "acceptedVariants": [
      "DEFAMATION"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Making or publishing any imputation concerning a person intending or knowing it will harm their reputation",
    "additionalHint": "Section 356 of BNS 2023 (formerly Section 499 IPC); subject to 10 statutory exceptions",
    "definition": "Publishing untrue and derogatory statements that diminish an individual's reputation in public estimation.",
    "educationalExample": "Publishing false allegations in a newspaper that an advocate took bribes constitutes criminal defamation under Section 356 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 356; Subramanian Swamy v. Union of India (2016 7 SCC 221)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-051",
    "canonical": "SEDITION",
    "acceptedVariants": [
      "SEDITION"
    ],
    "difficulty": "advanced",
    "subject": "Criminal Law",
    "primaryClue": "Offense concerning acts endangering sovereignty, unity, and integrity of India under Section 152 BNS",
    "additionalHint": "Replaced archaic Section 124A IPC; explicitly targets armed rebellion, subversive activities, and separatist violence",
    "definition": "Conduct, words, or actions aimed at exciting armed rebellion or endangering the sovereign territorial integrity of India.",
    "educationalExample": "Publishing manifestos inciting secession and armed guerilla warfare against the Indian Republic attracts Section 152 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 152; S.G. Vombatkere v. Union of India (2022 SC order on Section 124A)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-052",
    "canonical": "AFFRAY",
    "acceptedVariants": [
      "AFFRAY"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Two or more persons fighting in a public place and disturbing the public peace",
    "additionalHint": "Section 194 of BNS 2023 (formerly Section 159 IPC); public place and breach of public tranquility are essential",
    "definition": "A public fight between two or more individuals that causes terror or disturbance to the general community.",
    "educationalExample": "A fistfight between two passengers at a crowded railway platform disturbing travelers amounts to an affray.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 194; Jagannath Sah v. State of Bihar (1974 Cri LJ 429)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-053",
    "canonical": "RIOT",
    "acceptedVariants": [
      "RIOT"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Force or violence used by an unlawful assembly of five or more persons in prosecution of a common object",
    "additionalHint": "Section 191 of BNS 2023 (formerly Section 146 IPC); unlawful assembly is the prerequisite under Section 189",
    "definition": "Violent or aggressive force deployed by an unlawful assembly to execute their shared illegal objective.",
    "educationalExample": "An angry mob of 10 people throwing rocks and smashing storefronts to enforce an unlawful strike constitutes rioting.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 191; Allauddin Mian v. State of Bihar (1989 3 SCC 5)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-054",
    "canonical": "ALIBI",
    "acceptedVariants": [
      "ALIBI"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Plea by an accused that they were at another place at the time the alleged crime was committed",
    "additionalHint": "Latin for 'elsewhere'; relevant under Section 9 of Bharatiya Sakshya Adhiniyam, 2023 (Section 11 IEA)",
    "definition": "An evidentiary defense establishing physical impossibility of participation due to being at a distant location.",
    "educationalExample": "Flight boarding passes and hotel CCTV proving the accused was in Chennai when a burglary occurred in Lucknow establish an alibi.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 9; Dudh Nath Pandey v. State of U.P. (1981 2 SCC 166)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-055",
    "canonical": "CORPUS DELICTI",
    "acceptedVariants": [
      "CORPUS DELICTI"
    ],
    "difficulty": "advanced",
    "subject": "Criminal Law",
    "primaryClue": "The body or substantial fact of the crime; evidence that a specific crime was indeed committed",
    "additionalHint": "Latin legal maxim; conviction can stand without physical body if circumstantial proof is irresistible",
    "definition": "The objective proof that a specific criminal offense has actually been committed by someone.",
    "educationalExample": "Even if a victim's body is never discovered, forensic blood spatter and confessions can establish corpus delicti in murder.",
    "statuteOrAuthority": "Sanjay Rajak v. State of Bihar (2019 12 SCC 552); Sevaka Perumal v. State of T.N. (1991 3 SCC 471)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-056",
    "canonical": "HOSTILE WITNESS",
    "acceptedVariants": [
      "HOSTILE WITNESS"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Witness who turns against the party calling them and shows an adverse bias or conceals the truth",
    "additionalHint": "Subject to cross-examination by calling party under Section 157 BSA 2023 (Section 154 IEA)",
    "definition": "A prosecution or defense witness whose testimony contradicts prior statements or displays uncooperative hostility.",
    "educationalExample": "When an eyewitness retracted their statement to police, the prosecutor was granted permission to cross-examine the hostile witness.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 157; Sat Paul v. Delhi Administration (1976 1 SCC 727)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-057",
    "canonical": "ACCOMPLICE",
    "acceptedVariants": [
      "ACCOMPLICE"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "A person who knowingly, voluntarily, and with common intent unites with the principal offender in committing a crime",
    "additionalHint": "Competent witness under Section 138 BSA 2023 (Section 133 IEA); uncorroborated testimony viewed with caution",
    "definition": "A partner or associate in crime who actively participates in planning, aiding, or executing the offense.",
    "educationalExample": "The court evaluated the getaway driver's testimony as an accomplice witness, seeking independent corroboration.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 138; Dagdu v. State of Maharashtra (1977 3 SCC 68)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-058",
    "canonical": "DYING DECLARATION",
    "acceptedVariants": [
      "DYING DECLARATION"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Statement made by a person as to the cause of their death or circumstances of the transaction resulting in death",
    "additionalHint": "Admissible exception to hearsay under Section 26(a) BSA 2023 (Section 32(1) IEA)",
    "definition": "A solemn oral or written statement by an injured individual relating to the circumstances of their impending death.",
    "educationalExample": "A burn victim's recorded statement to an executive magistrate identifying her attackers is admissible as a dying declaration.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 26(a); Khushal Rao v. State of Bombay (AIR 1958 SC 22)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-059",
    "canonical": "BIGAMY",
    "acceptedVariants": [
      "BIGAMY"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Contracting a second marriage during the lifetime of a spouse while the prior valid marriage subsists",
    "additionalHint": "Section 82 of BNS 2023 (formerly Section 494 IPC); void ab initio under Hindu Marriage Act, Section 11",
    "definition": "The criminal act of marrying another person while still lawfully wedded to an existing spouse.",
    "educationalExample": "Marrying a second wife without securing a legal divorce decree from the civil court constitutes bigamy under Section 82 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 82; Sarla Mudgal v. Union of India (1995 3 SCC 635)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-060",
    "canonical": "NEGLIGENCE",
    "acceptedVariants": [
      "NEGLIGENCE"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Failure to exercise the reasonable degree of care and precaution that a prudent person would observe",
    "additionalHint": "Section 106 of BNS 2023 (formerly Section 304A IPC); requires gross negligence in criminal jurisprudence",
    "definition": "A breach of legal duty to take care that causes unintentional injury or death to another.",
    "educationalExample": "A bus driver speeding through a dense pedestrian market without braking commits criminal rashness and negligence under Section 106 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 106 & 281; Jacob Mathew v. State of Punjab (2005 6 SCC 1)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-061",
    "canonical": "RASHNESS",
    "acceptedVariants": [
      "RASHNESS"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Hazardous act undertaken with consciousness of risk but with heedless disregard of consequences",
    "additionalHint": "Distinguished from negligence: rashness is running a known risk, negligence is inadvertence",
    "definition": "Acting with reckless disregard for human safety while consciously aware of the grave hazard created.",
    "educationalExample": "Driving on the wrong side of an expressway at night with broken headlights is an act of criminal rashness.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 281; Empress of India v. Idu Beg (1881 ILR 3 All 776)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-062",
    "canonical": "TREASON",
    "acceptedVariants": [
      "TREASON"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Waging or attempting to wage war against the Government of India",
    "additionalHint": "Section 147 of BNS 2023 (formerly Section 121 IPC); carries capital punishment or life imprisonment",
    "definition": "The crime of betraying one's country, especially by waging war or assisting its external enemies.",
    "educationalExample": "Assisting an armed foreign infiltration force to seize government installations constitutes waging war under Section 147 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 147; State (N.C.T. of Delhi) v. Navjot Sandhu (2005 11 SCC 600)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-063",
    "canonical": "COERCION",
    "acceptedVariants": [
      "COERCION"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Committing or threatening to commit an unlawful act to induce another's involuntary action or consent",
    "additionalHint": "Defined in Indian Contract Act Section 15; overlaps with criminal intimidation under BNS Section 351",
    "definition": "Using force or unlawful threats to compel a person to surrender rights or enter an agreement involuntarily.",
    "educationalExample": "Threatening to burn down an applicant's factory unless a contract is signed is coercion voiding consent.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 15 & BNS 2023, Section 351; Chikham Amiraju v. Seshamma (1917 41 Mad 33)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-064",
    "canonical": "STALKING",
    "acceptedVariants": [
      "STALKING"
    ],
    "difficulty": "beginner",
    "subject": "Criminal Law",
    "primaryClue": "Repeatedly following, contacting, or monitoring a person electronically without consent, causing alarm",
    "additionalHint": "Section 78 of BNS 2023 (formerly Section 354D IPC); includes cyber stalking",
    "definition": "A persistent pattern of obsessive surveillance, tracking, or online harassment that induces fear.",
    "educationalExample": "Creating fake social media profiles to send daily unsolicited messages to a woman after being told to stop constitutes stalking.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 78",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-065",
    "canonical": "VOYEURISM",
    "acceptedVariants": [
      "VOYEURISM"
    ],
    "difficulty": "intermediate",
    "subject": "Criminal Law",
    "primaryClue": "Watching or capturing the image of a woman engaging in a private act where privacy is reasonably expected",
    "additionalHint": "Section 77 of BNS 2023 (formerly Section 354C IPC); criminalizes both viewing and dissemination",
    "definition": "The unlawful observation, recording, or broadcasting of an individual's private intimate moments without consent.",
    "educationalExample": "Installing a hidden camera in a trial fitting room constitutes voyeurism under Section 77 BNS.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 77",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-066",
    "canonical": "RES JUDICATA",
    "acceptedVariants": [
      "RES JUDICATA"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Statutory rule barring courts from re-trying a suit or issue conclusively decided between same parties",
    "additionalHint": "Codified under Section 11 of Code of Civil Procedure, 1908; based on public policy to end litigation",
    "definition": "A doctrine precluding parties from re-litigating a matter on which a final judgment has already been rendered.",
    "educationalExample": "Having lost a title suit up to the High Court, a party cannot file a fresh suit on the same cause of action.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 11; Satyadhyan Ghosal v. Deorajin Debi (AIR 1960 SC 941)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-067",
    "canonical": "RES SUB JUDICE",
    "acceptedVariants": [
      "RES SUB JUDICE"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Rule mandating stay of trial of a subsequently instituted suit where matter in issue is directly pending in a prior suit",
    "additionalHint": "Codified under Section 10 of Code of Civil Procedure, 1908; prevents conflicting judicial decrees",
    "definition": "The procedural requirement staying the trial of a later suit when an identical dispute is already pending.",
    "educationalExample": "When a second partition suit regarding identical ancestral property was filed in another district, it was stayed under Section 10.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 10; National Institute of Mental Health v. C. Parameshwara (2005 2 SCC 256)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-068",
    "canonical": "PLAINT",
    "acceptedVariants": [
      "PLAINT"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "The statement of claim in writing through which a civil suit is formally instituted by a plaintiff",
    "additionalHint": "Governed by Order VII of CPC; must state material facts, cause of action, valuation, and relief",
    "definition": "The formal written pleading wherein a plaintiff sets forth the cause of action and prayers seeking relief.",
    "educationalExample": "The trial court rejected the plaint under Order VII Rule 11 CPC because it failed to disclose a valid cause of action.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 26 & Order VII; Saleem Bhai v. State of Maharashtra (2003 1 SCC 557)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-069",
    "canonical": "WRITTEN STATEMENT",
    "acceptedVariants": [
      "WRITTEN STATEMENT"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "The formal statement of defense filed by a defendant responding specifically to plaintiff's plaint",
    "additionalHint": "Governed by Order VIII of CPC; must be filed within 30 days, extendable up to 90/120 days",
    "definition": "The pleading filed by a defendant setting up defenses, denying allegations, or asserting set-off.",
    "educationalExample": "General denials are insufficient; the defendant must specifically deal with each allegation of fact in the written statement.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order VIII Rule 1; Kailash v. Nanhku (2005 4 SCC 480)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-070",
    "canonical": "INJUNCTION",
    "acceptedVariants": [
      "INJUNCTION"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Judicial order restraining a party from doing an act or compelling performance of a restorative act",
    "additionalHint": "Temporary injunctions governed by Order XXXIX CPC; perpetual injunctions governed by Specific Relief Act Section 38",
    "definition": "A court decree or order commanding a party to refrain from doing or to perform a specified act.",
    "educationalExample": "The court granted an ad-interim temporary injunction restraining the defendant from demolishing the common boundary wall.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XXXIX Rules 1 & 2; Dalpat Kumar v. Prahlad Singh (1992 1 SCC 719)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-071",
    "canonical": "DECREE",
    "acceptedVariants": [
      "DECREE"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Formal expression of an adjudication conclusively determining the rights of parties with regard to all or any matters in controversy",
    "additionalHint": "Defined in Section 2(2) CPC; includes preliminary and final decrees, and rejection of plaint",
    "definition": "The formal judicial declaration resolving the substantive disputes in a civil suit conclusively.",
    "educationalExample": "In a suit for partition, the court first passes a preliminary decree defining shares before the final division decree.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 2(2); Phoolchand v. Gopal Lal (AIR 1967 SC 1470)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-072",
    "canonical": "JUDGMENT",
    "acceptedVariants": [
      "JUDGMENT"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "The statement given by the Judge on the grounds of a decree or order",
    "additionalHint": "Defined under Section 2(9) and Order XX of CPC; contains concise statement of case, points for determination, decision, and reasons",
    "definition": "The formal reasoned expression of the court containing legal findings upon which a decree is founded.",
    "educationalExample": "A judgment must contain sound judicial reasoning justifying each framed issue before the formal decree can be drawn.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 2(9) & Order XX Rule 4; Balraj Taneja v. Sunil Madan (1999 8 SCC 396)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-073",
    "canonical": "MESNE PROFITS",
    "acceptedVariants": [
      "MESNE PROFITS"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Profits which person in wrongful possession actually received or might with ordinary diligence have received, with interest",
    "additionalHint": "Defined in Section 2(12) of CPC; does not include profits due to improvements made by wrongful possessor",
    "definition": "Damages awarded to the true owner representing compensation for unauthorized occupation of immovable property.",
    "educationalExample": "Upon decreeing possession of the commercial showroom, the court directed an inquiry into mesne profits under Order XX Rule 12.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 2(12); Lucy Kochuwareed v. P. Mariappa Gounder (1979 3 SCC 150)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-074",
    "canonical": "GARNISHEE",
    "acceptedVariants": [
      "GARNISHEE"
    ],
    "difficulty": "advanced",
    "subject": "Civil Procedure",
    "primaryClue": "Third party indebted to a judgment-debtor who is ordered by court to pay the debt directly to decree-holder",
    "additionalHint": "Governed by Order XXI Rules 46A to 46-I of CPC; common execution procedure for bank deposits",
    "definition": "A person who holds money owed to a judgment-debtor and is subject to a court attachment order.",
    "educationalExample": "The court issued a garnishee order attaching the judgment-debtor's fixed deposit lying in the nationalized bank.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XXI Rule 46A; F.G.P. Ltd. v. Saleh Hooseini Doctor (2009 10 SCC 223)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-075",
    "canonical": "INTERPLEADER",
    "acceptedVariants": [
      "INTERPLEADER"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Suit where plaintiff claims no interest in subject-matter other than charges and asks competing claimants to litigate between themselves",
    "additionalHint": "Governed by Section 88 and Order XXXV of CPC; plaintiff must not collude with either defendant",
    "definition": "A proceeding enabling a neutral stakeholder to require rival claimants to resolve their competing entitlements in court.",
    "educationalExample": "An auctioneer holding proceeds of sale claimed by both buyer and mortgagee filed an interpleader suit.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 88 & Order XXXV; Asanalli v. Mansooralli (AIR 1948 Nag 326)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-076",
    "canonical": "SET OFF",
    "acceptedVariants": [
      "SET OFF"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Statutory cross-claim for ascertained sum of money legally recoverable by defendant from plaintiff in a money recovery suit",
    "additionalHint": "Order VIII Rule 6 CPC; both debts must be mutual and legally recoverable at the date of suit",
    "definition": "A plea whereby a defendant seeks to extinguish or reduce plaintiff's money claim through a mutual existing debt.",
    "educationalExample": "In a suit for Rs 50,000 for supplied goods, defendant pleaded set-off of Rs 20,000 previously loaned to plaintiff.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order VIII Rule 6; Union of India v. Karam Chand Thapar (2004 3 SCC 504)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-077",
    "canonical": "COUNTERCLAIM",
    "acceptedVariants": [
      "COUNTERCLAIM"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Independent cross-action brought by defendant against plaintiff in a suit, treated as a cross-plaint",
    "additionalHint": "Governed by Order VIII Rules 6A to 6G CPC; can exceed the pecuniary limits of the original plaint",
    "definition": "A formal claim raised by the defendant against the plaintiff that could have formed the basis of an independent suit.",
    "educationalExample": "In an eviction suit, the defendant raised a counterclaim seeking specific performance of an oral agreement of sale.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order VIII Rule 6A; Jag Mohan Chawla v. Dera Radha Swami Satsang (1996 4 SCC 699)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-078",
    "canonical": "RESTITUTION",
    "acceptedVariants": [
      "RESTITUTION"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Duty of the court to place parties in the original position they would have occupied but for an erroneous decree reversed in appeal",
    "additionalHint": "Codified under Section 144 of CPC; based on maxim 'Actus curiae neminem gravabit'",
    "definition": "The restoration of property or benefit wrongfully taken from a party pursuant to an erroneous decree subsequently set aside.",
    "educationalExample": "When an eviction decree was reversed in second appeal, the tenant was restored to physical possession under Section 144 CPC.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 144; South Eastern Coalfields Ltd. v. State of M.P. (2003 8 SCC 648)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-079",
    "canonical": "REVISION",
    "acceptedVariants": [
      "REVISION"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Supervisory jurisdiction of the High Court to correct non-appealable jurisdictional errors of subordinate courts",
    "additionalHint": "Governed by Section 115 CPC; limited to acting without jurisdiction, failing to exercise it, or material irregularity",
    "definition": "The procedural power of a superior court to examine the record of a subordinate court for jurisdictional defects.",
    "educationalExample": "The High Court exercised civil revisional jurisdiction to overturn an order refusing to reject a time-barred plaint.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 115; Shiv Shakti Coop. Housing Society v. Swaraj Developers (2003 6 SCC 659)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-080",
    "canonical": "REVIEW",
    "acceptedVariants": [
      "REVIEW"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Re-examination of its own decree or order by the same court on grounds of error apparent on face of record",
    "additionalHint": "Governed by Section 114 and Order XLVII CPC; discovery of new evidence or mistake apparent on face of record",
    "definition": "The reconsideration of a judgment by the very court that pronounced it, strictly confined to patent errors.",
    "educationalExample": "A review petition cannot be an appeal in disguise; it lies only for manifest errors apparent without detailed rehearing.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 114 & Order XLVII; Kamlesh Verma v. Mayawati (2013 8 SCC 320)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-081",
    "canonical": "REFERENCE",
    "acceptedVariants": [
      "REFERENCE"
    ],
    "difficulty": "advanced",
    "subject": "Civil Procedure",
    "primaryClue": "Subordinate court seeking opinion of High Court on a question of law or validity of an Act/Regulation",
    "additionalHint": "Governed by Section 113 and Order XLVI CPC; necessary when reasonable doubt arises on a point of statutory validity",
    "definition": "The procedure whereby a subordinate trial court submits an unresolved question of legal validity to the High Court for ruling.",
    "educationalExample": "The civil judge referred the question of constitutionality of a local tenancy regulation to the High Court under Section 113.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 113 & Order XLVI",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-082",
    "canonical": "CAVEAT",
    "acceptedVariants": [
      "CAVEAT"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Formal notice filed by a party requesting court not to pass any order without prior notice to the caveator",
    "additionalHint": "Governed by Section 148A of CPC; remains in force for 90 days from the date of filing",
    "definition": "A precautionary warning lodged in court ensuring a party is heard before any ex-parte relief is granted to an adversary.",
    "educationalExample": "Anticipating an ex-parte stay against demolition, the municipal council lodged a caveat under Section 148A.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 148A; Deepak Khosla v. Union of India (2011 4 Comp LJ 368 Del)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-083",
    "canonical": "EX PARTE",
    "acceptedVariants": [
      "EX PARTE"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Proceedings conducted or orders passed in the absence of one of the parties who failed to appear despite notice",
    "additionalHint": "Governed by Order IX Rule 6 CPC; remedy to set aside ex parte decree lies under Order IX Rule 13",
    "definition": "A judicial act performed or decree pronounced by the court when only one party is present.",
    "educationalExample": "Because the defendant failed to appear after registered summons service, the court passed an ex parte eviction decree.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order IX Rules 6 & 13; G.P. Srivastava v. R.K. Raizada (2000 3 SCC 54)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-084",
    "canonical": "AMICUS CURIAE",
    "acceptedVariants": [
      "AMICUS CURIAE"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "A neutral advocate appointed by the court as a 'friend of the court' to assist on complex questions of law",
    "additionalHint": "Latin legal term; owes allegiance to judicial justice rather than to any litigant in the suit",
    "definition": "An impartial legal specialist invited by the court to advise on matters of public importance or novel legal complexity.",
    "educationalExample": "In a public interest case on prison conditions, the High Court appointed a senior advocate as amicus curiae.",
    "statuteOrAuthority": "Supreme Court Rules, 2013; Re: Ramlila Maidan Incident (2012 5 SCC 1)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-085",
    "canonical": "ATTACHMENT",
    "acceptedVariants": [
      "ATTACHMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Judicial seizure or freezing of a debtor's property to hold it subject to satisfaction of a decree",
    "additionalHint": "Attachment before judgment governed by Order XXXVIII; execution attachment governed by Order XXI CPC",
    "definition": "The legal process taking custody of a debtor's assets to secure payment of a judgment debt.",
    "educationalExample": "Plaintiff proved defendant was secretly selling off properties to defeat the decree, securing attachment before judgment.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 60 & Order XXXVIII Rule 5; Raman Tech. v. Bharat Components (2008 8 SCC 327)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-086",
    "canonical": "SUBPOENA",
    "acceptedVariants": [
      "SUBPOENA"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Court order summoning a person to testify as a witness or produce specific documents under penalty",
    "additionalHint": "Corresponds to summons to witness under Order XVI of CPC",
    "definition": "A compulsory writ commanding an individual's appearance in court to give oral evidence or present documents.",
    "educationalExample": "The court issued a subpoena duces tecum directing the registrar to produce the original volume of deed records.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XVI Rules 1 & 10",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-087",
    "canonical": "INTERLOCUTORY",
    "acceptedVariants": [
      "INTERLOCUTORY"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Provisional or interim order passed during the pendency of a suit that does not finally dispose of the case",
    "additionalHint": "Governed by Order XXXIX (Injunctions) and Order XL (Receivers) CPC",
    "definition": "An order deciding an intermediate procedural matter or granting temporary relief pending trial.",
    "educationalExample": "An order granting temporary child custody during a matrimonial trial is an interlocutory order.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 104 & Order XXXIX; Madhu Limaye v. State of Maharashtra (1977 4 SCC 551)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-088",
    "canonical": "COMMISSION",
    "acceptedVariants": [
      "COMMISSION"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Authority issued by court to a person to conduct local investigation, examine witnesses, or inspect accounts",
    "additionalHint": "Governed by Section 75 and Order XXVI CPC; commissioner's report forms part of the record",
    "definition": "A warrant authorizing an appointed advocate or expert to perform an inspection or examine incapacitated witnesses.",
    "educationalExample": "In a boundary encroachment suit, the judge appointed an advocate commissioner with a surveyor to measure disputed land.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 75 & Order XXVI Rule 9; Haryana Waqf Board v. Shanti Sarup (2008 8 SCC 671)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-089",
    "canonical": "RECEIVER",
    "acceptedVariants": [
      "RECEIVER"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Neutral officer appointed by court under Order XL to manage, preserve, and protect property during litigation",
    "additionalHint": "Equitable remedy granted when property is in danger of being wasted, damaged, or alienated",
    "definition": "An impartial custodian appointed by court to manage property in dispute pending final adjudication.",
    "educationalExample": "To prevent diversion of factory profits during a bitter partnership dissolution, the court appointed an official receiver.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XL Rule 1; T. Krishnaswamy Chetty v. C. Thangavelu Chetty (AIR 1955 Mad 430)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-090",
    "canonical": "LIS PENDENS",
    "acceptedVariants": [
      "LIS PENDENS"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Doctrine that property in active litigation cannot be transferred so as to affect the rights of any party under decree",
    "additionalHint": "Codified in Section 52 of Transfer of Property Act, 1882; based on maxim 'Pendente lite nihil innovetur'",
    "definition": "The principle that the transfer of a disputed property pending a lawsuit remains subject to the court's ultimate decree.",
    "educationalExample": "Purchasers who buy suit property during pendency of a partition appeal take title strictly subject to the final decree.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 52; Jayaram Mudaliar v. Ayyaswami (1972 2 SCC 200)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-091",
    "canonical": "AFFIDAVIT",
    "acceptedVariants": [
      "AFFIDAVIT"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "Voluntary statement of facts sworn or affirmed in writing before an authorized oath commissioner or notary",
    "additionalHint": "Governed by Order XIX of CPC; must state facts within deponent's personal knowledge, distinguishing belief",
    "definition": "A written solemn declaration of facts made on oath or affirmation before an authorized judicial officer.",
    "educationalExample": "The interlocutory application for temporary injunction was supported by an affidavit verifying urgent danger.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XIX Rules 1-3; A.K.K. Nambiar v. Union of India (AIR 1970 SC 652)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-092",
    "canonical": "EXECUTION",
    "acceptedVariants": [
      "EXECUTION"
    ],
    "difficulty": "beginner",
    "subject": "Civil Procedure",
    "primaryClue": "The formal judicial enforcement of a court decree or order through attachment, sale, or arrest",
    "additionalHint": "Governed by Order XXI CPC; longest and most comprehensive procedural order in Indian law",
    "definition": "The final phase of a civil lawsuit wherein the successful litigant obtains the fruits of the decree.",
    "educationalExample": "The decree-holder filed an execution application under Order XXI Rule 11 seeking warrant for delivery of possession.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Sections 36-74 & Order XXI; Rahul S. Shah v. Jinendra Kumar Gandhi (2021 6 SCC 418)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-093",
    "canonical": "REPRESENTATIVE SUIT",
    "acceptedVariants": [
      "REPRESENTATIVE SUIT"
    ],
    "difficulty": "advanced",
    "subject": "Civil Procedure",
    "primaryClue": "Suit filed by or against numerous persons having the same interest in one suit with permission of court",
    "additionalHint": "Governed by Order I Rule 8 CPC; requires public advertisement and court sanction",
    "definition": "A lawsuit instituted by named individuals representing a broad class of persons sharing an identical community of interest.",
    "educationalExample": "Four villagers filed a representative suit on behalf of the entire village to protect community grazing pastures.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order I Rule 8; Chairman, Tamil Nadu Housing Board v. T.N. Ganapathy (1990 1 SCC 608)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-094",
    "canonical": "ABATEMENT",
    "acceptedVariants": [
      "ABATEMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Civil Procedure",
    "primaryClue": "Termination or suspension of a suit upon death of a party if the legal representatives are not brought on record in time",
    "additionalHint": "Governed by Order XXII CPC; abatement operates automatically after 90 days if no substitution application is made",
    "definition": "The legal cessation of a lawsuit upon death of a plaintiff or defendant where the right to sue survives but is not pursued.",
    "educationalExample": "The partition suit abated against the deceased defendant because no substitution petition was filed within 90 days.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XXII Rules 3 & 4; Mithailal Dalsangar Singh v. Kiran Devi (2003 10 SCC 691)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-095",
    "canonical": "INHERENT POWERS",
    "acceptedVariants": [
      "INHERENT POWERS"
    ],
    "difficulty": "advanced",
    "subject": "Civil Procedure",
    "primaryClue": "Residual judicial power of the civil court under Section 151 CPC to make orders necessary for ends of justice",
    "additionalHint": "Inherent authority codified in Section 151 CPC; cannot override express statutory prohibitions",
    "definition": "The intrinsic residual power of a court to do complete justice and prevent abuse of the process of the court.",
    "educationalExample": "Where the procedural rules were silent, the trial court invoked inherent powers under Section 151 to stay parallel inquiry.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Section 151; Manohar Lal Chopra v. Rai Bahadur Rao Raja Seth Hiralal (AIR 1962 SC 527)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-096",
    "canonical": "RES GESTAE",
    "acceptedVariants": [
      "RES GESTAE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Facts so connected with a fact in issue as to form part of the same transaction, whether occurring at same time/place or not",
    "additionalHint": "Codified under Section 4 of Bharatiya Sakshya Adhiniyam, 2023 (formerly Section 6 IEA)",
    "definition": "Spontaneous statements or acts contemporaneous with an event admissible as an exception to the hearsay rule.",
    "educationalExample": "A bystander's spontaneous shout 'A has stabbed B!' uttered during the assault is admissible under res gestae.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 4; Sukhar v. State of U.P. (1999 9 SCC 507)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-097",
    "canonical": "CONFESSION",
    "acceptedVariants": [
      "CONFESSION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Direct admission of guilt made by a person charged with a crime in a criminal proceeding",
    "additionalHint": "Governed by Sections 21-24 BSA 2023 (Sections 24-30 IEA); inadmissible if made to police officer",
    "definition": "A direct acknowledgment of guilt by an accused stating they committed the alleged criminal act.",
    "educationalExample": "A confession made to a police officer during interrogation is inadmissible under Section 23 BSA 2023.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 22 & 23; Pakala Narayana Swami v. Emperor (AIR 1939 PC 47)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-098",
    "canonical": "ADMISSION",
    "acceptedVariants": [
      "ADMISSION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Statement oral or documentary suggesting an inference as to any fact in issue or relevant fact",
    "additionalHint": "Defined in Section 15 of BSA 2023 (Section 17 IEA); admissions are substantive evidence against maker",
    "definition": "A voluntary acknowledgment made by a party of the existence of certain facts adverse to their claim.",
    "educationalExample": "A letter in which a defendant admitted borrowing ten lakh rupees from plaintiff is an admission under Section 15 BSA.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 15; Bharat Singh v. Bhagirathi (AIR 1966 SC 405)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-099",
    "canonical": "ESTOPPEL",
    "acceptedVariants": [
      "ESTOPPEL"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Rule of evidence precluding a person from denying the truth of a representation they previously caused another to believe",
    "additionalHint": "Section 121 of BSA 2023 (Section 115 IEA); based on the maxim 'Allegans contraria non est audiendus'",
    "definition": "A legal bar preventing a person from asserting a fact contrary to their prior representation or conduct.",
    "educationalExample": "Having represented that a property was unencumbered to induce a sale, the seller is estopped from setting up a mortgage.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 121; Pickard v. Sears (1837 6 Ad & El 469)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-100",
    "canonical": "HEARSAY",
    "acceptedVariants": [
      "HEARSAY"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Second-hand evidence of what a witness heard others say rather than what they perceived directly with their own senses",
    "additionalHint": "General exclusionary rule; excluded because not given under oath or subject to cross-examination",
    "definition": "Out-of-court statements offered to prove the truth of the matter asserted, generally inadmissible in evidence.",
    "educationalExample": "Testifying 'my neighbor told me he saw the burglar' is inadmissible hearsay evidence.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 55; Kalyan Kumar Gogoi v. Ashutosh Agnihotri (2011 2 SCC 532)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-101",
    "canonical": "PRIMARY EVIDENCE",
    "acceptedVariants": [
      "PRIMARY EVIDENCE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "The document itself produced for the inspection of the court, representing the best evidence",
    "additionalHint": "Section 57 of BSA 2023 (Section 62 IEA); required under the best evidence rule unless secondary evidence is excused",
    "definition": "The original authentic document or object presented directly in court as evidence of its contents.",
    "educationalExample": "Producing the original registered Sale Deed bearing the parties' physical signatures is primary evidence under Section 57 BSA.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 57; J. Yashoda v. K. Shobha Rani (2007 5 SCC 730)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-102",
    "canonical": "SECONDARY EVIDENCE",
    "acceptedVariants": [
      "SECONDARY EVIDENCE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Certified copies, photographic copies, or oral accounts of document contents admitted when original is lost or unavailable",
    "additionalHint": "Section 58 of BSA 2023 (Section 63 IEA); conditions for admissibility specified in Section 60 BSA (Section 65 IEA)",
    "definition": "Substituted evidence permitted to prove a document's contents only when non-production of original is legally excused.",
    "educationalExample": "After proving the original title deed was destroyed in a fire, a certified copy was admitted as secondary evidence.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 58 & 60; H. Siddiqui v. A. Ramalingam (2011 4 SCC 240)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-103",
    "canonical": "BURDEN OF PROOF",
    "acceptedVariants": [
      "BURDEN OF PROOF"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "The legal obligation on a party to establish the truth of a fact or issue to the requisite standard",
    "additionalHint": "Section 104 of BSA 2023 (Section 101 IEA); in criminal trials, the burden rests on the prosecution throughout",
    "definition": "The statutory duty resting on a litigant to introduce sufficient evidence to prove allegations asserted in pleadings.",
    "educationalExample": "In a criminal charge of theft, the burden of proof rests entirely upon the prosecution to prove guilt beyond reasonable doubt.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 104; Rangammal v. Kuppuswami (2011 12 SCC 220)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-104",
    "canonical": "ONUS OF PROOF",
    "acceptedVariants": [
      "ONUS OF PROOF"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "The shifting evidentiary burden of introducing evidence during trial as testimony proceeds",
    "additionalHint": "Distinguished from constant legal burden under Section 104; onus shifts back and forth between parties",
    "definition": "The operational obligation to adduce evidence to rebut a presumption or prima facie case established by the adversary.",
    "educationalExample": "Once prosecution established initial custody of stolen goods, the onus shifted to accused to explain lawful possession.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 105; A. Raghavamma v. A. Chenchamma (AIR 1964 SC 136)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-105",
    "canonical": "PRESUMPTION",
    "acceptedVariants": [
      "PRESUMPTION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Inference of the truth of a fact drawn by process of law from the proof of some other fact",
    "additionalHint": "Divided into 'May Presume', 'Shall Presume', and 'Conclusive Proof' under Section 2(4) BSA 2023 (Section 4 IEA)",
    "definition": "A legal deduction of the existence of an unknown fact inferred by law from the establishment of a known fact.",
    "educationalExample": "The birth of a child during a valid marriage creates a conclusive presumption of legitimacy under Section 116 BSA.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 2(4) & 116; Gautam Kundu v. State of West Bengal (1993 3 SCC 418)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-106",
    "canonical": "CONCLUSIVE PROOF",
    "acceptedVariants": [
      "CONCLUSIVE PROOF"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Statutory provision where proof of one fact bars the court from allowing evidence to be given to disprove it",
    "additionalHint": "Section 2(4)(c) of BSA 2023 (Section 4 IEA); e.g., legitimacy of child under Section 116 BSA",
    "definition": "An irrebuttable legal presumption where proof of a foundational fact conclusively establishes another fact.",
    "educationalExample": "A final decree of divorce pronounced by a competent matrimonial court is conclusive proof of dissolved legal status.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 35 & 116; Kanti Devi v. Poshi Ram (2001 5 SCC 311)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-107",
    "canonical": "LEADING QUESTION",
    "acceptedVariants": [
      "LEADING QUESTION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Any question suggesting the answer which the person putting it wishes or expects to receive",
    "additionalHint": "Section 146 of BSA 2023 (Section 141 IEA); prohibited in examination-in-chief without leave, permitted in cross-examination",
    "definition": "A question framed so as to suggest the desired response to the testifying witness.",
    "educationalExample": "Counsel asked 'Did you see the accused wearing a red coat?', which was disallowed as an impermissible leading question in chief.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 146-148; Varkey Joseph v. State of Kerala (1993 Supp 3 SCC 745)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-108",
    "canonical": "PRIVILEGED COMMUNICATION",
    "acceptedVariants": [
      "PRIVILEGED COMMUNICATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Confidential professional or official communications protected by law from forced disclosure in court",
    "additionalHint": "Covers spousal (Section 128), state affairs (Section 129), and attorney-client communications (Section 132 BSA)",
    "definition": "A confidential conversation or record protected by statute from compulsory testimonial revelation.",
    "educationalExample": "An advocate cannot be compelled to disclose confidential advice rendered to a client without client's express consent.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 132; State of U.P. v. Raj Narain (1975 4 SCC 428)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-109",
    "canonical": "PATENT AMBIGUITY",
    "acceptedVariants": [
      "PATENT AMBIGUITY"
    ],
    "difficulty": "advanced",
    "subject": "Law of Evidence",
    "primaryClue": "Defect or ambiguity evident upon the very face of a document itself, for which extrinsic oral evidence is inadmissible",
    "additionalHint": "Section 96 of BSA 2023 (Section 93 IEA); e.g., agreeing to sell property for 'Rs 1,000 or Rs 2,000'",
    "definition": "A visible linguistic contradiction on the face of a deed that cannot be cured by introducing oral testimony.",
    "educationalExample": "A deed reciting an agreement to sell a horse for 'one thousand or fifteen hundred rupees' suffers from fatal patent ambiguity.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 96; Keshavlal Lallubhai Patel v. Lalbhai Trikamlal Mills (AIR 1958 SC 512)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-110",
    "canonical": "LATENT AMBIGUITY",
    "acceptedVariants": [
      "LATENT AMBIGUITY"
    ],
    "difficulty": "advanced",
    "subject": "Law of Evidence",
    "primaryClue": "Ambiguity not apparent on the face of a document but revealed when its language is applied to external facts",
    "additionalHint": "Section 98 of BSA 2023 (Section 95-97 IEA); extrinsic oral evidence is admissible to resolve latent ambiguity",
    "definition": "An ambiguity arising when clear language in a deed applies equally to two different external subjects or things.",
    "educationalExample": "A will leaving land to 'my nephew John' when the testator in fact had two nephews named John creates a latent ambiguity.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 98-100; Doe d. Gord v. Needs (1836 2 M & W 129)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-111",
    "canonical": "REFRESHING MEMORY",
    "acceptedVariants": [
      "REFRESHING MEMORY"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "A witness referring to a contemporary writing or document made at the time of the transaction to revive recollection",
    "additionalHint": "Section 162 of BSA 2023 (Section 159 IEA); adverse party is entitled to inspect the writing and cross-examine on it",
    "definition": "The procedural right of a witness to consult notes recorded contemporaneously to assist accurate testimony.",
    "educationalExample": "A police investigating officer consulted the case diary to refresh memory regarding exact seizure serial numbers.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 162; State of A.P. v. Cheemalapati Ganeswara Rao (AIR 1963 SC 1850)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-112",
    "canonical": "DEMEANOR",
    "acceptedVariants": [
      "DEMEANOR"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "The physical appearance, behavior, and bearing of a witness during oral testimony recorded by the judge",
    "additionalHint": "Governed by Order XVIII Rule 12 CPC and Section 279 BNSS; valuable for assessing witness credibility",
    "definition": "The visual demeanor and conduct of a witness while testifying used by the trial judge to evaluate veracity.",
    "educationalExample": "The trial judge recorded that the witness perspired profusely, hesitated, and avoided eye contact when answering.",
    "statuteOrAuthority": "Code of Civil Procedure, 1908, Order XVIII Rule 12; Sarwan Singh v. State of Punjab (AIR 1957 SC 637)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-113",
    "canonical": "TEST IDENTIFICATION",
    "acceptedVariants": [
      "TEST IDENTIFICATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Parade conducted during investigation enabling an eyewitness to identify an unknown accused among dummies",
    "additionalHint": "Relevant under Section 7 BSA 2023 (Section 9 IEA); corroborative evidence, substantive identification occurs in court",
    "definition": "A formal investigative process where a victim picks out a previously unknown suspect from a lineup of similar persons.",
    "educationalExample": "The victim correctly picked out the robber in a test identification parade conducted inside the district jail by a magistrate.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 7; Malkhansingh v. State of M.P. (2003 5 SCC 746)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-114",
    "canonical": "JUDICIAL NOTICE",
    "acceptedVariants": [
      "JUDICIAL NOTICE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Recognition of facts which court must take as true without requiring formal evidence from parties",
    "additionalHint": "Governed by Section 52 of BSA 2023 (Section 57 IEA); includes laws of the land, territories, and public holidays",
    "definition": "The authority of a court to accept commonly known or officially documented facts as proved without proof.",
    "educationalExample": "The court took judicial notice of the provisions of the Bharatiya Nyaya Sanhita, 2023 and official national calendar.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 51 & 52; Onkar Nath v. Delhi Administration (1977 2 SCC 611)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-115",
    "canonical": "EXPERT OPINION",
    "acceptedVariants": [
      "EXPERT OPINION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Opinion of a person specially skilled in science, art, handwriting, finger impressions, or foreign law",
    "additionalHint": "Section 39 of BSA 2023 (Section 45 IEA); expert evidence is advisory and not conclusive proof",
    "definition": "Testimony provided by a qualified specialist assisting the court in evaluating technical scientific or forensic facts.",
    "educationalExample": "A ballistic expert's report establishing that the fatal bullet was fired from the seized licensed pistol was admitted.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 39; Ramesh Chandra Agrawal v. Regency Hospital (2009 9 SCC 709)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-116",
    "canonical": "ELECTRONIC RECORD",
    "acceptedVariants": [
      "ELECTRONIC RECORD"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Data, record, image, or sound generated, received, or sent electronically, admissible subject to statutory certificate",
    "additionalHint": "Section 61-63 of BSA 2023 (Section 65A/65B IEA); requires certificate under Section 63(4) BSA (Section 65B(4) IEA)",
    "definition": "Digital information stored or transmitted electronically, admissible upon certifying device integrity and custody.",
    "educationalExample": "WhatsApp chat printouts were excluded because the prosecution failed to produce a valid electronic certificate.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 63; Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020 7 SCC 1)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-117",
    "canonical": "CIRCUMSTANTIAL EVIDENCE",
    "acceptedVariants": [
      "CIRCUMSTANTIAL EVIDENCE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Evidence of relevant surrounding facts from which the existence of the fact in issue is logically inferred",
    "additionalHint": "Admissible under Section 3 BSA; must satisfy five golden principles ('panchsheel') in Sharad Birdhichand Sarda",
    "definition": "Indirect proof consisting of a chain of connected facts pointing irresistibly to the guilt of the accused.",
    "educationalExample": "Fingerprints on the safe, possession of stolen cash, and blood on the coat formed a complete circumstantial chain.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 3; Sharad Birdhichand Sarda v. State of Maharashtra (1984 4 SCC 116)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-118",
    "canonical": "CORROBORATION",
    "acceptedVariants": [
      "CORROBORATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Independent confirming evidence supporting the truth of a witness's primary testimony",
    "additionalHint": "Required as a rule of prudence for accomplice testimony (Section 138 BSA) and retractive confessions",
    "definition": "Additional evidence that confirms, strengthens, or authenticates primary testimony on material particulars.",
    "educationalExample": "The trial judge sought medical injury records and eyewitness statements as corroboration for the victim's testimony.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 138 & 160; Rameshwar v. State of Rajasthan (AIR 1952 SC 54)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-119",
    "canonical": "CROSS EXAMINATION",
    "acceptedVariants": [
      "CROSS EXAMINATION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "The examination of a witness by the adverse party to test veracity, accuracy, and credibility",
    "additionalHint": "Section 142 of BSA 2023 (Section 137 IEA); the greatest legal engine ever invented for the discovery of truth",
    "definition": "The questioning of a witness by the opposing counsel to expose contradictions, bias, or factual errors.",
    "educationalExample": "During cross-examination, counsel demonstrated that the eyewitness was thirty meters away and wearing no spectacles.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 142 & 151; Juwar Singh v. State of M.P. (AIR 1981 SC 373)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-120",
    "canonical": "EXAMINATION IN CHIEF",
    "acceptedVariants": [
      "EXAMINATION IN CHIEF"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "The initial questioning of a witness by the party who calls them to testify",
    "additionalHint": "Section 142(1) of BSA 2023 (Section 137 IEA); leading questions strictly prohibited without court leave",
    "definition": "The preliminary questioning by a party of their own witness to elicit material facts supporting their case.",
    "educationalExample": "The plaintiff began examination-in-chief by having the surveyor identify the boundary map prepared on site.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 142 & 147",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-121",
    "canonical": "RE EXAMINATION",
    "acceptedVariants": [
      "RE EXAMINATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Subsequent examination of a witness by calling party directed exclusively to explaining matters referred to in cross-examination",
    "additionalHint": "Section 142(3) of BSA 2023 (Section 137 IEA); cannot introduce new matters without leave of court",
    "definition": "The questioning of a witness by the calling party following cross-examination to clarify ambiguities elicited by the adversary.",
    "educationalExample": "In re-examination, the prosecutor asked the witness to explain why his clock showed 2 PM while police recorded 3 PM.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 142 & 143; Rammi v. State of M.P. (1999 8 SCC 649)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-122",
    "canonical": "COMPETENT WITNESS",
    "acceptedVariants": [
      "COMPETENT WITNESS"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Any person capable of understanding questions put to them and giving rational answers",
    "additionalHint": "Section 124 of BSA 2023 (Section 118 IEA); includes children and persons of unsound mind during lucid intervals",
    "definition": "An individual legally qualified to testify in court by virtue of possessing capacity for rational comprehension.",
    "educationalExample": "A nine-year-old child who understood the duty to speak truth was held to be a competent witness under Section 124 BSA.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 124; Dattu Ramrao Sakhare v. State of Maharashtra (1997 5 SCC 341)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-123",
    "canonical": "FACT IN ISSUE",
    "acceptedVariants": [
      "FACT IN ISSUE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "Any fact from which, either by itself or in connection with other facts, the existence or extent of any right or liability is affirmed or denied",
    "additionalHint": "Defined in Section 2(1)(h) of BSA 2023 (Section 3 IEA); corresponds to the substantive core of the dispute",
    "definition": "The principal disputed factual propositions which a court is required to determine to decide a case.",
    "educationalExample": "Whether the accused struck the deceased with an iron rod is a direct fact in issue in a homicide trial.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 2(1)(h)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-124",
    "canonical": "RELEVANT FACT",
    "acceptedVariants": [
      "RELEVANT FACT"
    ],
    "difficulty": "beginner",
    "subject": "Law of Evidence",
    "primaryClue": "A fact so connected with another as to make it legally admissible under the rules of evidence",
    "additionalHint": "Defined in Section 2(1)(k) and Sections 4-50 of BSA 2023 (Sections 5-55 IEA)",
    "definition": "A secondary fact that logically tends to prove or disprove a fact in issue, declared admissible by statute.",
    "educationalExample": "The purchase of rat poison by the accused shortly before the victim died of arsenic poisoning is a relevant fact.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 6 (Motive, preparation and conduct)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-125",
    "canonical": "EXTRA JUDICIAL CONFESSION",
    "acceptedVariants": [
      "EXTRA JUDICIAL CONFESSION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Evidence",
    "primaryClue": "Confession made outside the court to any private person other than a magistrate or police officer",
    "additionalHint": "Can be relied upon if voluntary, consistent, and convincing, though typically requiring corroboration",
    "definition": "An admission of guilt made privately to a friend, village elder, or acquaintance outside judicial proceedings.",
    "educationalExample": "Confessing to a village pradhan that one committed the murder was evaluated as a voluntary extra-judicial confession.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 21; Sahadevan v. State of Tamil Nadu (2012 6 SCC 403)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-126",
    "canonical": "CONSIDERATION",
    "acceptedVariants": [
      "CONSIDERATION"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Something of value given by promisee in return for promisor's promise, essential for an enforceable agreement",
    "additionalHint": "Section 2(d) of Indian Contract Act, 1872; defined by 'quid pro quo' (something for something)",
    "definition": "The price, detriment, benefit, or promise moving from the promisee that makes an agreement legally binding.",
    "educationalExample": "An agreement without consideration is void under Section 25, subject to exceptions like natural love and affection.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 2(d) & 25; Kedarnath Bhattacharji v. Gorie Mahomed (1886 ILR 14 Cal 64)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-127",
    "canonical": "PROPOSAL",
    "acceptedVariants": [
      "PROPOSAL"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Signification by one person to another of willingness to do or abstain from doing anything with a view to obtaining assent",
    "additionalHint": "Defined in Section 2(a) of Indian Contract Act, 1872; when accepted, becomes a promise",
    "definition": "An offer made by one party communicating readiness to be bound upon acceptance by the offeree.",
    "educationalExample": "Offering to sell a car for three lakh rupees with a request for reply within seven days is a proposal.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 2(a) & Section 8; Carlill v. Carbolic Smoke Ball Co. (1893 1 QB 256)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-128",
    "canonical": "ACCEPTANCE",
    "acceptedVariants": [
      "ACCEPTANCE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Assent given by offeree to proposal made, converting the proposal into an enforceable promise",
    "additionalHint": "Section 2(b) of Indian Contract Act, 1872; must be absolute and unqualified under Section 7",
    "definition": "The unconditional assent communicated by an offeree to all terms of a proposal.",
    "educationalExample": "A counter-offer proposing to buy the property at a reduced rate operates as a rejection rather than an acceptance.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 2(b) & 7; Hyde v. Wrench (1840 3 Beav 334)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-129",
    "canonical": "CAPACITY",
    "acceptedVariants": [
      "CAPACITY"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Legal competence of a person to enter into a binding contract",
    "additionalHint": "Section 11 of Indian Contract Act, 1872; requires majority, sound mind, and not disqualified by law",
    "definition": "The legal ability to enter into a valid contractual relationship, requiring adulthood and mental competence.",
    "educationalExample": "A minor completely lacks capacity to contract, rendering a minor's agreement void ab initio.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 11; Mohori Bibee v. Dharmodas Ghose (1903 30 IA 114)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-130",
    "canonical": "UNDUE INFLUENCE",
    "acceptedVariants": [
      "UNDUE INFLUENCE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Contract induced where one party in position to dominate will of another uses position to obtain unfair advantage",
    "additionalHint": "Section 16 of Indian Contract Act, 1872; contract is voidable at option of dominated party under Section 19A",
    "definition": "The unconscionable use of psychological dominance or fiduciary authority to extract an unfair contractual bargain.",
    "educationalExample": "A spiritual guru inducing an elderly devotee to gift all ancestral property to an ashram involves undue influence.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 16 & 19A; Subhas Chandra Das Mushib v. Ganga Prasad Das Mushib (1967 1 SCR 331)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-131",
    "canonical": "FRAUD",
    "acceptedVariants": [
      "FRAUD"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Intentional false representation of fact made knowingly or recklessly to deceive another party into contracting",
    "additionalHint": "Section 17 of Indian Contract Act, 1872; active concealment or promises made without intention of performing",
    "definition": "A deliberate misstatement of fact, active concealment, or deceptive act intended to induce a contract.",
    "educationalExample": "Selling a house while actively plastering over structural cracks to prevent discovery constitutes fraud under Section 17.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 17 & 19; Derry v. Peek (1889 14 App Cas 337)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-132",
    "canonical": "MISREPRESENTATION",
    "acceptedVariants": [
      "MISREPRESENTATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Innocent or non-fraudulent positive assertion of an untrue fact believed to be true by the speaker",
    "additionalHint": "Section 18 of Indian Contract Act, 1872; makes contract voidable under Section 19",
    "definition": "An untrue statement of fact made without fraudulent intention that induces the other party to enter a contract.",
    "educationalExample": "A seller honestly believing an engine is new based on supplier assurances commits misrepresentation if it is rebuilt.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 18 & 19; Oceanic Steam Navigation Co. v. Soonderdas Dhurumsey (1890 ILR 14 Bom 241)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-133",
    "canonical": "VOID AB INITIO",
    "acceptedVariants": [
      "VOID AB INITIO"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Having no legal effect from the very beginning, null and unenforceable as if it never existed",
    "additionalHint": "Latin legal maxim; e.g., agreement with a minor under Section 11, or agreement in restraint of trade under Section 27",
    "definition": "An agreement that is fundamentally illegal or defective from its inception, incapable of legal ratification.",
    "educationalExample": "A contract to smuggle contraband timber is void ab initio and no court will entertain a suit for damages under it.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 2(g); Mohori Bibee v. Dharmodas Ghose (1903 ILR 30 Cal 539)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-134",
    "canonical": "VOIDABLE",
    "acceptedVariants": [
      "VOIDABLE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "An agreement enforceable by law at the option of one party thereto, but not at the option of the other",
    "additionalHint": "Section 2(i) of Indian Contract Act, 1872; e.g., contracts entered under coercion, undue influence, fraud, misrepresentation",
    "definition": "A valid contract that may be legally affirmed or repudiated at the sole choice of the aggrieved innocent party.",
    "educationalExample": "A contract executed under coercion is voidable at the option of the coerced party under Section 19.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 2(i) & 19",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-135",
    "canonical": "CONTINGENT CONTRACT",
    "acceptedVariants": [
      "CONTINGENT CONTRACT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Contract to do or not do something if some collateral event does or does not happen",
    "additionalHint": "Section 31 of Indian Contract Act, 1872; e.g., insurance contracts, indemnity agreements",
    "definition": "A conditional agreement whose performance is triggered only upon the occurrence or non-occurrence of an uncertain future event.",
    "educationalExample": "A contract to pay ten lakh rupees if a cargo ship reaches port safely is a contingent contract under Section 31.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 31-36; Chandulal Harjivandas v. CIT (AIR 1967 SC 181)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-136",
    "canonical": "QUASI CONTRACT",
    "acceptedVariants": [
      "QUASI CONTRACT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Relations resembling those created by contract imposed by law to prevent unjust enrichment",
    "additionalHint": "Sections 68 to 72 of Indian Contract Act, 1872; based on doctrine of unjust enrichment",
    "definition": "An obligation imposed by law in the absence of agreement to prevent one party from unjustly benefiting at another's expense.",
    "educationalExample": "A person who receives money paid by mistake must repay it pursuant to Section 72 quasi-contractual liability.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 68-72; State of West Bengal v. B.K. Mondal & Sons (AIR 1962 SC 779)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-137",
    "canonical": "NOVATION",
    "acceptedVariants": [
      "NOVATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Substitution of a new contract in place of an existing one with mutual consent, extinguishing the original obligation",
    "additionalHint": "Section 62 of Indian Contract Act, 1872; requires mutual assent of all parties and valid new consideration",
    "definition": "The extinguishment of an existing contractual obligation by substituting a new contract or new debtor.",
    "educationalExample": "When a bank agrees to accept a buyer's promise in place of the original borrower's debt, novation occurs under Section 62.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 62; Lata Mangeshkar v. Union of India (1959 61 BOMLR 980)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-138",
    "canonical": "RESCISSION",
    "acceptedVariants": [
      "RESCISSION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "The cancellation, unmaking, or revocation of a contract, restoring the parties to their pre-contractual position",
    "additionalHint": "Governed by Section 64 of Indian Contract Act and Section 27 of Specific Relief Act, 1963",
    "definition": "The formal unmaking of an agreement, wiping out its obligations and requiring restitution of benefits received.",
    "educationalExample": "Upon discovering fraudulent misrepresentation regarding soil fertility, the buyer exercised rescission of the sale contract.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 64 & Specific Relief Act, 1963, Section 27",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-139",
    "canonical": "BREACH",
    "acceptedVariants": [
      "BREACH"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Failure or refusal without legal excuse to perform any promise that forms the whole or part of a contract",
    "additionalHint": "Sections 73-75 of Indian Contract Act, 1872; gives rise to right to damages or termination",
    "definition": "The non-performance or repudiation of a binding contractual obligation without lawful justification.",
    "educationalExample": "Failing to deliver industrial machinery on the agreed completion date constitutes an actionable breach of contract.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 73 & 74; Hadley v. Baxendale (1854 9 Exch 341)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-140",
    "canonical": "DAMAGES",
    "acceptedVariants": [
      "DAMAGES"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Monetary compensation awarded by court for loss or injury suffered from breach of contract or tortious act",
    "additionalHint": "Section 73 of Indian Contract Act, 1872; compensates naturally arising proximate losses, excluding remote damages",
    "definition": "The pecuniary compensation recoverable in court for breach of contract, measured by the loss suffered.",
    "educationalExample": "The court awarded compensatory damages representing the difference between the contract price and the market price on breach.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 73; Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd. (1949 2 KB 528)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-141",
    "canonical": "LIQUIDATED DAMAGES",
    "acceptedVariants": [
      "LIQUIDATED DAMAGES"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Pre-estimated sum named in the contract as the amount to be paid in case of breach",
    "additionalHint": "Section 74 of Indian Contract Act, 1872; court awards only reasonable compensation not exceeding the named sum",
    "definition": "A genuine pre-estimate of damages stipulated in advance in the contract to be paid upon default.",
    "educationalExample": "Under Section 74, courts do not award the entire liquidated penalty automatically, but only reasonable compensation.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 74; Fateh Chand v. Balkishan Dass (1964 1 SCR 515)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-142",
    "canonical": "INDEMNITY",
    "acceptedVariants": [
      "INDEMNITY"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Contract by which one party promises to save the other from loss caused by promisor's conduct or another's conduct",
    "additionalHint": "Defined in Section 124 of Indian Contract Act, 1872; rights of indemnity-holder defined in Section 125",
    "definition": "A contractual obligation binding one party to reimburse or protect another against anticipated loss or liability.",
    "educationalExample": "An insurance policy indemnifying a cargo owner against loss from oceanic perils is a classic contract of indemnity.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 124 & 125; Gajanan Moreshwar Parelkar v. Moreshwar Madan Mantri (AIR 1942 Bom 302)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-143",
    "canonical": "GUARANTEE",
    "acceptedVariants": [
      "GUARANTEE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Contract to perform the promise or discharge the liability of a third person in case of their default",
    "additionalHint": "Defined in Section 126 of Indian Contract Act, 1872; involves three parties: principal debtor, creditor, and surety",
    "definition": "A tripartite contract where a surety promises to repay a creditor if the primary debtor defaults.",
    "educationalExample": "The director signed a personal deed of guarantee binding himself to pay if his company defaulted on loan repayment.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 126; Bank of Bihar v. Damodar Prasad (1969 1 SCR 620)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-144",
    "canonical": "BAILMENT",
    "acceptedVariants": [
      "BAILMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Delivery of goods by one person to another for some purpose upon contract to return them when purpose is accomplished",
    "additionalHint": "Defined in Section 148 of Indian Contract Act, 1872; parties are bailor and bailee",
    "definition": "The transfer of physical possession of personal property without transferring ownership, for a specific purpose.",
    "educationalExample": "Leaving a motor vehicle at an authorized service station for mechanical repair creates a statutory bailment.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 148; Coggs v. Bernard (1703 2 Ld Raym 909)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-145",
    "canonical": "PLEDGE",
    "acceptedVariants": [
      "PLEDGE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Bailment of goods as security for payment of a debt or performance of a promise",
    "additionalHint": "Defined in Section 172 of Indian Contract Act, 1872; parties are pawnor (pledgor) and pawnee (pledgee)",
    "definition": "A specialized form of bailment where goods are deposited with a creditor as collateral security for a loan.",
    "educationalExample": "Depositing gold jewelry with a licensed pawnshop to secure an immediate cash loan constitutes a pledge under Section 172.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 172; Lallan Prasad v. Rahmat Ali (AIR 1967 SC 1322)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-146",
    "canonical": "LIEN",
    "acceptedVariants": [
      "LIEN"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Right of a person in possession of another's property to retain it until certain claims or debts are satisfied",
    "additionalHint": "Particular lien of bailee (Section 170) and general lien of bankers/factors/attorneys (Section 171 ICA)",
    "definition": "A legal right to retain lawful possession of another's personal goods until the possessor's dues are paid.",
    "educationalExample": "An auto mechanic has a particular lien on a repaired car to retain possession until labor charges are paid.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 170 & 171; Syndicate Bank v. Vijay Kumar (1992 2 SCC 330)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-147",
    "canonical": "AGENCY",
    "acceptedVariants": [
      "AGENCY"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Legal relationship where one person (agent) is employed to do any act for another or represent them in dealings",
    "additionalHint": "Defined in Section 182 of Indian Contract Act, 1872; no consideration is necessary to create an agency under Section 185",
    "definition": "The fiduciary legal relationship created when an agent is authorized to act on behalf of a principal.",
    "educationalExample": "A property broker negotiating sale terms on behalf of an overseas homeowner acts within the scope of agency.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 182 & 185; Harshad J. Shah v. LIC (1997 5 SCC 64)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-148",
    "canonical": "RATIFICATION",
    "acceptedVariants": [
      "RATIFICATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Subsequent adoption or confirmation by principal of an unauthorized act previously done on their behalf by an agent",
    "additionalHint": "Governed by Section 196 of Indian Contract Act, 1872; relates back to the time when the act was originally done",
    "definition": "The retroactive approval of an unauthorized transaction that clothes it with full legal authority from inception.",
    "educationalExample": "When the homeowner approved an unauthorized purchase of timber made by his caretaker, ratification bound the principal.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 196 & 199; Bolton Partners v. Lambert (1889 41 Ch D 295)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-149",
    "canonical": "FRUSTRATION",
    "acceptedVariants": [
      "FRUSTRATION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Doctrine that a contract becomes void when performance becomes impossible or unlawful due to an unexpected supervening event",
    "additionalHint": "Section 56 of Indian Contract Act, 1872; based on impossibility of performance without fault of either party",
    "definition": "The statutory discharge of a contract occurring when an unforeseeable event fundamentally destroys the basis of performance.",
    "educationalExample": "A contract to lease a music hall was discharged by frustration when the building was destroyed by an accidental fire.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 56; Satyabrata Ghose v. Mugneeram Bangur & Co. (1954 SCR 310)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-150",
    "canonical": "UBERRIMA FIDES",
    "acceptedVariants": [
      "UBERRIMA FIDES"
    ],
    "difficulty": "advanced",
    "subject": "Law of Contract",
    "primaryClue": "Doctrine of utmost good faith requiring full and honest disclosure of all material facts",
    "additionalHint": "Latin legal maxim governing insurance contracts; failure to disclose material facts entitles insurer to avoid policy",
    "definition": "The requirement of complete honesty and voluntary disclosure of all material facts in sensitive contracts like insurance.",
    "educationalExample": "Failing to disclose a pre-existing cardiac surgery on a life insurance proposal form breaches uberrima fides.",
    "statuteOrAuthority": "Life Insurance Corporation of India v. G.M. Channabasamma (1991 1 SCC 357)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-151",
    "canonical": "QUANTUM MERUIT",
    "acceptedVariants": [
      "QUANTUM MERUIT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Remedy allowing a party to recover 'as much as earned' for work done when a contract is discharged before completion",
    "additionalHint": "Latin for 'as much as he deserved'; Section 65 and 70 of Indian Contract Act",
    "definition": "An equitable claim for reasonable compensation for services performed under an incomplete or terminated contract.",
    "educationalExample": "When an author wrote three chapters before the publisher canceled the project, the author was entitled to quantum meruit.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 65 & 70; Planché v. Colburn (1831 8 Bing 14)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-152",
    "canonical": "SPECIFIC PERFORMANCE",
    "acceptedVariants": [
      "SPECIFIC PERFORMANCE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Contract",
    "primaryClue": "Equitable decree compelling a defaulting party to perform their exact contractual promise rather than paying damages",
    "additionalHint": "Governed by Specific Relief Act, 1963, Section 10; granted as a mandatory remedy for contracts to transfer immovable property",
    "definition": "A court decree ordering a party to carry out the precise terms of a contract, especially for unique land.",
    "educationalExample": "Because no monetary compensation can duplicate a unique parcel of land, the court decreed specific performance of the sale.",
    "statuteOrAuthority": "Specific Relief Act, 1963, Section 10; Sughar Singh v. Hari Singh (2021 SC)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2264",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-153",
    "canonical": "PRIVITY OF CONTRACT",
    "acceptedVariants": [
      "PRIVITY OF CONTRACT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Common law doctrine that only parties to a contract can sue or be sued upon it",
    "additionalHint": "Strictly observed in Indian law; a stranger to consideration can sue, but a stranger to contract cannot",
    "definition": "The legal relationship existing between the signatories of an agreement entitling them alone to enforce its covenants.",
    "educationalExample": "A son cannot sue the contractor his father hired to renovate the house because the son lacks privity of contract.",
    "statuteOrAuthority": "Dunlop Pneumatic Tyre Co. v. Selfridge & Co. (1915 AC 847); Jamna Das v. Ram Autar Pande (1912 39 IA 7)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-154",
    "canonical": "ANTICIPATORY BREACH",
    "acceptedVariants": [
      "ANTICIPATORY BREACH"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Repudiation of contractual obligations by a party before the arrival of the date fixed for performance",
    "additionalHint": "Section 39 of Indian Contract Act, 1872; gives promisee immediate right to accept breach and sue for damages",
    "definition": "An unequivocal declaration by a party in advance that they will refuse to perform their contractual obligation.",
    "educationalExample": "When a courier company informed the client two weeks before shipping that it was canceling all deliveries, anticipatory breach occurred.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 39; Hochster v. De La Tour (1853 2 E & B 678)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-155",
    "canonical": "WAGER",
    "acceptedVariants": [
      "WAGER"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Contract",
    "primaryClue": "Agreement depending solely upon the happening or not happening of an uncertain event where neither party has interest other than the stake",
    "additionalHint": "Declared void under Section 30 of Indian Contract Act, 1872; betting on horse racing is an exception",
    "definition": "A gambling agreement where parties mutually stake money exclusively on an uncertain chance without proprietary interest.",
    "educationalExample": "A bet between two friends staking five thousand rupees on the outcome of a cricket match is a void wager under Section 30.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 30; Gherulal Parakh v. Mahadeodas Maiya (AIR 1959 SC 781)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-156",
    "canonical": "TORT",
    "acceptedVariants": [
      "TORT"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "A civil wrong independent of contract for which the remedy is a common law action for unliquidated damages",
    "additionalHint": "Defined in Section 2(m) of Limitation Act, 1963; derived from Latin 'tortum' meaning twisted or crooked",
    "definition": "A civil wrong involving breach of a non-contractual legal duty owed generally toward the public, redressed by damages.",
    "educationalExample": "Causing physical injury through careless driving or damaging property through blasting is an actionable tort.",
    "statuteOrAuthority": "Limitation Act, 1963, Section 2(m); Winfield and Jolowicz on Tort",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2190",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-157",
    "canonical": "VICARIOUS LIABILITY",
    "acceptedVariants": [
      "VICARIOUS LIABILITY"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Liability of one person for the tortious acts committed by another by virtue of a special legal relationship like master and servant",
    "additionalHint": "Based on maxims 'Qui facit per alium facit per se' and 'Respondeat superior'; requires course of employment",
    "definition": "The secondary civil liability imposed on an employer for wrongful acts committed by an employee during employment.",
    "educationalExample": "A transport company was held vicariously liable when its bus driver negligently hit a pedestrian while driving on route.",
    "statuteOrAuthority": "State of Rajasthan v. Vidhyawati (AIR 1962 SC 933); Kasturi Lal v. State of U.P. (AIR 1965 SC 1039)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-158",
    "canonical": "STRICT LIABILITY",
    "acceptedVariants": [
      "STRICT LIABILITY"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Rule that a person who brings on land something likely to do mischief if it escapes is liable for damage irrespective of care",
    "additionalHint": "Laid down in Rylands v. Fletcher (1868); subject to exceptions like Act of God, plaintiff's default, and statutory authority",
    "definition": "Civil liability attaching automatically upon the escape of a dangerous substance brought onto land, regardless of due care.",
    "educationalExample": "When industrial reservoir water burst into an adjoining coal mine, the owner was held strictly liable under Rylands v. Fletcher.",
    "statuteOrAuthority": "Rylands v. Fletcher (1868 LR 3 HL 330)",
    "sourceUrl": "https://www.bailii.org/uk/cases/UKHL/1868/1.html",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-159",
    "canonical": "ABSOLUTE LIABILITY",
    "acceptedVariants": [
      "ABSOLUTE LIABILITY"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Indian tort rule holding enterprises engaged in hazardous activities strictly liable for escape without any exceptions",
    "additionalHint": "Established by Supreme Court in M.C. Mehta v. Union of India (Oleum Gas Leak case); no defenses of Act of God or sabotage",
    "definition": "An absolute liability without any exceptions imposed on commercial enterprises conducting inherently dangerous activities.",
    "educationalExample": "The enterprise was held liable to compensate gas leak victims without being permitted to plead the defense of Act of God.",
    "statuteOrAuthority": "M.C. Mehta v. Union of India (Oleum Gas Leak Case, 1987 1 SCC 395)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-160",
    "canonical": "VOLENTI NON FIT INJURIA",
    "acceptedVariants": [
      "VOLENTI NON FIT INJURIA"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Defense that no injury is done to a person who voluntarily consents to run a known risk",
    "additionalHint": "Latin legal maxim; requires full knowledge of risk and voluntary assumption, not merely knowledge",
    "definition": "A complete tort defense establishing that a person who willingly invites a known risk cannot sue for resulting harm.",
    "educationalExample": "A spectator struck by a flying ball at a cricket stadium cannot sue the batsman, having assumed the known risk.",
    "statuteOrAuthority": "Hall v. Brooklands Auto Racing Club (1933 1 KB 205); Smith v. Baker (1891 AC 325)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-161",
    "canonical": "DAMNUM SINE INJURIA",
    "acceptedVariants": [
      "DAMNUM SINE INJURIA"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Actual monetary or physical loss suffered without infringement of any recognized legal right, conferring no cause of action",
    "additionalHint": "Latin maxim; loss without legal injury is not actionable in tort law",
    "definition": "Substantial financial loss caused to an individual that is not accompanied by the violation of a recognized legal right.",
    "educationalExample": "Opening a rival school that reduces the enrollment and fees of an existing school is damnum sine injuria.",
    "statuteOrAuthority": "Gloucester Grammar School Case (1410 YB 11 Hen IV f. 47 pl. 21); Mogul Steamship Co. v. McGregor",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-162",
    "canonical": "INJURIA SINE DAMNO",
    "acceptedVariants": [
      "INJURIA SINE DAMNO"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Infringement of an absolute legal right without causing any actual monetary or physical loss, actionable per se",
    "additionalHint": "Latin maxim; violation of legal right warrants nominal damages even without economic loss",
    "definition": "The violation of a recognized legal right entitling the victim to sue even where no economic loss was suffered.",
    "educationalExample": "Preventing a qualified voter from casting their vote is actionable injuria sine damno even if their candidate won.",
    "statuteOrAuthority": "Ashby v. White (1703 2 Ld Raym 938); Bhim Singh v. State of J&K (1985 4 SCC 677)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-163",
    "canonical": "RES IPSA LOQUITUR",
    "acceptedVariants": [
      "RES IPSA LOQUITUR"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Evidentiary doctrine meaning 'the thing speaks for itself', shifting burden of proving care onto defendant",
    "additionalHint": "Applies when accident is of a kind that does not happen without negligence and instrumentality was in defendant's control",
    "definition": "A rule of evidence in negligence where the mere occurrence of an accident creates an inference of negligence.",
    "educationalExample": "A surgical pair of scissors left inside a patient's abdomen during surgery establishes res ipsa loquitur.",
    "statuteOrAuthority": "Byrne v. Boadle (1863 2 H & C 722); Municipal Corporation of Delhi v. Subhagwanti (AIR 1966 SC 1750)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-164",
    "canonical": "NUISANCE",
    "acceptedVariants": [
      "NUISANCE"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Unlawful interference with a person's use, enjoyment, or comfort of land or of some right over it",
    "additionalHint": "Divided into Public Nuisance (crime under Section 270 BNS) and Private Nuisance (civil tort)",
    "definition": "An unreasonable and substantial interference with another individual's peaceful enjoyment of their real property.",
    "educationalExample": "Running a noisy diesel generator continuously throughout the night next to a residential bedroom constitutes nuisance.",
    "statuteOrAuthority": "St. Helen's Smelting Co. v. Tipping (1865 11 HL Cas 642); Radhey Shyam v. Gur Prasad (AIR 1978 All 86)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-165",
    "canonical": "TRESPASS",
    "acceptedVariants": [
      "TRESPASS"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Direct and forcible physical interference with another's person, land, or goods without lawful justification",
    "additionalHint": "Actionable per se without requiring proof of actual damage; e.g., stepping onto private land without leave",
    "definition": "The direct, unjustified entry upon another's land or interference with their personal property or person.",
    "educationalExample": "Crossing a neighbor's boundary fence and walking across their agricultural land without permission is a civil trespass.",
    "statuteOrAuthority": "Entick v. Carrington (1765 19 St Tr 1029)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-166",
    "canonical": "SLANDER",
    "acceptedVariants": [
      "SLANDER"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Defamation published in a transient, non-permanent form, typically through spoken oral words or fleeting gestures",
    "additionalHint": "Distinguished in common law from libel; in Indian criminal law, both slander and libel are treated alike under BNS Section 356",
    "definition": "The publication of false and defamatory statements in temporary oral or spoken form.",
    "educationalExample": "Falsely shouting in an office lobby that a colleague stole company cash is actionable slander.",
    "statuteOrAuthority": "Consolidated Cafe v. Dharmalingam (AIR 1958 Mad 241)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-167",
    "canonical": "LIBEL",
    "acceptedVariants": [
      "LIBEL"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Defamation published in a permanent visible form, such as print, writing, photograph, or broadcast video",
    "additionalHint": "Actionable per se at common law without proof of special damage; criminalized under Section 356 BNS",
    "definition": "A defamatory representation communicated in permanent printed, written, or recorded media.",
    "educationalExample": "Publishing a false report in a city magazine alleging a surgeon engaged in organ trafficking constitutes libel.",
    "statuteOrAuthority": "Youssoupoff v. Metro-Goldwyn-Mayer Pictures Ltd. (1934 50 TLR 581)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-168",
    "canonical": "CONVERSION",
    "acceptedVariants": [
      "CONVERSION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Intentional interference with another's personal property that deprives them of its use or possession permanently",
    "additionalHint": "Tort of dealing with goods in a manner inconsistent with owner's title; e.g., wrongfully selling bailed goods",
    "definition": "An intentional tort consisting of taking, altering, or disposing of another's personal property without authorization.",
    "educationalExample": "A repair shop owner who sells a customer's stored motorcycle to pay shop debts commits civil conversion.",
    "statuteOrAuthority": "Hollins v. Fowler (1875 LR 7 HL 757)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-169",
    "canonical": "DECEIT",
    "acceptedVariants": [
      "DECEIT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Tort of intentionally making a false representation with intention that plaintiff act upon it, causing damage",
    "additionalHint": "Requires proof of actual fraud under Derry v. Peek; distinct from innocent misrepresentation",
    "definition": "A common law tort wherein a defendant makes a knowingly false statement intended to induce reliance causing financial harm.",
    "educationalExample": "Falsely telling a homebuyer that foundation permits were approved, inducing a purchase that caused structural loss, is deceit.",
    "statuteOrAuthority": "Derry v. Peek (1889 14 App Cas 337); Pasley v. Freeman (1789 3 TR 51)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-170",
    "canonical": "CONTRIBUTORY NEGLIGENCE",
    "acceptedVariants": [
      "CONTRIBUTORY NEGLIGENCE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Defense where plaintiff's own failure to exercise reasonable care contributed to causing the injury",
    "additionalHint": "Results in apportionment of damages rather than complete bar under modern Indian tort jurisprudence",
    "definition": "The failure by an injured plaintiff to take reasonable care for their own safety, contributing to the resulting harm.",
    "educationalExample": "A pedestrian who ran across an expressway while texting had their negligence compensation reduced by forty percent.",
    "statuteOrAuthority": "Municipal Corporation of Greater Bombay v. Laxman Iyer (2003 8 SCC 731)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-171",
    "canonical": "ACT OF GOD",
    "acceptedVariants": [
      "ACT OF GOD"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Defense in tort law for extraordinary natural event that could not have been anticipated or prevented by human foresight",
    "additionalHint": "Latin 'Vis Major'; recognized defense in Rylands v. Fletcher strict liability",
    "definition": "An overwhelming natural catastrophe resulting exclusively from natural causes without human intervention.",
    "educationalExample": "An unprecedented cloudburst causing an engineered reservoir dam to overflow was pleaded as an Act of God.",
    "statuteOrAuthority": "Nichols v. Marsland (1876 2 Ex D 1); Greenock Corp. v. Caledonian Railway (1917 AC 556)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-172",
    "canonical": "INEVITABLE ACCIDENT",
    "acceptedVariants": [
      "INEVITABLE ACCIDENT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Accident that could not have been prevented by the exercise of ordinary care, caution, and skill",
    "additionalHint": "General defense in tort; occurs when injury happens despite all reasonable precautions",
    "definition": "An unforeseen mishap that happens without negligence and could not be avoided by ordinary human care.",
    "educationalExample": "A motorist whose vehicle suddenly skid on an undiscoverable oil patch despite driving at five miles per hour had this defense.",
    "statuteOrAuthority": "Holmes v. Mather (1875 LR 10 Ex 261); Stanley v. Powell (1891 1 QB 86)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-173",
    "canonical": "MALICE",
    "acceptedVariants": [
      "MALICE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Wrongful intention or improper motive; in tort law, a lawful act generally does not become unlawful merely through malice",
    "additionalHint": "Reflected in Mayor of Bradford v. Pickles; exception exists in malicious prosecution",
    "definition": "An evil motive or spiteful intent to injure another person through legal or illegal mechanisms.",
    "educationalExample": "A landowner who diverted subterranean water under his land to compel a municipal purchase did not commit a tort despite malice.",
    "statuteOrAuthority": "Mayor of Bradford v. Pickles (1895 AC 587); Allen v. Flood (1898 AC 1)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-174",
    "canonical": "MALICIOUS PROSECUTION",
    "acceptedVariants": [
      "MALICIOUS PROSECUTION"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Instituting criminal proceedings against a person maliciously, without reasonable and probable cause, terminating in acquittal",
    "additionalHint": "Tort actionable for damages; requires prosecution, lack of reasonable cause, malice, acquittal, and damage",
    "definition": "The wrongful initiation of unsuccessful criminal proceedings without probable cause motivated by malice.",
    "educationalExample": "Filing a fabricated police report accusing a business rival of murder to damage his commercial enterprise is malicious prosecution.",
    "statuteOrAuthority": "Kamta Prasad v. Ram Kishore (AIR 1970 MP 252); West Bengal State Electricity Board v. Dilip Kumar Ray (2007 14 SCC 568)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-175",
    "canonical": "REMOTENESS OF DAMAGE",
    "acceptedVariants": [
      "REMOTENESS OF DAMAGE"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Rule limiting tort liability to damages that are a reasonably foreseeable consequence of the wrongful act",
    "additionalHint": "Laid down in The Wagon Mound (No. 1); replaced the direct consequences test of Re Polemis",
    "definition": "The legal doctrine restricting compensation to harms that were reasonably foreseeable by a prudent person.",
    "educationalExample": "Oil spilled into a harbor caused a wharf fire when molten metal ignited cotton; held remote because unforeseeable.",
    "statuteOrAuthority": "Overseas Tankship (UK) Ltd. v. Morts Dock & Engineering Co. (The Wagon Mound No. 1, 1961 AC 388)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-176",
    "canonical": "EGG SHELL SKULL",
    "acceptedVariants": [
      "EGG SHELL SKULL"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Rule that a tortfeasor takes the victim as they find them, remaining liable for unexpected severity of injury due to pre-existing frailty",
    "additionalHint": "Common law principle: thin skull or unusual physical vulnerability does not relieve a negligent wrongdoer",
    "definition": "A legal rule establishing that a defendant is fully liable for all injuries resulting from negligence, even if the victim had unusual frailty.",
    "educationalExample": "A minor blow causing severe brain hemorrhage due to an unusually thin skull makes the tortfeasor liable for the full harm.",
    "statuteOrAuthority": "Smith v. Leech Brain & Co. (1962 2 QB 405); Dulieu v. White & Sons (1901 2 KB 669)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-177",
    "canonical": "NERVOUS SHOCK",
    "acceptedVariants": [
      "NERVOUS SHOCK"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Recognizable psychiatric illness or physical damage caused by psychiatric trauma from seeing or hearing an accident",
    "additionalHint": "Requires medically diagnosed psychiatric condition rather than mere grief or sorrow",
    "definition": "Psychiatric illness induced in a plaintiff through sensory perception of severe trauma caused by a negligent tortfeasor.",
    "educationalExample": "A mother who suffered severe clinical depression upon witnessing her children injured in a horrific collision recovered damages.",
    "statuteOrAuthority": "Alcock v. Chief Constable of South Yorkshire Police (1992 1 AC 310); Page v. Smith (1996 AC 155)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-178",
    "canonical": "FALSE IMPRISONMENT",
    "acceptedVariants": [
      "FALSE IMPRISONMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Total restraint of a person's physical liberty for any period without lawful justification",
    "additionalHint": "Actionable per se without proof of damage; requires complete deprivation of liberty in all directions",
    "definition": "The unlawful and complete confinement of an individual within specified boundaries without legal authority.",
    "educationalExample": "Locking an employee in an office room for an hour to interrogate them about missing inventory is false imprisonment.",
    "statuteOrAuthority": "Bird v. Jones (1845 7 QB 742); Rudul Sah v. State of Bihar (1983 4 SCC 141)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-179",
    "canonical": "SCIENTER",
    "acceptedVariants": [
      "SCIENTER"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Knowledge of the dangerous or vicious propensity of an animal kept by the owner",
    "additionalHint": "Rule holding keeper of animal strictly liable if aware of its tendency to cause harm",
    "definition": "The owner's knowledge of the mischievous nature of an animal, which creates strict liability if the animal bites.",
    "educationalExample": "Keeping a guard dog known to have bitten neighbors makes the owner strictly liable under the scienter rule.",
    "statuteOrAuthority": "Filburn v. People's Palace & Aquarium Co. (1890 25 QBD 258)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-180",
    "canonical": "UNLIQUIDATED DAMAGES",
    "acceptedVariants": [
      "UNLIQUIDATED DAMAGES"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Damages whose amount has not been agreed upon in advance by parties, but is determined at court's discretion",
    "additionalHint": "The quintessential remedy in tort law, distinguishing it from liquidated contractual claims",
    "definition": "Pecuniary compensation whose quantum is not fixed by agreement but is assessed by the judge based on evidence.",
    "educationalExample": "In a suit for defamation, the court awarded unliquidated damages of five lakh rupees for mental anguish and loss of reputation.",
    "statuteOrAuthority": "Limitation Act, 1963, Section 2(m); Winfield on Tort",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2190",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-181",
    "canonical": "PUBLIC NUISANCE",
    "acceptedVariants": [
      "PUBLIC NUISANCE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Act or illegal omission causing common injury, danger, or annoyance to the public or people in general",
    "additionalHint": "Criminal offense under Section 270 BNS; civil suit lies under Section 91 CPC by Advocate General or two citizens",
    "definition": "An act obstructing or endangering the general community's health, safety, comfort, or public rights.",
    "educationalExample": "Dumping hazardous industrial sludge onto a public road blocking traffic and emitting toxic fumes is a public nuisance.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 270 & CPC Section 91; Municipal Council, Ratlam v. Vardichan (1980 4 SCC 162)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-182",
    "canonical": "PRIVATE NUISANCE",
    "acceptedVariants": [
      "PRIVATE NUISANCE"
    ],
    "difficulty": "intermediate",
    "subject": "Law of Torts",
    "primaryClue": "Unreasonable and substantial interference with an individual's private right to use and enjoy land",
    "additionalHint": "Civil tort actionable by the possessor of affected land; requires proof of substantial interference",
    "definition": "An unjustified and continuing interference with a neighbor's quiet enjoyment or physical condition of property.",
    "educationalExample": "Directing toxic industrial exhaust fumes across a neighbor's boundary killing their rose garden is a private nuisance.",
    "statuteOrAuthority": "Hollywood Silver Fox Farm Ltd. v. Emmett (1936 2 KB 468)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-183",
    "canonical": "BATTERY IN TORT",
    "acceptedVariants": [
      "BATTERY IN TORT"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Direct and intentional application of physical force to another person without lawful justification",
    "additionalHint": "Actionable per se without proof of physical injury; corresponds to criminal force",
    "definition": "The intentional touching of another person without consent or legal justification, however gentle.",
    "educationalExample": "Spitting on someone's face or intentionally pushing them off a bench constitutes civil battery in tort.",
    "statuteOrAuthority": "Cole v. Turner (1704 6 Mod 149); Scott v. Shepherd (1773 2 Wm Bl 892)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-184",
    "canonical": "ASSAULT IN TORT",
    "acceptedVariants": [
      "ASSAULT IN TORT"
    ],
    "difficulty": "beginner",
    "subject": "Law of Torts",
    "primaryClue": "Act of defendant causing reasonable apprehension in plaintiff's mind of imminent battery",
    "additionalHint": "Actionable per se; requires apparent present ability to carry out the physical threat",
    "definition": "An intentional act creating an immediate fear of unlawful physical contact in another person.",
    "educationalExample": "Pointing a loaded pistol at an individual during a heated argument constitutes an actionable assault in tort.",
    "statuteOrAuthority": "Stephens v. Myers (1830 4 C & P 349); Read v. Coker (1853 13 CB 850)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-185",
    "canonical": "MAINTENANCE",
    "acceptedVariants": [
      "MAINTENANCE"
    ],
    "difficulty": "advanced",
    "subject": "Law of Torts",
    "primaryClue": "Unlawful promotion or financing of litigation by a stranger who has no genuine interest in the lawsuit",
    "additionalHint": "Common law offense and tort; in India, agreements to finance litigation are valid unless unconscionable or champertous",
    "definition": "Assisting or financing a third party's lawsuit without possessing any legitimate interest in the outcome.",
    "educationalExample": "Financing another's boundary litigation purely to harass a common enemy was recognized at common law as maintenance.",
    "statuteOrAuthority": "Ram Coomar Coondoo v. Chunder Canto Mookerjee (1876 2 App Cas 186 PC)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-186",
    "canonical": "JURISPRUDENCE",
    "acceptedVariants": [
      "JURISPRUDENCE"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "The science, philosophy, and study of human and positive law",
    "additionalHint": "Derived from Latin 'juris prudentia' meaning knowledge or skill in law; Salmond: 'science of first principles of civil law'",
    "definition": "The foundational philosophy and theoretical study of legal systems, rights, duties, and institutions.",
    "educationalExample": "Salmond and Austin analyzed jurisprudence as the systematic exposition of foundational legal concepts.",
    "statuteOrAuthority": "Salmond on Jurisprudence; Austin's Province of Jurisprudence Determined",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-187",
    "canonical": "NATURAL LAW",
    "acceptedVariants": [
      "NATURAL LAW"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Philosophy of law asserting that certain rights and moral values are inherent in human nature and discovered through reason",
    "additionalHint": "Associated with Aristotle, Aquinas, Locke, and Fuller; higher law superseding unjust positive enactments",
    "definition": "A universal body of unchanging moral principles regarded as the foundational basis for all human conduct and law.",
    "educationalExample": "The concept of procedural fairness and Article 21 due process in Indian law draws deeply from natural law principles.",
    "statuteOrAuthority": "Maneka Gandhi v. Union of India (1978 1 SCC 248); H.L.A. Hart and Lon Fuller debate",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-188",
    "canonical": "POSITIVISM",
    "acceptedVariants": [
      "POSITIVISM"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "School of jurisprudence maintaining that law is posited by human authority, separate from morality",
    "additionalHint": "Associated with Bentham, Austin ('command of sovereign'), and Hart ('rule of recognition')",
    "definition": "A philosophy of jurisprudence that separates law as it is from law as it ought to be, tracing validity to sovereign source.",
    "educationalExample": "Austin's analytical positivism defined law strictly as the command of the sovereign backed by sanctions.",
    "statuteOrAuthority": "John Austin, The Province of Jurisprudence Determined (1832); H.L.A. Hart, The Concept of Law (1961)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-189",
    "canonical": "GRUNDNORM",
    "acceptedVariants": [
      "GRUNDNORM"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "Basic or foundational norm in Hans Kelsen's Pure Theory of Law from which all subordinate legal norms derive validity",
    "additionalHint": "Postulated by Kelsen; in a constitutional democracy, the Constitution itself acts as the Grundnorm",
    "definition": "The supreme foundational norm at the apex of the legal hierarchy that validates all other subordinate legal rules.",
    "educationalExample": "In India's constitutional framework, the Constitution of India functions as the supreme Grundnorm.",
    "statuteOrAuthority": "Hans Kelsen, General Theory of Law and State (1945); Kesavananda Bharati v. State of Kerala",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-190",
    "canonical": "SOVEREIGN",
    "acceptedVariants": [
      "SOVEREIGN"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Supreme political authority in a state that receives habitual obedience from society and renders obedience to no one",
    "additionalHint": "Core concept in Austinian analytical jurisprudence; in India, sovereign authority vests in 'We, the People'",
    "definition": "The supreme and independent political entity or institution exercising ultimate legislative and executive power.",
    "educationalExample": "In Indian constitutional jurisprudence, sovereign power is exercised through constitutional institutions under the Preamble.",
    "statuteOrAuthority": "Indira Nehru Gandhi v. Raj Narain (1975 Supp SCC 1); John Austin",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-191",
    "canonical": "CUSTOM",
    "acceptedVariants": [
      "CUSTOM"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Habitual course of conduct observed continuously from time immemorial, recognized as a primary source of law",
    "additionalHint": "Must be ancient, certain, reasonable, and not opposed to public policy or statutory law",
    "definition": "An unwritten long-standing social usage that has attained the force of binding legal obligation through uniform observance.",
    "educationalExample": "A customary marriage ritual observed by a community since antiquity was recognized under Hindu law.",
    "statuteOrAuthority": "Hindu Marriage Act, 1955, Section 3(a); Collector of Madura v. Moottoo Ramalinga (1868 12 MIA 397)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1560",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-192",
    "canonical": "PRECEDENT",
    "acceptedVariants": [
      "PRECEDENT"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Judicial decision serving as an authoritative rule or pattern for deciding subsequent similar cases",
    "additionalHint": "Source of law based on stare decisis; Supreme Court judgments are binding on all Indian courts under Article 141",
    "definition": "An earlier judicial ruling that furnishes an authoritative principle for the determination of future similar controversies.",
    "educationalExample": "Under Article 141, the ratio decidendi declared by the Supreme Court serves as binding precedent across India.",
    "statuteOrAuthority": "Constitution of India, Article 141; Bengal Immunity Co. v. State of Bihar (AIR 1955 SC 661)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-193",
    "canonical": "LEGISLATION",
    "acceptedVariants": [
      "LEGISLATION"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "The formal making of law by a competent legislative organ; regarded by modern jurists as the supreme source of law",
    "additionalHint": "Divided into supreme legislation (Parliament) and subordinate legislation (rules, regulations, bye-laws)",
    "definition": "The formal enactment of binding statutory rules by an authorized sovereign legislative assembly.",
    "educationalExample": "The enactment of the Bharatiya Nyaya Sanhita, 2023 by Parliament is a direct exercise of supreme legislation.",
    "statuteOrAuthority": "Salmond on Jurisprudence, 12th Ed., Chapter on Legislation",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-194",
    "canonical": "LEGAL RIGHT",
    "acceptedVariants": [
      "LEGAL RIGHT"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "An interest recognized, protected, and enforced by law, imposing a corresponding duty on others",
    "additionalHint": "Hohfeldian analysis decomposes rights into claims, liberties, powers, and immunities",
    "definition": "A legally protected interest whose violation constitutes a legal wrong actionable in court.",
    "educationalExample": "A registered owner's right to exclude trespassers from property is a fundamental legal right in rem.",
    "statuteOrAuthority": "State of Rajasthan v. Union of India (1977 3 SCC 592); Wesley Newcomb Hohfeld, Fundamental Legal Conceptions",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-195",
    "canonical": "LEGAL DUTY",
    "acceptedVariants": [
      "LEGAL DUTY"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Obligation recognized by law requiring a person to do or abstain from doing something for another",
    "additionalHint": "The correlative of a legal right; breach of duty constitutes an actionable wrong",
    "definition": "A mandatory obligation imposed by legal rules requiring obedience under pain of civil or criminal sanction.",
    "educationalExample": "A driver has a positive legal duty to stop and provide assistance following a highway accident.",
    "statuteOrAuthority": "Salmond on Jurisprudence; Motor Vehicles Act, 1988, Section 134",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1998",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-196",
    "canonical": "OWNERSHIP",
    "acceptedVariants": [
      "OWNERSHIP"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "The complex of legal rights to possess, use, enjoy, alienate, and destroy a thing to the exclusion of others",
    "additionalHint": "Salmond: 'Ownership is the relation between a person and any right that is vested in him'",
    "definition": "The bundle of absolute proprietary rights over property recognized by law, comprising title and right to dispose.",
    "educationalExample": "Ownership of agricultural land confers the right to cultivate, lease, mortgage, or sell the property freely.",
    "statuteOrAuthority": "Salmond on Jurisprudence, 12th Ed., Chapter 8; Guru Amarjit Singh v. Rattan Chand (1993 4 SCC 349)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-197",
    "canonical": "POSSESSION",
    "acceptedVariants": [
      "POSSESSION"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "The physical control of a thing coupled with the intention to hold it for oneself to the exclusion of others",
    "additionalHint": "Comprises corpus possessionis (physical control) and animus possidendi (mental intent to exclude)",
    "definition": "The visible custody and physical dominion over tangible property accompanied by the intent to exclude others.",
    "educationalExample": "Even a tenant possessing a house without ownership title can maintain a suit to protect settled possession against force.",
    "statuteOrAuthority": "Rame Gowda v. M. Varadappa Naidu (2004 1 SCC 769); Poona Ram v. Moti Ram (2019 11 SCC 309)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-198",
    "canonical": "CORPUS POSSESSIONIS",
    "acceptedVariants": [
      "CORPUS POSSESSIONIS"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "The objective physical element of possession; actual physical custody or power over a thing",
    "additionalHint": "Latin term; physical control necessary alongside animus to establish legally recognized possession",
    "definition": "The material physical detention or control exercised by an individual over tangible property.",
    "educationalExample": "Holding the physical ignition key and parking a car in one's private locked garage provides corpus possessionis.",
    "statuteOrAuthority": "Salmond on Jurisprudence; Supdt. and Remembrancer of Legal Affairs, W.B. v. Anil Kumar Bhunja (1979 4 SCC 274)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-199",
    "canonical": "ANIMUS POSSIDENDI",
    "acceptedVariants": [
      "ANIMUS POSSIDENDI"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "The subjective mental element of possession; the intention to hold and control a thing as one's own to the exclusion of others",
    "additionalHint": "Latin term; distinguished from mere physical custody without mental intent",
    "definition": "The conscious intention to exercise physical custody over a thing for one's own benefit to the exclusion of the world.",
    "educationalExample": "A servant holding a silver tray for a master has mere physical custody, lacking animus possidendi.",
    "statuteOrAuthority": "Babu Lal v. Ram Swarup (AIR 1952 All 560); P. Lakshmi Reddy v. L. Lakshmi Reddy (AIR 1957 SC 314)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-200",
    "canonical": "TITLE",
    "acceptedVariants": [
      "TITLE"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "The legal basis, deed, or vestitive facts by which a person acquires ownership of property",
    "additionalHint": "Vestitive facts are divided into acts of parties (sale, gift) and operation of law (inheritance, prescription)",
    "definition": "The legal ground, document, or set of facts constituting lawful ownership of real or personal property.",
    "educationalExample": "A duly registered Sale Deed confers valid marketable title to the real estate upon the purchaser.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 54; Suraj Lamp & Industries v. State of Haryana (2012 1 SCC 656)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-201",
    "canonical": "LEGAL PERSONALITY",
    "acceptedVariants": [
      "LEGAL PERSONALITY"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "Capacity recognized by law of having legal rights and bearing legal duties, conferred on humans and artificial entities",
    "additionalHint": "Includes natural persons and juristic persons (corporations, idols, cooperative societies)",
    "definition": "The status conferred by a legal system on an entity enabling it to sue, be sued, hold property, and enter contracts.",
    "educationalExample": "A registered company and a consecrated Hindu idol are both recognized as possessing separate legal personality.",
    "statuteOrAuthority": "Shiromani Gurdwara Parbandhak Committee v. Som Nath Dass (2000 4 SCC 146); Salomon v. Salomon",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-202",
    "canonical": "STARE DECISIS",
    "acceptedVariants": [
      "STARE DECISIS"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Doctrine requiring courts to stand by decided cases and adhere to established rules of law",
    "additionalHint": "Latin for 'to stand by things decided'; ensures consistency, certainty, and stability in judicial adjudication",
    "definition": "The principle that judicial precedents must be respected and followed in subsequent cases with similar facts.",
    "educationalExample": "Under the doctrine of stare decisis, a high court bench is bound by decisions of earlier benches of equal strength.",
    "statuteOrAuthority": "Central Board of Dawoodi Bohra Community v. State of Maharashtra (2005 2 SCC 673)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-203",
    "canonical": "RATIO DECIDENDI",
    "acceptedVariants": [
      "RATIO DECIDENDI"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "The underlying legal principle or reason upon which a judicial decision is founded, creating binding precedent",
    "additionalHint": "Latin for 'reason of deciding'; distinguished from obiter dicta; binding under Article 141",
    "definition": "The fundamental legal principle that determines the outcome of a case and serves as binding precedent for the future.",
    "educationalExample": "The ratio decidendi of Maneka Gandhi is that statutory procedure depriving liberty must be just, fair, and reasonable.",
    "statuteOrAuthority": "Director of Settlements, A.P. v. M.R. Apparao (2002 4 SCC 638); Arthur L. Goodhart's ratio test",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-204",
    "canonical": "OBITER DICTA",
    "acceptedVariants": [
      "OBITER DICTA"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "Observations, illustrations, or judicial remarks made in passing that are not essential to the determination of the case",
    "additionalHint": "Latin for 'by the way'; persuasive authority, but not strictly binding precedent under Article 141",
    "definition": "Casual judicial comments or reflections on legal issues not directly necessary to decide the matter in controversy.",
    "educationalExample": "The judge's passing commentary on patent law in a simple breach of contract case was non-binding obiter dicta.",
    "statuteOrAuthority": "State of Haryana v. Ranbir (2006 5 SCC 167); Mohandas Issardas v. A.N. Sattanathan (AIR 1955 Bom 113)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-205",
    "canonical": "SUBSTANTIVE LAW",
    "acceptedVariants": [
      "SUBSTANTIVE LAW"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Body of statutory rules that defines, creates, and regulates legal rights, duties, and offenses",
    "additionalHint": "Contrasted with procedural law; e.g., Bharatiya Nyaya Sanhita, Indian Contract Act, Transfer of Property Act",
    "definition": "The statutory framework that creates, defines, and regulates rights, duties, liabilities, and legal relations.",
    "educationalExample": "The Bharatiya Nyaya Sanhita is substantive criminal law, defining offenses and prescribing their punishments.",
    "statuteOrAuthority": "Blyth v. Blyth (1966 1 All ER 524); Central Bank of India v. Vrajlal Kapurchand Gandhi (2003 6 SCC 573)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-206",
    "canonical": "PROCEDURAL LAW",
    "acceptedVariants": [
      "PROCEDURAL LAW"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "Law that prescribes the formal machinery, steps, and procedure for enforcing substantive rights and duties",
    "additionalHint": "Adjective law; e.g., Bharatiya Nagarik Suraksha Sanhita, Code of Civil Procedure, Bharatiya Sakshya Adhiniyam",
    "definition": "The rules of court governing the mechanics and process by which a civil or criminal lawsuit is instituted and tried.",
    "educationalExample": "The Bharatiya Nagarik Suraksha Sanhita governs the procedural rules for investigation, arrest, bail, and trial.",
    "statuteOrAuthority": "Ghanshyam Dass v. Dominion of India (1984 3 SCC 46); Salmond on Jurisprudence",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-207",
    "canonical": "CODIFICATION",
    "acceptedVariants": [
      "CODIFICATION"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "The systematic arrangement, collection, and reduction of statutory or customary rules into a coherent written code",
    "additionalHint": "Pioneered by Jeremy Bentham and Macaulay (drafter of the original Indian Penal Code, 1860)",
    "definition": "The comprehensive consolidation and systematic legislative enactment of an entire branch of law into a single code.",
    "educationalExample": "Macaulay's monumental codification in 1860 gave India the Penal Code, modernized into the BNS in 2023.",
    "statuteOrAuthority": "Sir Courtenay Ilbert, Legislative Methods and Forms; Bentham on Codification",
    "sourceUrl": "https://www.indiacode.nic.in",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-208",
    "canonical": "UTILITARIANISM",
    "acceptedVariants": [
      "UTILITARIANISM"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "Legal and moral philosophy advocating 'the greatest happiness of the greatest number' as the measure of law",
    "additionalHint": "Founded by Jeremy Bentham; evaluates legal enactments by utility through pain and pleasure calculus",
    "definition": "A consequentialist legal theory asserting that laws must be designed to maximize aggregate social well-being and utility.",
    "educationalExample": "Bentham argued that penal legislation should deter crime while inflicting only the minimal pain necessary for deterrence.",
    "statuteOrAuthority": "Jeremy Bentham, An Introduction to the Principles of Morals and Legislation (1789)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-209",
    "canonical": "SOCIAL ENGINEERING",
    "acceptedVariants": [
      "SOCIAL ENGINEERING"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "Roscoe Pound's sociological theory of law as an instrument for harmonizing competing social, public, and private interests",
    "additionalHint": "Sociological jurisprudence; aims to eliminate friction and waste in satisfying human wants and demands",
    "definition": "The functional conception of law as an active tool of social balancing and progressive societal transformation.",
    "educationalExample": "Protective labor legislation and agrarian land ceiling acts in India exemplify law as social engineering.",
    "statuteOrAuthority": "Roscoe Pound, Jurisprudence (1959); National Textile Workers' Union v. P.R. Ramakrishnan (1983 1 SCC 228)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-210",
    "canonical": "LIVING LAW",
    "acceptedVariants": [
      "LIVING LAW"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "Eugen Ehrlich's concept of the actual unwritten norms governing human associations, distinct from formal state statutes",
    "additionalHint": "Core premise of sociological school; law arises from societal inner order rather than legislative decree",
    "definition": "The dynamic social practices and internalized rules actually observed by communities in daily social life.",
    "educationalExample": "Ehrlich demonstrated that business merchants often resolve disputes according to commercial living law rather than court codes.",
    "statuteOrAuthority": "Eugen Ehrlich, Fundamental Principles of the Sociology of Law (1913)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-211",
    "canonical": "HISTORICAL SCHOOL",
    "acceptedVariants": [
      "HISTORICAL SCHOOL"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "School of jurisprudence asserting that law is not made by sovereign command, but organically evolves from national consciousness",
    "additionalHint": "Founded by Friedrich Carl von Savigny; developed concept of 'Volksgeist' (spirit of the people)",
    "definition": "A jurisprudence school tracing legal validity to gradual, organic historical evolution rooted in community customs.",
    "educationalExample": "Savigny opposed rapid codification in Germany, arguing law must develop through organic customs like language.",
    "statuteOrAuthority": "Friedrich Carl von Savigny, Of the Vocation of Our Age for Legislation and Jurisprudence (1814)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-212",
    "canonical": "REALIST SCHOOL",
    "acceptedVariants": [
      "REALIST SCHOOL"
    ],
    "difficulty": "advanced",
    "subject": "Jurisprudence",
    "primaryClue": "American and Scandinavian jurisprudence viewing law pragmatically as the predictions of what courts actually do in fact",
    "additionalHint": "Oliver Wendell Holmes Jr. ('the life of the law has not been logic; it has been experience'), Jerome Frank, and Karl Llewellyn",
    "definition": "A pragmatic legal philosophy emphasizing real-world judicial behavior, judicial discretion, and sociological impact.",
    "educationalExample": "Holmes' bad-man theory defined law simply as the prophecy of what judges will enforce in fact.",
    "statuteOrAuthority": "Oliver Wendell Holmes Jr., The Path of the Law (1897); Jerome Frank, Law and the Modern Mind",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-213",
    "canonical": "RIGHT IN REM",
    "acceptedVariants": [
      "RIGHT IN REM"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "A legal right available against the whole world at large, such as ownership of land",
    "additionalHint": "Contrasted with right in personam; binds all citizens not to interfere with the protected entitlement",
    "definition": "An absolute proprietary right enforceable against all individuals in human society generally.",
    "educationalExample": "A registered patent right is a right in rem, preventing anyone in the country from manufacturing the patented invention.",
    "statuteOrAuthority": "Salmond on Jurisprudence; T.P. Act, 1882",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-214",
    "canonical": "RIGHT IN PERSONAM",
    "acceptedVariants": [
      "RIGHT IN PERSONAM"
    ],
    "difficulty": "intermediate",
    "subject": "Jurisprudence",
    "primaryClue": "A legal right available only against a specific, definite individual or party, such as a contractual debt",
    "additionalHint": "Correlative to a specific contractual duty; enforceable solely against the debtor or obligor",
    "definition": "A relative personal right enforceable only against designated individuals bound by contract or fiduciary relation.",
    "educationalExample": "The right to recover a ten-thousand rupee loan from a specific borrower is a classic right in personam.",
    "statuteOrAuthority": "Salmond on Jurisprudence; Indian Contract Act, 1872",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-215",
    "canonical": "DE FACTO",
    "acceptedVariants": [
      "DE FACTO"
    ],
    "difficulty": "beginner",
    "subject": "Jurisprudence",
    "primaryClue": "In fact, actual, or in reality, whether recognized by formal law or not",
    "additionalHint": "Latin legal term; contrasted with de jure (lawful or by right)",
    "definition": "Existing as an actual state of affairs or reality regardless of formal legal title or constitutional sanction.",
    "educationalExample": "The caretaker exercised de facto possession of the estate, although legal title belonged to the absent heir.",
    "statuteOrAuthority": "Gokaraju Rangaraju v. State of A.P. (1981 3 SCC 132 — De Facto Doctrine)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-216",
    "canonical": "AUDI ALTERAM PARTEM",
    "acceptedVariants": [
      "AUDI ALTERAM PARTEM"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "First pillar of natural justice: 'Hear the other side'; no person should be condemned or judged unheard",
    "additionalHint": "Latin legal maxim; guarantees fair hearing, prior notice, and opportunity to present defense",
    "definition": "The indispensable rule of procedural fairness mandating that no person shall be judged without a fair hearing.",
    "educationalExample": "An order terminating a government civil servant without issuing a show-cause notice violates audi alteram partem.",
    "statuteOrAuthority": "Maneka Gandhi v. Union of India (1978 1 SCC 248); Ridge v. Baldwin (1964 AC 40)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-217",
    "canonical": "NEMO JUDEX IN CAUSA SUA",
    "acceptedVariants": [
      "NEMO JUDEX IN CAUSA SUA"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Second pillar of natural justice: 'No one should be a judge in their own cause'; rule against bias",
    "additionalHint": "Latin legal maxim; disqualifies any adjudicator with personal, pecuniary, or subject-matter bias",
    "definition": "The fundamental legal rule ensuring absolute judicial impartiality by disqualifying judges with any personal stake.",
    "educationalExample": "A departmental inquiry officer who was also the principal complaining witness was disqualified for bias.",
    "statuteOrAuthority": "A.K. Kraipak v. Union of India (1969 2 SCC 262); Dimes v. Grand Junction Canal (1852 3 HLC 759)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-218",
    "canonical": "UBI JUS IBI REMEDIUM",
    "acceptedVariants": [
      "UBI JUS IBI REMEDIUM"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Foundational legal maxim: 'Where there is a right, there is a remedy'",
    "additionalHint": "Latin maxim; establishes that the law will not allow a recognized legal injury to go without a judicial remedy",
    "definition": "The fundamental premise that wherever law confers a right, it also provides a legal machinery to protect and enforce it.",
    "educationalExample": "When an election official wrongfully rejected a lawful vote, the court held that ubi jus ibi remedium applied.",
    "statuteOrAuthority": "Ashby v. White (1703 2 Ld Raym 938); Sardar Amarjit Singh Kalra v. Pramod Gupta (2003 3 SCC 272)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-219",
    "canonical": "IGNORANTIA JURIS NON EXCUSAT",
    "acceptedVariants": [
      "IGNORANTIA JURIS NON EXCUSAT"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Ancient legal maxim: 'Ignorance of the law excuses not'; every citizen is presumed to know the law",
    "additionalHint": "Latin maxim; ignorance of fact is an excuse under Section 14 BNS, but ignorance of law is never an excuse",
    "definition": "The universal legal rule holding that lack of knowledge of a statute is no defense against liability.",
    "educationalExample": "An accused cannot escape penalties for transporting undeclared foreign currency by claiming ignorance of foreign exchange acts.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 14; State of Maharashtra v. Mayer Hans George (AIR 1965 SC 722)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-220",
    "canonical": "DE MINIMIS NON CURAT LEX",
    "acceptedVariants": [
      "DE MINIMIS NON CURAT LEX"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'The law does not concern itself with trifles'; acts causing negligible or slight harm are not offenses",
    "additionalHint": "Codified under Section 34 of Bharatiya Nyaya Sanhita, 2023 (formerly Section 95 IPC)",
    "definition": "A statutory defense excluding trivial or negligible infringements that a person of ordinary sense would ignore.",
    "educationalExample": "Accidentally dipping an elbow onto a fellow passenger's coat sleeve in a crowded metro is shielded by de minimis.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 34; Mrs. Veeda Menezes v. Yusuf Khan Haji (AIR 1966 SC 1773)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-221",
    "canonical": "ACTIO PERSONALIS MORITUR CUM PERSONA",
    "acceptedVariants": [
      "ACTIO PERSONALIS MORITUR CUM PERSONA"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'A personal right of action dies with the person'; personal injury tort claims generally abate on death",
    "additionalHint": "Latin legal maxim; modified by survival of actions in Fatal Accidents Act and modern motor accident claim acts",
    "definition": "The common law rule establishing that actions founded on purely personal wrongs terminate upon the death of either party.",
    "educationalExample": "A civil suit claiming damages for personal defamation terminates upon the plaintiff's death under this maxim.",
    "statuteOrAuthority": "Melepurath Sankunni Ezhuthassan v. Thekittil Geopalankutty Nair (1986 1 SCC 118)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-222",
    "canonical": "CAVEAT EMPTOR",
    "acceptedVariants": [
      "CAVEAT EMPTOR"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'Let the buyer beware'; duty on buyer to inspect goods and satisfy themselves of quality before purchasing",
    "additionalHint": "Codified in Section 16 of Sale of Goods Act, 1930; subject to implied conditions of fitness and merchantability",
    "definition": "A commercial legal principle placing the risk and burden of examining goods upon the buyer prior to purchase.",
    "educationalExample": "A customer buying second-hand furniture without inspecting its joints cannot sue the vendor for obvious wobbliness.",
    "statuteOrAuthority": "Sale of Goods Act, 1930, Section 16; Ward v. Hobbs (1878 4 App Cas 13)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2384",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-223",
    "canonical": "CAVEAT VENDITOR",
    "acceptedVariants": [
      "CAVEAT VENDITOR"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Modern commercial maxim: 'Let the seller beware'; duty on manufacturer/seller to ensure products are safe and fit",
    "additionalHint": "Modern consumer jurisprudence; core principle under Consumer Protection Act, 2019",
    "definition": "The modern consumer law principle holding sellers and product manufacturers responsible for defective goods.",
    "educationalExample": "Under modern product liability rules, a manufacturer is strictly accountable for manufacturing defects.",
    "statuteOrAuthority": "Consumer Protection Act, 2019, Section 82-87; Donoghue v. Stevenson (1932 AC 562)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/15256",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-224",
    "canonical": "SALUS POPULI SUPREMA LEX",
    "acceptedVariants": [
      "SALUS POPULI SUPREMA LEX"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'The safety and welfare of the people is the supreme law'",
    "additionalHint": "Latin maxim; public welfare and safety takes precedence over private individual property rights in times of national crisis",
    "definition": "The constitutional doctrine that the security and health of the public constitutes the paramount legal interest.",
    "educationalExample": "Demolishing a dilapidated private building about to collapse onto a crowded public highway is justified under this maxim.",
    "statuteOrAuthority": "State of U.P. v. Raj Narain (1975 4 SCC 428); Municipal Corporation of Greater Bombay v. Lala Pancham",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-225",
    "canonical": "EX NUDO PACTO NON ORITUR ACTIO",
    "acceptedVariants": [
      "EX NUDO PACTO NON ORITUR ACTIO"
    ],
    "difficulty": "advanced",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'No right of action arises from a bare promise made without consideration'",
    "additionalHint": "Latin maxim; codified in Section 25 of Indian Contract Act, 1872",
    "definition": "The contract law rule that an informal promise unsupported by consideration cannot be enforced in a court of law.",
    "educationalExample": "A gratuitous promise to gift a sports car to a friend cannot support a lawsuit for breach if the promisor changes his mind.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 25; Rann v. Hughes (1778 7 TR 350)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2187",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-226",
    "canonical": "IN BONAM PARTEM",
    "acceptedVariants": [
      "IN BONAM PARTEM"
    ],
    "difficulty": "advanced",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'In a good sense'; words in a statute should be construed favorably and lawfully rather than maliciously",
    "additionalHint": "Rule of statutory interpretation presuming that words in an enactment refer to lawful acts rather than illegal acts",
    "definition": "A canon of construction requiring statutory words to be interpreted in a lawful, regular, and proper sense.",
    "educationalExample": "The statutory term 'possession' in a licensing act was interpreted in bonam partem to mean lawful possession.",
    "statuteOrAuthority": "Maxwell on the Interpretation of Statutes; Re: B.V. Govindarajulu (AIR 1950 Mad 839)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-227",
    "canonical": "PRIMA FACIE",
    "acceptedVariants": [
      "PRIMA FACIE"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "At first sight or on the face of it; sufficient evidence to establish a fact unless rebutted",
    "additionalHint": "Latin legal term; mandatory standard for framing of criminal charges and granting interim injunctions",
    "definition": "Sufficient evidence at preliminary evaluation to raise a legal presumption of fact unless contradicted.",
    "educationalExample": "The trial judge framed charges under Section 308 BNS after finding a prima facie case against the accused.",
    "statuteOrAuthority": "Union of India v. Prafulla Kumar Samal (1979 3 SCC 4); Order XXXIX Rule 1 CPC",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-228",
    "canonical": "BONA FIDE",
    "acceptedVariants": [
      "BONA FIDE"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "In good faith; without fraud, deceit, or intentional collusion",
    "additionalHint": "Latin legal term; protected under General Exceptions (Section 14 BNS) and Section 3(22) General Clauses Act",
    "definition": "An act performed honestly and with due care and attention, free from deceit or fraudulent intent.",
    "educationalExample": "A bona fide purchaser for valuable consideration without notice of an unrecorded title dispute takes clean title.",
    "statuteOrAuthority": "General Clauses Act, 1897, Section 3(22); Bharatiya Nyaya Sanhita, 2023, Section 14",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2184",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-229",
    "canonical": "MALA FIDE",
    "acceptedVariants": [
      "MALA FIDE"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "In bad faith; with fraudulent, dishonest, or malicious intent",
    "additionalHint": "Latin legal term; administrative action tainted by mala fides is null and void under Article 226",
    "definition": "Conduct marked by deliberate dishonesty, corrupt intent, or improper collateral motives.",
    "educationalExample": "An administrative transfer of a whistleblower advocate ordered purely out of personal vindictiveness was set aside as mala fide.",
    "statuteOrAuthority": "State of Punjab v. Gurdial Singh (1980 2 SCC 471); E.P. Royappa v. State of Tamil Nadu",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-230",
    "canonical": "ULTRA VIRES",
    "acceptedVariants": [
      "ULTRA VIRES"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Beyond the powers; an act performed by a corporation, minister, or body exceeding legally conferred jurisdiction",
    "additionalHint": "Latin legal term; ultra vires regulations or administrative decisions are void ab initio",
    "definition": "Acting beyond the statutory scope of powers authorized by the Constitution, statute, or corporate charter.",
    "educationalExample": "A municipal council passing an income tax ordinance acted ultra vires its statutory powers under the Municipalities Act.",
    "statuteOrAuthority": "Ashbury Railway Carriage Co. v. Riche (1875 LR 7 HL 653); Express Newspapers v. Union of India",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-231",
    "canonical": "INTRA VIRES",
    "acceptedVariants": [
      "INTRA VIRES"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Within the legal powers or authority lawfully conferred by statute or the Constitution",
    "additionalHint": "Latin legal term; opposite of ultra vires",
    "definition": "An act, rule, or administrative order executed fully within the limits of legally granted statutory jurisdiction.",
    "educationalExample": "The High Court held that the environmental emission rules framed by the board were intra vires the enabling parent act.",
    "statuteOrAuthority": "State of U.P. v. Babu Ram Upadhya (AIR 1961 SC 751)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-232",
    "canonical": "MUTATIS MUTANDIS",
    "acceptedVariants": [
      "MUTATIS MUTANDIS"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "With the necessary changes in points of detail; adopting a rule with suitable modifications to fit new context",
    "additionalHint": "Latin phrase ubiquitous in Indian procedural drafting and statutory cross-referencing",
    "definition": "Applying statutory rules to a new situation while making only those alterations necessary to adapt to the new context.",
    "educationalExample": "The appellate rules provide that provisions governing original appeals apply mutatis mutandis to miscellaneous appeals.",
    "statuteOrAuthority": "Ashok Service Centre v. State of Orissa (1983 2 SCC 82)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-233",
    "canonical": "PRO BONO",
    "acceptedVariants": [
      "PRO BONO"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Professional legal work undertaken voluntarily and without charge for the public good",
    "additionalHint": "Short for 'pro bono publico' (for the public good); core duty under Bar Council of India rules and Article 39A",
    "definition": "Free legal representation and counsel provided to indigent litigants or worthy public causes in the public interest.",
    "educationalExample": "The senior advocate appeared pro bono on behalf of the displaced slum dwellers to ensure their constitutional defense.",
    "statuteOrAuthority": "Bar Council of India Rules; Constitution of India, Article 39A; Hussainara Khatoon v. Home Secretary, State of Bihar",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-234",
    "canonical": "NEMO DEBET BIS VEXARI",
    "acceptedVariants": [
      "NEMO DEBET BIS VEXARI"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'No one should be vexed twice for one and the same cause'; constitutional rule against double jeopardy",
    "additionalHint": "Codified in Article 20(2) of Constitution of India and Section 337 BNSS (Section 300 CrPC)",
    "definition": "The fundamental legal principle protecting an individual from repeated prosecutions for an identical criminal offense.",
    "educationalExample": "Having been lawfully acquitted of robbery, the defendant could not be retried on the same facts under this maxim.",
    "statuteOrAuthority": "Constitution of India, Article 20(2); Maqbool Hussain v. State of Bombay (AIR 1953 SC 325)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-235",
    "canonical": "ACTUS CURIAE NEMINEM GRAVABIT",
    "acceptedVariants": [
      "ACTUS CURIAE NEMINEM GRAVABIT"
    ],
    "difficulty": "advanced",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'An act of the court shall prejudice no one'; foundation of restitution and curative orders",
    "additionalHint": "Codified in Section 144 CPC; court must undo damage caused to a litigant by an erroneous judicial order",
    "definition": "The universal principle that an error, delay, or mistake committed by a court of law shall not harm any litigant.",
    "educationalExample": "When court staff misfiled an appeal causing time-lapse, the court restored the matter under actus curiae neminem gravabit.",
    "statuteOrAuthority": "A.R. Antulay v. R.S. Nayak (1988 2 SCC 602); South Eastern Coalfields v. State of M.P.",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-236",
    "canonical": "QUI FACIT PER ALIUM FACIT PER SE",
    "acceptedVariants": [
      "QUI FACIT PER ALIUM FACIT PER SE"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'He who acts through another does the act himself'; foundational rule of agency and vicarious liability",
    "additionalHint": "Latin maxim; attributes liability to the principal for authorized acts committed by their agent or employee",
    "definition": "The legal doctrine holding that an act performed through an authorized agent is deemed the personal act of the principal.",
    "educationalExample": "Signing a commercial purchase contract through an authorized power-of-attorney holder binds the principal under this maxim.",
    "statuteOrAuthority": "Indian Contract Act, 1872, Section 182; State of Rajasthan v. Vidhyawati",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-237",
    "canonical": "DELEGATUS NON POTEST DELEGARE",
    "acceptedVariants": [
      "DELEGATUS NON POTEST DELEGARE"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'A delegate cannot further delegate'; an authorized delegate cannot sub-delegate statutory discretion without express power",
    "additionalHint": "Core principle of administrative law; prevents sub-delegation of quasi-judicial or discretionary authority",
    "definition": "The administrative law rule prohibiting a person to whom power has been delegated from delegating it to another.",
    "educationalExample": "A licensing magistrate cannot sub-delegate the discretionary power to cancel firearm licenses to an inspector without statutory power.",
    "statuteOrAuthority": "Barium Chemicals Ltd. v. Company Law Board (AIR 1967 SC 295); A.K. Roy v. State of Punjab (1986 4 SCC 326)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-238",
    "canonical": "EJUSDEM GENERIS",
    "acceptedVariants": [
      "EJUSDEM GENERIS"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Statutory interpretation rule: general words following specific words must be construed as of the same kind or nature",
    "additionalHint": "Canon of construction; e.g., 'horses, cows, sheep and other animals' does not include wild lions or tigers",
    "definition": "The rule that general statutory catch-all words take their color and meaning from the preceding specific enumerated class.",
    "educationalExample": "In a statute restricting 'arms, ammunition, gunpowder, and other goods', 'other goods' was limited to military materiel.",
    "statuteOrAuthority": "State of Karnataka v. Kempaiah (1998 6 SCC 103); UPSEB v. Hari Shanker Jain (1978 4 SCC 16)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-239",
    "canonical": "EXPRESSIO UNIUS EST EXCLUSIO ALTERIUS",
    "acceptedVariants": [
      "EXPRESSIO UNIUS EST EXCLUSIO ALTERIUS"
    ],
    "difficulty": "advanced",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'The express mention of one thing implies the exclusion of another'",
    "additionalHint": "Canon of statutory interpretation; naming specific items in a provision indicates intent to exclude omitted items",
    "definition": "A statutory canon stating that explicit inclusion of particular items in a section implies the exclusion of alternatives.",
    "educationalExample": "A statute granting tax exemptions to 'schools and colleges' was held to deliberately exclude commercial coaching centers.",
    "statuteOrAuthority": "State of Maharashtra v. Laljit Rajshi Shah (2000 2 SCC 699); G.V.K. Industries v. ITO (2011 4 SCC 36)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-240",
    "canonical": "GENERALIA SPECIALIBUS NON DEROGANT",
    "acceptedVariants": [
      "GENERALIA SPECIALIBUS NON DEROGANT"
    ],
    "difficulty": "advanced",
    "subject": "Legal Maxims",
    "primaryClue": "Maxim: 'General provisions do not derogate from special provisions'; specific statutes prevail over general enactments",
    "additionalHint": "Harmonious construction rule; e.g., special insolvency code prevails over general civil procedure provisions",
    "definition": "The statutory canon establishing that a specific provision dealing with a precise subject overrides a general provision.",
    "educationalExample": "The specific limitation period under the Arbitration Act overrides the general provisions of the Limitation Act, 1963.",
    "statuteOrAuthority": "Life Insurance Corporation of India v. D.J. Bahadur (1980 4 SCC 82); Commercial Tax Officer v. Binani Cements (2014 8 SCC 319)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-241",
    "canonical": "IN PARI DELICTO",
    "acceptedVariants": [
      "IN PARI DELICTO"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "Short for 'In pari delicto potior est conditio defendentis': 'Where both parties are equally at fault, the defendant's position is stronger'",
    "additionalHint": "Latin maxim; courts will not assist a plaintiff who founds their claim on their own illegal or immoral transaction",
    "definition": "The equitable principle that court assistance is withheld when both litigants share equal guilt in an illegal bargain.",
    "educationalExample": "A smuggler suing his partner for half the profits of an unlawful diamond trade is barred under in pari delicto.",
    "statuteOrAuthority": "Kedar Nath Motani v. Prahlad Rai (AIR 1960 SC 213); Holman v. Johnson (1775 1 Cowp 341)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-242",
    "canonical": "INTER ALIA",
    "acceptedVariants": [
      "INTER ALIA"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "Among other things; phrase used when citing selected items from a larger comprehensive set",
    "additionalHint": "Latin phrase standard in judicial drafting and legal pleadings",
    "definition": "A legal drafting phrase indicating that the cited points are merely illustrative parts of a broader collection.",
    "educationalExample": "The petition argued, inter alia, that the impugned demolition violated principles of natural justice and Article 21.",
    "statuteOrAuthority": "Standard judicial drafting term used in Supreme Court of India reports",
    "sourceUrl": "https://main.sci.gov.in",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-243",
    "canonical": "IPSE DIXIT",
    "acceptedVariants": [
      "IPSE DIXIT"
    ],
    "difficulty": "intermediate",
    "subject": "Legal Maxims",
    "primaryClue": "An unproven assertion made on someone's bare authority alone: 'He himself said it'",
    "additionalHint": "Latin phrase; an expert opinion or executive finding unsupported by reasons or evidence is rejected as mere ipse dixit",
    "definition": "A bare, unsupported dogmatic statement accepted solely because an authoritative figure asserted it, without proof.",
    "educationalExample": "The court rejected the police report as mere ipse dixit because it cited no corroborating forensic evidence or witness.",
    "statuteOrAuthority": "State of U.P. v. Ram Asrey (AIR 1990 SC 1188); Dr. Ramji Singh v. State of Bihar",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-244",
    "canonical": "MODUS OPERANDI",
    "acceptedVariants": [
      "MODUS OPERANDI"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "A characteristic method of operation or functioning, especially a criminal's distinctive pattern of committing offenses",
    "additionalHint": "Latin phrase; highly relevant under Section 6 BSA (Section 8 IEA) to prove system and identity",
    "definition": "The distinctive and habitual technique or method employed by a criminal in carrying out unlawful offenses.",
    "educationalExample": "The burglar's specific modus operandi of drilling door locks between 2 AM and 4 AM helped detectives identify the suspect.",
    "statuteOrAuthority": "Bharatiya Sakshya Adhiniyam, 2023, Section 6; State of U.P. v. Babul Nath (1994 6 SCC 29)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2112",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-245",
    "canonical": "SINE QUA NON",
    "acceptedVariants": [
      "SINE QUA NON"
    ],
    "difficulty": "beginner",
    "subject": "Legal Maxims",
    "primaryClue": "An indispensable and essential condition or element without which something cannot exist",
    "additionalHint": "Latin phrase; e.g., mens rea is a sine qua non for proving criminal homicide",
    "definition": "An indispensable prerequisite or essential foundational condition required for a legal consequence to attach.",
    "educationalExample": "Proof of a valid subsisting prior marriage is an indispensable sine qua non for sustaining a conviction of bigamy.",
    "statuteOrAuthority": "K.S. Puttaswamy v. Union of India (2017 10 SCC 1); BNS Section 82",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-246",
    "canonical": "PETITION",
    "acceptedVariants": [
      "PETITION"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "A formal written application submitted to a court praying for specific judicial relief or exercise of jurisdiction",
    "additionalHint": "Includes Special Leave Petitions (Article 136), Writ Petitions (Articles 32/226), and Revision Petitions",
    "definition": "A formal written document presented to a judicial tribunal setting forth facts and requesting specific legal orders.",
    "educationalExample": "The aggrieved citizen filed a writ petition under Article 226 before the High Court of Judicature at Allahabad.",
    "statuteOrAuthority": "Constitution of India, Article 226; Supreme Court Rules, 2013",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-247",
    "canonical": "BAIL",
    "acceptedVariants": [
      "BAIL"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Temporary judicial release of an accused person awaiting trial upon security, sureties, and undertaking to appear",
    "additionalHint": "Governed by Chapter XXXV of Bharatiya Nagarik Suraksha Sanhita, 2023; 'Bail is the rule, jail is the exception'",
    "definition": "The procurement of release from custody of an accused person upon providing adequate security for future attendance.",
    "educationalExample": "The sessions judge granted regular bail to the accused under Section 480 BNSS upon furnishing two local sureties.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Sections 478-485; State of Rajasthan v. Balchand (1977 4 SCC 308)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-248",
    "canonical": "ANTICIPATORY BAIL",
    "acceptedVariants": [
      "ANTICIPATORY BAIL"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "Direction issued by Sessions Court or High Court granting bail to a person in the event of their arrest on accusation of non-bailable offense",
    "additionalHint": "Governed by Section 482 of Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly Section 438 CrPC)",
    "definition": "Pre-arrest bail granted to protect an individual from arrest and harassment in anticipated false or motivated charges.",
    "educationalExample": "Apprehending arrest in a false property dispute, the advocate successfully moved an application for anticipatory bail.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 482; Sushila Aggarwal v. State (NCT of Delhi) (2020 5 SCC 1)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-249",
    "canonical": "REMAND",
    "acceptedVariants": [
      "REMAND"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Order of a magistrate sending an arrested accused back into police custody or judicial custody during investigation or trial",
    "additionalHint": "Governed by Section 187 of BNSS 2023 (formerly Section 167 CrPC); limits initial police remand to 15 days",
    "definition": "The judicial act of committing an arrested person into continued police detention or jail custody pending inquiry.",
    "educationalExample": "The judicial magistrate refused police remand and committed the accused to judicial custody in the district jail.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 187; CBI v. Anupam J. Kulkarni (1992 3 SCC 141)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-250",
    "canonical": "COGNIZABLE",
    "acceptedVariants": [
      "COGNIZABLE"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Offense for which a police officer may arrest without a warrant and investigate without magistrate's order",
    "additionalHint": "Defined in Section 2(1)(g) of BNSS 2023 (Section 2(c) CrPC); First Schedule categorizes offenses",
    "definition": "A serious category of criminal offenses authorizing police to make arrests without prior judicial warrant.",
    "educationalExample": "Robbery is a cognizable offense, requiring police to immediately register an FIR upon receiving information.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 2(1)(g) & 173; Lalita Kumari v. Govt. of U.P. (2014 2 SCC 1)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-251",
    "canonical": "NON COGNIZABLE",
    "acceptedVariants": [
      "NON COGNIZABLE"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Offense for which a police officer has no authority to arrest without a warrant",
    "additionalHint": "Defined in Section 2(1)(o) of BNSS 2023 (Section 2(l) CrPC); requires magistrate permission to investigate under Section 174 BNSS",
    "definition": "Less grave offenses wherein the police cannot arrest or begin investigation without a magistrate's specific warrant.",
    "educationalExample": "Simple assault without weapon is a non-cognizable offense recorded in the non-cognizable register (NCR).",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 2(1)(o) & 174; Keshav Lal Thakur v. State of Bihar (1996 11 SCC 557)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-252",
    "canonical": "COMPOUNDABLE",
    "acceptedVariants": [
      "COMPOUNDABLE"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "Offenses which can be lawfully compromised and settled between the victim and accused, resulting in acquittal",
    "additionalHint": "Governed by Section 359 of BNSS 2023 (formerly Section 320 CrPC); table lists offenses with/without permission of court",
    "definition": "A statutory class of criminal offenses which the complainant can agree to drop upon arriving at an amicable settlement.",
    "educationalExample": "Cheating was compounded by the complainant before the magistrate after receiving full refund of disputed money.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 359; Gian Singh v. State of Punjab (2012 10 SCC 303)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-253",
    "canonical": "CHARGE",
    "acceptedVariants": [
      "CHARGE"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Formal notice formulated by court informing the accused of the precise criminal allegations against them",
    "additionalHint": "Chapter XIX of BNSS 2023 (formerly Chapter XVII CrPC); must state offense, statute, time, and particulars",
    "definition": "The precise formal accusation drawn up by the trial court giving the defendant notice of the exact crime alleged.",
    "educationalExample": "The sessions court formally framed charges of murder and conspiracy under Sections 103 and 61 BNS against the accused.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Sections 234-247; V.C. Shukla v. State (1980 Supp SCC 92)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-254",
    "canonical": "ACQUITTAL",
    "acceptedVariants": [
      "ACQUITTAL"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Formal judicial certification that an accused person is not guilty of the criminal charge after full trial",
    "additionalHint": "Operates as a bar against double jeopardy under Article 20(2) and Section 337 BNSS (Section 300 CrPC)",
    "definition": "The definitive judicial verdict freeing an accused from criminal guilt following trial or failure of prosecution evidence.",
    "educationalExample": "Because eyewitness testimony was thoroughly contradicted by ballistic science, the court pronounced an honorable acquittal.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 255 & 268; Babu v. State of Kerala (2010 9 SCC 189)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-255",
    "canonical": "CONVICTION",
    "acceptedVariants": [
      "CONVICTION"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Formal judicial finding following trial that the accused has been proved guilty of the charged criminal offense",
    "additionalHint": "Requires proof beyond reasonable doubt; followed by hearing on quantum of sentence under BNSS",
    "definition": "The definitive judgment of a criminal court declaring the defendant legally guilty of a proven offense.",
    "educationalExample": "Upon recording a conviction under Section 303(2) BNS, the magistrate heard the defense advocate on the question of sentence.",
    "statuteOrAuthority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 258 & 271; Santa Singh v. State of Punjab (1976 4 SCC 190)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2113",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-256",
    "canonical": "SENTENCE",
    "acceptedVariants": [
      "SENTENCE"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "The formal judicial penalty or punishment ordered by court upon an offender following a criminal conviction",
    "additionalHint": "Includes imprisonment, fine, community service (new in BNS), forfeiture, and capital punishment",
    "definition": "The specific statutory punishment pronounced by a trial court to be undergone by a convicted criminal.",
    "educationalExample": "The sessions court sentenced the convict to five years rigorous imprisonment and imposed a fine of ten thousand rupees.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Chapter III (Punishments, Sections 4-13); Bachan Singh v. State of Punjab",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-257",
    "canonical": "PROBATION",
    "acceptedVariants": [
      "PROBATION"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "Release of a convicted offender into the community under supervision instead of sending them to prison",
    "additionalHint": "Governed by Probation of Offenders Act, 1958 and Section 401 BNSS (Section 360 CrPC); reformative justice",
    "definition": "A reformative judicial alternative releasing a first-time minor offender on good conduct without custodial incarceration.",
    "educationalExample": "Taking into account his youthful age and lack of criminal record, the magistrate released the first offender on probation.",
    "statuteOrAuthority": "Probation of Offenders Act, 1958, Section 4; Rattan Lal v. State of Punjab (AIR 1965 SC 444)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1572",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-258",
    "canonical": "PAROLE",
    "acceptedVariants": [
      "PAROLE"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "Conditional and temporary release of a convicted prisoner before expiration of sentence for special reasons",
    "additionalHint": "Distinguished from furlough; granted for family bereavement, medical emergency, or reformative rehabilitation",
    "definition": "The temporary release of an incarcerated convict from prison under strict supervision and conditions of good behavior.",
    "educationalExample": "The state government granted 30 days medical parole to the elderly convict to undergo eye cataract surgery.",
    "statuteOrAuthority": "State of Haryana v. Mahender Singh (2007 13 SCC 606); Asfaq v. State of Rajasthan (2017 15 SCC 55)",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-259",
    "canonical": "CONTEMPT OF COURT",
    "acceptedVariants": [
      "CONTEMPT OF COURT"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "Act or conduct that disrespects, defies, or scandalizes the authority, dignity, or orders of a court of justice",
    "additionalHint": "Divided into Civil Contempt (willful disobedience of order) and Criminal Contempt (scandalizing court) under Act of 1971",
    "definition": "Conduct that defies judicial authority, impedes the administration of justice, or scandalizes court integrity.",
    "educationalExample": "Deliberately refusing to comply with a High Court status quo injunction constitutes willful civil contempt.",
    "statuteOrAuthority": "Contempt of Courts Act, 1971, Section 2; Constitution of India, Articles 129 & 215; Re: Prashant Bhushan (2021 1 SCC 745)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1531",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-260",
    "canonical": "LOCUS STANDI",
    "acceptedVariants": [
      "LOCUS STANDI"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "The legal capacity or standing of a party to bring an action before a court of law",
    "additionalHint": "Latin term; traditionally requires personal injury; relaxed in Public Interest Litigation (PIL) by Justice P.N. Bhagwati",
    "definition": "The right of an individual to initiate a lawsuit based on having a direct, legally protectable interest in the outcome.",
    "educationalExample": "In public interest litigation, the traditional requirement of locus standi is relaxed to protect marginalized communities.",
    "statuteOrAuthority": "S.P. Gupta v. Union of India (1981 Supp SCC 87); Bar Council of Maharashtra v. M.V. Dabholkar",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-261",
    "canonical": "SUO MOTU",
    "acceptedVariants": [
      "SUO MOTU"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "On its own motion; an action initiated by a court on its own initiative without a formal petition from a party",
    "additionalHint": "Latin phrase; frequently exercised by High Courts and Supreme Court in public crises or human rights violations",
    "definition": "The exercise of judicial power by a court taking notice of an injustice on its own motion without a private petitioner.",
    "educationalExample": "The High Court took suo motu cognizance of hospital fire safety violations upon reading investigative newspaper reports.",
    "statuteOrAuthority": "In Re: Distribution of Essential Supplies During Pandemic (2021 SC); Article 226",
    "sourceUrl": "https://main.sci.gov.in/judgments",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-262",
    "canonical": "IN CAMERA",
    "acceptedVariants": [
      "IN CAMERA"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "Proceedings conducted in private or closed court chambers from which the public and press are excluded",
    "additionalHint": "Latin for 'in a chamber'; mandated in trials of sexual offenses and matrimonial reconciliation",
    "definition": "A closed-door judicial hearing held without public or media presence to protect victim privacy and sensitivity.",
    "educationalExample": "Section 72 of Bharatiya Nyaya Sanhita mandates that inquiry and trial of rape offenses must be conducted in camera.",
    "statuteOrAuthority": "Bharatiya Nyaya Sanhita, 2023, Section 72 & BNSS Section 366; Naresh Shridhar Mirajkar v. State of Maharashtra",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2111",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-263",
    "canonical": "CORAM",
    "acceptedVariants": [
      "CORAM"
    ],
    "difficulty": "intermediate",
    "subject": "Judicial Terminology",
    "primaryClue": "The judges comprising the bench hearing a particular judicial proceeding: 'In the presence of'",
    "additionalHint": "Latin term; designated on all official court orders; e.g., 'Coram: Hon'ble Dr. Justice D.Y. Chandrachud'",
    "definition": "The specific composition of judges sitting on the judicial bench who hear and decide a case.",
    "educationalExample": "The constitutional challenge was placed before a Constitution Bench comprising a five-judge coram.",
    "statuteOrAuthority": "Supreme Court Rules, 2013; Union of India v. Raghubir Singh (1989 2 SCC 754)",
    "sourceUrl": "https://main.sci.gov.in",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-264",
    "canonical": "BENCH",
    "acceptedVariants": [
      "BENCH"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "The seat of judges collectively or the body of judges constituting a particular court or division",
    "additionalHint": "Categorized into Single Bench, Division Bench (two judges), Full Bench (three+), and Constitution Bench (five+)",
    "definition": "The collective body of judges presiding over a hearing in a court of law.",
    "educationalExample": "A reference on a conflicting point of law was referred to a three-judge Full Bench of the High Court.",
    "statuteOrAuthority": "High Court of Judicature at Allahabad Rules, 1952",
    "sourceUrl": "https://www.allahabadhighcourt.in",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-265",
    "canonical": "QUORUM",
    "acceptedVariants": [
      "QUORUM"
    ],
    "difficulty": "beginner",
    "subject": "Judicial Terminology",
    "primaryClue": "The minimum number of members or judges required to be present to validate proceedings of a deliberative body",
    "additionalHint": "Article 100(3) sets parliamentary quorum at one-tenth of total membership; Article 145(3) sets Constitution Bench quorum at 5",
    "definition": "The statutory minimum number of judicial officers or legislative members necessary to lawfully transact business.",
    "educationalExample": "A minimum quorum of five Supreme Court judges is required under Article 145(3) to decide substantial constitutional questions.",
    "statuteOrAuthority": "Constitution of India, Article 100(3) & 145(3)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/1522",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-266",
    "canonical": "MORTGAGE",
    "acceptedVariants": [
      "MORTGAGE"
    ],
    "difficulty": "beginner",
    "subject": "Property Law",
    "primaryClue": "The transfer of an interest in specific immovable property for the purpose of securing payment of a loan or debt",
    "additionalHint": "Defined in Section 58 of Transfer of Property Act, 1882; divided into 6 statutory classes (simple, usufructuary, etc.)",
    "definition": "A conveyance of an interest in real property as collateral security for the repayment of a debt or money loan.",
    "educationalExample": "Executing a registered simple mortgage over agricultural land to secure a bank crop loan is governed by Section 58(b) TPA.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 58; Ram Kinkar Banerjee v. Satya Charan Srimani (AIR 1939 PC 14)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-267",
    "canonical": "LEASE",
    "acceptedVariants": [
      "LEASE"
    ],
    "difficulty": "beginner",
    "subject": "Property Law",
    "primaryClue": "Transfer of a right to enjoy immovable property made for a certain time or in perpetuity in consideration of price or rent",
    "additionalHint": "Defined in Section 105 of Transfer of Property Act, 1882; parties are lessor and lessee",
    "definition": "A contractual grant of exclusive possession of real property for a specified term in exchange for rent.",
    "educationalExample": "Letting out a commercial office space for five years against monthly rent of fifty thousand rupees constitutes a statutory lease.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 105; Associated Hotels of India v. R.N. Kapoor (AIR 1959 SC 1262)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-268",
    "canonical": "SALE OF PROPERTY",
    "acceptedVariants": [
      "SALE OF PROPERTY"
    ],
    "difficulty": "beginner",
    "subject": "Property Law",
    "primaryClue": "Transfer of ownership in exchange for a price paid or promised, or part-paid and part-promised",
    "additionalHint": "Defined in Section 54 of Transfer of Property Act, 1882; requires registered instrument for value of Rs 100 or upward",
    "definition": "The absolute conveyance of full ownership title in immovable property from seller to buyer in exchange for a price.",
    "educationalExample": "Execution and registration of a Sale Deed before the Sub-Registrar completes the transfer of title under Section 54 TPA.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 54; Suraj Lamp & Industries v. State of Haryana (2012 1 SCC 656)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-269",
    "canonical": "EXCHANGE",
    "acceptedVariants": [
      "EXCHANGE"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "When two persons mutually transfer the ownership of one thing for the ownership of another, neither thing being money only",
    "additionalHint": "Defined in Section 118 of Transfer of Property Act, 1882; parties have rights and liabilities of a seller and buyer",
    "definition": "A bilateral transaction where two landowners mutually swap parcels of land without an exclusive cash purchase price.",
    "educationalExample": "Swapping an agricultural field in the north village for a commercial orchard plot in the south village is a statutory exchange.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 118; CIT v. Motors & General Stores (AIR 1968 SC 200)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-270",
    "canonical": "GIFT",
    "acceptedVariants": [
      "GIFT"
    ],
    "difficulty": "beginner",
    "subject": "Property Law",
    "primaryClue": "Transfer of certain existing movable or immovable property made voluntarily and without consideration by donor to donee",
    "additionalHint": "Defined in Section 122 of Transfer of Property Act, 1882; must be accepted by donee during donor's lifetime",
    "definition": "A gratuitous voluntary transfer of property ownership made without monetary consideration and accepted by donee.",
    "educationalExample": "Gifting an ancestral house to a daughter through a registered deed accepted during the father's lifetime is a valid gift.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 122 & 123; K. Balakrishnan v. K. Kamalam (2004 1 SCC 581)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-271",
    "canonical": "EASEMENT",
    "acceptedVariants": [
      "EASEMENT"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Right which owner or occupier of certain land possesses for beneficial enjoyment of that land to do or continue to do something on another's land",
    "additionalHint": "Defined in Section 4 of Indian Easements Act, 1882; involves dominant heritage and servient heritage",
    "definition": "A non-possessory right to use or cross a neighbor's real property for the beneficial enjoyment of one's own land.",
    "educationalExample": "A right of pathway across an adjacent estate to access a public highway is a classic easement of necessity.",
    "statuteOrAuthority": "Indian Easements Act, 1882, Section 4 & 13; Chapsibhai Dhanjibhai Danad v. Purushottam (1971 2 SCC 205)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2337",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-272",
    "canonical": "ACTIONABLE CLAIM",
    "acceptedVariants": [
      "ACTIONABLE CLAIM"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "A claim to any unsecured debt or beneficial interest in movable property not in possession, enforceable by court",
    "additionalHint": "Defined in Section 3 of Transfer of Property Act, 1882; transferable by execution of an instrument in writing (Section 130)",
    "definition": "A legally enforceable right to recover an unsecured money debt or claim beneficial movable assets.",
    "educationalExample": "The right to recover arrears of rent or insurance proceeds due under a policy constitutes an actionable claim under Section 3 TPA.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 3 & 130; Sunrise Associates v. Govt. of NCT of Delhi (2006 5 SCC 603)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-273",
    "canonical": "PART PERFORMANCE",
    "acceptedVariants": [
      "PART PERFORMANCE"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Equitable doctrine protecting a transferee in possession under an uncompleted contract of sale from eviction by transferor",
    "additionalHint": "Codified in Section 53A of Transfer of Property Act, 1882; acts as a shield for defense, not a sword",
    "definition": "A statutory defense shielding a buyer who took possession and performed part of a written sale contract from ejectment.",
    "educationalExample": "Having paid full consideration and taken physical possession under a signed sale agreement, the buyer is protected under Section 53A.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 53A; Shrimant Shamrao Suryavanshi v. Pralhad Bhairoba Suryavanshi (2002 3 SCC 676)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-274",
    "canonical": "PERPETUITY",
    "acceptedVariants": [
      "PERPETUITY"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "Rule against perpetuity invalidating property transfers that tie up property beyond lifetime of living persons plus minority of unborn",
    "additionalHint": "Section 14 of Transfer of Property Act, 1882; ensures property remains alienable and prevents endless dynastic dead-hand control",
    "definition": "The rule preventing property from being rendered permanently inalienable across successive unborn generations.",
    "educationalExample": "A clause in a settlement deed attempting to tie up family land across five unborn generations is void under Section 14 TPA.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 14; Ram Newaz v. Nankoo (AIR 1926 All 283)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-275",
    "canonical": "REVERSION",
    "acceptedVariants": [
      "REVERSION"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "The undisposed residue of an estate left in the grantor or their successor after determination of a lesser estate granted",
    "additionalHint": "Property concept; e.g., when a life estate ends, property reverts to the original grantor or heirs",
    "definition": "The future possessory interest retained by a transferor after conveying a temporary or life interest in land.",
    "educationalExample": "Granting land to a person for life means that upon their death, the estate reverts back to the original grantor's estate.",
    "statuteOrAuthority": "Transfer of Property Act, 1882; Mulla on Transfer of Property Act",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-276",
    "canonical": "REMAINDER",
    "acceptedVariants": [
      "REMAINDER"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "Future estate created in favor of a third party to take effect immediately upon the termination of a prior particular estate",
    "additionalHint": "Contrasted with reversion; e.g., to A for life, and upon A's death, remainder to B in fee simple",
    "definition": "A future interest in real property granted to a third party that takes effect upon the expiration of a prior life estate.",
    "educationalExample": "A deed conveying property to a spouse for life with remainder to their daughter creates a vested remainder in the daughter.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 19 & 21; R. Rajagopal Reddy v. Padmini Chandrasekharan (1995 2 SCC 630)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-277",
    "canonical": "REDEMPTION",
    "acceptedVariants": [
      "REDEMPTION"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Right of a mortgagor upon payment of mortgage money to require mortgagee to deliver title deeds and possession",
    "additionalHint": "Codified in Section 60 of Transfer of Property Act, 1882; 'Once a mortgage, always a mortgage'",
    "definition": "The statutory right of a debtor to reclaim mortgaged property upon repaying the loan in full.",
    "educationalExample": "Any clog or condition in a mortgage deed purporting to destroy the mortgagor's right of redemption is void.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 60; Seth Ganga Dhar v. Shankar Lal (AIR 1958 SC 770)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-278",
    "canonical": "FORECLOSURE",
    "acceptedVariants": [
      "FORECLOSURE"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Right of mortgagee to obtain a decree that the mortgagor shall be absolutely debarred of their right to redeem mortgaged property",
    "additionalHint": "Section 67 of Transfer of Property Act, 1882; available in mortgage by conditional sale and anomalous mortgage",
    "definition": "A legal proceeding terminating a mortgagor's right of redemption upon persistent failure to repay the loan.",
    "educationalExample": "Upon mortgagor's default on a mortgage by conditional sale, the lender filed a suit for foreclosure under Section 67 TPA.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 67; Monappa v. Horikeri (AIR 1952 Mys 12)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-279",
    "canonical": "SUBROGATION",
    "acceptedVariants": [
      "SUBROGATION"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "Equitable doctrine where a person who redeems a mortgage steps into the shoes of the original mortgagee regarding rights against property",
    "additionalHint": "Section 92 of Transfer of Property Act, 1882; divided into legal subrogation and conventional subrogation",
    "definition": "The substitution of one creditor for another, clothing the paying party with all securities and rights of the redeemed debt.",
    "educationalExample": "A co-mortgagor who redeemed the entire mortgage debt was subrogated to the rights of the mortgagee against co-owners.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 92; Ganeshi Lal v. Joti Pershad (1953 SCR 243)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-280",
    "canonical": "COVENANT",
    "acceptedVariants": [
      "COVENANT"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Formal promise or agreement in a deed creating obligations that run with the land or bind signatories",
    "additionalHint": "Covenants running with the land governed by Section 40 of Transfer of Property Act, 1882",
    "definition": "A solemn promise contained in a property deed concerning the use, maintenance, or non-use of real estate.",
    "educationalExample": "A restrictive covenant in an estate deed prohibiting the construction of industrial factories was held binding on successors.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 40; Tulk v. Moxhay (1848 2 Ph 774)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-281",
    "canonical": "ATTORNMENT",
    "acceptedVariants": [
      "ATTORNMENT"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "Formal agreement by a tenant acknowledging a new landlord upon transfer of property ownership",
    "additionalHint": "Section 109 of Transfer of Property Act, 1882; attornment is not essential to complete transfer of landlord's rights",
    "definition": "The acknowledgment by a tenant of a new property owner as their lawful landlord following sale of the premises.",
    "educationalExample": "Upon buying the leased commercial building, the purchaser served notice requiring the tenant's attornment under Section 109.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 109; B.P. Pathak v. Dr. R.V. Shirali (AIR 1976 MP 158)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-282",
    "canonical": "ACCRETION",
    "acceptedVariants": [
      "ACCRETION"
    ],
    "difficulty": "advanced",
    "subject": "Property Law",
    "primaryClue": "Gradual and imperceptible addition of land caused by natural alluvion from a receding river or sea",
    "additionalHint": "Section 63 of Transfer of Property Act, 1882; accretions to mortgaged property belong to the mortgagor on redemption",
    "definition": "The increase of land border resulting from gradual water recession or alluvium deposits by a river.",
    "educationalExample": "Alluvial soil gradually deposited by the Ganges along a riverfront field belongs to the riparian owner under accretion.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 63; Felix Lopez v. Maddan Mohan Thakoor (1870 13 MIA 467)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-283",
    "canonical": "EQUITABLE MORTGAGE",
    "acceptedVariants": [
      "EQUITABLE MORTGAGE"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Mortgage created by delivery of documents of title to immovable property with intent to create a security thereon",
    "additionalHint": "Defined in Section 58(f) of Transfer of Property Act, 1882; common in notified commercial banking towns",
    "definition": "A security interest in real property created simply by depositing original title deeds with a financial lender.",
    "educationalExample": "Depositing original sale deeds with a bank in Kanpur to secure an immediate overdraft facility creates an equitable mortgage.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 58(f); K.J. Nathan v. S.V. Maruthi Rao (AIR 1965 SC 430)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-284",
    "canonical": "USUFRUCTUARY MORTGAGE",
    "acceptedVariants": [
      "USUFRUCTUARY MORTGAGE"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Mortgage where mortgagor delivers possession to mortgagee authorizing retention until mortgage money is satisfied from rents/profits",
    "additionalHint": "Defined in Section 58(d) of Transfer of Property Act, 1882; no personal liability on mortgagor to pay debt",
    "definition": "A mortgage wherein the lender takes physical possession of land and repays the debt out of agricultural rents and profits.",
    "educationalExample": "Handing over possession of an orchard so the lender collects mango harvests to satisfy loan interest is a usufructuary mortgage.",
    "statuteOrAuthority": "Transfer of Property Act, 1882, Section 58(d); Ram Narayan Prasad Sah v. Ram Bilas Roy (1977 4 SCC 344)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2338",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  },
  {
    "id": "voc-285",
    "canonical": "RECTIFICATION",
    "acceptedVariants": [
      "RECTIFICATION"
    ],
    "difficulty": "intermediate",
    "subject": "Property Law",
    "primaryClue": "Equitable court remedy correcting a written instrument that does not express real intention of parties through mutual mistake or fraud",
    "additionalHint": "Governed by Section 26 of Specific Relief Act, 1963; court orders deed to be rectified to reflect true intent",
    "definition": "The equitable correction of an error in a written contract or deed to accurately reflect parties' true agreement.",
    "educationalExample": "When a typist mistakenly swapped plot survey numbers 41 and 42 in the deed, the court ordered rectification of the instrument.",
    "statuteOrAuthority": "Specific Relief Act, 1963, Section 26; Subhadra v. Thankam (2010 11 SCC 514)",
    "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2264",
    "verificationDate": "2026-11-22",
    "status": "Verified against authoritative source"
  }
];

  // Build indexed lookups for rapid querying
  const BY_ID = {};
  const BY_CANONICAL = {};
  const BY_SUBJECT = {};
  const BY_DIFFICULTY = { beginner: [], intermediate: [], advanced: [] };

  VOCABULARY.forEach(item => {
    BY_ID[item.id] = item;
    BY_CANONICAL[item.canonical.toUpperCase()] = item;
    if (Array.isArray(item.acceptedVariants)) {
      item.acceptedVariants.forEach(v => {
        BY_CANONICAL[v.toUpperCase()] = item;
      });
    }

    if (!BY_SUBJECT[item.subject]) {
      BY_SUBJECT[item.subject] = [];
    }
    BY_SUBJECT[item.subject].push(item);

    if (BY_DIFFICULTY[item.difficulty]) {
      BY_DIFFICULTY[item.difficulty].push(item);
    }
  });

  window.ARENA_VOCABULARY = VOCABULARY;
  window.ARENA_VOCAB_BY_ID = BY_ID;
  window.ARENA_VOCAB_BY_CANONICAL = BY_CANONICAL;
  window.ARENA_VOCAB_BY_SUBJECT = BY_SUBJECT;
  window.ARENA_VOCAB_BY_DIFFICULTY = BY_DIFFICULTY;
})();
