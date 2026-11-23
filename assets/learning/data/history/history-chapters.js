/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * History of India Chapters Metadata Module (Paper I — General Knowledge)
 * Covers 15 Comprehensive Chronological Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "ch-hist-01",
    "subjectId": "gk-history",
    "number": 1,
    "title": "Prehistoric India & Archaeological Foundations",
    "scope": "Paleolithic, Mesolithic, Neolithic and Chalcolithic cultures; Belan valley archaeological evidence; Bhimbetka rock shelters; early settlements and agricultural domestication.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "High"
  },
  {
    "id": "ch-hist-02",
    "subjectId": "gk-history",
    "number": 2,
    "title": "Indus Valley Civilization (Bronze Age Urbanism)",
    "scope": "Geographical extent, grid town planning, sanitation systems, Harappa, Mohenjo-daro, Lothal dockyard, Kalibangan, Alamgirpur (UP), economic trade, arts, seals, and decline theories.",
    "topicsCount": 3,
    "mcqsCount": 14,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-03",
    "subjectId": "gk-history",
    "number": 3,
    "title": "The Vedic Age (Early & Later Vedic Periods)",
    "scope": "Rigvedic pastoral society, Sabha and Samiti, tribal chiefs (Rajan), transition to Later Vedic agrarian state, Varna stratification, ritualism, iron technology (Painted Grey Ware), and Vedic literature.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-hist-04",
    "subjectId": "gk-history",
    "number": 4,
    "title": "Mahajanapadas & Heterodox Religious Movements",
    "scope": "Sixteen Mahajanapadas in 6th century BCE; rise of Magadha (Haryanka, Shishunaga, Nanda); life and doctrines of Gautama Buddha; Buddhist Councils; Jainism and Vardhamana Mahavira.",
    "topicsCount": 3,
    "mcqsCount": 14,
    "pyqsCount": 4,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-05",
    "subjectId": "gk-history",
    "number": 5,
    "title": "The Mauryan Empire (Imperial Unification)",
    "scope": "Chandragupta Maurya, Chanakya's Arthashastra, Megasthenes' Indica, Bindusara, Ashoka the Great, Kalinga War, Dhamma policy, Major and Minor Rock Edicts, administration, and decline.",
    "topicsCount": 3,
    "mcqsCount": 14,
    "pyqsCount": 4,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-06",
    "subjectId": "gk-history",
    "number": 6,
    "title": "Post-Mauryan Dynasties & The Classical Gupta Age",
    "scope": "Shungas, Kanvas, Indo-Greeks, Shakas, Kushana Empire (Kanishka & 78 CE Shaka Era), Sangam Age in South India, Gupta Empire golden age, Samudragupta (Prayag Prashasti), and Chandragupta II.",
    "topicsCount": 3,
    "mcqsCount": 12,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-07",
    "subjectId": "gk-history",
    "number": 7,
    "title": "Early Medieval India & Regional Kingdoms",
    "scope": "Harshavardhana of Kannauj (UP) and Xuanzang accounts; Tripartite Struggle for Kannauj; Rajput clans; Imperial Cholas of South India, local self-government (Uttiramerur inscription), and maritime trade.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-hist-08",
    "subjectId": "gk-history",
    "number": 8,
    "title": "The Delhi Sultanate (1206\u20131526)",
    "scope": "Five Sultanate Dynasties: Mamluk/Slave, Khilji (Alauddin's market & military reforms), Tughlaq (Muhammad bin Tughlaq experiments & Firoz Shah), Sayyids, and Lodis (Foundation of Agra 1504).",
    "topicsCount": 3,
    "mcqsCount": 12,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-09",
    "subjectId": "gk-history",
    "number": 9,
    "title": "Bhakti, Sufi & Regional Religious Traditions",
    "scope": "Bhakti movement: Saguna and Nirguna traditions, Ramananda, Kabir, Ravidas, Guru Nanak, Mirabai, Chaitanya; Sufi silsilas (Chishti, Suhrawardi), Nizamuddin Auliya, Amir Khusrau, and syncretism.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-hist-10",
    "subjectId": "gk-history",
    "number": 10,
    "title": "The Mughal Empire (1526\u20131707)",
    "scope": "Babur (Panipat, Khanwa), Humayun, Sher Shah Suri's administrative & land revenue reforms (Rupiya, GT Road), Akbar's Mansabdari & Zabti systems, Jahangir, Shah Jahan, Aurangzeb, and decline.",
    "topicsCount": 3,
    "mcqsCount": 14,
    "pyqsCount": 4,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-11",
    "subjectId": "gk-history",
    "number": 11,
    "title": "European Expansion & British East India Company",
    "scope": "Arrival of Portuguese, Dutch, English, French; Carnatic Wars; Battle of Plassey (1757); Battle of Buxar (1764) & Treaty of Allahabad (1765); Subsidiary Alliance; Doctrine of Lapse; Land revenue settlements.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-12",
    "subjectId": "gk-history",
    "number": 12,
    "title": "The Great Revolt of 1857 & Uttar Pradesh Centres",
    "scope": "Causes of the 1857 uprising; Mangal Pandey at Barrackpore; Meerut outbreak; Major UP centres: Lucknow (Hazrat Mahal), Kanpur (Nana Saheb), Jhansi (Lakshmibai), Allahabad (Liaqat Ali); Government of India Act 1858.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 4,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-13",
    "subjectId": "gk-history",
    "number": 13,
    "title": "Indian National Movement (1885\u20131947)",
    "scope": "Foundation of INC (1885); Moderates vs Extremists; Partition of Bengal (1905) & Swadeshi; Home Rule League; Gandhian era: Non-Cooperation, Civil Disobedience, Quit India (1942 Ballia UP); INA & Independence.",
    "topicsCount": 4,
    "mcqsCount": 16,
    "pyqsCount": 5,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-14",
    "subjectId": "gk-history",
    "number": 14,
    "title": "Constitutional & Administrative British Enactments",
    "scope": "Regulating Act 1773, Pitt's India Act 1784, Charter Acts (1813, 1833, 1853), Indian Councils Acts (1861, 1892, 1909 Morley-Minto), Government of India Act 1919 (Dyarchy), and Government of India Act 1935.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 4,
    "estimatedMinutes": 50,
    "weightage": "Very High"
  },
  {
    "id": "ch-hist-15",
    "subjectId": "gk-history",
    "number": 15,
    "title": "Independence, Partition & Integration of States",
    "scope": "Cabinet Mission Plan 1946; Mountbatten Plan 3rd June 1947; Indian Independence Act 1947; Partition tragedies; Sardar Patel and integration of 565 princely states (Junagadh, Hyderabad, Kashmir); State Reorganization 1956.",
    "topicsCount": 2,
    "mcqsCount": 10,
    "pyqsCount": 4,
    "estimatedMinutes": 50,
    "weightage": "High"
  }
];

  global.HISTORY_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : global);
