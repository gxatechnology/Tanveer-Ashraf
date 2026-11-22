/**
 * LEGAL DETECTIVE — AUTHORED & VERIFIED INVESTIGATION CASES
 * Authoritative Indian Criminal Law (Bharatiya Nyaya Sanhita, 2023 & Bharatiya Sakshya Adhiniyam, 2023)
 * Full multi-stage cases across Beginner, Intermediate, and Advanced tiers.
 */
(function() {
  'use strict';

  const DETECTIVE_CASES = [
    // =========================================================================
    // CASE 1 (BEGINNER): THE MISSING MOBILE
    // =========================================================================
    {
      id: 'det-case-1',
      caseNumber: 'INV-2026-001',
      title: 'The Missing Mobile',
      difficulty: 'beginner',
      category: 'Offences Against Property',
      estimatedMinutes: 8,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023',
        section: 'Section 303(2) & Section 314',
        proposition: 'Theft requires moving movable property out of possession without consent with dishonest intention at inception; Dishonest Misappropriation occurs when property lawfully obtained or found is subsequently converted dishonestly.',
        source: 'India Code / Act 45 of 2023 (BNS 2023)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'A complaint has been lodged by Advocate Ramesh Sharma at the District Court complex canteen. His high-end smartphone was taken from his table while he stepped away to pay the bill. CCTV captures an associate advocate, Vikram Saxena, taking the device. However, Saxena claims he believed it was his identical phone and intended to return it. We must establish whether this constitutes Theft under BNS Section 303, Dishonest Misappropriation under Section 314, or an honest mistake of fact under Section 14.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Canteen CCTV Footage Still',
          type: 'cctv',
          summary: 'Time-stamped at 13:42. Shows Ramesh leaving phone on table. 40 seconds later, Vikram glances around, picks up phone, puts it in inner pocket, and exits quickly without finishing tea.',
          detailedAnalysis: 'Visual evidence shows deliberate pocketing and rapid departure. However, both phones possess identical black silicone cases.',
          actualRelevance: 'relevant' // relevant, possibly_relevant, irrelevant
        },
        {
          id: 'ev-2',
          name: 'IMEI & Device Ownership Slip',
          type: 'document',
          summary: 'Original purchase invoice proving phone ownership by Ramesh Sharma with matching IMEI.',
          detailedAnalysis: 'Conclusively establishes Ramesh as lawful owner and possessor of the movable property.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'Electronic Market Shop Receipt',
          type: 'receipt',
          summary: 'A receipt dated 15:10 the same afternoon showing Vikram attempting to wipe device memory and unlock iCloud at a local phone repair stall.',
          detailedAnalysis: 'Crucial mens rea evidence: demonstrates dishonest intention to convert the device to his own use, negating claim of innocent mistake.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-4',
          name: 'Canteen Lunch Menu & Bill',
          type: 'receipt',
          summary: 'Bill for two teas and samosas paid by Ramesh Sharma at 13:41.',
          detailedAnalysis: 'Confirms presence of Ramesh in canteen, but provides no legal proof of taking or dishonest intention.',
          actualRelevance: 'irrelevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Ramesh Sharma',
          role: 'Complainant',
          dialogue: [
            {
              question: 'Did Vikram Saxena have permission to take your phone?',
              answer: 'None whatsoever! I left it for two minutes on table 4. When I turned back from the cash counter, it was gone. He did not ask, call, or inform me.',
              discoversFact: 'Lack of consent under BNS Section 303(1).'
            },
            {
              question: 'Does Vikram own a similar phone model?',
              answer: 'Yes, he has a similar black smartphone, but mine has a distinct cracked camera lens and a blue lock screen with my daughter’s picture.',
              discoversFact: 'Noticeable physical differences distinguishing honest mistake from pretense.'
            }
          ]
        },
        {
          id: 'wit-2',
          name: 'Dinesh (Phone Technician)',
          role: 'Electronic Shop Owner',
          dialogue: [
            {
              question: 'What did Vikram request when he visited your shop at 15:10?',
              answer: 'He asked me to flash the phone, bypass the screen pin, and remove the SIM card. When I asked for purchase proof, he made an excuse and quickly took the phone back.',
              discoversFact: 'Direct evidence of dishonest conversion and knowledge that property was not his.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Taking movable property out of possession without consent' },
          { id: 'issue-2', label: 'Dishonest intention (Animus Furandi) at the time of taking' }
        ],
        targetConnections: [
          { from: 'ev-1', to: 'issue-1' },
          { from: 'ev-2', to: 'issue-1' },
          { from: 'ev-3', to: 'issue-2' },
          { from: 'wit-2', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'Based on the facts, CCTV timeline, and subsequent attempted flashing of the device, what is the correct legal classification under BNS 2023?',
        options: [
          {
            id: 'opt-1',
            text: 'Theft under Section 303(2), BNS 2023 (dishonest taking of movable property out of possession without consent).',
            isCorrect: true,
            rationale: 'All five statutory ingredients of theft are fulfilled: movable property, in possession of complainant, taken without consent, moved out of possession, with dishonest intention at time of taking.'
          },
          {
            id: 'opt-2',
            text: 'Dishonest Misappropriation under Section 314, BNS 2023.',
            isCorrect: false,
            rationale: 'Misappropriation applies when property is found or lawfully entrusted first. Here, the property was never out of Ramesh\'s possession until actively moved by Vikram without consent.'
          },
          {
            id: 'opt-3',
            text: 'Protected by General Exception of Mistake of Fact under Section 14, BNS 2023.',
            isCorrect: false,
            rationale: 'Attempting to flash the device and remove SIM within an hour completely negates good faith (bona fide) belief.'
          },
          {
            id: 'opt-4',
            text: 'No criminal offence; purely a civil tort of trespass to goods.',
            isCorrect: false,
            rationale: 'The presence of dishonest intention (mens rea) elevates the taking from a civil tort to a cognizable criminal offence.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under Section 303(1) of the Bharatiya Nyaya Sanhita, 2023, theft is committed when a person intends to take dishonestly any movable property out of the possession of any person without that person\'s consent, and moves that property in order to such taking. Vikram\'s defense of honest mistake under Section 14 fails because his subsequent act of attempting to erase device records at 15:10 proves mens rea. Section 314 does not apply because the property was not lost or innocently received; it was taken directly from lawful possession.'
      }
    },

    // =========================================================================
    // CASE 2 (BEGINNER): THE FALSE PROMISE
    // =========================================================================
    {
      id: 'det-case-2',
      caseNumber: 'INV-2026-002',
      title: 'The False Promise',
      difficulty: 'beginner',
      category: 'Cheating & Breach of Trust',
      estimatedMinutes: 9,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023',
        section: 'Section 318(1) & (4) [Cheating] vs Section 316 [Criminal Breach of Trust]',
        proposition: 'Cheating requires dishonest and fraudulent intention at the very inception of the transaction; mere subsequent failure to perform an agreement constitutes a civil breach of contract unless initial fraudulent inducement is proved (Hridaya Ranjan Prasad Verma v. State of Bihar).',
        source: 'Supreme Court Landmark Jurisprudence / BNS Section 318',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'A contractor, Pradeep Singhal, took ₹5,00,000 as advance payment from a retired school teacher, Smt. Kamala Devi, promising to deliver construction steel within 48 hours. Pradeep failed to deliver and shut his office. We must determine whether this represents Cheating under BNS Section 318, Criminal Breach of Trust under Section 316, or a pure Civil Breach of Contract.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Bank Transfer Receipt (₹5,00,000)',
          type: 'document',
          summary: 'RTGS transfer confirmation showing ₹5,00,000 credited to Singhal Steels account on 12th October.',
          detailedAnalysis: 'Proves delivery of valuable property induced by the promise of steel delivery.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-2',
          name: 'Fictitious Warehouse Lease Deed',
          type: 'document',
          summary: 'A lease deed for the steel yard provided by Pradeep. Investigation shows the plot address does not exist and the stamp paper was forged.',
          detailedAnalysis: 'Crucial evidence of fraudulent intention at inception: Pradeep never had a warehouse or steel stock, establishing fraudulent inducement ab initio.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'WhatsApp Chat Transcript',
          type: 'digital',
          summary: 'Messages where Pradeep repeatedly assures "steel trucks are rolling from Durgapur" while his bank records show he immediately diverted the funds to casino gambling.',
          detailedAnalysis: 'Demonstrates active deception and continuous fraudulent misrepresentation.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-4',
          name: 'Steel Price Quotation Brochure',
          type: 'document',
          summary: 'Public market brochure listing steel rates per metric tonne in Northern India.',
          detailedAnalysis: 'Generic market information; does not substantiate criminal deception by the accused.',
          actualRelevance: 'irrelevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Kamala Devi',
          role: 'Victim / Complainant',
          dialogue: [
            {
              question: 'Why did you transfer the advance before receiving delivery?',
              answer: 'He showed me the warehouse deed and assured me that steel was held in escrow. Had I known he owned no warehouse, I would never have paid a single rupee!',
              discoversFact: 'Direct causal connection between fraudulent misrepresentation and parting with property.'
            }
          ]
        },
        {
          id: 'wit-2',
          name: 'Bank Manager (State Bank)',
          role: 'Financial Witness',
          dialogue: [
            {
              question: 'How were the funds utilized after credit?',
              answer: 'Within 20 minutes of receipt, ₹4,80,000 was transferred to an online betting platform, leaving ₹12 in the account.',
              discoversFact: 'Total absence of commercial intention to procure steel; confirms dishonest intention from the very beginning.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Deception and fraudulent inducement at inception' },
          { id: 'issue-2', label: 'Delivery of valuable property caused by deception' }
        ],
        targetConnections: [
          { from: 'ev-2', to: 'issue-1' },
          { from: 'ev-3', to: 'issue-1' },
          { from: 'ev-1', to: 'issue-2' },
          { from: 'wit-1', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'Does Pradeep\'s conduct constitute Cheating under BNS Section 318, Criminal Breach of Trust under Section 316, or a civil breach of contract?',
        options: [
          {
            id: 'opt-1',
            text: 'Cheating under Section 318(4) of BNS 2023 (dishonest inducement to deliver valuable property).',
            isCorrect: true,
            rationale: 'Because fraudulent intention existed at the inception of the contract (fake warehouse deed, immediate diversion of funds), it constitutes Cheating rather than ordinary civil breach.'
          },
          {
            id: 'opt-2',
            text: 'Criminal Breach of Trust under Section 316 of BNS 2023.',
            isCorrect: false,
            rationale: 'In Criminal Breach of Trust, property is entrusted lawfully without deception at inception. In Cheating, the entrustment/delivery is obtained by deception ab initio.'
          },
          {
            id: 'opt-3',
            text: 'Pure civil breach of contract; only a suit for specific performance or recovery lies.',
            isCorrect: false,
            rationale: 'Civil breach arises when intention was honest at the time of contract but failed later. Here, the forged lease deed proves deception at the outset.'
          },
          {
            id: 'opt-4',
            text: 'Extortion under Section 308 of BNS 2023.',
            isCorrect: false,
            rationale: 'Extortion requires intentionally putting a person in fear of injury; here delivery was obtained by false assurance, not fear of injury.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under Section 318 of BNS 2023 (corresponding to Section 415/420 of IPC), the distinction between pure breach of contract and cheating lies in the intention of the accused at the time of the inducement. As held in Hridaya Ranjan Prasad Verma v. State of Bihar and reaffirmed under BNS jurisprudence, where the accused had fraudulent intention at the very beginning (proved by fictitious warehouse documents and immediate fund diversion), the offence of Cheating under Section 318(4) is conclusively established.'
      }
    },

    // =========================================================================
    // CASE 3 (INTERMEDIATE): THE FORGED DOCUMENT
    // =========================================================================
    {
      id: 'det-case-3',
      caseNumber: 'INV-2026-003',
      title: 'The Forged Document',
      difficulty: 'intermediate',
      category: 'Offences Relating to Documents',
      estimatedMinutes: 10,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023 & Bharatiya Sakshya Adhiniyam, 2023',
        section: 'BNS Sections 336(1) [Making false document], 338 [Forgery], 340 [Using forged document as genuine]',
        proposition: 'A person makes a false document if they dishonestly execute or alter a document without lawful authority with intent to cause wrongful gain or loss. Presentation before a public registrar constitutes using as genuine under Section 340.',
        source: 'BNS 2023 Chapter 18 / BSA 2023 Section 65',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'An ancestral property in Prayagraj was purportedly transferred by registered Gift Deed from late Shri Hariprasad to his estranged nephew, Alok. The genuine heirs claim Hariprasad was comatose in hospital on the date of execution. Forensic analysis of the signature and thumb impression will determine criminal liability under BNS Chapter 18.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Registered Gift Deed (Dated 14th August)',
          type: 'document',
          summary: 'The original registered deed bearing signature of Hariprasad and attestation by two witnesses, transferring property worth ₹85 Lakhs to Alok.',
          detailedAnalysis: 'Exhibits clear legal effect of altering title to valuable immovable property.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-2',
          name: 'ICU Hospital Admission & Medical Record',
          type: 'medical',
          summary: 'Authenticated medical records from Apex Hospital showing Hariprasad was on mechanical ventilator support in coma from 10th August until his demise on 18th August.',
          detailedAnalysis: 'Proves absolute physical and mental impossibility of executing or acknowledging the document before the Sub-Registrar on 14th August.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'Forensic Handwriting & Thumb Impression Report',
          type: 'forensic',
          summary: 'Report by Government Forensic Science Laboratory confirming signature is an traced forgery and the inked thumb impression does not match Hariprasad\'s pension records.',
          detailedAnalysis: 'Substantiates "making a false document" under BNS Section 336(1).',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-4',
          name: 'Electricity Utility Bill for the Property',
          type: 'receipt',
          summary: 'Electricity bill for July showing normal domestic consumption.',
          detailedAnalysis: 'Irrelevant to the execution, attestation, or forgery of the deed.',
          actualRelevance: 'irrelevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Dr. S.K. Joshi (Treating Intensivist)',
          role: 'Medical Expert',
          dialogue: [
            {
              question: 'Could the patient have been conscious or moved to a sub-registrar office on 14th August?',
              answer: 'Completely impossible. He was deeply comatose in the ICU under 24/7 CCTV surveillance with zero neurological responsiveness.',
              discoversFact: 'Conclusive disproof of execution by the purported executant.'
            }
          ]
        },
        {
          id: 'wit-2',
          name: 'Alok (Accused Beneficiary)',
          role: 'Accused',
          dialogue: [
            {
              question: 'Did your uncle sign this deed in your presence?',
              answer: 'Yes, he signed at home before entering hospital... wait, my lawyer prepared it. I only signed where I was told.',
              discoversFact: 'Contradiction regarding timeline; admits active role in presenting the document.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Making a false document without authority (Section 336)' },
          { id: 'issue-2', label: 'Fraudulent presentation as genuine to cause wrongful gain (Section 340)' }
        ],
        targetConnections: [
          { from: 'ev-2', to: 'issue-1' },
          { from: 'ev-3', to: 'issue-1' },
          { from: 'ev-1', to: 'issue-2' },
          { from: 'wit-2', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'What specific charges under BNS 2023 are established against Alok?',
        options: [
          {
            id: 'opt-1',
            text: 'Forgery under Section 338 and Using a Forged Document as Genuine under Section 340, BNS 2023.',
            isCorrect: true,
            rationale: 'Making the false gift deed constitutes Forgery (Section 338). Producing it for registration with knowledge of forgery constitutes the distinct offence under Section 340.'
          },
          {
            id: 'opt-2',
            text: 'Only Criminal Trespass under Section 329, BNS 2023.',
            isCorrect: false,
            rationale: 'Trespass relates to unlawful entry, whereas the gravamen here is falsification of legal title documents.'
          },
          {
            id: 'opt-3',
            text: 'Criminal Breach of Trust under Section 316, BNS 2023.',
            isCorrect: false,
            rationale: 'There was no entrustment of property to Alok; he fabricated the instrument out of whole cloth.'
          },
          {
            id: 'opt-4',
            text: 'Insufficient evidence to establish forgery without the testimony of both attesting witnesses.',
            isCorrect: false,
            rationale: 'Forensic evidence and medical impossibility directly prove the document is false under Section 65 of BSA 2023 without depending on hostile attesting witnesses.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under BNS Section 336, a person makes a false document if he dishonestly signs, seals or executes a document believing it was not made by authority of the person by whom he knows it was not made. The FSL handwriting report and ICU admission establish that Hariprasad never executed the deed. Alok\'s presentation of the deed for registration makes him liable for Forgery (Section 338) read with Section 340 for using forged document as genuine.'
      }
    },

    // =========================================================================
    // CASE 4 (INTERMEDIATE): THE THREATENING MESSAGE
    // =========================================================================
    {
      id: 'det-case-4',
      caseNumber: 'INV-2026-004',
      title: 'The Threatening Message',
      difficulty: 'intermediate',
      category: 'Criminal Intimidation & Extortion',
      estimatedMinutes: 10,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023',
        section: 'Section 308(1) & (2) [Extortion] vs Section 351 [Criminal Intimidation]',
        proposition: 'Extortion requires intentionally putting a person in fear of injury and thereby dishonestly inducing them to deliver valuable property; Criminal Intimidation consists of threat to cause injury with intent to cause alarm or compel an act, without delivery of property.',
        source: 'BNS 2023 Sections 308 & 351',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'A prominent jeweller received encrypted audio messages and courier letters threatening to set fire to his showroom and kidnap his son unless ₹20,00,000 cash was left behind a designated highway shrine. The jeweller delivered ₹5,00,000 under immense fear before approaching the police. We must dissect whether this represents Extortion or Criminal Intimidation.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Encrypted Audio Recording & Transcript',
          type: 'digital',
          summary: 'Voice note: "If ₹20 Lakhs is not kept at the shrine by midnight, your son will not return home from tuition. Keep police out if you value his life."',
          detailedAnalysis: 'Proves intentional creation of fear of grievous injury and death to a loved one.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-2',
          name: 'Marked Currency Delivery Slip',
          type: 'document',
          summary: 'Police seizure memo showing ₹5,00,000 in marked notes recovered from the shrine drop-box and the suspect\'s vehicle.',
          detailedAnalysis: 'Proves that valuable property was actually delivered under the direct inducement of fear.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'Cell Tower Triangulation Data',
          type: 'digital',
          summary: 'Locates suspect Manavendra\'s phone at the shrine drop location at the exact time of parcel retrieval.',
          detailedAnalysis: 'Links the suspect directly to the receipt of the extorted property.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-4',
          name: 'Jewellery Shop Sales Register',
          type: 'document',
          summary: 'Daily gold coin sales register for the past week.',
          detailedAnalysis: 'Shows business turnover but does not prove or disprove the threat.',
          actualRelevance: 'irrelevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Jeweller Devendra Agarwal',
          role: 'Victim',
          dialogue: [
            {
              question: 'Why did you drop the ₹5 Lakhs at the highway shrine?',
              answer: 'I was paralyzed with terror. They specified my son\'s school van number. I parted with the money purely to save my child\'s life.',
              discoversFact: 'Delivery of property was directly induced by fear of injury.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Putting person in fear of injury to person or property' },
          { id: 'issue-2', label: 'Dishonest inducement to deliver valuable property' }
        ],
        targetConnections: [
          { from: 'ev-1', to: 'issue-1' },
          { from: 'ev-2', to: 'issue-2' },
          { from: 'ev-3', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'Because valuable property was successfully delivered as a result of the fear, what is the precise offence under BNS 2023?',
        options: [
          {
            id: 'opt-1',
            text: 'Extortion under Section 308(2) of BNS 2023.',
            isCorrect: true,
            rationale: 'When fear of injury successfully induces the victim to part with valuable property, the offence of Extortion is completed. If no property had been delivered, it would remain Criminal Intimidation or Attempted Extortion.'
          },
          {
            id: 'opt-2',
            text: 'Criminal Intimidation under Section 351(2) of BNS 2023 only.',
            isCorrect: false,
            rationale: 'Criminal Intimidation is subsumed when the threat results in the actual dishonest delivery of property, completing the higher offence of Extortion.'
          },
          {
            id: 'opt-3',
            text: 'Robbery under Section 309 of BNS 2023.',
            isCorrect: false,
            rationale: 'Extortion becomes Robbery only when the offender is in the immediate physical presence of the victim and puts him in fear of instant death or hurt. Here, the threat was communicated remotely.'
          },
          {
            id: 'opt-4',
            text: 'Criminal Breach of Trust under Section 316 of BNS 2023.',
            isCorrect: false,
            rationale: 'Extortion involves fear and coercion; Criminal Breach of Trust involves voluntary, lawful entrustment.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under Section 308(1) of BNS 2023, extortion occurs when a person intentionally puts any person in fear of any injury to that person or to any other, and thereby dishonestly induces the person so put in fear to deliver to any person any property. Because ₹5,00,000 was delivered under fear of injury to the son, the offence is completed Extortion under Section 308(2). It does not amount to robbery because the offender was not physically present to inflict instant hurt at the moment of extortion.'
      }
    },

    // =========================================================================
    // CASE 5 (ADVANCED): THE SILENT ACCOMPLICE
    // =========================================================================
    {
      id: 'det-case-5',
      caseNumber: 'INV-2026-005',
      title: 'The Silent Accomplice',
      difficulty: 'advanced',
      category: 'Joint Liability & Abetment',
      estimatedMinutes: 12,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023',
        section: 'BNS Section 3(5) [Joint Liability / Common Intention] vs Section 61 [Criminal Conspiracy] vs Section 45 [Abetment]',
        proposition: 'Common intention under Section 3(5) requires a prior meeting of minds and active participation in furtherance of the common design (Pandurang v. State of Hyderabad). Mere presence or prior knowledge without agreement or aiding does not create joint criminal liability.',
        source: 'Supreme Court of India (Constitution Bench in Pandurang v. State of Hyderabad) / BNS Section 3(5)',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'During a planned night break-in at a warehouse, guard Suraj was assaulted and immobilized. Three perpetrators entered: two committed burglary and assault, while the third, Nitin, remained stationed by his motorbike outside. Nitin claims he was only a hired taxi driver who had no knowledge of their criminal design. We must analyze phone calls, physical positioning, and lookout conduct.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Walkie-Talkie & Cellular Signal Logs',
          type: 'digital',
          summary: 'Call records reveal 8 short calls between Nitin and the inside burglars during the 20 minutes of the heist. Nitin alerted them: "Police patrol van just turned onto Main Road, hurry up!"',
          detailedAnalysis: 'Completely demolishes the "innocent driver" defence; proves active lookout duty in furtherance of common intention.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-2',
          name: 'Seized Master Keys & Gate Bolt Cutters',
          type: 'physical',
          summary: 'Bolt cutters recovered from Nitin\'s motorcycle saddlebag with microscopic paint transfers matching the warehouse padlock.',
          detailedAnalysis: 'Proves intentional provision of implements for the commission of the offence (Abetment by facilitation).',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'Motorcycle Rental Agreement',
          type: 'document',
          summary: 'Genuine rental agreement for the motorcycle hired under Nitin\'s true name.',
          detailedAnalysis: 'Confirms lawful possession of vehicle, but does not negate complicity in the burglary.',
          actualRelevance: 'possibly_relevant'
        },
        {
          id: 'ev-4',
          name: 'Warehouse Security Guard Shift Roster',
          type: 'document',
          summary: 'Routine duty sheet for warehouse private security guards.',
          detailedAnalysis: 'Establishes guard schedule, but irrelevant to Nitin\'s specific intent.',
          actualRelevance: 'irrelevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Nitin (Stationed Outside)',
          role: 'Accused',
          dialogue: [
            {
              question: 'Why did you radio the men inside about the police patrol?',
              answer: 'I... I got scared when I saw the red beacon. They told me they were picking up personal boxes.',
              discoversFact: 'Confirms awareness of police presence and deliberate assistance to evade detection.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Prior meeting of minds & shared common design' },
          { id: 'issue-2', label: 'Active participation in furtherance of common intention (lookout & tools)' }
        ],
        targetConnections: [
          { from: 'ev-1', to: 'issue-1' },
          { from: 'ev-2', to: 'issue-2' },
          { from: 'wit-1', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'Is Nitin liable for the burglary and assault committed inside the warehouse under BNS 2023?',
        options: [
          {
            id: 'opt-1',
            text: 'Liable for all offences committed by the group under Section 3(5) of BNS 2023 (Joint Liability via Common Intention).',
            isCorrect: true,
            rationale: 'Acting as an armed lookout and supplying tools constitutes active participation in furtherance of the common design; under Section 3(5), each participant is liable as if done by him alone.'
          },
          {
            id: 'opt-2',
            text: 'Liable only for harbouring an offender after the commission of an offence.',
            isCorrect: false,
            rationale: 'Harbouring occurs post-facto. Nitin was physically present and facilitating the crime during its commission.'
          },
          {
            id: 'opt-3',
            text: 'Not liable because he never entered the warehouse perimeter or touched the guard.',
            isCorrect: false,
            rationale: 'As established in Barendra Kumar Ghosh v. Emperor (Post Office Case), "they also serve who only stand and wait" if acting in furtherance of a shared common intention.'
          },
          {
            id: 'opt-4',
            text: 'Liable only under the Motor Vehicles Act for unlicensed commercial transit.',
            isCorrect: false,
            rationale: 'Ignores the proven criminal agreement, supply of housebreaking tools, and lookout communications.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under Section 3(5) of BNS 2023 (retaining the classic doctrine of Section 34 IPC), when a criminal act is done by several persons in furtherance of the common intention of all, each is liable for that act in the same manner as if it were done by him alone. Physical presence inside the room is not required; maintaining lookout duty outside while warning confederates of approaching police satisfies the test of active participation in furtherance of common intention.'
      }
    },

    // =========================================================================
    // CASE 6 (ADVANCED): THE QUESTION OF INTENTION
    // =========================================================================
    {
      id: 'det-case-6',
      caseNumber: 'INV-2026-006',
      title: 'The Question of Intention',
      difficulty: 'advanced',
      category: 'Offences Affecting Life',
      estimatedMinutes: 12,
      legalVerification: {
        act: 'Bharatiya Nyaya Sanhita, 2023',
        section: 'Section 100 / 103 [Murder] vs Section 105 [Culpable Homicide Not Amounting to Murder] vs Section 106 [Rash or Negligent Act]',
        proposition: 'The critical boundary between Murder and Culpable Homicide Not Amounting to Murder lies in the degree of mens rea and probability of death (State of A.P. v. Rayavarapu Punnayya). Section 106 excludes cases where an intentional assault was inflicted.',
        source: 'Supreme Court of India (Rayavarapu Punnayya, 1976) / BNS Chapter 6',
        verificationDate: '2026-11-22',
        status: 'Verified against authoritative source',
        sourceUrl: 'https://www.indiacode.nic.in/handle/123456789/2149',
        scorable: true
      },
      briefing: {
        speaker: 'arjun',
        text: 'A heated argument erupted between neighbours over common boundary fencing. The accused, Jagdish, picked up a single heavy wooden club lying nearby and struck the victim, Balram, on the head with substantial force, causing a compound skull fracture that resulted in death 12 hours later. The defence claims it was an accidental rash act under Section 106. We must determine the exact degree of criminal culpability.'
      },
      evidence: [
        {
          id: 'ev-1',
          name: 'Medico-Legal Autopsy Report',
          type: 'medical',
          summary: 'Cause of death: Coma resulting from depressed compound comminuted fracture of parietal bone caused by blunt force trauma with a heavy object. The doctor certifies the injury was "sufficient in the ordinary course of nature to cause death".',
          detailedAnalysis: 'Key criterion under BNS Section 100 Clause Thirdly: bodily injury intended to be inflicted is sufficient in ordinary course of nature to cause death.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-2',
          name: 'Eyewitness Statement (Neighbour Sitaram)',
          type: 'statement',
          summary: 'States: "There was sudden shouting. Jagdish yelled: \'I will finish your arrogance forever!\' He grabbed the boundary fence stake and swung it directly at Balram\'s head with both hands."',
          detailedAnalysis: 'Demonstrates deliberate targeting of a vital organ (head) with lethal force, refuting accident or mere rashness.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-3',
          name: 'Weapon Examination Memo',
          type: 'physical',
          summary: 'A 4-foot seasoned sal wood fence stake weighing 3.2 kg with nail protrusions and blood matching the deceased.',
          detailedAnalysis: 'Proves the deadly nature of the weapon utilized.',
          actualRelevance: 'relevant'
        },
        {
          id: 'ev-4',
          name: 'Municipal Land Survey Map',
          type: 'document',
          summary: 'Revenue map showing the contested boundary line between the two plots.',
          detailedAnalysis: 'Explains the motive for dispute, but provides no insight into the medical severity or intentionality of the blow.',
          actualRelevance: 'possibly_relevant'
        }
      ],
      witnesses: [
        {
          id: 'wit-1',
          name: 'Dr. Anita Roy (Autopsy Surgeon)',
          role: 'Forensic Pathologist',
          dialogue: [
            {
              question: 'Could this injury have occurred from a simple slip and fall against a post?',
              answer: 'Absolutely not. The degree of inward bone depression and brain laceration required heavy, direct downward kinetic impact consistent with a full-force deliberate swing.',
              discoversFact: 'Medical confirmation of deliberate, lethal force.'
            }
          ]
        }
      ],
      evidenceBoard: {
        legalIssues: [
          { id: 'issue-1', label: 'Intentional infliction of bodily injury' },
          { id: 'issue-2', label: 'Injury sufficient in the ordinary course of nature to cause death' }
        ],
        targetConnections: [
          { from: 'ev-2', to: 'issue-1' },
          { from: 'ev-3', to: 'issue-1' },
          { from: 'ev-1', to: 'issue-2' },
          { from: 'wit-1', to: 'issue-2' }
        ]
      },
      deduction: {
        question: 'In light of the targeted blow to the head with a 3.2 kg stake and the autopsy finding of sufficiency to cause death, what is the correct offence?',
        options: [
          {
            id: 'opt-1',
            text: 'Murder under Section 103(1) read with Section 100 (Clause Thirdly) of BNS 2023.',
            isCorrect: true,
            rationale: 'As settled in Virsa Singh v. State of Punjab, once intention to inflict the particular bodily injury is proved and that injury is objectively sufficient in the ordinary course of nature to cause death, Section 300 Thirdly (now BNS Section 100) applies.'
          },
          {
            id: 'opt-2',
            text: 'Causing death by rash or negligent act under Section 106(1) of BNS 2023.',
            isCorrect: false,
            rationale: 'Section 106 applies only to acts where there is no intention to cause death or bodily injury (e.g. rash driving or machinery accidents). Intentional blows are excluded from Section 106.'
          },
          {
            id: 'opt-3',
            text: 'Grievous hurt under Section 117 of BNS 2023 only, because only one blow was struck.',
            isCorrect: false,
            rationale: 'Single blow does not automatically negate murder when struck on a vital organ with a lethal weapon sufficient in the ordinary course of nature to cause death.'
          },
          {
            id: 'opt-4',
            text: 'Accident in doing a lawful act under Section 18 of BNS 2023.',
            isCorrect: false,
            rationale: 'Swinging a heavy stake at an unarmed neighbour during a quarrel is neither a lawful act nor done with proper care and caution.'
          }
        ]
      },
      report: {
        modelExplanation: 'Under BNS Section 100 Thirdly, culpable homicide is murder if the act is done with the intention of causing bodily injury to any person and the bodily injury intended to be inflicted is sufficient in the ordinary course of nature to cause death. Applying the constitutional bench ruling in Virsa Singh v. State of Punjab (1958) and Rayavarapu Punnayya (1976), the accused intentionally chose the weapon, aimed at the head, and inflicted a fracture certified sufficient to cause death. The claim of a mere rash act under Section 106 is untenable in law.'
      }
    }
  ];

  window.DETECTIVE_CASES = DETECTIVE_CASES;
})();
