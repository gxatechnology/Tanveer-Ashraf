/**
 * Tanveer Ashraf Judicial Prep - International Organisations & Current International Affairs Chapters (Paper II Law)
 */
(function(global) {
  'use strict';
  var INTERNATIONAL_LAW_CHAPTERS = [
  {
    "id": "ch-ilaw-01",
    "subjectId": "law-international",
    "number": 1,
    "order": 1,
    "title": "Nature, Basis & Jurisprudential Foundation of Public International Law",
    "description": "Definition of International Law (Oppenheim, Starke, Brierly), Austin's critique ('positive international morality'), basis of obligation (Natural Law, Positivism, Consent Theory, Pacta Sunt Servanda), whether international law is true law.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-02",
    "subjectId": "law-international",
    "number": 2,
    "order": 2,
    "title": "Sources of International Law & Article 38(1) ICJ Statute",
    "description": "Hierarchy of sources under Article 38(1): International Conventions, Custom (opinio juris sive necessitatis, state practice, Lotus case, North Sea Continental Shelf), General Principles of Law, Subsidiary means, Jus Cogens (peremptory norms).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-ilaw-03",
    "subjectId": "law-international",
    "number": 3,
    "order": 3,
    "title": "Relationship Between International Law & Municipal Law",
    "description": "Theories: Monism (Kelsen, Scelle) vs Dualism (Triepel, Anzilotti), Transformation Theory, Specific Adoption Theory, Indian constitutional approach (Article 51(c), 253, Gramophone Co., Vishaka, Puttaswamy).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-04",
    "subjectId": "law-international",
    "number": 4,
    "order": 4,
    "title": "Subjects of International Law & International Legal Personality",
    "description": "States as primary subjects, international organizations (Reparation for Injuries Case 1949), individuals (human rights, war crimes, piracy jure gentium), insurgents and belligerents.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-ilaw-05",
    "subjectId": "law-international",
    "number": 5,
    "order": 5,
    "title": "State Recognition, De Jure vs De Facto & Legal Effects",
    "description": "Theories of recognition: Constitutive Theory (Oppenheim, Hall) vs Declaratory / Evidentiary Theory (Brierly, Fischer), De facto vs De jure recognition, retroactive effect of recognition, legal consequences of non-recognition (Luther v. Sagor).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-06",
    "subjectId": "law-international",
    "number": 6,
    "order": 6,
    "title": "State Territory, Acquisition & Law of the Sea (UNCLOS)",
    "description": "Modes of acquiring territory: Occupation, Prescription, Accretion, Cession, Annexation/Conquest (prohibited post-1945); UNCLOS maritime zones (Territorial Sea, Contiguous Zone, EEZ, Continental Shelf, High Seas).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-ilaw-07",
    "subjectId": "law-international",
    "number": 7,
    "order": 7,
    "title": "State Jurisdiction, Immunities & Act of State Doctrine",
    "description": "Principles of jurisdiction: Territorial, Nationality (active/passive personality), Protective, Universal jurisdiction; Sovereign immunity (absolute vs restrictive doctrine), Act of State doctrine.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-08",
    "subjectId": "law-international",
    "number": 8,
    "order": 8,
    "title": "Extradition, Asylum & Human Rights Protections",
    "description": "Law of Extradition: Double criminality, Rule of Speciality, non-extradition of political offenders; Asylum: Territorial vs Diplomatic asylum, Principle of Non-Refoulement (Article 33 Refugee Convention).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-09",
    "subjectId": "law-international",
    "number": 9,
    "order": 9,
    "title": "State Responsibility & Treatment of Aliens",
    "description": "Draft Articles on Responsibility of States for Internationally Wrongful Acts (ILC 2001), attribution of conduct, circumstances precluding wrongfulness (force majeure, distress, necessity), diplomatic protection (Calvo clause).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-ilaw-10",
    "subjectId": "law-international",
    "number": 10,
    "order": 10,
    "title": "Law of Treaties & Vienna Convention on Law of Treaties 1969",
    "description": "VCLT 1969: Definition of treaty, conclusion, reservation rules (Reservations to Genocide Convention Advisory Opinion), invalidity (coercion, corruption, error), termination (Rebus Sic Stantibus, material breach).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-ilaw-11",
    "subjectId": "law-international",
    "number": 11,
    "order": 11,
    "title": "The United Nations: Origin, Principles & General Assembly",
    "description": "Purposes and Principles under Articles 1 & 2 UN Charter, sovereign equality, domestic jurisdiction (Art 2(7)), General Assembly powers (Articles 10-14), Uniting for Peace Resolution 377A.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-ilaw-12",
    "subjectId": "law-international",
    "number": 12,
    "order": 12,
    "title": "UN Security Council: Powers, Veto & Chapter VII Actions",
    "description": "Composition (Article 23), voting procedure and Veto (Article 27), pacific settlement under Chapter VI, binding sanctions and military enforcement under Chapter VII (Articles 39, 41, 42), self-defense (Article 51).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-ilaw-13",
    "subjectId": "law-international",
    "number": 13,
    "order": 13,
    "title": "International Court of Justice: Statute, Jurisdiction & Precedents",
    "description": "Composition, election of judges, ad hoc judges (Art 31), contentious jurisdiction (compromis, compromissory clause, Optional Clause Art 36(2)), advisory jurisdiction (Art 65), enforcement of judgments (Article 94 UN Charter).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-ilaw-14",
    "subjectId": "law-international",
    "number": 14,
    "order": 14,
    "title": "Specialized Agencies, International Criminal Law & Contemporary Regimes",
    "description": "Specialized agencies under Articles 57 & 63 (ILO, WHO, UNESCO, WTO), International Criminal Court (ICC Rome Statute 1998, complementarity), Universal Declaration of Human Rights 1948, Geneva Conventions 1949.",
    "estimatedMinutes": 50
  }
];
  global.INTERNATIONAL_LAW_CHAPTERS = INTERNATIONAL_LAW_CHAPTERS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: INTERNATIONAL_LAW_CHAPTERS, INTERNATIONAL_LAW_CHAPTERS: INTERNATIONAL_LAW_CHAPTERS };
  }
})(typeof window !== 'undefined' ? window : global);
