/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Culture Authentic Historical PYQ Mapping (Paper I — General Knowledge)
 * Maps 30 Authentic Historical Questions from questions.js without altering base data.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "pyqId": "pyq-cult-001",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-01",
    "topicId": "top-cult-01-01",
    "originalQuestionId": "2012-GK-52",
    "year": 2012,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Which one of the following sites is not in the World Heritage List of UNESCO: (a) Champaner-Pavgarh ",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2012 Paper I."
  },
  {
    "pyqId": "pyq-cult-002",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-01",
    "topicId": "top-cult-01-02",
    "originalQuestionId": "2012-GK-73",
    "year": 2012,
    "paper": "Paper I (General Knowledge)",
    "questionText": "'Kalinga Award' is given by UNESCO for contribution in the field of: (a) Literature (b) Sports (c) P",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2012 Paper I."
  },
  {
    "pyqId": "pyq-cult-003",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-01",
    "topicId": "top-cult-01-03",
    "originalQuestionId": "2012-GK-122",
    "year": 2012,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The 1st exclusively Hindi language newspaper 'Udant martand' was published from Kanpur in 1826. Is e",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2012 Paper I."
  },
  {
    "pyqId": "pyq-cult-004",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-02",
    "topicId": "top-cult-02-01",
    "originalQuestionId": "2013-GK-32",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who is authorised to issue coins in India? (A) RBI (B) SBI (C) Ministry of Finance (D) None of the a",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-005",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-02",
    "topicId": "top-cult-02-02",
    "originalQuestionId": "2013-GK-99",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Rivers Ganga and Yamuna are mentioned together for the first time in- (A) Rigveda (B) Atharvaveda (C",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-006",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-03",
    "topicId": "top-cult-03-01",
    "originalQuestionId": "2013-GK-103",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who had constructed the Martanda temple of Kashmir? (A) Chandrapida (B) Lalitaditya (C) Avantivarman",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-007",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-03",
    "topicId": "top-cult-03-02",
    "originalQuestionId": "2013-GK-105",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Which of the following temples was a well known centre of Higher Education? (A) Dasavatara temple at",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-008",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-03",
    "topicId": "top-cult-03-03",
    "originalQuestionId": "2013-GK-106",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Match List I with List II and select the correct answer from the code given below the lists: List I ",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-009",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-04",
    "topicId": "top-cult-04-01",
    "originalQuestionId": "2013-GK-113",
    "year": 2013,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who was the author of Humayun-nama? (A) Humayun (B) Gulbadan Begam (C) Inayat Khan (D) Ahmad Yadgar",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2013 Paper I."
  },
  {
    "pyqId": "pyq-cult-010",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-04",
    "topicId": "top-cult-04-02",
    "originalQuestionId": "2015-GK-5",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "In which year, Taj Mahal was included in UNESCO's list of World Heritage Sites? (A) 1973 (B) 1983 (C",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-011",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-04",
    "topicId": "top-cult-04-03",
    "originalQuestionId": "2015-GK-7",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who among the following has authored the recent book: 'Gods of Corruption highlighting involvement o",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-012",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-05",
    "topicId": "top-cult-05-01",
    "originalQuestionId": "2015-GK-33",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "'Rajm Nama' is the Persian translation of (A) Arthashastra (B) Ramayana (C) Mahabharata (D) Upanisha",
    "correctAnswer": "C",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-013",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-05",
    "topicId": "top-cult-05-02",
    "originalQuestionId": "2015-GK-36",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Musical Instrument 'Sitar' was invented by (A) Amir Khusro (B) Ramdas (C) Tansen (D) Haridas",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-014",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-06",
    "topicId": "top-cult-06-01",
    "originalQuestionId": "2015-GK-58",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Whose relics are preserved in the Second Stupa at Sanchi? (A) Missionaries of Ashokan age (B) Lord B",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-015",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-06",
    "topicId": "top-cult-06-02",
    "originalQuestionId": "2015-GK-59",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Which temple of North India has its Shikhar (spire) in Dravid style? (A) Bhitargaon (B) Deogarh (C) ",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-016",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-07",
    "topicId": "top-cult-07-01",
    "originalQuestionId": "2015-GK-84",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The basic-structure theory of the Constitution of India Implies that (A) Fundamental Rights cannot b",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-017",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-07",
    "topicId": "top-cult-07-02",
    "originalQuestionId": "2015-GK-120",
    "year": 2015,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Dr. Suniti Solomon, who passed away recently, was associated with which field? (A) Film (B) Medical ",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2015 Paper I."
  },
  {
    "pyqId": "pyq-cult-018",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-08",
    "topicId": "top-cult-08-01",
    "originalQuestionId": "2016-GK-3",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The author of the book 2014 : The Election that Changed India is : (a) Rajdeep Sardesai (b) Sanjay b",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-019",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-08",
    "topicId": "top-cult-08-02",
    "originalQuestionId": "2016-GK-9",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The Author of the book \"The accidental Prime Minister\" is : (a) Sanjay Baru (b) Natwar Singh (c) Say",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-020",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-09",
    "topicId": "top-cult-09-01",
    "originalQuestionId": "2016-GK-26",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The author of the book \"India Rising : Fresh Hope, New Fears\" is : / \" (a) Shiv K. Kumar (b) Sanjeev",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-021",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-09",
    "topicId": "top-cult-09-02",
    "originalQuestionId": "2016-GK-96",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "In which of the following Ajanta Caves, the painting of Padmapani Avalokitesvara was found? (a) Cave",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-022",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-09",
    "topicId": "top-cult-09-03",
    "originalQuestionId": "2016-GK-102",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The Brihadeswara temple at Tanjavur was built by : (a) Pulakesin II (b) Rajaraja-I (c) Vishnuvardhan",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-023",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-10",
    "topicId": "top-cult-10-01",
    "originalQuestionId": "2016-GK-107",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who among the following was the philosopher king of Panchala as mentioned in the Upnishads? (a) Ajat",
    "correctAnswer": "D",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-024",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-10",
    "topicId": "top-cult-10-02",
    "originalQuestionId": "2016-GK-129",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Match List-I with List-II and select the correct answer by using the codes given below the lists: Li",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-025",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-11",
    "topicId": "top-cult-11-01",
    "originalQuestionId": "2016-GK-141",
    "year": 2016,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The author of the book 'The Idea of Justice' is : (a) Plato (b) Amartya Sen (c) John Rawls (d) Arist",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2016 Paper I."
  },
  {
    "pyqId": "pyq-cult-026",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-11",
    "topicId": "top-cult-11-02",
    "originalQuestionId": "2018-GK-53",
    "year": 2018,
    "paper": "Paper I (General Knowledge)",
    "questionText": "The author of 'Planned Economy for India' is (a) Sir M. Visvesvaraya (b) Dr. K.P. Sector (c) K.M. Mu",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2018 Paper I."
  },
  {
    "pyqId": "pyq-cult-027",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-12",
    "topicId": "top-cult-12-01",
    "originalQuestionId": "2018-GK-74",
    "year": 2018,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Who amongst the following was also a poet and a musician and took delight in his title of Kaviraja' ",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2018 Paper I."
  },
  {
    "pyqId": "pyq-cult-028",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-12",
    "topicId": "top-cult-12-02",
    "originalQuestionId": "2018-GK-75",
    "year": 2018,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Which of the following kings of Rashtrakuta dynasty built the famous Kaliash temple of Ellora? (a) D",
    "correctAnswer": "B",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2018 Paper I."
  },
  {
    "pyqId": "pyq-cult-029",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-01",
    "topicId": "top-cult-01-01",
    "originalQuestionId": "2018-GK-77",
    "year": 2018,
    "paper": "Paper I (General Knowledge)",
    "questionText": "Which one of the following temples has been described as 'a landmark in the evolution of the buildin",
    "correctAnswer": "A",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2018 Paper I."
  },
  {
    "pyqId": "pyq-cult-030",
    "subjectId": "gk-culture",
    "chapterId": "ch-cult-01",
    "topicId": "top-cult-01-02",
    "originalQuestionId": "2018-GK-79",
    "year": 2018,
    "paper": "Paper I (General Knowledge)",
    "questionText": "How many image of Yoginis are preserved in the \"Chaunsatha Yogini Temple\" at Bheraghat? (a) 64 (b) 5",
    "correctAnswer": "C",
    "historicalNote": "Authentic historical UP PCS-J examination question from 2018 Paper I."
  }
];

  global.CULTURE_PYQS = DATA;
  global.CULTURE_PYQ_MAPPING = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { pyqs: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
