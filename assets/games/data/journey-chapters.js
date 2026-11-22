/**
 * Tanveer Ashraf Judicial Prep - Game 8: Road to Judiciary Chapters
 * 9 Campaign Chapters from Law Academy to the Seat of Justice
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  const JOURNEY_CHAPTERS = [
    {
      id: "ch-01",
      number: 1,
      title: "The Law Academy",
      tagline: "Foundational Maxims & Statutory Definitions",
      lore: "Every great judicial career begins with mastery of the fundamental axioms of jurisprudence, legal vocabulary, and basic statutory terms.",
      discipline: "Legal Vocabulary & Jurisprudence",
      mentorId: "kavita",
      mentorName: "Prof. Kavita Sharma",
      mentorRole: "Legal Vocabulary Mentor",
      mentorAvatar: "assets/games/images/characters/crossword/kavita.svg",
      unlockedCriteria: "Initial Chapter (Always Unlocked)",
      totalMissions: 4,
      coords: { x: 12, y: 78 },
      badgeIcon: "🏛️",
      minLevel: 1
    },
    {
      id: "ch-02",
      number: 2,
      title: "The Constitutional Citadel",
      tagline: "Fundamental Rights, Writs & Constitutional Morality",
      lore: "Ascend the citadel of supreme organic law. Defend Fundamental Rights under Article 32 and 226, resolve emergency powers, and uphold the Basic Structure.",
      discipline: "Constitutional Law",
      mentorId: "aditi",
      mentorName: "Prof. Aditi Menon",
      mentorRole: "Constitutional Law Scholar",
      mentorAvatar: "assets/games/images/characters/myth/aditi.svg",
      unlockedCriteria: "Complete Chapter 1 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 26, y: 62 },
      badgeIcon: "📜",
      minLevel: 2
    },
    {
      id: "ch-03",
      number: 3,
      title: "The Criminal Fortress",
      tagline: "Bharatiya Nyaya Sanhita, 2023 & Substantive Penal Law",
      lore: "Navigate the revamped substantive penal code. Distinguish culpable homicide from murder, evaluate general exceptions, and master 2024 penal reforms.",
      discipline: "Bharatiya Nyaya Sanhita, 2023",
      mentorId: "ananya",
      mentorName: "Adv. Ananya Rao",
      mentorRole: "Defense Counsel Mentor",
      mentorAvatar: "assets/games/images/characters/court/ananya.svg",
      unlockedCriteria: "Complete Chapter 2 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 42, y: 50 },
      badgeIcon: "🛡️",
      minLevel: 3
    },
    {
      id: "ch-04",
      number: 4,
      title: "The Evidence Vault",
      tagline: "Bharatiya Sakshya Adhiniyam, 2023 & Admissibility",
      lore: "Unlock the evidentiary archives. Determine digital evidence admissibility under Section 63, evaluate dying declarations, and apply statutory presumptions.",
      discipline: "Bharatiya Sakshya Adhiniyam, 2023",
      mentorId: "bose",
      mentorName: "Dr. Devendra Bose",
      mentorRole: "Keeper of the Archives",
      mentorAvatar: "assets/games/images/characters/scramble/bose.svg",
      unlockedCriteria: "Complete Chapter 3 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 58, y: 42 },
      badgeIcon: "🔐",
      minLevel: 4
    },
    {
      id: "ch-05",
      number: 5,
      title: "The Civil Justice District",
      tagline: "Code of Civil Procedure, 1908 & Substantive Civil Law",
      lore: "Enter the bustling civil courts. Master territorial and pecuniary jurisdiction, res judicata, temporary injunctions, and execution of money decrees.",
      discipline: "Code of Civil Procedure, 1908",
      mentorId: "kabir",
      mentorName: "Adv. Kabir Mehta",
      mentorRole: "Senior Prosecution Advocate",
      mentorAvatar: "assets/games/images/characters/court/kabir.svg",
      unlockedCriteria: "Complete Chapter 4 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 72, y: 52 },
      badgeIcon: "⚖️",
      minLevel: 5
    },
    {
      id: "ch-06",
      number: 6,
      title: "The Investigation Bureau",
      tagline: "Bharatiya Nagarik Suraksha Sanhita, 2023 & Investigation",
      lore: "Step into police headquarters and forensic stations. Scrutinize Zero FIRs, mandatory videography under Section 105, remand, and anticipatory bail.",
      discipline: "Bharatiya Nagarik Suraksha Sanhita, 2023",
      mentorId: "arjun",
      mentorName: "Det. Arjun Rathore",
      mentorRole: "Senior Criminal Investigator",
      mentorAvatar: "assets/games/images/characters/detective/arjun.svg",
      unlockedCriteria: "Complete Chapter 5 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 84, y: 68 },
      badgeIcon: "🔎",
      minLevel: 6
    },
    {
      id: "ch-07",
      number: 7,
      title: "The Judicial Courtroom",
      tagline: "Trial Procedure, Evidentiary Evaluation & Judicial Orders",
      lore: "Take your place on the junior judicial bench. Rule on evidentiary objections, frame criminal and civil charges, and author structured judicial decisions.",
      discipline: "Courtroom Procedure & Order Writing",
      mentorId: "nandini",
      mentorName: "Chief Judge Nandini Sen",
      mentorRole: "Judicial Bench Presiding Officer",
      mentorAvatar: "assets/games/images/characters/court/nandini.svg",
      unlockedCriteria: "Complete Chapter 6 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 74, y: 28 },
      badgeIcon: "👨‍⚖️",
      minLevel: 7
    },
    {
      id: "ch-08",
      number: 8,
      title: "The Grand Examination Hall",
      tagline: "UP PCS-J Full Multi-Discipline Simulation",
      lore: "Face the ultimate qualifying simulation: Paper I (General Knowledge & Legal Awareness) and Paper II (Law) historical past question gauntlet.",
      discipline: "UP PCS-J Past Examination Bank",
      mentorId: "vikram",
      mentorName: "Justice Vikram Sahay",
      mentorRole: "High Court Patron & Exam Evaluator",
      mentorAvatar: "assets/games/images/characters/court/vikram.svg",
      unlockedCriteria: "Complete Chapter 7 Missions (3 of 4)",
      totalMissions: 4,
      coords: { x: 48, y: 18 },
      badgeIcon: "🏆",
      minLevel: 8
    },
    {
      id: "ch-09",
      number: 9,
      title: "The Seat of Justice",
      tagline: "Capstone Learning Mastery & Educational Recognition",
      lore: "The culmination of rigorous judicial preparation. Having mastered foundational doctrine, criminal enactments, civil procedure, and judicial order writing, you claim your Capstone Educational Recognition.",
      discipline: "Judicial Discretion & Ethics",
      mentorId: "vikram",
      mentorName: "Justice Vikram Sahay",
      mentorRole: "High Court Patron",
      mentorAvatar: "assets/games/images/characters/court/vikram.svg",
      unlockedCriteria: "Complete Chapter 8 Missions (3 of 4) & Reach Level 10",
      totalMissions: 4,
      coords: { x: 20, y: 14 },
      badgeIcon: "👑",
      minLevel: 10
    }
  ];

  if (typeof window !== 'undefined') {
    window.JOURNEY_CHAPTERS = JOURNEY_CHAPTERS;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = JOURNEY_CHAPTERS;
  }
})();
