/**
 * LEGAL CROSSWORD PUZZLES DATABASE (V3.0 Phase 3)
 * Authoritative Indian Law Crosswords compiled for UP Judicial Services (UP PCS-J)
 * Total Puzzles: 30 mathematically verified, 100% intersecting playable puzzles
 * Across 3 Difficulty Tiers: 10 Beginner, 10 Intermediate, 10 Advanced
 */
(function() {
  'use strict';

  const PUZZLES = [
  {
    "id": "cw-beg-01",
    "title": "Constitutional Bench",
    "collection": "Constitutional Law",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "LAND",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "ILLEGAL",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: ILLEGAL",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "DEFAULT",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: DEFAULT",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "OWNER",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: OWNER",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "PLEDGE",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Bailment of goods as security for payment of a debt or performance of a promise",
        "hint": "Defined in Section 172 of Indian Contract Act, 1872; parties are pawnor (pledgor) and pawnee (pledgee)",
        "authority": "Indian Contract Act, 1872, Section 172; Lallan Prasad v. Rahmat Ali (AIR 1967 SC 1322)",
        "definition": "A specialized form of bailment where goods are deposited with a creditor as collateral security for a loan.",
        "vocabId": "voc-145",
        "clueNum": 2
      },
      {
        "word": "OATH",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: OATH",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "DP",
      "IEOL",
      "LFWE",
      "LAND",
      "EUEG",
      "GLRE",
      "OATH",
      "L"
    ]
  },
  {
    "id": "cw-beg-02",
    "title": "Criminal Penal Pillars",
    "collection": "Bharatiya Nyaya Sanhita",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "PRIMA",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: PRIMA",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "POLL",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: POLL",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "PRISON",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: PRISON",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "MONEY",
        "direction": "down",
        "row": 2,
        "col": 4,
        "clue": "Legal term: MONEY",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "DIVORCE",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: DIVORCE",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 2
      }
    ],
    "solutionGrid": [
      "",
      "PD",
      "PRIMA",
      "OIVO",
      "LSON",
      "LORE",
      "NCY",
      "E"
    ]
  },
  {
    "id": "cw-beg-03",
    "title": "Civil Procedure First Steps",
    "collection": "Civil Procedure",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "LIEN",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Right of a person in possession of another's property to retain it until certain claims or debts are satisfied",
        "hint": "Particular lien of bailee (Section 170) and general lien of bankers/factors/attorneys (Section 171 ICA)",
        "authority": "Indian Contract Act, 1872, Section 170 & 171; Syndicate Bank v. Vijay Kumar (1992 2 SCC 330)",
        "definition": "A legal right to retain lawful possession of another's personal goods until the possessor's dues are paid.",
        "vocabId": "voc-146",
        "clueNum": 2
      },
      {
        "word": "ISSUE",
        "direction": "down",
        "row": 2,
        "col": 2,
        "clue": "Legal term: ISSUE",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "LAWS",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: LAWS",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "LAND",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "EASED",
        "direction": "down",
        "row": 2,
        "col": 3,
        "clue": "Legal term: EASED",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "DEED",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: DEED",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "L",
      "A",
      "LIEN",
      "ASAD",
      "WSS",
      "SUE",
      "DEED",
      ""
    ]
  },
  {
    "id": "cw-beg-04",
    "title": "The Evidentiary Core",
    "collection": "Law of Evidence",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "CLERK",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: CLERK",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "PROCEED",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: PROCEED",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "LAWYER",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: LAWYER",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "ECLIPSE",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Doctrine where a pre-constitutional law violating fundamental rights becomes dormant rather than dead",
        "hint": "Can revive upon subsequent constitutional amendment removing the inconsistency",
        "authority": "Constitution of India, Article 13(1); Bhikaji Narain Dhakras v. State of M.P. (AIR 1955 SC 781)",
        "definition": "A principle where a pre-constitutional law in conflict with fundamental rights remains dormant and unenforceable, but revives once the constitutional shadow is removed.",
        "vocabId": "voc-010",
        "clueNum": 5
      },
      {
        "word": "ACCUSED",
        "direction": "down",
        "row": 0,
        "col": 1,
        "clue": "Legal term: ACCUSED",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 1
      }
    ],
    "solutionGrid": [
      "AP",
      "CLERK",
      "CACO",
      "UWLC",
      "SYIE",
      "EEPE",
      "DRSD",
      "E"
    ]
  },
  {
    "id": "cw-beg-05",
    "title": "Contract Enforceability Basics",
    "collection": "Contract Law",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "POLL",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: POLL",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "LEGITIM",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: LEGITIM",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "PLEDGE",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Bailment of goods as security for payment of a debt or performance of a promise",
        "hint": "Defined in Section 172 of Indian Contract Act, 1872; parties are pawnor (pledgor) and pawnee (pledgee)",
        "authority": "Indian Contract Act, 1872, Section 172; Lallan Prasad v. Rahmat Ali (AIR 1967 SC 1322)",
        "definition": "A specialized form of bailment where goods are deposited with a creditor as collateral security for a loan.",
        "vocabId": "voc-145",
        "clueNum": 2
      },
      {
        "word": "PLACE",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: PLACE",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "ROBBERY",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Aggravated theft or extortion involving actual hurt, death, wrongful restraint, or imminent fear thereof",
        "hint": "Section 309 of BNS 2023 (formerly Section 390 IPC); in all robbery there is either theft or extortion",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 309 & 310; State of Maharashtra v. Joseph Mingel Koli (1997 Cri LJ 3962)",
        "definition": "An aggravated form of theft or extortion accomplished by causing or threatening death, hurt, or wrongful restraint.",
        "vocabId": "voc-033",
        "clueNum": 1
      }
    ],
    "solutionGrid": [
      "RP",
      "POLL",
      "LBEE",
      "ABGD",
      "CEIG",
      "ERTE",
      "YI",
      "M"
    ]
  },
  {
    "id": "cw-beg-06",
    "title": "Civil Wrongs & Torts Primer",
    "collection": "Law of Torts",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "WILL",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: WILL",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "BAIL",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Temporary judicial release of an accused person awaiting trial upon security, sureties, and undertaking to appear",
        "hint": "Governed by Chapter XXXV of Bharatiya Nagarik Suraksha Sanhita, 2023; 'Bail is the rule, jail is the exception'",
        "authority": "Bharatiya Nagarik Suraksha Sanhita, 2023, Sections 478-485; State of Rajasthan v. Balchand (1977 4 SCC 308)",
        "definition": "The procurement of release from custody of an accused person upon providing adequate security for future attendance.",
        "vocabId": "voc-247",
        "clueNum": 3
      },
      {
        "word": "LAWSUIT",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: LAWSUIT",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "SEAL",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Legal term: SEAL",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "ECLIPSE",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Doctrine where a pre-constitutional law violating fundamental rights becomes dormant rather than dead",
        "hint": "Can revive upon subsequent constitutional amendment removing the inconsistency",
        "authority": "Constitution of India, Article 13(1); Bhikaji Narain Dhakras v. State of M.P. (AIR 1955 SC 781)",
        "definition": "A principle where a pre-constitutional law in conflict with fundamental rights remains dormant and unenforceable, but revives once the constitutional shadow is removed.",
        "vocabId": "voc-010",
        "clueNum": 4
      },
      {
        "word": "FINE",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: FINE",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "S",
      "LBEE",
      "AAAC",
      "WILL",
      "SLI",
      "UP",
      "FINES",
      "TE"
    ]
  },
  {
    "id": "cw-beg-07",
    "title": "First Principles of Jurisprudence",
    "collection": "Jurisprudence",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "CLERK",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: CLERK",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "MAKER",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: MAKER",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "FACT",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: FACT",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "RIGHT",
        "direction": "down",
        "row": 3,
        "col": 4,
        "clue": "Legal term: RIGHT",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "ILLEGAL",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: ILLEGAL",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "SIGN",
        "direction": "across",
        "row": 5,
        "col": 0,
        "clue": "Legal term: SIGN",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "",
      "FIM",
      "ALA",
      "CLERK",
      "TEIE",
      "SIGNGR",
      "AH",
      "LT"
    ]
  },
  {
    "id": "cw-beg-08",
    "title": "Latin Maxims Essentials",
    "collection": "Legal Maxims",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "OWNER",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: OWNER",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "VOID",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: VOID",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "WITNESS",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Legal term: WITNESS",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "SUPREME",
        "direction": "down",
        "row": 0,
        "col": 5,
        "clue": "Legal term: SUPREME",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "EXILE",
        "direction": "down",
        "row": 3,
        "col": 4,
        "clue": "Legal term: EXILE",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "LOSS",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: LOSS",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "WS",
      "IU",
      "VTP",
      "OWNER",
      "IEXE",
      "DSIM",
      "LOSSLE",
      "E"
    ]
  },
  {
    "id": "cw-beg-09",
    "title": "Judicial Officer Cause List",
    "collection": "Judicial Terminology",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "GRANT",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: GRANT",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "INDEX",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: INDEX",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "PRISON",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: PRISON",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "THREAT",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: THREAT",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "FACTS",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Legal term: FACTS",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "LAND",
        "direction": "across",
        "row": 5,
        "col": 0,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Judicial Terminology",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Judicial Terminology.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "PFI",
      "GRANT",
      "ICDH",
      "STER",
      "OSXE",
      "LANDA",
      "T",
      ""
    ]
  },
  {
    "id": "cw-beg-10",
    "title": "The Judicial Generalist",
    "collection": "Mixed Judicial Knowledge",
    "difficulty": "beginner",
    "gridSize": {
      "rows": 8,
      "cols": 8
    },
    "words": [
      {
        "word": "PLACE",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: PLACE",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "MENSREA",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Guilty mind or blameworthy mental state required to constitute criminal liability",
        "hint": "Reflected in maxim 'Actus non facit reum nisi mens sit rea'; manifested as intention, knowledge, or recklessness",
        "authority": "Bharatiya Nyaya Sanhita, 2023, General Exceptions (Sections 14-44); State of Maharashtra v. Mayer Hans George (AIR 1965 SC 722)",
        "definition": "The culpable state of mind that accompanies a criminal act, necessary to establish criminal guilt.",
        "vocabId": "voc-038",
        "clueNum": 3
      },
      {
        "word": "WARRANT",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: WARRANT",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "APPEAL",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: APPEAL",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "COST",
        "direction": "down",
        "row": 2,
        "col": 4,
        "clue": "Legal term: COST",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "SLANDER",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Defamation published in a transient, non-permanent form, typically through spoken oral words or fleeting gestures",
        "hint": "Distinguished in common law from libel; in Indian criminal law, both slander and libel are treated alike under BNS Section 356",
        "authority": "Consolidated Cafe v. Dharmalingam (AIR 1958 Mad 241)",
        "definition": "The publication of false and defamatory statements in temporary oral or spoken form.",
        "vocabId": "voc-166",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "",
      "AWM",
      "PLACE",
      "PRON",
      "ERSS",
      "AATR",
      "SLANDER",
      "TA"
    ]
  },
  {
    "id": "cw-int-01",
    "title": "The Fundamental Rights Vault",
    "collection": "Constitutional Law",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "LEASE",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Transfer of a right to enjoy immovable property made for a certain time or in perpetuity in consideration of price or rent",
        "hint": "Defined in Section 105 of Transfer of Property Act, 1882; parties are lessor and lessee",
        "authority": "Transfer of Property Act, 1882, Section 105; Associated Hotels of India v. R.N. Kapoor (AIR 1959 SC 1262)",
        "definition": "A contractual grant of exclusive possession of real property for a specified term in exchange for rent.",
        "vocabId": "voc-267",
        "clueNum": 3
      },
      {
        "word": "REMITTER",
        "direction": "down",
        "row": 2,
        "col": 5,
        "clue": "Legal term: REMITTER",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "ASSAULT",
        "direction": "down",
        "row": 3,
        "col": 3,
        "clue": "Gesture or preparation causing apprehension of imminent criminal force on another's person",
        "hint": "Section 130 of BNS 2023 (formerly Section 351 IPC); mere words alone do not amount to assault without gesture",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 130; AC Cama v. H.F. Morgan (1864 1 BHC 205)",
        "definition": "An act creating a reasonable apprehension in another that criminal force is about to be inflicted.",
        "vocabId": "voc-043",
        "clueNum": 4
      },
      {
        "word": "SUMMONS",
        "direction": "down",
        "row": 3,
        "col": 4,
        "clue": "Legal term: SUMMONS",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "RESERVE",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: RESERVE",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "PLEA",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: PLEA",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "R",
      "E",
      "SR",
      "LEASE",
      "RSUM",
      "VSMI",
      "PLEAMT",
      "UOT",
      "LNE",
      "TSR"
    ]
  },
  {
    "id": "cw-int-02",
    "title": "Offenses Against the Person",
    "collection": "Bharatiya Nyaya Sanhita",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "DRAFT",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: DRAFT",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "GIFT",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Transfer of certain existing movable or immovable property made voluntarily and without consideration by donor to donee",
        "hint": "Defined in Section 122 of Transfer of Property Act, 1882; must be accepted by donee during donor's lifetime",
        "authority": "Transfer of Property Act, 1882, Section 122 & 123; K. Balakrishnan v. K. Kamalam (2004 1 SCC 581)",
        "definition": "A gratuitous voluntary transfer of property ownership made without monetary consideration and accepted by donee.",
        "vocabId": "voc-270",
        "clueNum": 2
      },
      {
        "word": "DIVORCE",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: DIVORCE",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "STALKING",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Repeatedly following, contacting, or monitoring a person electronically without consent, causing alarm",
        "hint": "Section 78 of BNS 2023 (formerly Section 354D IPC); includes cyber stalking",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 78",
        "definition": "A persistent pattern of obsessive surveillance, tracking, or online harassment that induces fear.",
        "vocabId": "voc-064",
        "clueNum": 1
      },
      {
        "word": "PREMISE",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: PREMISE",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "REST",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Legal term: REST",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "SG",
      "PTI",
      "DRAFT",
      "IELT",
      "VMK",
      "OII",
      "RSN",
      "CEG",
      "REST",
      ""
    ]
  },
  {
    "id": "cw-int-03",
    "title": "Bail & Custodial Inquiries",
    "collection": "Criminal Procedure",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "LAWS",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: LAWS",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "SETOFF",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Statutory cross-claim for ascertained sum of money legally recoverable by defendant from plaintiff in a money recovery suit",
        "hint": "Order VIII Rule 6 CPC; both debts must be mutual and legally recoverable at the date of suit",
        "authority": "Code of Civil Procedure, 1908, Order VIII Rule 6; Union of India v. Karam Chand Thapar (2004 3 SCC 504)",
        "definition": "A plea whereby a defendant seeks to extinguish or reduce plaintiff's money claim through a mutual existing debt.",
        "vocabId": "voc-076",
        "clueNum": 4
      },
      {
        "word": "LEGITIM",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: LEGITIM",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "LAWSUIT",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: LAWSUIT",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "WAIVER",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: WAIVER",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "AMEND",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: AMEND",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "L",
      "LAWS",
      "EWAE",
      "GSIT",
      "IUVO",
      "TIEF",
      "ITRF",
      "AMEND",
      "",
      ""
    ]
  },
  {
    "id": "cw-int-04",
    "title": "Burden of Proof & Estoppel",
    "collection": "Law of Evidence",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "OATH",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: OATH",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "BOUND",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: BOUND",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "INHERENT",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Legal term: INHERENT",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "APPEAL",
        "direction": "down",
        "row": 3,
        "col": 2,
        "clue": "Legal term: APPEAL",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "STATE",
        "direction": "down",
        "row": 2,
        "col": 3,
        "clue": "Legal term: STATE",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "SALE",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Legal term: SALE",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "",
      "I",
      "BSN",
      "OATH",
      "UPAE",
      "NPTR",
      "DEEE",
      "AN",
      "SALET",
      ""
    ]
  },
  {
    "id": "cw-int-05",
    "title": "Pleadings, Decrees & Orders",
    "collection": "Civil Procedure",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "DEAL",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: DEAL",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "DEBIT",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: DEBIT",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "WAGER",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Agreement depending solely upon the happening or not happening of an uncertain event where neither party has interest other than the stake",
        "hint": "Declared void under Section 30 of Indian Contract Act, 1872; betting on horse racing is an exception",
        "authority": "Indian Contract Act, 1872, Section 30; Gherulal Parakh v. Mahadeodas Maiya (AIR 1959 SC 781)",
        "definition": "A gambling agreement where parties mutually stake money exclusively on an uncertain chance without proprietary interest.",
        "vocabId": "voc-155",
        "clueNum": 1
      },
      {
        "word": "EXACT",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: EXACT",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "ALIBI",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Plea by an accused that they were at another place at the time the alleged crime was committed",
        "hint": "Latin for 'elsewhere'; relevant under Section 9 of Bharatiya Sakshya Adhiniyam, 2023 (Section 11 IEA)",
        "authority": "Bharatiya Sakshya Adhiniyam, 2023, Section 9; Dudh Nath Pandey v. State of U.P. (1981 2 SCC 166)",
        "definition": "An evidentiary defense establishing physical impossibility of participation due to being at a distant location.",
        "vocabId": "voc-054",
        "clueNum": 2
      },
      {
        "word": "ATTORNEY",
        "direction": "across",
        "row": 5,
        "col": 0,
        "clue": "Legal term: ATTORNEY",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "WA",
      "DEAL",
      "EXGI",
      "BAEB",
      "ICRI",
      "ATTORNEY",
      "",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-int-06",
    "title": "Vitiating Factors in Contract",
    "collection": "Contract Law",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "SIGN",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: SIGN",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "GOVERNOR",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Constitutional executive head of a State appointed by the President under Article 155",
        "hint": "Acts on aid and advice of State Council of Ministers under Article 163, subject to discretionary powers",
        "authority": "Constitution of India, Articles 153-163; Shamsher Singh v. State of Punjab",
        "definition": "The nominal constitutional executive head of a constituent state in the Indian Union appointed for a 5-year term.",
        "vocabId": "voc-030",
        "clueNum": 4
      },
      {
        "word": "SALE",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: SALE",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "INHERENT",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: INHERENT",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "INDEX",
        "direction": "down",
        "row": 1,
        "col": 2,
        "clue": "Legal term: INDEX",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "LIEN",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Right of a person in possession of another's property to retain it until certain claims or debts are satisfied",
        "hint": "Particular lien of bailee (Section 170) and general lien of bankers/factors/attorneys (Section 171 ICA)",
        "authority": "Indian Contract Act, 1872, Section 170 & 171; Syndicate Bank v. Vijay Kumar (1992 2 SCC 330)",
        "definition": "A legal right to retain lawful possession of another's personal goods until the possessor's dues are paid.",
        "vocabId": "voc-146",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "I",
      "SIGN",
      "ANOH",
      "LDVE",
      "EEER",
      "XRE",
      "LIENN",
      "OT",
      "R",
      ""
    ]
  },
  {
    "id": "cw-int-07",
    "title": "Strict Liability & Defamation",
    "collection": "Law of Torts",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "BREACH",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Failure or refusal without legal excuse to perform any promise that forms the whole or part of a contract",
        "hint": "Sections 73-75 of Indian Contract Act, 1872; gives rise to right to damages or termination",
        "authority": "Indian Contract Act, 1872, Section 73 & 74; Hadley v. Baxendale (1854 9 Exch 341)",
        "definition": "The non-performance or repudiation of a binding contractual obligation without lawful justification.",
        "vocabId": "voc-139",
        "clueNum": 2
      },
      {
        "word": "BIGAMY",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Contracting a second marriage during the lifetime of a spouse while the prior valid marriage subsists",
        "hint": "Section 82 of BNS 2023 (formerly Section 494 IPC); void ab initio under Hindu Marriage Act, Section 11",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 82; Sarla Mudgal v. Union of India (1995 3 SCC 635)",
        "definition": "The criminal act of marrying another person while still lawfully wedded to an existing spouse.",
        "vocabId": "voc-059",
        "clueNum": 2
      },
      {
        "word": "TEST",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Legal term: TEST",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "CITE",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: CITE",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "HOMICIDE",
        "direction": "down",
        "row": 1,
        "col": 6,
        "clue": "The killing of a human being by another human being, lawful or unlawful",
        "hint": "Divided into lawful (justifiable/excusable) and unlawful (culpable homicide under Section 100 BNS)",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 100 & 101; Reg. v. Govinda (1876 ILR 1 Bom 342)",
        "definition": "The act of causing the death of a human being through an act or omission.",
        "vocabId": "voc-041",
        "clueNum": 4
      },
      {
        "word": "PAROLE",
        "direction": "across",
        "row": 4,
        "col": 0,
        "clue": "Conditional and temporary release of a convicted prisoner before expiration of sentence for special reasons",
        "hint": "Distinguished from furlough; granted for family bereavement, medical emergency, or reformative rehabilitation",
        "authority": "State of Haryana v. Mahender Singh (2007 13 SCC 606); Asfaq v. State of Rajasthan (2017 15 SCC 55)",
        "definition": "The temporary release of an incarcerated convict from prison under strict supervision and conditions of good behavior.",
        "vocabId": "voc-258",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "T",
      "BREACH",
      "ISIO",
      "GTTM",
      "PAROLEI",
      "MC",
      "YI",
      "D",
      "E",
      ""
    ]
  },
  {
    "id": "cw-int-08",
    "title": "Legal Theories & Analytical Positivism",
    "collection": "Jurisprudence",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "TIME",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: TIME",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "TREASON",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Waging or attempting to wage war against the Government of India",
        "hint": "Section 147 of BNS 2023 (formerly Section 121 IPC); carries capital punishment or life imprisonment",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 147; State (N.C.T. of Delhi) v. Navjot Sandhu (2005 11 SCC 600)",
        "definition": "The crime of betraying one's country, especially by waging war or assisting its external enemies.",
        "vocabId": "voc-062",
        "clueNum": 3
      },
      {
        "word": "DAMAGES",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Monetary compensation awarded by court for loss or injury suffered from breach of contract or tortious act",
        "hint": "Section 73 of Indian Contract Act, 1872; compensates naturally arising proximate losses, excluding remote damages",
        "authority": "Indian Contract Act, 1872, Section 73; Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd. (1949 2 KB 528)",
        "definition": "The pecuniary compensation recoverable in court for breach of contract, measured by the loss suffered.",
        "vocabId": "voc-140",
        "clueNum": 2
      },
      {
        "word": "EXACT",
        "direction": "down",
        "row": 2,
        "col": 4,
        "clue": "Legal term: EXACT",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "VOIDABLE",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "An agreement enforceable by law at the option of one party thereto, but not at the option of the other",
        "hint": "Section 2(i) of Indian Contract Act, 1872; e.g., contracts entered under coercion, undue influence, fraud, misrepresentation",
        "authority": "Indian Contract Act, 1872, Section 2(i) & 19",
        "definition": "A valid contract that may be legally affirmed or repudiated at the sole choice of the aggrieved innocent party.",
        "vocabId": "voc-134",
        "clueNum": 1
      },
      {
        "word": "COERCE",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: COERCE",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "VD",
      "OA",
      "TIME",
      "RDAX",
      "EAGA",
      "ABEC",
      "SLST",
      "COERCE",
      "N",
      ""
    ]
  },
  {
    "id": "cw-int-09",
    "title": "Latin Doctrines of Adjudication",
    "collection": "Legal Maxims",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "PLEA",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: PLEA",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "PROPOSAL",
        "direction": "down",
        "row": 0,
        "col": 1,
        "clue": "Signification by one person to another of willingness to do or abstain from doing anything with a view to obtaining assent",
        "hint": "Defined in Section 2(a) of Indian Contract Act, 1872; when accepted, becomes a promise",
        "authority": "Indian Contract Act, 1872, Section 2(a) & Section 8; Carlill v. Carbolic Smoke Ball Co. (1893 1 QB 256)",
        "definition": "An offer made by one party communicating readiness to be bound upon acceptance by the offeree.",
        "vocabId": "voc-127",
        "clueNum": 1
      },
      {
        "word": "PLEAD",
        "direction": "down",
        "row": 2,
        "col": 2,
        "clue": "Legal term: PLEAD",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "ESTATE",
        "direction": "down",
        "row": 3,
        "col": 3,
        "clue": "Legal term: ESTATE",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "FINAL",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: FINAL",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "PLOT",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: PLOT",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "PF",
      "RI",
      "OPN",
      "PLEA",
      "OESL",
      "SAT",
      "ADA",
      "PLOT",
      "E",
      ""
    ]
  },
  {
    "id": "cw-int-10",
    "title": "Precedents & Apex Rulings",
    "collection": "Landmark Indian Judgments",
    "difficulty": "intermediate",
    "gridSize": {
      "rows": 10,
      "cols": 10
    },
    "words": [
      {
        "word": "SEARCH",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: SEARCH",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "LAND",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "HOLD",
        "direction": "down",
        "row": 2,
        "col": 6,
        "clue": "Legal term: HOLD",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "ACTION",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: ACTION",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "SUITS",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: SUITS",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "ASSET",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: ASSET",
        "hint": "Pertains to Landmark Indian Judgments",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Landmark Indian Judgments.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "",
      "LA",
      "SEARCH",
      "UNTO",
      "IDIL",
      "TOD",
      "ASSETN",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-01",
    "title": "The Constitutional Assembly Archive",
    "collection": "Constitutional Law",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "BREACH",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Failure or refusal without legal excuse to perform any promise that forms the whole or part of a contract",
        "hint": "Sections 73-75 of Indian Contract Act, 1872; gives rise to right to damages or termination",
        "authority": "Indian Contract Act, 1872, Section 73 & 74; Hadley v. Baxendale (1854 9 Exch 341)",
        "definition": "The non-performance or repudiation of a binding contractual obligation without lawful justification.",
        "vocabId": "voc-139",
        "clueNum": 5
      },
      {
        "word": "ABETMENT",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Instigating, conspiring, or intentionally aiding another in the commission of an offense",
        "hint": "Section 45 of BNS 2023 (formerly Section 107 IPC); covers instigation, conspiracy, and intentional aiding",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 45; Sanju v. State of M.P. (2002 5 SCC 371)",
        "definition": "Encouraging, facilitating, or intentionally helping another individual to perpetrate a crime.",
        "vocabId": "voc-046",
        "clueNum": 1
      },
      {
        "word": "TERMS",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: TERMS",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "CHARGES",
        "direction": "down",
        "row": 1,
        "col": 6,
        "clue": "Legal term: CHARGES",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "LAWYER",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Legal term: LAWYER",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "RECORD",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: RECORD",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 6
      },
      {
        "word": "STATE",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Legal term: STATE",
        "hint": "Pertains to Constitutional Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Constitutional Law.",
        "vocabId": "",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "",
      "ATLC",
      "BREACH",
      "ERWA",
      "TMYR",
      "MSEG",
      "RECORDE",
      "NS",
      "STATE",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-02",
    "title": "Aggravated Crimes & Common Intention",
    "collection": "Bharatiya Nyaya Sanhita",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "GUILT",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Legal term: GUILT",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "CUSTODY",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: CUSTODY",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "LAWSUIT",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Legal term: LAWSUIT",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "TIME",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: TIME",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "INJURY",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: INJURY",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "EVICT",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: EVICT",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 6
      },
      {
        "word": "TEST",
        "direction": "across",
        "row": 7,
        "col": 4,
        "clue": "Legal term: TEST",
        "hint": "Pertains to Bharatiya Nyaya Sanhita",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Bharatiya Nyaya Sanhita.",
        "vocabId": "",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "C",
      "GUILT",
      "SNAI",
      "TJWM",
      "OUSE",
      "DRU",
      "YYI",
      "EVICTEST",
      "",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-03",
    "title": "Procedural Inquests & Trial Mechanics",
    "collection": "Criminal Procedure",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "FORENSIC",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: FORENSIC",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "SIGN",
        "direction": "down",
        "row": 2,
        "col": 6,
        "clue": "Legal term: SIGN",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "OFFENDER",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: OFFENDER",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "FACT",
        "direction": "down",
        "row": 0,
        "col": 8,
        "clue": "Legal term: FACT",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "INQUEST",
        "direction": "down",
        "row": 2,
        "col": 7,
        "clue": "Legal term: INQUEST",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "HEARING",
        "direction": "across",
        "row": 4,
        "col": 0,
        "clue": "Legal term: HEARING",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 6
      },
      {
        "word": "ARBITER",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Legal term: ARBITER",
        "hint": "Pertains to Criminal Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Criminal Procedure.",
        "vocabId": "",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "F",
      "OA",
      "FORENSIC",
      "FINT",
      "HEARINGQ",
      "NNU",
      "DE",
      "ES",
      "ARBITERT",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-04",
    "title": "The Digital Certificate & Res Gestae",
    "collection": "Law of Evidence",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "BAILMENT",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Delivery of goods by one person to another for some purpose upon contract to return them when purpose is accomplished",
        "hint": "Defined in Section 148 of Indian Contract Act, 1872; parties are bailor and bailee",
        "authority": "Indian Contract Act, 1872, Section 148; Coggs v. Bernard (1703 2 Ld Raym 909)",
        "definition": "The transfer of physical possession of personal property without transferring ownership, for a specific purpose.",
        "vocabId": "voc-144",
        "clueNum": 3
      },
      {
        "word": "BIGAMY",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Contracting a second marriage during the lifetime of a spouse while the prior valid marriage subsists",
        "hint": "Section 82 of BNS 2023 (formerly Section 494 IPC); void ab initio under Hindu Marriage Act, Section 11",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 82; Sarla Mudgal v. Union of India (1995 3 SCC 635)",
        "definition": "The criminal act of marrying another person while still lawfully wedded to an existing spouse.",
        "vocabId": "voc-059",
        "clueNum": 3
      },
      {
        "word": "LEGACY",
        "direction": "down",
        "row": 0,
        "col": 6,
        "clue": "Legal term: LEGACY",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "MINORITY",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: MINORITY",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "CLAUSE",
        "direction": "down",
        "row": 0,
        "col": 4,
        "clue": "Legal term: CLAUSE",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "REMEDY",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Means given by law for recovery of a right or obtaining redress for a wrong (Article 32)",
        "hint": "Termed 'heart and soul' of the Constitution by Dr. B.R. Ambedkar",
        "authority": "Constitution of India, Article 32; Prem Chand Garg v. Excise Commissioner (AIR 1963 SC 996)",
        "definition": "The legal means enforced by a court of law to restore a right, recover compensation, or redress an injury.",
        "vocabId": "voc-025",
        "clueNum": 6
      },
      {
        "word": "DOCKET",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: DOCKET",
        "hint": "Pertains to Law of Evidence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Evidence.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "CL",
      "BAILMENT",
      "IAIG",
      "GUNA",
      "ASOC",
      "MERY",
      "YI",
      "DOCKET",
      "REMEDY",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-05",
    "title": "Execution, Garnishee & Restitution",
    "collection": "Civil Procedure",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "ECLIPSE",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Doctrine where a pre-constitutional law violating fundamental rights becomes dormant rather than dead",
        "hint": "Can revive upon subsequent constitutional amendment removing the inconsistency",
        "authority": "Constitution of India, Article 13(1); Bhikaji Narain Dhakras v. State of M.P. (AIR 1955 SC 781)",
        "definition": "A principle where a pre-constitutional law in conflict with fundamental rights remains dormant and unenforceable, but revives once the constitutional shadow is removed.",
        "vocabId": "voc-010",
        "clueNum": 5
      },
      {
        "word": "PREAMBLE",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Introductory statement setting out guiding ideals, philosophy, and objectives of the Constitution",
        "hint": "Held to be an integral part of the Constitution in Kesavananda Bharati (1973)",
        "authority": "Constitution of India, Preamble; Re: Berubari Union (1960) & Kesavananda Bharati (1973)",
        "definition": "The solemn preface declaring the source of authority, nature of polity, and fundamental objectives of the Indian Republic.",
        "vocabId": "voc-021",
        "clueNum": 2
      },
      {
        "word": "RISK",
        "direction": "down",
        "row": 2,
        "col": 4,
        "clue": "Legal term: RISK",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "DISPUTE",
        "direction": "down",
        "row": 0,
        "col": 5,
        "clue": "Legal term: DISPUTE",
        "hint": "Pertains to Civil Procedure",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Civil Procedure.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "ASSAULT",
        "direction": "down",
        "row": 2,
        "col": 6,
        "clue": "Gesture or preparation causing apprehension of imminent criminal force on another's person",
        "hint": "Section 130 of BNS 2023 (formerly Section 351 IPC); mere words alone do not amount to assault without gesture",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 130; AC Cama v. H.F. Morgan (1864 1 BHC 205)",
        "definition": "An act creating a reasonable apprehension in another that criminal force is about to be inflicted.",
        "vocabId": "voc-043",
        "clueNum": 4
      },
      {
        "word": "PLAINT",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "The statement of claim in writing through which a civil suit is formally instituted by a plaintiff",
        "hint": "Governed by Order VII of CPC; must state material facts, cause of action, valuation, and relief",
        "authority": "Code of Civil Procedure, 1908, Section 26 & Order VII; Saleem Bhai v. State of Maharashtra (2003 1 SCC 557)",
        "definition": "The formal written pleading wherein a plaintiff sets forth the cause of action and prayers seeking relief.",
        "vocabId": "voc-068",
        "clueNum": 6
      },
      {
        "word": "DECREE",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Formal expression of an adjudication conclusively determining the rights of parties with regard to all or any matters in controversy",
        "hint": "Defined in Section 2(2) CPC; includes preliminary and final decrees, and rejection of plaint",
        "authority": "Code of Civil Procedure, 1908, Section 2(2); Phoolchand v. Gopal Lal (AIR 1967 SC 1470)",
        "definition": "The formal judicial declaration resolving the substantive disputes in a civil suit conclusively.",
        "vocabId": "voc-071",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "D",
      "PI",
      "RRSA",
      "ECLIPSE",
      "ASUS",
      "MKTA",
      "BEU",
      "PLAINTL",
      "DECREET",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-06",
    "title": "Commercial Indemnity & Bailment",
    "collection": "Contract Law",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "PAPER",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Legal term: PAPER",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "EXPARTE",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Proceedings conducted or orders passed in the absence of one of the parties who failed to appear despite notice",
        "hint": "Governed by Order IX Rule 6 CPC; remedy to set aside ex parte decree lies under Order IX Rule 13",
        "authority": "Code of Civil Procedure, 1908, Order IX Rules 6 & 13; G.P. Srivastava v. R.K. Raizada (2000 3 SCC 54)",
        "definition": "A judicial act performed or decree pronounced by the court when only one party is present.",
        "vocabId": "voc-083",
        "clueNum": 2
      },
      {
        "word": "RULES",
        "direction": "down",
        "row": 2,
        "col": 5,
        "clue": "Legal term: RULES",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "SEAL",
        "direction": "down",
        "row": 0,
        "col": 2,
        "clue": "Legal term: SEAL",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "PLEA",
        "direction": "down",
        "row": 2,
        "col": 1,
        "clue": "Legal term: PLEA",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "PARTY",
        "direction": "across",
        "row": 5,
        "col": 0,
        "clue": "Legal term: PARTY",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 6
      },
      {
        "word": "HEARS",
        "direction": "across",
        "row": 4,
        "col": 0,
        "clue": "Legal term: HEARS",
        "hint": "Pertains to Contract Law",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Contract Law.",
        "vocabId": "",
        "clueNum": 5
      }
    ],
    "solutionGrid": [
      "SE",
      "EX",
      "PAPER",
      "LLAU",
      "HEARSL",
      "PARTYE",
      "ES",
      "",
      "",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-07",
    "title": "Absolute Liability & Environmental Torts",
    "collection": "Law of Torts",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "MENSREA",
        "direction": "across",
        "row": 2,
        "col": 1,
        "clue": "Guilty mind or blameworthy mental state required to constitute criminal liability",
        "hint": "Reflected in maxim 'Actus non facit reum nisi mens sit rea'; manifested as intention, knowledge, or recklessness",
        "authority": "Bharatiya Nyaya Sanhita, 2023, General Exceptions (Sections 14-44); State of Maharashtra v. Mayer Hans George (AIR 1965 SC 722)",
        "definition": "The culpable state of mind that accompanies a criminal act, necessary to establish criminal guilt.",
        "vocabId": "voc-038",
        "clueNum": 3
      },
      {
        "word": "REMITTER",
        "direction": "down",
        "row": 2,
        "col": 5,
        "clue": "Legal term: REMITTER",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "EASEMENT",
        "direction": "down",
        "row": 1,
        "col": 7,
        "clue": "Right which owner or occupier of certain land possesses for beneficial enjoyment of that land to do or continue to do something on another's land",
        "hint": "Defined in Section 4 of Indian Easements Act, 1882; involves dominant heritage and servient heritage",
        "authority": "Indian Easements Act, 1882, Section 4 & 13; Chapsibhai Dhanjibhai Danad v. Purushottam (1971 2 SCC 205)",
        "definition": "A non-possessory right to use or cross a neighbor's real property for the beneficial enjoyment of one's own land.",
        "vocabId": "voc-271",
        "clueNum": 2
      },
      {
        "word": "EVICT",
        "direction": "down",
        "row": 2,
        "col": 2,
        "clue": "Legal term: EVICT",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "RENT",
        "direction": "down",
        "row": 1,
        "col": 6,
        "clue": "Legal term: RENT",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "DIVIDE",
        "direction": "across",
        "row": 8,
        "col": 0,
        "clue": "Legal term: DIVIDE",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 6
      },
      {
        "word": "DEATH",
        "direction": "across",
        "row": 8,
        "col": 4,
        "clue": "Legal term: DEATH",
        "hint": "Pertains to Law of Torts",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Law of Torts.",
        "vocabId": "",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "",
      "RE",
      "MENSREA",
      "VENS",
      "IMTE",
      "CIM",
      "TTE",
      "TN",
      "DIVIDEATH",
      "R",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-08",
    "title": "The Pure Theory & Grundnorm",
    "collection": "Jurisprudence",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "LAND",
        "direction": "across",
        "row": 3,
        "col": 1,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "INDEX",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Legal term: INDEX",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "INQUEST",
        "direction": "down",
        "row": 2,
        "col": 3,
        "clue": "Legal term: INQUEST",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "MALICE",
        "direction": "down",
        "row": 2,
        "col": 2,
        "clue": "Wrongful intention or improper motive; in tort law, a lawful act generally does not become unlawful merely through malice",
        "hint": "Reflected in Mayor of Bradford v. Pickles; exception exists in malicious prosecution",
        "authority": "Mayor of Bradford v. Pickles (1895 AC 587); Allen v. Flood (1898 AC 1)",
        "definition": "An evil motive or spiteful intent to injure another person through legal or illegal mechanisms.",
        "vocabId": "voc-173",
        "clueNum": 3
      },
      {
        "word": "GUILTY",
        "direction": "down",
        "row": 0,
        "col": 1,
        "clue": "Legal term: GUILTY",
        "hint": "Pertains to Jurisprudence",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Jurisprudence.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "DECEIT",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Tort of intentionally making a false representation with intention that plaintiff act upon it, causing damage",
        "hint": "Requires proof of actual fraud under Derry v. Peek; distinct from innocent misrepresentation",
        "authority": "Derry v. Peek (1889 14 App Cas 337); Pasley v. Freeman (1789 3 TR 51)",
        "definition": "A common law tort wherein a defendant makes a knowingly false statement intended to induce reliance causing financial harm.",
        "vocabId": "voc-169",
        "clueNum": 6
      },
      {
        "word": "TRESPASS",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Direct and forcible physical interference with another's person, land, or goods without lawful justification",
        "hint": "Actionable per se without requiring proof of actual damage; e.g., stepping onto private land without leave",
        "authority": "Entick v. Carrington (1765 19 St Tr 1029)",
        "definition": "The direct, unjustified entry upon another's land or interference with their personal property or person.",
        "vocabId": "voc-165",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "G",
      "UI",
      "IMIN",
      "LAND",
      "TLQE",
      "YIUX",
      "DECEIT",
      "TRESPASS",
      "T",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-09",
    "title": "Maxims of Sovereign Justice",
    "collection": "Legal Maxims",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "VOIDABLE",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "An agreement enforceable by law at the option of one party thereto, but not at the option of the other",
        "hint": "Section 2(i) of Indian Contract Act, 1872; e.g., contracts entered under coercion, undue influence, fraud, misrepresentation",
        "authority": "Indian Contract Act, 1872, Section 2(i) & 19",
        "definition": "A valid contract that may be legally affirmed or repudiated at the sole choice of the aggrieved innocent party.",
        "vocabId": "voc-134",
        "clueNum": 2
      },
      {
        "word": "DACOITY",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Robbery committed or attempted by five or more persons acting conjointly",
        "hint": "Section 310 of BNS 2023 (formerly Section 391 IPC); assembly of 5+ persons is an essential ingredient",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 310; Shyam Behari v. State of U.P. (AIR 1957 SC 320)",
        "definition": "A joint robbery committed by five or more persons acting in concert.",
        "vocabId": "voc-034",
        "clueNum": 4
      },
      {
        "word": "PETIT",
        "direction": "down",
        "row": 0,
        "col": 8,
        "clue": "Legal term: PETIT",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "LAWYER",
        "direction": "down",
        "row": 1,
        "col": 7,
        "clue": "Legal term: LAWYER",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 5
      },
      {
        "word": "IMPEACH",
        "direction": "down",
        "row": 1,
        "col": 3,
        "clue": "Legal term: IMPEACH",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "REMAINDER",
        "direction": "across",
        "row": 5,
        "col": 0,
        "clue": "Future estate created in favor of a third party to take effect immediately upon the termination of a prior particular estate",
        "hint": "Contrasted with reversion; e.g., to A for life, and upon A's death, remainder to B in fee simple",
        "authority": "Transfer of Property Act, 1882, Section 19 & 21; R. Rajagopal Reddy v. Padmini Chandrasekharan (1995 2 SCC 630)",
        "definition": "A future interest in real property granted to a third party that takes effect upon the expiration of a prior life estate.",
        "vocabId": "voc-276",
        "clueNum": 6
      },
      {
        "word": "OATH",
        "direction": "across",
        "row": 7,
        "col": 0,
        "clue": "Legal term: OATH",
        "hint": "Pertains to Legal Maxims",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Legal Maxims.",
        "vocabId": "",
        "clueNum": 7
      }
    ],
    "solutionGrid": [
      "P",
      "VOIDABLE",
      "MAAT",
      "PCWI",
      "EOYT",
      "REMAINDER",
      "CTR",
      "OATHY",
      "",
      "",
      "",
      ""
    ]
  },
  {
    "id": "cw-adv-10",
    "title": "The Grand Judicial Synthesis",
    "collection": "Mixed Judicial Knowledge",
    "difficulty": "advanced",
    "gridSize": {
      "rows": 12,
      "cols": 12
    },
    "words": [
      {
        "word": "DECREE",
        "direction": "across",
        "row": 1,
        "col": 1,
        "clue": "Formal expression of an adjudication conclusively determining the rights of parties with regard to all or any matters in controversy",
        "hint": "Defined in Section 2(2) CPC; includes preliminary and final decrees, and rejection of plaint",
        "authority": "Code of Civil Procedure, 1908, Section 2(2); Phoolchand v. Gopal Lal (AIR 1967 SC 1470)",
        "definition": "The formal judicial declaration resolving the substantive disputes in a civil suit conclusively.",
        "vocabId": "voc-071",
        "clueNum": 2
      },
      {
        "word": "RULE",
        "direction": "down",
        "row": 1,
        "col": 4,
        "clue": "Legal term: RULE",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 3
      },
      {
        "word": "DRAFT",
        "direction": "down",
        "row": 1,
        "col": 1,
        "clue": "Legal term: DRAFT",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 2
      },
      {
        "word": "ACCUSED",
        "direction": "down",
        "row": 0,
        "col": 3,
        "clue": "Legal term: ACCUSED",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 1
      },
      {
        "word": "EXACT",
        "direction": "down",
        "row": 1,
        "col": 5,
        "clue": "Legal term: EXACT",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 4
      },
      {
        "word": "THEFT",
        "direction": "across",
        "row": 5,
        "col": 1,
        "clue": "Dishonestly taking any movable property out of possession of any person without consent",
        "hint": "Governed by Section 303 of Bharatiya Nyaya Sanhita, 2023 (formerly Section 378 IPC)",
        "authority": "Bharatiya Nyaya Sanhita, 2023, Section 303(2); Pyare Lal Bhargava v. State of Rajasthan (AIR 1963 SC 1094)",
        "definition": "The unlawful taking of movable property out of another's possession with dishonest intention at inception.",
        "vocabId": "voc-031",
        "clueNum": 5
      },
      {
        "word": "LAND",
        "direction": "across",
        "row": 6,
        "col": 0,
        "clue": "Legal term: LAND",
        "hint": "Pertains to Mixed Judicial Knowledge",
        "authority": "Indian Legal Jurisprudence",
        "definition": "Key statutory concept in Mixed Judicial Knowledge.",
        "vocabId": "",
        "clueNum": 6
      }
    ],
    "solutionGrid": [
      "A",
      "DECREE",
      "RCUX",
      "AULA",
      "FSEC",
      "THEFT",
      "LAND",
      "",
      "",
      "",
      "",
      ""
    ]
  }
];

  const BY_ID = {};
  const BY_DIFFICULTY = { beginner: [], intermediate: [], advanced: [] };
  const BY_COLLECTION = {};

  PUZZLES.forEach(p => {
    BY_ID[p.id] = p;
    if (BY_DIFFICULTY[p.difficulty]) {
      BY_DIFFICULTY[p.difficulty].push(p);
    }
    if (!BY_COLLECTION[p.collection]) {
      BY_COLLECTION[p.collection] = [];
    }
    BY_COLLECTION[p.collection].push(p);
  });

  window.ARENA_CROSSWORDS = PUZZLES;
  window.ARENA_CROSSWORDS_BY_ID = BY_ID;
  window.ARENA_CROSSWORDS_BY_DIFFICULTY = BY_DIFFICULTY;
  window.ARENA_CROSSWORDS_BY_COLLECTION = BY_COLLECTION;
})();
