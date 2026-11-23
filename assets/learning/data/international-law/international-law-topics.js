/**
 * Tanveer Ashraf Judicial Prep - International Organisations & Current International Affairs Topics (Paper II Law)
 */
(function(global) {
  'use strict';
  var INTERNATIONAL_LAW_TOPICS = [
  {
    "id": "top-ilaw-01-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-01",
    "number": 1,
    "order": 1,
    "title": "Nature & Definition of International Law",
    "summary": "Traditional vs modern definitions: Oppenheim (law of nations), J.G. Starke, Brierly; whether international law is a 'vanishing point of jurisprudence' (Holland) or true law with sanctions.",
    "keyProvisions": [
      "Oppenheim's definition of International Law",
      "Holland's 'vanishing point' critique",
      "Hart's concept of law as primary and secondary rules"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-01-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-01",
    "number": 2,
    "order": 2,
    "title": "Theories on the Basis of International Law",
    "summary": "Natural Law Theory (Grotius, Vitoria), Positivist Theory (Bynkershoek, Martens), Consent Theory / Auto-Limitation (Jellinek, Triepel), Pacta Sunt Servanda (Anzilotti).",
    "keyProvisions": [
      "Hugo Grotius father of international law (De Jure Belli ac Pacis 1625)",
      "Pacta Sunt Servanda",
      "Positivist vs Naturalist debate"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-01-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-01",
    "number": 3,
    "order": 3,
    "title": "Sanctions & Enforcement in International Law",
    "summary": "Decentralized sanctions, collective security under Chapter VII UN Charter, self-help, countermeasures, public opinion, economic retaliation, international adjudication.",
    "keyProvisions": [
      "UN Charter Chapter VII enforcement",
      "Countermeasures conditions (Gabčíkovo-Nagymaros Case)",
      "Legal nature of international obligation"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-02-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-02",
    "number": 4,
    "order": 4,
    "title": "Article 38(1) ICJ Statute: Codification of Sources",
    "summary": "Formal vs material sources, Article 38(1) hierarchy: (a) International Conventions, (b) Custom, (c) General Principles, (d) Judicial decisions & publicist teachings as subsidiary means.",
    "keyProvisions": [
      "Article 38(1) Statute of the ICJ",
      "Article 59 ICJ Statute (no binding doctrine of stare decisis)",
      "Ex aequo et bono power under Article 38(2)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-02-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-02",
    "number": 5,
    "order": 5,
    "title": "International Custom: State Practice & Opinio Juris",
    "summary": "Two essential elements: diuturnitas (uniform and consistent state practice) and opinio juris sive necessitatis (conviction of legal necessity), Lotus case (1927), North Sea Continental Shelf cases (1969), persistent objector rule.",
    "keyProvisions": [
      "North Sea Continental Shelf Cases (ICJ 1969)",
      "SS Lotus Case (PCIJ 1927)",
      "Right of Passage over Indian Territory (Portugal v. India 1960)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-02-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-02",
    "number": 6,
    "order": 6,
    "title": "General Principles of Law & Jus Cogens",
    "summary": "General principles recognized by civilized nations (res judicata, estoppel, good faith, subrogation, unjust enrichment, Chorzow Factory principle); Jus Cogens (Article 53 VCLT 1969 peremptory norms).",
    "keyProvisions": [
      "Chorzow Factory Case (PCIJ 1928 - reparation principle)",
      "Article 53 Vienna Convention on Law of Treaties 1969",
      "Obligations Erga Omnes (Barcelona Traction 1970)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-03-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-03",
    "number": 7,
    "order": 7,
    "title": "Theories of Monism & Dualism",
    "summary": "Monist Theory (Kelsen's Grundnorm hierarchy, Scelle): international and municipal law belong to single legal order; Dualist Theory (Triepel, Anzilotti): two distinct and separate legal systems with different subjects, sources, and principles.",
    "keyProvisions": [
      "Hans Kelsen monist doctrine",
      "Heinrich Triepel and Dionisio Anzilotti dualism",
      "Coordination Theory (Fitzmaurice, Rousseau)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-03-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-03",
    "number": 8,
    "order": 8,
    "title": "Transformation & Specific Adoption Doctrines",
    "summary": "Doctrine of Transformation: international treaty must be transformed into municipal statute by parliamentary enactment; Specific Adoption / Incorporation Theory: customary international law is part of the law of the land (Blackstone doctrine).",
    "keyProvisions": [
      "Transformation doctrine",
      "Blackstonian doctrine of incorporation",
      "Mortensen v. Peters (1906)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-03-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-03",
    "number": 9,
    "order": 9,
    "title": "Indian Constitutional Jurisprudence on International Law",
    "summary": "Article 51(c) (foster respect for international law and treaty obligations), Article 253 (legislation for giving effect to international agreements), Dualist application: Gramophone Co. v. Birendra Bahadur Pandey (1984), Vishaka (1997), Puttaswamy (2017).",
    "keyProvisions": [
      "Constitution of India Articles 51(c), 73, 253",
      "Gramophone Co. of India v. Birendra Bahadur Pandey (1984)",
      "Vishaka v. State of Rajasthan (1997)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-04-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-04",
    "number": 10,
    "order": 10,
    "title": "States as Primary Subjects & The Montevideo Criteria",
    "summary": "Montevideo Convention on Rights and Duties of States 1933 Article 1: (a) permanent population, (b) defined territory, (c) government, (d) capacity to enter into relations with other states; Sovereignty and independence.",
    "keyProvisions": [
      "Montevideo Convention 1933 Article 1",
      "Customary legal personality of sovereign states",
      "Failed states vs micro-states"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-04-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-04",
    "number": 11,
    "order": 11,
    "title": "International Legal Personality: Non-State Entities & Individuals",
    "summary": "Reparation for Injuries Suffered in Service of UN (ICJ Advisory Opinion 1949, objective international personality of UN), individuals as subjects (Nuremberg trials, ICC, international human rights petitions), insurgents and national liberation movements.",
    "keyProvisions": [
      "Reparation for Injuries Case (ICJ 1949)",
      "Nuremberg Tribunal principle: crimes are committed by individuals",
      "Universal jurisdiction over piracy and genocide"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-05-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-05",
    "number": 12,
    "order": 12,
    "title": "Theories of Recognition: Constitutive vs Declaratory",
    "summary": "Constitutive Theory (Hegel, Oppenheim, Anzilotti): act of recognition creates statehood; Declaratory / Evidentiary Theory (Hall, Brierly, Fischer): statehood exists independently, recognition merely acknowledges existing fact.",
    "keyProvisions": [
      "Constitutive Theory vs Declaratory Theory",
      "Article 3 Montevideo Convention 1933",
      "Tinoco Concessions Arbitration (1923)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-05-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-05",
    "number": 13,
    "order": 13,
    "title": "De Facto vs De Jure Recognition",
    "summary": "De facto recognition (provisional, revocable, given when authority is established but lacks full permanence); De jure recognition (formal, permanent, irrevocable, establishing full diplomatic relations).",
    "keyProvisions": [
      "Distinction between De Facto and De Jure",
      "Luther v. Sagor (1921)",
      "Bank of Ethiopia v. National Bank of Egypt (1937)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-05-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-05",
    "number": 14,
    "order": 14,
    "title": "Legal Effects of Recognition & Non-Recognition",
    "summary": "Right to sue in municipal courts of recognizing state, diplomatic immunity, control of state assets abroad, retroactive effect of recognition; Stimson Doctrine of non-recognition of illegal territorial changes.",
    "keyProvisions": [
      "Retroactivity doctrine of recognition",
      "Stimson Doctrine (1932)",
      "Civil Air Transport Inc. v. Central Air Transport Corp (1953)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-06-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-06",
    "number": 15,
    "order": 15,
    "title": "Modes of Acquiring & Losing State Territory",
    "summary": "Five traditional modes: Occupation (terra nullius, effective control, Island of Palmas Case 1928, Eastern Greenland 1933), Prescription (adverse possession), Accretion, Cession, Conquest (illegal under Art 2(4) UN Charter).",
    "keyProvisions": [
      "Island of Palmas Case (Max Huber 1928)",
      "Legal Status of Eastern Greenland (PCIJ 1933)",
      "Clipperton Island Case (1931)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-06-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-06",
    "number": 16,
    "order": 16,
    "title": "Law of the Sea: Maritime Zones Under UNCLOS 1982",
    "summary": "Baselines, Internal Waters, Territorial Sea (12 nm, sovereignty subject to innocent passage Art 17), Contiguous Zone (24 nm, customs/fiscal/immigration/sanitary laws), Exclusive Economic Zone (200 nm sovereign rights over resources).",
    "keyProvisions": [
      "UNCLOS 1982 Articles 3, 17, 33, 56",
      "Innocent Passage requirements (Article 19)",
      "Enrica Lexie Case (Italy v. India 2020)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-06-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-06",
    "number": 17,
    "order": 17,
    "title": "Continental Shelf, High Seas & Common Heritage of Mankind",
    "summary": "Continental Shelf (seabed and subsoil up to 200/350 nm, Truman Proclamation 1945), High Seas freedoms (navigation, fishing, overflight, laying cables), The Area as Common Heritage of Mankind (Article 136), International Seabed Authority (ISA).",
    "keyProvisions": [
      "UNCLOS Articles 76, 87 (High Seas Freedoms), 136 (Common Heritage)",
      "International Seabed Authority (Kingston, Jamaica)",
      "Deep seabed mining regulations"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-07-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-07",
    "number": 18,
    "order": 18,
    "title": "Principles of State Jurisdiction: Territorial to Universal",
    "summary": "Territorial Principle (subjective vs objective territoriality, effects doctrine), Nationality Principle (active vs passive personality), Protective Principle (national security threats), Universal Jurisdiction (piracy jure gentium, war crimes, genocide, Eichmann trial).",
    "keyProvisions": [
      "SS Lotus Case (PCIJ 1927 extraterritoriality)",
      "Attorney General of Israel v. Eichmann (1962)",
      "Universal jurisdiction treaties"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-07-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-07",
    "number": 19,
    "order": 19,
    "title": "State Immunity: Absolute vs Restrictive Doctrine",
    "summary": "Par in parem non habet imperium (equals have no jurisdiction over equals), evolution from Absolute Immunity (The Schooner Exchange v. McFaddon 1812) to Restrictive Immunity (acts jure imperii sovereign acts vs acts jure gestionis commercial acts).",
    "keyProvisions": [
      "The Schooner Exchange v. McFaddon (US Supreme Court 1812)",
      "Acts jure imperii vs acts jure gestionis",
      "Jurisdictional Immunities of the State (Germany v. Italy, ICJ 2012)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-08-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-08",
    "number": 20,
    "order": 20,
    "title": "Law of Extradition: Principles & International Standards",
    "summary": "Extradition definition (Starke), no duty to extradite without treaty, Double Criminality principle, Rule of Speciality (tried only for offense for which extradited), non-extradition of political offenders (Castioni, Meunier cases), death penalty assurance.",
    "keyProvisions": [
      "Extradition Act 1962 (India)",
      "Re Castioni (1891)",
      "Rule of Speciality (US v. Rauscher 1886)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-08-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-08",
    "number": 21,
    "order": 21,
    "title": "Territorial & Diplomatic Asylum: The Asylum Case",
    "summary": "Territorial asylum (derives from sovereignty over territory, Article 14 UDHR), Diplomatic asylum (extra-territorial refuge in diplomatic mission premises, exceptional nature, Columbia v. Peru - Haya de la Torre Case, ICJ 1950).",
    "keyProvisions": [
      "Asylum Case (Colombia v. Peru, ICJ 1950)",
      "Haya de la Torre Case (ICJ 1951)",
      "Universal Declaration of Human Rights Article 14"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-08-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-08",
    "number": 22,
    "order": 22,
    "title": "The Principle of Non-Refoulement in Refugee Law",
    "summary": "Article 33 of the 1951 Convention Relating to the Status of Refugees: prohibition of expulsion or return of refugee to territory where life or freedom threatened; status as customary international law and jus cogens norm.",
    "keyProvisions": [
      "1951 Refugee Convention Article 33",
      "1967 Protocol Relating to the Status of Refugees",
      "Non-refoulement as customary international law"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-09-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-09",
    "number": 23,
    "order": 23,
    "title": "State Responsibility: Internationally Wrongful Acts",
    "summary": "ILC Articles on State Responsibility 2001 (James Crawford), two elements: conduct attributable to state and breach of international obligation; attribution rules (state organs, persons exercising governmental authority, ultra vires acts Art 7).",
    "keyProvisions": [
      "ILC Draft Articles on State Responsibility 2001 Articles 1, 2, 4, 7, 8",
      "Nicaragua Case (effective control test)",
      "Tadic Case (overall control test)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-09-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-09",
    "number": 24,
    "order": 24,
    "title": "Circumstances Precluding Wrongfulness & Reparation",
    "summary": "Chapter V ILC Articles: Consent (Art 20), Self-defense (Art 21), Countermeasures (Art 22), Force majeure (Art 23), Distress (Art 24), Necessity (Art 25); Forms of reparation: Restitution, Compensation, Satisfaction (Chorzow Factory 1928).",
    "keyProvisions": [
      "ILC Articles 20-25 (Circumstances Precluding Wrongfulness)",
      "ILC Articles 34-37 (Forms of Reparation)",
      "Rainbow Warrior Arbitration (New Zealand v. France 1990)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-10-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-10",
    "number": 25,
    "order": 25,
    "title": "Vienna Convention on the Law of Treaties 1969: Formation",
    "summary": "VCLT 1969 'Treaty of Treaties', definition Article 2(1)(a) written agreement between States governed by international law, full powers (Art 7), consent to be bound (signature, ratification, accession), entry into force.",
    "keyProvisions": [
      "VCLT 1969 Articles 2, 7, 11, 14, 24",
      "Pacta sunt servanda (Article 26)",
      "Internal law cannot justify failure to perform treaty (Article 27)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-10-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-10",
    "number": 26,
    "order": 26,
    "title": "Reservations to Treaties & The Compatibility Rule",
    "summary": "Definition of reservation (Art 2(1)(d)), Reservations to the Convention on the Prevention and Punishment of the Crime of Genocide (ICJ Advisory Opinion 1951), Compatibility test: reservation permissible unless incompatible with object and purpose of treaty (Article 19 VCLT).",
    "keyProvisions": [
      "Reservations to Genocide Convention (ICJ 1951)",
      "VCLT 1969 Articles 19-23",
      "Legal effect of objection to reservation (Article 21)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-10-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-10",
    "number": 27,
    "order": 27,
    "title": "Invalidity, Termination & Clausula Rebus Sic Stantibus",
    "summary": "Grounds of invalidity: Ultra vires (Art 46), Error (Art 48), Fraud (Art 49), Corruption (Art 50), Coercion (Arts 51-52), Conflict with Jus Cogens (Art 53); Termination: Material breach (Art 60), Impossibility of performance (Art 61), Fundamental change of circumstances (Rebus sic stantibus, Art 62).",
    "keyProvisions": [
      "VCLT 1969 Articles 53 (Jus Cogens invalidity), 60 (Material Breach), 62 (Rebus Sic Stantibus)",
      "Fisheries Jurisdiction Case (UK v. Iceland 1973)",
      "Gabčíkovo-Nagymaros Project Case (ICJ 1997)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-11-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-11",
    "number": 28,
    "order": 28,
    "title": "UN Charter Purposes, Principles & Domestic Jurisdiction",
    "summary": "Preamble and Articles 1-2, sovereign equality of states (Art 2(1)), peaceful settlement (Art 2(3)), prohibition of force (Art 2(4)), domestic jurisdiction limitation (Art 2(7)), exception for Chapter VII enforcement measures.",
    "keyProvisions": [
      "UN Charter Articles 1, 2(1), 2(4), 2(7)",
      "Nicaragua Case (ICJ 1986 on Art 2(4) custom)",
      "Interpretation of Article 2(7) domestic jurisdiction"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-11-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-11",
    "number": 29,
    "order": 29,
    "title": "UN General Assembly: Legal Powers & Resolution 377A",
    "summary": "Composition (Art 9), functions and powers (Arts 10-17), voting on important questions by two-thirds majority (Art 18), recommendations under Arts 10-14, Uniting for Peace Resolution 377A (1950) filling vacuum when Security Council paralyzed by veto.",
    "keyProvisions": [
      "UN Charter Articles 10, 11, 12, 14, 18",
      "Uniting for Peace Resolution 377A (GA 1950)",
      "Certain Expenses of the United Nations (ICJ 1962)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-12-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-12",
    "number": 30,
    "order": 30,
    "title": "UN Security Council: Composition, Voting & Veto Jurisprudence",
    "summary": "Article 23 composition (5 permanent, 10 non-permanent), Article 27 voting formula (procedural vs substantive, double veto, permanent member concurrence), ICJ Namibia Advisory Opinion 1971 (abstention does not constitute veto).",
    "keyProvisions": [
      "UN Charter Articles 23, 27",
      "Namibia Advisory Opinion (ICJ 1971)",
      "Double veto procedure under San Francisco Statement 1945"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-12-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-12",
    "number": 31,
    "order": 31,
    "title": "Chapter VII Enforcement Actions & Article 51 Self-Defense",
    "summary": "Determination of threat/breach (Art 39), provisional measures (Art 40), non-military sanctions (Art 41), military enforcement action (Art 42), inherent right of individual or collective self-defense against armed attack (Article 51, Caroline criteria).",
    "keyProvisions": [
      "UN Charter Articles 39, 41, 42, 51",
      "The Caroline Case (1837) necessity and proportionality",
      "Nicaragua Case (ICJ 1986 armed attack threshold)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-13-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-13",
    "number": 32,
    "order": 32,
    "title": "International Court of Justice: Organization & Composition",
    "summary": "15 judges elected for 9-year terms by GA and SC (Arts 3, 4, 8, 13 Statute), one-third elected every 3 years, ad hoc judges under Article 31, chambers (Art 26), official languages (English and French).",
    "keyProvisions": [
      "ICJ Statute Articles 2, 3, 9 (representation of main forms of civilization), 13, 31 (Judges Ad Hoc)",
      "Peace Palace, The Hague"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-ilaw-13-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-13",
    "number": 33,
    "order": 33,
    "title": "ICJ Contentious Jurisdiction & The Optional Clause",
    "summary": "Article 34(1) only States may be parties, basis of jurisdiction: special agreement (compromis), treaty compromissory clause, Optional Clause under Article 36(2) (reciprocity, reservations, Connally reservation), forum prorogatum.",
    "keyProvisions": [
      "ICJ Statute Articles 34(1), 36(1), 36(2), 36(6) (competence de la competence)",
      "Norwegian Loans Case (France v. Norway 1957)",
      "Right of Passage Case (1960)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-13-03",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-13",
    "number": 34,
    "order": 34,
    "title": "Advisory Opinions & Enforcement Under Article 94",
    "summary": "Advisory opinions requested by GA, SC, and authorized organs/agencies under Article 96 UN Charter and Article 65 ICJ Statute, non-binding legal guidance; Article 94 UN Charter enforcement by Security Council, Kulbhushan Jadhav case.",
    "keyProvisions": [
      "UN Charter Articles 94, 96",
      "ICJ Statute Article 65",
      "Jadhav Case (India v. Pakistan, ICJ Judgment July 17, 2019)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-14-01",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-14",
    "number": 35,
    "order": 35,
    "title": "International Criminal Court (ICC) & Rome Statute 1998",
    "summary": "Rome Statute 1998 entered into force 2002, seat in The Hague, independent court not a UN organ, four core crimes: Genocide, Crimes Against Humanity, War Crimes, Aggression; Principle of Complementarity (Article 17, court of last resort).",
    "keyProvisions": [
      "Rome Statute of the ICC 1998 Articles 1, 5, 12, 13 (Referrals by State, SC, or Prosecutor proprio motu), 17 (Complementarity)",
      "Ad hoc tribunals (ICTY, ICTR) precursors"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-ilaw-14-02",
    "subjectId": "law-international",
    "chapterId": "ch-ilaw-14",
    "number": 36,
    "order": 36,
    "title": "Specialized Agencies & Multilateral Humanitarian Treaties",
    "summary": "Relationship agreements under UN Charter Articles 57 & 63, ILO, WHO, UNESCO, FAO, WTO, Universal Declaration of Human Rights 1948, Geneva Conventions 1949 and Additional Protocols.",
    "keyProvisions": [
      "UN Charter Articles 57 & 63",
      "Universal Declaration of Human Rights 1948",
      "Geneva Conventions I to IV of 1949"
    ],
    "estimatedMinutes": 20
  }
];
  global.INTERNATIONAL_LAW_TOPICS = INTERNATIONAL_LAW_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: INTERNATIONAL_LAW_TOPICS, INTERNATIONAL_LAW_TOPICS: INTERNATIONAL_LAW_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
