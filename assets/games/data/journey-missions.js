/**
 * Tanveer Ashraf Judicial Prep - Game 8: Road to Judiciary Missions
 * 36 Authoritative Missions Connected to Real Games & Historical Testing
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  const JOURNEY_MISSIONS = [
    // -------------------------------------------------------------------------
    // CHAPTER 1: THE LAW ACADEMY (Missions 1 - 4)
    // -------------------------------------------------------------------------
    {
      id: "m-acad-01",
      chapterId: "ch-01",
      number: 1,
      title: "First Steps in the Lexicon",
      game: "crossword",
      gameUrl: "crossword.html?missionId=m-acad-01&puzzle=puzzle-01",
      description: "Enter the Lexicon Chamber and solve your first 9x9 statutory crossword puzzle. Master fundamental legal terminology.",
      criteria: { minScore: 50, minAccuracy: 60 },
      rewardXP: 120,
      badge: "Lexicon Initiate",
      mentorBriefing: "Welcome to the Academy. Precision in language is the bedrock of judicial craft. Solve the introductory crossword with care."
    },
    {
      id: "m-acad-02",
      chapterId: "ch-01",
      number: 2,
      title: "Cipher of the Ancients",
      game: "word-scramble",
      gameUrl: "word-scramble.html?missionId=m-acad-02&mode=standard&count=5",
      description: "Decrypt five scrambled statutory words in the Code Breaker archive.",
      criteria: { minScore: 60, minAccuracy: 70 },
      rewardXP: 130,
      badge: "Cipher Solver",
      mentorBriefing: "An advocate who hesitates over definitions is already lost. Decrypt these essential legal terms swiftly."
    },
    {
      id: "m-acad-03",
      chapterId: "ch-01",
      number: 3,
      title: "Axioms of Memory",
      game: "memory-match",
      gameUrl: "memory-match.html?missionId=m-acad-03&mode=legal_maxims&pairs=6",
      description: "Match six pairs of classic Latin legal maxims with their English definitions in under 120 seconds.",
      criteria: { minScore: 80, targetTime: 120 },
      rewardXP: 140,
      badge: "Maxim Master",
      mentorBriefing: "Maxims like 'Ubi jus ibi remedium' and 'Audi alteram partem' must be second nature to any future judge."
    },
    {
      id: "m-acad-04",
      chapterId: "ch-01",
      number: 4,
      title: "The Academy Qualifying Quiz",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-acad-04&mode=classic&subject=Jurisprudence&count=5",
      description: "Examine five core jurisprudential propositions in the Chamber of Truth and identify valid legal axioms.",
      criteria: { minScore: 40, minAccuracy: 80 },
      rewardXP: 160,
      badge: "Academy Graduate",
      mentorBriefing: "Your final test in the Academy. Distinguish analytical positivism from natural law before ascending to the Citadel."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 2: THE CONSTITUTIONAL CITADEL (Missions 5 - 8)
    // -------------------------------------------------------------------------
    {
      id: "m-const-01",
      chapterId: "ch-02",
      number: 5,
      title: "The Writ Chamber",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-const-01&mode=classic&subject=Constitutional%20Law&count=8",
      description: "Examine eight constitutional propositions covering Articles 32, 226, 14, 19, and 21.",
      criteria: { minScore: 60, minAccuracy: 75 },
      rewardXP: 180,
      badge: "Writ Arbiter",
      mentorBriefing: "The Constitution is the supreme law of India. Prerogative writs are the shields of the citizen against arbitrary power."
    },
    {
      id: "m-const-02",
      chapterId: "ch-02",
      number: 6,
      title: "Decrypting the Preamble",
      game: "word-scramble",
      gameUrl: "word-scramble.html?missionId=m-const-02&mode=manuscript&count=5",
      description: "Decrypt five core constitutional manuscript terms including 'Secular', 'Socialist', and 'Integrity'.",
      criteria: { minScore: 70, minAccuracy: 80 },
      rewardXP: 190,
      badge: "Constitutional Scribe",
      mentorBriefing: "The Preamble is the key to open the minds of the makers. Decipher each constitutional pledge."
    },
    {
      id: "m-const-03",
      chapterId: "ch-02",
      number: 7,
      title: "Citadel Crossword: Part III",
      game: "crossword",
      gameUrl: "crossword.html?missionId=m-const-03&puzzle=puzzle-05",
      description: "Solve a specialized 9x9 crossword focused entirely on Fundamental Rights and Directive Principles.",
      criteria: { minScore: 70, minAccuracy: 75 },
      rewardXP: 200,
      badge: "Rights Champion",
      mentorBriefing: "Do not confuse unenumerated rights under Article 21 with explicit text. Crossword clues test subtle distinctions."
    },
    {
      id: "m-const-04",
      chapterId: "ch-02",
      number: 8,
      title: "Citadel Guardian Trial",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-const-04&mode=precedent_challenge&subject=Constitutional%20Law&count=8",
      description: "Complete the Precedent Challenge on landmark Supreme Court decisions from Kesavananda to Puttaswamy.",
      criteria: { minScore: 70, minAccuracy: 75 },
      rewardXP: 220,
      badge: "Citadel Guardian",
      mentorBriefing: "A judge must know not just what was decided, but the exact ratio decidendi. Prove your precedent mastery."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 3: THE CRIMINAL FORTRESS (Missions 9 - 12)
    // -------------------------------------------------------------------------
    {
      id: "m-crim-01",
      chapterId: "ch-03",
      number: 9,
      title: "The BNS Section Sprint",
      game: "section-sprint",
      gameUrl: "section-sprint.html?missionId=m-crim-01&mode=number_to_title&time=60",
      description: "Recall Bharatiya Nyaya Sanhita, 2023 sections at high speed. Score at least 80 points in 60 seconds.",
      criteria: { minScore: 80, targetTime: 60 },
      rewardXP: 210,
      badge: "Sprint Tactician",
      mentorBriefing: "In criminal trials, section numbers must spring to mind instantly. No judicial officer fumbles through indexes during arguments."
    },
    {
      id: "m-crim-02",
      chapterId: "ch-03",
      number: 10,
      title: "Substantive Law Transitions",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-crim-02&mode=old_vs_new&subject=Historical%20IPC%20vs%20BNS%20Transitions&count=8",
      description: "Navigate 8 transition questions matching old IPC sections to new BNS provisions.",
      criteria: { minScore: 70, minAccuracy: 75 },
      rewardXP: 220,
      badge: "Transition Scholar",
      mentorBriefing: "The 2024 transition is the single biggest hurdle for aspirants this year. Master the IPC-to-BNS conversions."
    },
    {
      id: "m-crim-03",
      chapterId: "ch-03",
      number: 11,
      title: "Investigation File: The Midnight Heist",
      game: "legal-detective",
      gameUrl: "legal-detective.html?missionId=m-crim-03&caseId=case-1",
      description: "Investigate Case File 1 with Det. Arjun Rathore. Scrutinize forensic clues, interview witnesses, and frame exact BNS charges.",
      criteria: { minScore: 80, minAccuracy: 70 },
      rewardXP: 240,
      badge: "Criminal Investigator",
      mentorBriefing: "Clues tell a story, but sections define the crime. Ensure every charge is supported by concrete material on record."
    },
    {
      id: "m-crim-04",
      chapterId: "ch-03",
      number: 12,
      title: "Fortress General Exceptions",
      game: "crossword",
      gameUrl: "crossword.html?missionId=m-crim-04&puzzle=puzzle-09",
      description: "Solve Puzzle 9 covering Chapter III General Exceptions of the BNS: infancy, insanity, intoxication, and private defence.",
      criteria: { minScore: 75, minAccuracy: 80 },
      rewardXP: 250,
      badge: "Fortress Commander",
      mentorBriefing: "General exceptions protect the innocent. Distinguish medical from legal insanity before proceeding."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 4: THE EVIDENCE VAULT (Missions 13 - 16)
    // -------------------------------------------------------------------------
    {
      id: "m-evid-01",
      chapterId: "ch-04",
      number: 13,
      title: "Digital Certificate Clearance",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-evid-01&mode=find_error&subject=Bharatiya%20Sakshya%20Adhiniyam,%202023&count=6",
      description: "Identify statutory misconceptions regarding electronic evidence under Section 63 BSA.",
      criteria: { minScore: 60, minAccuracy: 75 },
      rewardXP: 240,
      badge: "Evidence Evaluator",
      mentorBriefing: "Electronic records are primary evidence under Section 57, but certificate compliance under Section 63 is mandatory. Spot the flaws."
    },
    {
      id: "m-evid-02",
      chapterId: "ch-04",
      number: 14,
      title: "Evidentiary Presumptions Memory",
      game: "memory-match",
      gameUrl: "memory-match.html?missionId=m-evid-02&mode=statutory_terms&pairs=8",
      description: "Match 8 pairs of statutory presumptions (dowry death, rape consent, legitimacy, accomplice).",
      criteria: { minScore: 90, targetTime: 120 },
      rewardXP: 250,
      badge: "Presumption Analyst",
      mentorBriefing: "Never confuse 'may presume', 'shall presume', and 'conclusive proof'. Match each presumption with its legal consequence."
    },
    {
      id: "m-evid-03",
      chapterId: "ch-04",
      number: 15,
      title: "The Missing Evidentiary Vowels",
      game: "word-scramble",
      gameUrl: "word-scramble.html?missionId=m-evid-03&mode=missing_vowel&count=8",
      description: "Reconstruct 8 key evidentiary doctrines with missing vowels in the Code Breaker.",
      criteria: { minScore: 75, minAccuracy: 80 },
      rewardXP: 260,
      badge: "Evidentiary Scribe",
      mentorBriefing: "Hearsay, res gestae, and dying declarations must be recognized even when key letters are obscured."
    },
    {
      id: "m-evid-04",
      chapterId: "ch-04",
      number: 16,
      title: "Courtroom Trial: Evidentiary Objections",
      game: "courtroom",
      gameUrl: "courtroom.html?missionId=m-evid-04&caseId=court-case-1",
      description: "Preside over Courtroom Case 1. Rule on leading questions, hearsay objections, and police confession admissibility.",
      criteria: { minScore: 80, minAccuracy: 75 },
      rewardXP: 280,
      badge: "Vault Warden",
      mentorBriefing: "The courtroom is your realm. Rule firmly on objections from Adv. Kabir and Adv. Ananya."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 5: THE CIVIL JUSTICE DISTRICT (Missions 17 - 20)
    // -------------------------------------------------------------------------
    {
      id: "m-civ-01",
      chapterId: "ch-05",
      number: 17,
      title: "Pleadings & Injunctions Clearance",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-civ-01&mode=correct_law&subject=Code%20of%20Civil%20Procedure,%201908&count=6",
      description: "Correct flawed civil propositions regarding Order VII Rule 11, Order XXXIX, and written statement deadlines.",
      criteria: { minScore: 70, minAccuracy: 80 },
      rewardXP: 270,
      badge: "Civil Arbiter",
      mentorBriefing: "Civil procedure requires mathematical rigor. One mistake in limitation or jurisdiction dismisses a rightful claim."
    },
    {
      id: "m-civ-02",
      chapterId: "ch-05",
      number: 18,
      title: "Civil District Crossword",
      game: "crossword",
      gameUrl: "crossword.html?missionId=m-civ-02&puzzle=puzzle-13",
      description: "Solve CPC Crossword 13 featuring res judicata, counter-claim, set-off, and execution concepts.",
      criteria: { minScore: 75, minAccuracy: 75 },
      rewardXP: 280,
      badge: "Procedure Architect",
      mentorBriefing: "Fill in the grid with essential civil terms. Watch for the distinction between legal and equitable set-off."
    },
    {
      id: "m-civ-03",
      chapterId: "ch-05",
      number: 19,
      title: "Contractual Obligations Trial",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-civ-03&mode=classic&subject=Law%20of%20Contract&count=8",
      description: "Evaluate eight propositions under the Indian Contract Act: past consideration, minor contracts, and frustration.",
      criteria: { minScore: 65, minAccuracy: 75 },
      rewardXP: 290,
      badge: "Contract Jurist",
      mentorBriefing: "Contracts govern commercial civil society. Determine when an agreement is void ab initio vs voidable."
    },
    {
      id: "m-civ-04",
      chapterId: "ch-05",
      number: 20,
      title: "Property & Lis Pendens Exceptions",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-civ-04&mode=exception_hunter&subject=Transfer%20of%20Property%20Act,%201882&count=6",
      description: "Identify statutory exceptions under Section 10, 14, 52, and 53A of the Transfer of Property Act.",
      criteria: { minScore: 70, minAccuracy: 75 },
      rewardXP: 310,
      badge: "District Magistrate",
      mentorBriefing: "Property law is filled with fine exceptions. You have earned your seat as an authority on civil justice."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 6: THE INVESTIGATION BUREAU (Missions 21 - 24)
    // -------------------------------------------------------------------------
    {
      id: "m-inv-01",
      chapterId: "ch-06",
      number: 21,
      title: "The Forensic Bureau Mystery",
      game: "legal-detective",
      gameUrl: "legal-detective.html?missionId=m-inv-01&caseId=case-2",
      description: "Examine crime scene videography, search memos under BNSS 105, and autopsy findings in Case 2.",
      criteria: { minScore: 80, minAccuracy: 75 },
      rewardXP: 300,
      badge: "Forensic Investigator",
      mentorBriefing: "Audio-video recording is now mandatory under BNSS Section 105. Check whether the investigating officer complied."
    },
    {
      id: "m-inv-02",
      chapterId: "ch-06",
      number: 22,
      title: "Custodial Safeguard Scramble",
      game: "word-scramble",
      gameUrl: "word-scramble.html?missionId=m-inv-02&mode=reverse_cipher&count=6",
      description: "Decrypt reverse ciphers of arrestee rights, medical examination, and notice of appearance under BNSS.",
      criteria: { minScore: 75, minAccuracy: 80 },
      rewardXP: 310,
      badge: "Rights Protector",
      mentorBriefing: "D.K. Basu guidelines are now codified in BNSS. Decrypt these vital constitutional protections."
    },
    {
      id: "m-inv-03",
      chapterId: "ch-06",
      number: 23,
      title: "Remand & Anticipatory Bail Gauntlet",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-inv-03&mode=classic&subject=Bharatiya%20Nagarik%20Suraksha%20Sanhita,%202023&count=8",
      description: "Test your understanding of the new 15-day police custody rules across 40/60 days and bail under Section 479.",
      criteria: { minScore: 70, minAccuracy: 80 },
      rewardXP: 320,
      badge: "Liberty Arbiter",
      mentorBriefing: "Section 187 BNSS altered police remand drastically. Ensure you know the exact limits before ruling on liberty."
    },
    {
      id: "m-inv-04",
      chapterId: "ch-06",
      number: 24,
      title: "Bureau Rapid Recall Sprint",
      game: "section-sprint",
      gameUrl: "section-sprint.html?missionId=m-inv-04&mode=title_to_number&time=60",
      description: "Match 10 BNSS procedure titles to section numbers within 60 seconds.",
      criteria: { minScore: 100, targetTime: 60 },
      rewardXP: 340,
      badge: "Bureau Chief",
      mentorBriefing: "High speed, zero errors. You are now prepared to preside over complex criminal committals."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 7: THE JUDICIAL COURTROOM (Missions 25 - 28)
    // -------------------------------------------------------------------------
    {
      id: "m-crt-01",
      chapterId: "ch-07",
      number: 25,
      title: "The Matrimonial Property Trial",
      game: "courtroom",
      gameUrl: "courtroom.html?missionId=m-crt-01&caseId=court-case-2",
      description: "Preside over Courtroom Proceeding 2. Evaluate dowry allegations, maintain procedural decorum, and draft judgment.",
      criteria: { minScore: 85, minAccuracy: 80 },
      rewardXP: 350,
      badge: "Bench Presiding Officer",
      mentorBriefing: "Matrimonial disputes demand emotional detachment and strict statutory scrutiny. Preside with dignity."
    },
    {
      id: "m-crt-02",
      chapterId: "ch-07",
      number: 26,
      title: "The Custodial Encounter Inquiry",
      game: "legal-detective",
      gameUrl: "legal-detective.html?missionId=m-crt-02&caseId=case-3",
      description: "Investigate a high-stakes custodial encounter. Uncover contradictions between GD entries and medical reports.",
      criteria: { minScore: 85, minAccuracy: 80 },
      rewardXP: 360,
      badge: "Truth Seeker",
      mentorBriefing: "No police officer is above the law. Use Magisterial inquest principles to expose the truth."
    },
    {
      id: "m-crt-03",
      chapterId: "ch-07",
      number: 27,
      title: "Confidence of the Bench",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-crt-03&mode=confidence_challenge&count=10",
      description: "Complete a 10-question high-stakes Confidence Challenge. Wager your conviction accurately to score 120+ points.",
      criteria: { minScore: 120, minAccuracy: 80 },
      rewardXP: 380,
      badge: "Conviction Jurist",
      mentorBriefing: "A timid judge wavers; a reckless judge errs. Calibrate your judicial confidence with precision."
    },
    {
      id: "m-crt-04",
      chapterId: "ch-07",
      number: 28,
      title: "Structured Order Delivery",
      game: "courtroom",
      gameUrl: "courtroom.html?missionId=m-crt-04&caseId=court-case-3",
      description: "Author a complete, legally sound judicial decree in Courtroom Case 3 with structured reasoning.",
      criteria: { minScore: 90, minAccuracy: 85 },
      rewardXP: 400,
      badge: "Senior Presiding Judge",
      mentorBriefing: "Your order will be scrutinized in appeal. Ensure every finding of fact has a clear legal foundation."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 8: THE GRAND EXAMINATION HALL (Missions 29 - 32)
    // -------------------------------------------------------------------------
    {
      id: "m-exam-01",
      chapterId: "ch-08",
      number: 29,
      title: "UP PCS-J Paper II Law Gauntlet",
      game: "tests",
      gameUrl: "tests.html?missionId=m-exam-01&paper=law&count=20",
      description: "Complete a 20-question randomized mock test from actual UP PCS-J Paper II previous year questions.",
      criteria: { minScore: 30, minAccuracy: 75 },
      rewardXP: 420,
      badge: "Paper II Aspirant",
      mentorBriefing: "This is the real test environment. Negative marking applies: 2 marks for correct, 1/3 negative deduction."
    },
    {
      id: "m-exam-02",
      chapterId: "ch-08",
      number: 30,
      title: "The Grand Truth Trial",
      game: "myth-buster",
      gameUrl: "myth-buster.html?missionId=m-exam-02&mode=grand_trial&count=20",
      description: "Face the 20-question comprehensive timed statutory trial covering all 12 legal disciplines.",
      criteria: { minScore: 160, minAccuracy: 80 },
      rewardXP: 450,
      badge: "Grand Trial Laureate",
      mentorBriefing: "Twenty questions from Constitution to Torts. Keep your composure under time pressure."
    },
    {
      id: "m-exam-03",
      chapterId: "ch-08",
      number: 31,
      title: "UP PCS-J Paper I GK Challenge",
      game: "tests",
      gameUrl: "tests.html?missionId=m-exam-03&paper=gk&count=20",
      description: "Complete a 20-question mock test from UP PCS-J Paper I (General Knowledge & Legal Awareness).",
      criteria: { minScore: 14, minAccuracy: 70 },
      rewardXP: 430,
      badge: "Paper I Laureate",
      mentorBriefing: "A judicial officer must be well-versed in constitutional history, national events, and international institutions."
    },
    {
      id: "m-exam-04",
      chapterId: "ch-08",
      number: 32,
      title: "Master Crossword Marathon",
      game: "crossword",
      gameUrl: "crossword.html?missionId=m-exam-04&puzzle=puzzle-25",
      description: "Solve Championship Crossword 25 integrating terms across criminal, civil, constitutional, and tort law.",
      criteria: { minScore: 90, minAccuracy: 85 },
      rewardXP: 480,
      badge: "Hall Laureate",
      mentorBriefing: "You have conquered the examination hall. The High Court Collegium awaits your final confirmation."
    },

    // -------------------------------------------------------------------------
    // CHAPTER 9: THE SEAT OF JUSTICE (Missions 33 - 36)
    // -------------------------------------------------------------------------
    {
      id: "m-seat-01",
      chapterId: "ch-09",
      number: 33,
      title: "The High Court Collegium Hearing",
      game: "courtroom",
      gameUrl: "courtroom.html?missionId=m-seat-01&caseId=court-case-6",
      description: "Preside over the final judicial bench trial in Case 6 before Justice Vikram Sahay.",
      criteria: { minScore: 90, minAccuracy: 85 },
      rewardXP: 500,
      badge: "Collegium Certified",
      mentorBriefing: "I will be observing from the bench. Deliver justice without fear or favor, affection or ill-will."
    },
    {
      id: "m-seat-02",
      chapterId: "ch-09",
      number: 34,
      title: "The Supreme Investigation File",
      game: "legal-detective",
      gameUrl: "legal-detective.html?missionId=m-seat-02&caseId=case-6",
      description: "Solve Case File 6: The Grand Judicial Conspiracy. Sift through forensic evidence and unmask the mastermind.",
      criteria: { minScore: 90, minAccuracy: 85 },
      rewardXP: 520,
      badge: "Master Inquisitor",
      mentorBriefing: "The final case file tests every skill you have acquired across the entire journey."
    },
    {
      id: "m-seat-03",
      chapterId: "ch-09",
      number: 35,
      title: "Championship Mixed Sprint",
      game: "section-sprint",
      gameUrl: "section-sprint.html?missionId=m-seat-03&mode=mixed&time=90",
      description: "Achieve at least 150 points in a 90-second mixed BNS recall sprint.",
      criteria: { minScore: 150, targetTime: 90 },
      rewardXP: 550,
      badge: "Statutory Virtuoso",
      mentorBriefing: "Flawless recall. The hallmark of a truly distinguished judicial mind."
    },
    {
      id: "m-seat-04",
      chapterId: "ch-09",
      number: 36,
      title: "Curriculum Completion & Educational Achievement",
      game: "judiciary-journey",
      gameUrl: "judiciary-journey.html?missionId=m-seat-04&action=educational_achievement",
      description: "Complete your 36-mission judicial preparation curriculum and receive your personal educational achievement document.",
      criteria: { minScore: 100 },
      rewardXP: 1000,
      badge: "Judicial Preparation Master",
      mentorBriefing: "Tanveer Ashraf, your campaign preparation is complete. Step forward to review and claim your educational achievement certificate."
    }
  ];

  if (typeof window !== 'undefined') {
    window.JOURNEY_MISSIONS = JOURNEY_MISSIONS;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = JOURNEY_MISSIONS;
  }
})();
