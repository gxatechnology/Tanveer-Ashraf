/**
 * BE THE JUDGE: THE COURTROOM — AUTHORED & VERIFIED JUDICIAL HEARINGS
 * Comprehensive Civil, Criminal, Evidentiary and Constitutional Hearings
 * Governed by Bharatiya Nagarik Suraksha Sanhita 2023 (BNSS), Bharatiya Sakshya Adhiniyam 2023 (BSA),
 * Code of Civil Procedure (CPC), and Constitution of India.
 */
(function() {
  'use strict';

  const COURTROOM_CASES = [
    // =========================================================================
    // CASE 1 (BEGINNER): THE QUESTION OF POSSESSION (INTERIM INJUNCTION)
    // =========================================================================
    {
      id: 'court-case-1',
      caseNumber: 'OS-2026-104',
      title: 'The Question of Possession',
      difficulty: 'beginner',
      category: 'Civil Procedure & Specific Relief',
      estimatedMinutes: 10,
      legalVerification: {
        act: 'Code of Civil Procedure, 1908 & Specific Relief Act, 1963',
        section: 'Order XXXIX Rules 1 & 2 CPC / Section 38 Specific Relief Act',
        proposition: 'Temporary injunction requires establishing three mandatory pillars: (1) Prima facie case, (2) Balance of convenience, (3) Irreparable injury that cannot be compensated in money. Settled peaceful possession must be protected against forcible dispossession without due process of law (Rame Gowda v. M. Varadappa Naidu).',
        source: 'Supreme Court of India (Rame Gowda v. M. Varadappa Naidu, 2004 1 SCC 769)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2191',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Calling Original Suit No. 104 of 2026: Suresh Chandra versus Mahendra Pratap. Application under Order XXXIX Rules 1 and 2 of the Code of Civil Procedure for temporary injunction restraining the defendant from forcibly dispossessing the plaintiff from agricultural plot No. 42.'
        },
        arguments: [
          {
            speaker: 'ananya',
            counselType: 'Plaintiff Counsel',
            text: 'May it please the Court. My client Suresh Chandra has been in continuous, settled cultivation of Plot No. 42 for over 14 years. We have submitted electricity pump records, Khasra revenue entries for 2012–2025, and tax receipts. The defendant, who recently purchased an adjacent plot, arrived with armed labourers on Sunday attempting to bulldoze the standing wheat crop. If an ad-interim injunction is not granted today, my client\'s standing crop will be destroyed, causing irreparable injury that cannot be remedied by damages.'
          },
          {
            speaker: 'aditya',
            counselType: 'Defendant Counsel',
            text: 'I vehemently oppose the application, Your Honour! The plaintiff is a rank trespasser with zero registered title. My client holds a registered Sale Deed executed by the lawful owner last month. An injunction cannot be granted against the true owner in favor of a trespasser. Title must prevail over unauthorized occupation!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Khasra Revenue Entries (2012–2025)',
            nature: 'Public Revenue Record',
            evidentiaryRole: 'Proves prima facie settled, continuous and peaceful agricultural possession by the plaintiff.',
            weight: 'High probative value for possession'
          },
          {
            id: 'ex-2',
            name: 'Photographs of Standing Wheat Crop & Tube-Well',
            nature: 'Physical Evidence',
            evidentiaryRole: 'Demonstrates active investment and immediate danger of irreparable crop destruction.',
            weight: 'Substantiates irreparable injury'
          },
          {
            id: 'ex-3',
            name: 'Defendant\'s Registered Sale Deed (Dated Last Month)',
            nature: 'Title Document',
            evidentiaryRole: 'Proves title claims, but does not prove immediate physical possession on the spot.',
            weight: 'Valid for title, but does not authorize forcible extra-judicial eviction'
          }
        ],
        questionsToParties: [
          {
            target: 'Defence Counsel (Adv. Aditya)',
            question: 'Has your client initiated any formal suit for recovery of possession under Section 5 or 6 of the Specific Relief Act?',
            response: 'No, Your Honour, we have not filed a separate suit yet, as we believed our registered sale deed gave us the immediate right of entry.'
          },
          {
            target: 'Plaintiff Counsel (Adv. Ananya)',
            question: 'Is the plaintiff willing to provide an undertaking not to alter the nature of the suit land pending trial?',
            response: 'Yes, Your Honour! We undertake to maintain status quo and not create any third-party rights or change the agricultural character.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether the plaintiff has established settled possession amounting to a prima facie case for interim protection.',
            isCore: true
          },
          {
            id: 'issue-2',
            text: 'Whether a true owner is legally entitled to forcibly dispossess an occupant in settled possession without due process of law.',
            isCore: true
          },
          {
            id: 'issue-3',
            text: 'Whether the suit is barred by limitation.',
            isCore: false
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'ALLOW the application: Grant temporary injunction restraining the defendant from dispossessing the plaintiff except by due course of law, and direct both parties to maintain status quo.',
            isCorrect: true,
            rationale: 'In Indian law (Rame Gowda case), even a true owner cannot take the law into his own hands to forcibly evict a person in settled possession. Due process under law is mandatory.'
          },
          {
            id: 'dec-2',
            text: 'DISMISS the application: Since the defendant holds registered title, he is entitled to take possession immediately by any means necessary.',
            isCorrect: false,
            rationale: 'Legally erroneous. The rule of law prohibits forcible extra-judicial dispossession by true owners.'
          },
          {
            id: 'dec-3',
            text: 'Order the arrest and civil imprisonment of the defendant immediately.',
            isCorrect: false,
            rationale: 'Disproportionate and procedurally incompetent at the hearing of an Order 39 interim application without violation of an existing injunction order.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'Plaintiff has produced continuous revenue entries (Khasra) establishing settled agricultural possession since 2012.', isSelected: true },
            { id: 'f-2', text: 'Defendant claims title under a recent registered sale deed but has not instituted proceedings for recovery of possession.', isSelected: true },
            { id: 'f-3', text: 'The suit property was previously owned by the East India Company in 1845.', isSelected: false }
          ],
          lawPool: [
            { id: 'l-1', text: 'Order XXXIX Rules 1 & 2 CPC: A party in settled peaceful possession is entitled to protect their possession against forcible eviction (Rame Gowda v. M. Varadappa Naidu).', isSelected: true },
            { id: 'l-2', text: 'The Indian Contract Act governs the creation of agency agreements.', isSelected: false }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'Application under Order XXXIX Rules 1 & 2 is ALLOWED. Parties are directed to maintain status quo regarding possession and nature of property till disposal of suit. Defendant is restrained from dispossessing plaintiff without due process of law.', isSelected: true },
            { id: 'o-2', text: 'Suit is dismissed with costs.', isSelected: false }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'Excellent judicial discernment. In Indian civil jurisprudence, settled possession is protected against the entire world except the true owner, and even the true owner can dispossess only by recourse to law. By upholding the three pillars of Order XXXIX (prima facie case, balance of convenience, irreparable injury) and directing due process, your order embodies the core tenet: the court will never sanction self-help or forcible extra-judicial evictions.'
        }
      }
    },

    // =========================================================================
    // CASE 2 (BEGINNER): THE PROCEDURAL OBJECTION (RES JUDICATA)
    // =========================================================================
    {
      id: 'court-case-2',
      caseNumber: 'CS-2026-088',
      title: 'The Procedural Objection',
      difficulty: 'beginner',
      category: 'Civil Procedure Code',
      estimatedMinutes: 9,
      legalVerification: {
        act: 'Code of Civil Procedure, 1908',
        section: 'Section 11 [Res Judicata] vs Order IX Rule 9 / Order II Rule 2',
        proposition: 'Res Judicata under Section 11 CPC applies only when the matter directly and substantially in issue in the subsequent suit was "heard and finally decided" on merits in the former suit by a competent court. Dismissal for default of appearance under Order IX Rule 8 is not a decision on merits and does not operate as res judicata (though a fresh suit on the same cause of action is barred under Order IX Rule 9).',
        source: 'Supreme Court of India (State of U.P. v. Nawab Hussain / Erach Boman Khavar v. Tukaram Sridhar Bhat)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2191',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Civil Suit No. 88 of 2026: Bankey Lal versus Chhotelal. Preliminary objection raised by the defendant that the suit is barred by the doctrine of Res Judicata under Section 11 of the Code of Civil Procedure.'
        },
        arguments: [
          {
            speaker: 'aditya',
            counselType: 'Defendant Counsel',
            text: 'Your Honour, this is an abuse of the judicial process. The plaintiff filed an identical suit for recovery of money (Suit No. 12 of 2023) two years ago based on the very same promissory note. That earlier suit was dismissed by this very court. He cannot drag my client back to court on the same cause of action! The suit must be dismissed as barred by Res Judicata under Section 11 CPC.'
          },
          {
            speaker: 'ananya',
            counselType: 'Plaintiff Counsel',
            text: 'The learned defence counsel is misleading the court on the true nature of the previous dismissal! The previous Suit No. 12 of 2023 was never "heard and finally decided" on merits. On the date fixed for issues, my client\'s advocate suffered a heart attack, neither party appeared, and the court dismissed the suit for default under Order IX Rule 3 CPC. Because there was no adjudication on merits, Section 11 cannot apply!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Certified Copy of Order Sheet in Suit No. 12 of 2023',
            nature: 'Judicial Record',
            evidentiaryRole: 'Records: "Neither party present. Dismissed for default of appearance of both parties under Order IX Rule 3 CPC."',
            weight: 'Conclusively proves absence of hearing or adjudication on merits'
          },
          {
            id: 'ex-2',
            name: 'Plaint in Current Suit No. 88 of 2026',
            nature: 'Pleading',
            evidentiaryRole: 'Shows cause of action based on the same debt, but instituted within the surviving period of limitation.',
            weight: 'Substantiates identity of subject matter'
          }
        ],
        questionsToParties: [
          {
            target: 'Defendant Counsel (Adv. Aditya)',
            question: 'Can you show any issue framed, evidence recorded, or finding on merits delivered in the 2023 order sheet?',
            response: 'No findings were recorded, Your Honour, but the court closed the file and dismissed the suit.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether a dismissal of a former suit for default of appearance under Order IX constitutes a matter "heard and finally decided" on merits under Section 11 CPC.',
            isCore: true
          },
          {
            id: 'issue-2',
            text: 'Whether the appropriate procedural remedy was an application under Order IX Rule 4 or whether a fresh suit lies.',
            isCore: true
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'OVERRULE the objection of Res Judicata: Section 11 CPC does not apply because the previous suit was dismissed for default without any hearing or decision on merits.',
            isCorrect: true,
            rationale: 'Section 11 strictly requires that the former suit must have been "heard and finally decided". A dismissal for default under Order IX Rule 3 does not bar a fresh suit under Order IX Rule 4 subject to limitation.'
          },
          {
            id: 'dec-2',
            text: 'SUSTAIN the objection and dismiss the suit with exemplary costs under Section 11 CPC.',
            isCorrect: false,
            rationale: 'Legally erroneous. Res judicata cannot be invoked without a prior adjudication on merits.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'Previous Suit No. 12 of 2023 was dismissed for default under Order IX Rule 3 CPC due to non-appearance of both parties.', isSelected: true },
            { id: 'f-2', text: 'No issues were framed, no evidence was led, and no adjudication on merits was rendered in the former proceeding.', isSelected: true }
          ],
          lawPool: [
            { id: 'l-1', text: 'Section 11 CPC: Fundamental precondition of Res Judicata is that the issue must have been "heard and finally decided" on merits by a court of competent jurisdiction.', isSelected: true },
            { id: 'l-2', text: 'Under Order IX Rule 4 CPC, where a suit is dismissed under Rule 3, the plaintiff may bring a fresh suit subject to limitation.', isSelected: true }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'The preliminary objection of Res Judicata under Section 11 CPC is OVERRULED. The suit shall proceed to framing of issues.', isSelected: true },
            { id: 'o-2', text: 'The suit is dismissed as barred by res judicata.', isSelected: false }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'Flawless analysis of procedural law. Many prelims candidates confuse dismissal for default with res judicata. You correctly identified that without an adjudication on merits, Section 11 CPC is inapplicable. Furthermore, because both parties were absent (Order IX Rule 3), even Order IX Rule 9 does not bar a fresh suit; Order IX Rule 4 expressly permits a fresh suit if filed within limitation.'
        }
      }
    },

    // =========================================================================
    // CASE 3 (INTERMEDIATE): THE BAIL APPLICATION
    // =========================================================================
    {
      id: 'court-case-3',
      caseNumber: 'BA-2026-042',
      title: 'The Bail Application',
      difficulty: 'intermediate',
      category: 'Criminal Procedure & Personal Liberty',
      estimatedMinutes: 11,
      legalVerification: {
        act: 'Bharatiya Nagarik Suraksha Sanhita, 2023 & Constitution of India',
        section: 'Section 480 / 483 BNSS (corresponding to Section 437 / 439 CrPC) & Article 21',
        proposition: 'Bail is the rule, jail is the exception (State of Rajasthan v. Balchand / P. Chidambaram v. CBI / Satender Kumar Antil v. CBI). In non-bailable offences not punishable with death or life imprisonment, bail should not be withheld as a punitive measure when the triple test (flight risk, tampering with evidence, influencing witnesses) is satisfied.',
        source: 'Supreme Court of India (Satender Kumar Antil v. CBI, 2022 / BNS & BNSS 2023)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2150',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Bail Application No. 42 of 2026: State versus Mohit Tandon. Crime No. 210 of 2026 registered under Section 318(4) [Cheating] of Bharatiya Nyaya Sanhita, 2023. Accused has been in judicial custody for 45 days. Chargesheet has been filed.'
        },
        arguments: [
          {
            speaker: 'aditya',
            counselType: 'Defence Counsel',
            text: 'May it please Your Honour. My client Mohit Tandon is a chartered accountant and lifelong resident of Lucknow with deep familial roots and no criminal antecedents. Investigation is complete, the chargesheet has been submitted before the Magistrate, and all relevant documents are in police custody. Continued incarceration violates Article 21. As settled by the Supreme Court in Satender Kumar Antil, bail is the rule and jail is the exception. We are ready to furnish heavy local sureties and surrender his passport.'
          },
          {
            speaker: 'ananya',
            counselType: 'Public Prosecutor',
            text: 'The State strongly opposes bail! The accused is charged with cheating several investors of ₹18 Lakhs. Economic offences corrode public trust. If released on bail, he may use his financial connections to influence the prosecution witnesses during the upcoming trial!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Investigation Status & Chargesheet Memo',
            nature: 'Police Report',
            evidentiaryRole: 'Proves investigation is concluded, chargesheet is filed, and custodial interrogation is no longer required.',
            weight: 'Decisive factor in non-capital magisterial offences'
          },
          {
            id: 'ex-2',
            name: 'Criminal Antecedents Verification Certificate',
            nature: 'Official Police Record',
            evidentiaryRole: 'Certifies clean prior record with zero pending FIRs or convictions.',
            weight: 'Negates habitual offender presumption'
          },
          {
            id: 'ex-3',
            name: 'Proof of Local Immovable Property & Surrendered Passport',
            nature: 'Affidavit & Property Papers',
            evidentiaryRole: 'Confirms deep local roots and complete negation of flight risk.',
            weight: 'Satisfies flight risk prong of the triple test'
          }
        ],
        questionsToParties: [
          {
            target: 'Public Prosecutor (Adv. Ananya)',
            question: 'Has the State recorded any specific attempt or threat by the accused or his associates to intimidate any witness during the 45 days of custody?',
            response: 'There is no formal complaint of direct threats, Your Honour, but the possibility always exists in financial crimes.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether continued pre-trial detention is justified when the investigation is complete, chargesheet is filed, and the offence is not punishable with death or life imprisonment.',
            isCore: true
          },
          {
            id: 'issue-2',
            text: 'Whether generalized apprehension of witness tampering justifies refusal of bail in the absence of concrete material.',
            isCore: true
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'GRANT regular bail with stringent conditions: Furnishing two local solvent sureties of ₹1,00,000 each, surrender of passport, prohibition on leaving jurisdiction without permission, and undertaking not to contact witnesses.',
            isCorrect: true,
            rationale: 'Consistent with Satender Kumar Antil and Sanjay Chandra v. CBI: pre-trial detention cannot be punitive. When the triple test is satisfied and chargesheet is filed, bail should be granted subject to robust conditions.'
          },
          {
            id: 'dec-2',
            text: 'REJECT bail outright solely because the offence involves financial cheating of ₹18 Lakhs.',
            isCorrect: false,
            rationale: 'Error in law. Gravamen of offence alone without flight risk or tampering risk does not justify indefinite pre-trial detention.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'Investigation is complete, chargesheet has been filed, and documentary evidence is already in police custody.', isSelected: true },
            { id: 'f-2', text: 'Accused has no prior criminal antecedents and has established deep community ties in the jurisdiction.', isSelected: true },
            { id: 'f-3', text: 'The prosecution has presented no evidence of actual witness intimidation.', isSelected: true }
          ],
          lawPool: [
            { id: 'l-1', text: 'BNSS Section 483 / Article 21: Pre-trial detention is not punitive; bail is the rule and jail the exception where the triple test is satisfied.', isSelected: true }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'Bail application is ALLOWED. Accused shall be released on furnishing a personal bond of ₹1,00,000 with two solvent local sureties each, subject to conditions.', isSelected: true }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'Judicial maturity at its best. A judge must never confuse the severity of an allegation with pre-trial punishment. Under the Constitution and the BNSS, bail protects personal liberty while conditions secure trial attendance. You correctly applied the triple test and balanced the state\'s interest with the liberty of the citizen.'
        }
      }
    },

    // =========================================================================
    // CASE 4 (INTERMEDIATE): THE QUESTION OF ADMISSIBILITY (ELECTRONIC RECORDS)
    // =========================================================================
    {
      id: 'court-case-4',
      caseNumber: 'SESS-2026-031',
      title: 'The Question of Admissibility',
      difficulty: 'intermediate',
      category: 'Law of Evidence & Electronic Records',
      estimatedMinutes: 11,
      legalVerification: {
        act: 'Bharatiya Sakshya Adhiniyam, 2023',
        section: 'Section 61 & Section 63(4) BSA 2023 (corresponding to Section 65A/65B of Indian Evidence Act, 1872)',
        proposition: 'Electronic records are admissible as secondary evidence only upon strict compliance with the mandatory statutory certificate under Section 63(4) of BSA 2023 (Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal). Oral evidence cannot substitute for the mandatory electronic certificate.',
        source: 'Supreme Court of India (Arjun Panditrao Khotkar, 2020 7 SCC 1 / BSA 2023 Section 63)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2151',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Sessions Trial No. 31 of 2026: State versus Rakesh Kumar. Prosecution seeks to introduce and mark as Exhibit P-4 a pen-drive containing alleged phone call recordings and WhatsApp screenshots.'
        },
        arguments: [
          {
            speaker: 'ananya',
            counselType: 'Public Prosecutor',
            text: 'Your Honour, the prosecution tenders this pen-drive containing audio recordings of the extortion demands and screenshots of chats. The investigating officer has testified from the witness box that he downloaded these files from the victim\'s laptop to this pen-drive. The evidence is vital to the prosecution case.'
          },
          {
            speaker: 'aditya',
            counselType: 'Defence Counsel',
            text: 'Objection, Your Honour! The pen-drive is secondary electronic evidence. Under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023, secondary electronic records cannot be admitted into evidence without the mandatory certificate under Section 63(4) signed by the person in lawful management of the device. No certificate is produced. As held by the 3-judge bench of the Supreme Court in Arjun Panditrao Khotkar, Section 65B (now Section 63 BSA) is mandatory! Oral testimony of an IO cannot bypass the statute!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Kingston 32GB Pen-Drive (Uncertified Copy)',
            nature: 'Secondary Electronic Storage Media',
            evidentiaryRole: 'Contains .mp3 audio files and .jpeg screenshot exports copied from private laptop.',
            weight: 'Inadmissible without statutory Section 63(4) BSA certificate'
          },
          {
            id: 'ex-2',
            name: 'Investigating Officer Oral Deposition',
            nature: 'Oral Witness Testimony',
            evidentiaryRole: 'IO states he performed the copy paste operation himself.',
            weight: 'Cannot cure absence of statutory electronic certificate'
          }
        ],
        questionsToParties: [
          {
            target: 'Public Prosecutor (Adv. Ananya)',
            question: 'Has the prosecution produced the original laptop/server itself, or an accompanying certificate under Section 63(4) of BSA 2023 signed by the owner of the source device?',
            response: 'We have not filed the certificate yet, Your Honour, but the IO is offering oral sworn evidence.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether secondary electronic evidence (pen-drive copy) can be admitted in evidence without the mandatory certificate under Section 63(4) of BSA 2023.',
            isCore: true
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'SUSTAIN the defence objection: The pen-drive copy is inadmissible as secondary evidence at this stage for want of the mandatory certificate under Section 63(4) of BSA 2023, granting prosecution liberty to cure the defect by producing the requisite certificate.',
            isCorrect: true,
            rationale: 'Settled by Supreme Court in Arjun Panditrao Khotkar: Section 65B/63 is a mandatory statutory condition precedent. However, the trial court can direct the production of the certificate before the conclusion of trial.'
          },
          {
            id: 'dec-2',
            text: 'OVERRULE the objection and mark the pen-drive as primary evidence because the IO is an honest police officer.',
            isCorrect: false,
            rationale: 'Legally erroneous. A pen-drive copy is by definition secondary evidence, and the law does not permit oral witness testimony to supersede the mandatory statutory certificate.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'The pen-drive tendered by the prosecution is secondary electronic evidence copied from a third-party laptop.', isSelected: true },
            { id: 'f-2', text: 'No certificate under Section 63(4) of Bharatiya Sakshya Adhiniyam, 2023 has been furnished with the electronic record.', isSelected: true }
          ],
          lawPool: [
            { id: 'l-1', text: 'Section 63(4) BSA 2023 (Arjun Panditrao Khotkar): Production of statutory certificate is a mandatory condition precedent for admitting secondary electronic records.', isSelected: true }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'Defence objection is SUSTAINED. The pen-drive cannot be marked as an exhibit without compliance with Section 63(4) BSA 2023. Prosecution is granted 14 days to produce the statutory certificate.', isSelected: true }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'Spot-on evidentiary ruling! The law of electronic evidence under Section 63 of BSA 2023 is one of the most critical and heavily tested topics in the Judicial Services examination. By adhering to the binding precedent in Arjun Panditrao Khotkar, you maintained strict adherence to the statutory framework while preserving fairness by allowing the prosecution an opportunity to produce the certificate.'
        }
      }
    },

    // =========================================================================
    // CASE 5 (ADVANCED): THE CIRCUMSTANTIAL EVIDENCE
    // =========================================================================
    {
      id: 'court-case-5',
      caseNumber: 'SESS-2026-077',
      title: 'The Circumstantial Evidence',
      difficulty: 'advanced',
      category: 'Criminal Trial & Standard of Proof',
      estimatedMinutes: 12,
      legalVerification: {
        act: 'Bharatiya Sakshya Adhiniyam, 2023 & BNS 2023',
        section: 'Section 3 BSA 2023 [Definition of Proved] / Section 103 BNS',
        proposition: 'In cases based on circumstantial evidence, the prosecution must establish the five golden principles ("Panchsheel") laid down in Sharad Birdhichand Sarda v. State of Maharashtra: (1) Circumstances fully established, (2) Consistent only with guilt, (3) Conclusive nature, (4) Exclude every hypothesis of innocence, (5) Chain of evidence so complete as to leave no reasonable ground for innocence.',
        source: 'Supreme Court of India (Sharad Birdhichand Sarda v. State of Maharashtra, 1984 4 SCC 116 / Hanumant v. State of M.P.)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2151',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Sessions Case No. 77 of 2026: State of U.P. versus Sunil Verma. Final judgment hearing in a trial for murder under Section 103(1) of Bharatiya Nyaya Sanhita, 2023. Case rests entirely on circumstantial evidence.'
        },
        arguments: [
          {
            speaker: 'ananya',
            counselType: 'Public Prosecutor',
            text: 'Your Honour, the circumstantial chain is unbroken. First, motive: the accused had a business rivalry with the deceased. Second, "last seen theory": PW-3 saw the accused walking near the deceased\'s farm at 8:00 PM. Third, the deceased was found strangled the next morning at 7:00 AM. Fourth, accused could not explain his whereabouts during police interrogation. The chain points unerringly to the guilt of the accused!'
          },
          {
            speaker: 'aditya',
            counselType: 'Defence Counsel',
            text: 'Your Honour, the prosecution case is built on suspicion and conjectures! The gap between the alleged "last seen" at 8:00 PM and the discovery of the body at 7:00 AM is over 11 hours—a massive time gap during which countless people accessed the open farm. No weapon or fingerprints connecting my client were found. The autopsy surgeon admits time of death could be 3:00 AM. Suspicion, howsoever strong, cannot take the place of legal proof!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Autopsy & Post-Mortem Report',
            nature: 'Medical Evidence',
            evidentiaryRole: 'Fixes time of death between 2:00 AM and 4:00 AM. Death by ligature strangulation.',
            weight: 'Establishes substantial 6 to 8-hour gap after the alleged "last seen" sighting'
          },
          {
            id: 'ex-2',
            name: 'Forensic FSL Fingerprint & DNA Report',
            nature: 'Scientific Evidence',
            evidentiaryRole: 'States: "No latent fingerprints or biological DNA of the accused Sunil Verma was detected on the ligature rope or clothing of deceased."',
            weight: 'Total absence of physical or scientific corroboration'
          },
          {
            id: 'ex-3',
            name: 'PW-3 Deposition (Last Seen Witness)',
            nature: 'Oral Deposition',
            evidentiaryRole: 'Admits the farm is along a public thoroughfare and many village residents walk past every evening.',
            weight: 'Dilutes exclusivity of last seen theory'
          }
        ],
        questionsToParties: [
          {
            target: 'Public Prosecutor (Adv. Ananya)',
            question: 'Apart from the alleged sighting at 8:00 PM, is there any recovery under Section 23 of BSA 2023 (disclosure statement) or any call record placing the accused at the scene at 3:00 AM?',
            response: 'No, Your Honour. There is no Section 23 recovery and no mobile tower data for that late hour.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether the "last seen theory" can form the sole basis of conviction when there is an unexplained 7 to 8-hour gap prior to the estimated time of death on an open public path.',
            isCore: true
          },
          {
            id: 'issue-2',
            text: 'Whether the prosecution has satisfied the five golden principles ("Panchsheel") of circumstantial evidence to eliminate reasonable doubt.',
            isCore: true
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'ACQUIT the accused of the charge of murder: The chain of circumstantial evidence is broken. An 8-hour gap in an open thoroughfare without physical or forensic corroboration fails to meet the standard of proof beyond reasonable doubt.',
            isCorrect: true,
            rationale: 'Sharad Birdhichand Sarda & Bodhraj v. State of J&K: Last seen theory cannot sustain conviction where the time gap is long and possibilities of others intervening exist. Suspicion cannot take the place of proof.'
          },
          {
            id: 'dec-2',
            text: 'CONVICT the accused for Murder because motive is established and the accused failed to prove an alibi under Section 106 of BSA 2023.',
            isCorrect: false,
            rationale: 'Error in law. Section 106 BSA cannot be invoked to shift the primary burden onto the accused when the prosecution has failed to establish a complete circumstantial chain.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'The time gap between the alleged last seen sighting (8:00 PM) and the medical time of death (3:00 AM) exceeds seven hours.', isSelected: true },
            { id: 'f-2', text: 'No forensic, DNA, fingerprint, or recovery evidence connects the accused with the scene of the crime.', isSelected: true },
            { id: 'f-3', text: 'The scene of occurrence was an open agricultural path accessible to all members of the public.', isSelected: true }
          ],
          lawPool: [
            { id: 'l-1', text: 'Sharad Birdhichand Sarda v. State of Maharashtra: The circumstances must form a complete chain excluding every hypothesis consistent with the innocence of the accused.', isSelected: true }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'The prosecution has failed to prove the charge beyond all reasonable doubt. Accused Sunil Verma is ACQUITTED of the charge under Section 103(1) BNS 2023.', isSelected: true }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'A truly commendable judicial judgment. The pressure on a trial judge in heinous offences is enormous, but a judicial mind must never substitute outrage or moral conviction for legal proof. By faithfully applying the Panchsheel of Sharad Birdhichand Sarda, you upheld the cornerstone of Indian criminal jurisprudence: better that ten guilty escape than one innocent suffer.'
        }
      }
    },

    // =========================================================================
    // CASE 6 (ADVANCED): THE CONSTITUTIONAL CHALLENGE (ARTICLE 226)
    // =========================================================================
    {
      id: 'court-case-6',
      caseNumber: 'WRIT-2026-512',
      title: 'The Constitutional Challenge',
      difficulty: 'advanced',
      category: 'Constitutional Law & Natural Justice',
      estimatedMinutes: 12,
      legalVerification: {
        act: 'Constitution of India',
        section: 'Article 226 & Article 14',
        proposition: 'Administrative orders causing civil consequences passed in complete violation of natural justice (Audi Alteram Partem) are void and violative of Article 14 (Maneka Gandhi v. Union of India / State of Orissa v. Dr. Bina Pani Dei). The doctrine of post-decisional hearing cannot cure a pre-decisional hearing violation where immediate deprivation occurred without statutory urgency.',
        source: 'Supreme Court of India (Maneka Gandhi, 1978 / Bina Pani Dei, 1967)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/1522',
        scorable: true
      },
      proceedings: {
        clerkIntro: {
          speaker: 'nandini',
          text: 'Writ Petition (Civil) No. 512 of 2026: Modern Educational Society versus State of Uttar Pradesh & Others. Challenge under Article 226 of the Constitution of India seeking a writ of certiorari quashing an executive cancellation order revoking school recognition.'
        },
        arguments: [
          {
            speaker: 'ananya',
            counselType: 'Petitioner Counsel',
            text: 'May it please the Court. The petitioner runs an educational institution serving 800 rural students. On 10th October, the District Education Officer issued a summary order cancelling recognition with immediate effect based on an anonymous complaint regarding playground dimensions. No show-cause notice was served. No inspection report was shared. No hearing was granted. The order entails grave civil consequences and is palpably arbitrary, violating Article 14 and the fundamental tenets of natural justice as settled in Maneka Gandhi.'
          },
          {
            speaker: 'aditya',
            counselType: 'Standing Counsel for the State',
            text: 'Your Honour, the writ petition is premature. The State has administrative authority to ensure safety standards. We are willing to grant the petitioner a post-decisional hearing next month. When an alternative remedy of departmental representation exists, the High Court should not exercise discretionary writ jurisdiction under Article 226!'
          }
        ],
        exhibits: [
          {
            id: 'ex-1',
            name: 'Impugned Cancellation Order',
            nature: 'Administrative Order',
            evidentiaryRole: 'Shows immediate revocation of recognition without reciting any show-cause notice or response.',
            weight: 'Face of the record demonstrates natural justice breach'
          },
          {
            id: 'ex-2',
            name: 'RTI Response from Education Department',
            nature: 'Public Information Record',
            evidentiaryRole: 'Confirms in writing: "No prior show cause notice was issued to the school management before issuance of cancellation order."',
            weight: 'Conclusively establishes non-issuance of notice'
          }
        ],
        questionsToParties: [
          {
            target: 'State Counsel (Adv. Aditya)',
            question: 'Was there any imminent structural collapse or emergency endangering child lives that necessitated dispensing with basic show-cause notice?',
            response: 'The complaint alleged minor boundary discrepancies, Your Honour. There was no immediate physical collapse.'
          }
        ],
        legalIssues: [
          {
            id: 'issue-1',
            text: 'Whether an administrative order entailing severe civil consequences can be sustained when passed in breach of Audi Alteram Partem without statutory urgency.',
            isCore: true
          },
          {
            id: 'issue-2',
            text: 'Whether the existence of an alternative departmental remedy bars the writ court when natural justice is violated.',
            isCore: true
          }
        ],
        decisionOptions: [
          {
            id: 'dec-1',
            text: 'ALLOW the writ petition: Issue a writ of certiorari quashing the cancellation order for violating natural justice and Article 14, granting liberty to the department to initiate fresh proceedings strictly in accordance with law after issuing show-cause notice.',
            isCorrect: true,
            rationale: 'Settled by Supreme Court in Whirlpool Corporation v. Registrar of Trade Marks: Alternative remedy is no bar where fundamental rights or natural justice are violated. In Bina Pani Dei, an order involving civil consequences without hearing is null and void.'
          },
          {
            id: 'dec-2',
            text: 'DISMISS the writ petition and direct the petitioner to submit to a post-decisional hearing next month.',
            isCorrect: false,
            rationale: 'Erroneous. Post-decisional hearing cannot cure a fait accompli where students are already displaced and the order was passed with total disregard of due process.'
          }
        ],
        orderBuilder: {
          factsPool: [
            { id: 'f-1', text: 'The impugned order revoking school recognition was passed without serving a show-cause notice or sharing the inspection material.', isSelected: true },
            { id: 'f-2', text: 'The order inflicts immediate and irreversible civil consequences upon the institution and 800 enrolled students.', isSelected: true }
          ],
          lawPool: [
            { id: 'l-1', text: 'Article 14 & 226 (Maneka Gandhi / Whirlpool Corp): Violation of natural justice renders an administrative action void; alternative remedy is no bar to writ jurisdiction.', isSelected: true }
          ],
          operativeOrderPool: [
            { id: 'o-1', text: 'Writ Petition is ALLOWED. The impugned cancellation order is QUASHED by a writ of certiorari. Liberty reserved to respondents to proceed afresh after notice.', isSelected: true }
          ]
        },
        mentorFeedback: {
          speaker: 'vikram',
          text: 'A profound judgment embodying constitutional supremacy. As a judge, you stood between administrative arbitrariness and the rule of law. Citing Whirlpool Corporation and Maneka Gandhi, you reaffirmed that natural justice is not a mere technicality, but the soul of Article 14. An exceptional judicial performance.'
        }
      }
    }
  ];

  window.COURTROOM_CASES = COURTROOM_CASES;
})();
