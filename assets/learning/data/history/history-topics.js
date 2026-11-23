/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * History of India Topics Metadata Module (Paper I — General Knowledge)
 * Covers 38 Comprehensive Chronological Topics across 15 Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "top-hist-01-01",
    "chapterId": "ch-hist-01",
    "subjectId": "gk-history",
    "title": "Paleolithic, Mesolithic & Neolithic Eras: Lithic Tools, Domestication & Rock Art",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-01-02",
    "chapterId": "ch-hist-01",
    "subjectId": "gk-history",
    "title": "Chalcolithic Cultures, Copper Hoards & Belan Valley UP Archaeology",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-hist-02-01",
    "chapterId": "ch-hist-02",
    "subjectId": "gk-history",
    "title": "Indus Valley Geography, Citadel Town Planning, Grid Streets & Drainage",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-02-02",
    "chapterId": "ch-hist-02",
    "subjectId": "gk-history",
    "title": "Major IVC Sites: Harappa, Mohenjo-daro, Lothal, Dholavira & Alamgirpur (UP)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-02-03",
    "chapterId": "ch-hist-02",
    "subjectId": "gk-history",
    "title": "Harappan Economy, Long-Distance Trade, Seals, Script & Decline Hypotheses",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-hist-03-01",
    "chapterId": "ch-hist-03",
    "subjectId": "gk-history",
    "title": "Early Vedic Period: Rigvedic Polity (Sabha/Samiti), Pastoral Economy & Deities",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-03-02",
    "chapterId": "ch-hist-03",
    "subjectId": "gk-history",
    "title": "Later Vedic Transition: Agrarian Settlement, PGW Culture, Varna & Sacrificial Religion",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-04-01",
    "chapterId": "ch-hist-04",
    "subjectId": "gk-history",
    "title": "The 16 Mahajanapadas & Imperial Ascendancy of Magadha (Bimbisara to Nandas)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-04-02",
    "chapterId": "ch-hist-04",
    "subjectId": "gk-history",
    "title": "Buddhism: Gautama Buddha's Life, Four Noble Truths, Eightfold Path & Four Buddhist Councils",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  },
  {
    "id": "top-hist-04-03",
    "chapterId": "ch-hist-04",
    "subjectId": "gk-history",
    "title": "Jainism: Vardhamana Mahavira, Triratna, Five Vows, Anekantavada & Jain Councils",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-05-01",
    "chapterId": "ch-hist-05",
    "subjectId": "gk-history",
    "title": "Chandragupta Maurya, Kautilya's Arthashastra & Mauryan Imperial Administration",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-05-02",
    "chapterId": "ch-hist-05",
    "subjectId": "gk-history",
    "title": "Emperor Ashoka: Kalinga War (261 BCE), Policy of Dhamma & Major Rock Edicts",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-hist-05-03",
    "chapterId": "ch-hist-05",
    "subjectId": "gk-history",
    "title": "Mauryan Art, Ashokan Lion Capital at Sarnath (UP), Espionage & Empire Decline",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-06-01",
    "chapterId": "ch-hist-06",
    "subjectId": "gk-history",
    "title": "Post-Mauryan Dynasties: Shungas, Indo-Greeks, Shakas & The Kushanas (Kanishka 78 CE)",
    "order": 1,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-06-02",
    "chapterId": "ch-hist-06",
    "subjectId": "gk-history",
    "title": "The Sangam Age in South India: Cheras, Cholas, Pandyas & Sangam Literature",
    "order": 2,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-06-03",
    "chapterId": "ch-hist-06",
    "subjectId": "gk-history",
    "title": "The Gupta Classical Empire: Samudragupta's Prayag Prashasti (UP), Chandragupta II & Golden Age",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-07-01",
    "chapterId": "ch-hist-07",
    "subjectId": "gk-history",
    "title": "Harshavardhana of Kannauj (UP), Xuanzang & Tripartite Struggle for Kannauj",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-07-02",
    "chapterId": "ch-hist-07",
    "subjectId": "gk-history",
    "title": "Imperial Cholas: Rajaraja I, Rajendra I, Naval Expeditions & Village Autonomy (Uttiramerur)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-hist-08-01",
    "chapterId": "ch-hist-08",
    "subjectId": "gk-history",
    "title": "Mamluk / Slave Dynasty: Qutbuddin Aibak, Iltutmish, Razia Sultan & Balban's Blood and Iron",
    "order": 1,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-08-02",
    "chapterId": "ch-hist-08",
    "subjectId": "gk-history",
    "title": "Khilji Dynasty: Alauddin Khilji's Market Control, Dagh/Chehra System & Deccan Campaigns",
    "order": 2,
    "mcqsCount": 4,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-08-03",
    "chapterId": "ch-hist-08",
    "subjectId": "gk-history",
    "title": "Tughlaqs, Sayyids & Lodis: Muhammad bin Tughlaq Projects, Firoz Shah & Sikandar Lodi (Agra 1504)",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-09-01",
    "chapterId": "ch-hist-09",
    "subjectId": "gk-history",
    "title": "Bhakti Movement: Nirguna & Saguna Traditions, Kabir, Ravidas, Tulsidas (UP), Mirabai",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-09-02",
    "chapterId": "ch-hist-09",
    "subjectId": "gk-history",
    "title": "Sufism in India: Chishti Silsila (Moinuddin Chishti, Nizamuddin Auliya), Amir Khusrau & Synthesis",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-10-01",
    "chapterId": "ch-hist-10",
    "subjectId": "gk-history",
    "title": "Babur (Panipat 1526, Khanwa 1527), Humayun & Sher Shah Suri's Administrative Reforms",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-hist-10-02",
    "chapterId": "ch-hist-10",
    "subjectId": "gk-history",
    "title": "Emperor Akbar: Mansabdari System (Zat/Sawar), Todar Mal's Dahsala, Sulh-i-Kul & Fatehpur Sikri (UP)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  },
  {
    "id": "top-hist-10-03",
    "chapterId": "ch-hist-10",
    "subjectId": "gk-history",
    "title": "Jahangir, Shah Jahan (Golden Age of Architecture, Taj Mahal), Aurangzeb & Decline",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-11-01",
    "chapterId": "ch-hist-11",
    "subjectId": "gk-history",
    "title": "European Trading Companies, Battle of Plassey (1757) & Battle of Buxar (1764, Treaty of Allahabad)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 27
  },
  {
    "id": "top-hist-11-02",
    "chapterId": "ch-hist-11",
    "subjectId": "gk-history",
    "title": "British Expansionist Policies: Subsidiary Alliance, Doctrine of Lapse & Land Revenue Settlements",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 28
  },
  {
    "id": "top-hist-12-01",
    "chapterId": "ch-hist-12",
    "subjectId": "gk-history",
    "title": "The Revolt of 1857: Underlying Causes, Mangal Pandey & Outbreak at Meerut (10 May 1857)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 27
  },
  {
    "id": "top-hist-12-02",
    "chapterId": "ch-hist-12",
    "subjectId": "gk-history",
    "title": "Revolt of 1857 in Uttar Pradesh: Lucknow, Kanpur, Jhansi, Allahabad, Leaders & 1858 Proclamation",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 28
  },
  {
    "id": "top-hist-13-01",
    "chapterId": "ch-hist-13",
    "subjectId": "gk-history",
    "title": "Birth of Indian National Congress (1885), Moderate Phase & Economic Critique of Colonialism",
    "order": 1,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-13-02",
    "chapterId": "ch-hist-13",
    "subjectId": "gk-history",
    "title": "Partition of Bengal (1905), Swadeshi Movement, Surat Split (1907) & Home Rule Leagues (1916)",
    "order": 2,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-13-03",
    "chapterId": "ch-hist-13",
    "subjectId": "gk-history",
    "title": "Gandhian Movements: Non-Cooperation (Chauri Chaura 1922 UP), Kakori Action (1925) & Civil Disobedience",
    "order": 3,
    "mcqsCount": 4,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-13-04",
    "chapterId": "ch-hist-13",
    "subjectId": "gk-history",
    "title": "Final Surge to Independence: Quit India Movement (1942 Ballia UP), INA Trials & Cabinet Mission Plan",
    "order": 4,
    "mcqsCount": 4,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-hist-14-01",
    "chapterId": "ch-hist-14",
    "subjectId": "gk-history",
    "title": "Company Constitutional Acts: Regulating Act 1773, Pitt's India Act 1784 & Charter Acts (1793\u20131853)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-14-02",
    "chapterId": "ch-hist-14",
    "subjectId": "gk-history",
    "title": "Crown Constitutional Acts: Councils Acts (1861, 1892, 1909), GoI Act 1919 & GoI Act 1935",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-15-01",
    "chapterId": "ch-hist-15",
    "subjectId": "gk-history",
    "title": "Wavell Plan, Mountbatten 3rd June Plan, Partition & Indian Independence Act 1947",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-hist-15-02",
    "chapterId": "ch-hist-15",
    "subjectId": "gk-history",
    "title": "Integration of Princely States (Sardar Patel & V.P. Menon), Linguistic Reorganization & Republic Formation",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  }
];

  global.HISTORY_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : global);
