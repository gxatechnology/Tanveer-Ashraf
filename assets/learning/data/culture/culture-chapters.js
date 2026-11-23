/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Culture Chapters Metadata Module (Paper I — General Knowledge)
 * Covers 12 Comprehensive Thematic Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "ch-cult-01",
    "subjectId": "gk-culture",
    "number": 1,
    "title": "Indian Temple Architecture: Nagara, Dravida & Vesara Styles",
    "description": "Evolution of temple styles, ground plans, Shikhara designs, mandapas, and representative regional masterpieces."
  },
  {
    "id": "ch-cult-02",
    "subjectId": "gk-culture",
    "number": 2,
    "title": "Indian Sculpture & Metallurgy: From IVC to Chola Bronzes",
    "description": "Gandhara, Mathura, Sarnath, and Amaravati sculptural schools; lost-wax metallurgy and Nataraja bronze iconography."
  },
  {
    "id": "ch-cult-03",
    "subjectId": "gk-culture",
    "number": 3,
    "title": "Classical & Folk Dances of India",
    "description": "Eight Sangeet Natak Akademi classical dance forms, Natyashastra principles, and Kathak traditions in Uttar Pradesh."
  },
  {
    "id": "ch-cult-04",
    "subjectId": "gk-culture",
    "number": 4,
    "title": "Indian Classical Music & Vocal Traditions",
    "description": "Hindustani and Carnatic music, ragas, talas, Dhrupad, Khayal, Thumri, and legendary Gharanas of Uttar Pradesh."
  },
  {
    "id": "ch-cult-05",
    "subjectId": "gk-culture",
    "number": 5,
    "title": "Indian Painting Traditions: Murals to Miniatures",
    "description": "Ajanta and Ellora rock-cut murals; Mughal, Rajasthani (Kishangarh Bani Thani), and Pahari miniature schools."
  },
  {
    "id": "ch-cult-06",
    "subjectId": "gk-culture",
    "number": 6,
    "title": "UNESCO World Heritage & Intangible Cultural Heritage",
    "description": "UNESCO cultural heritage monuments in India and UP; intangible cultural heritage including Kumbh Mela and Ramlila."
  },
  {
    "id": "ch-cult-07",
    "subjectId": "gk-culture",
    "number": 7,
    "title": "Classical Literature, Sanskrit Dramas & Sangam Corpus",
    "description": "Epics, Puranas, Kalidasa, Bhasa, Bhavabhuti, and the ancient Tamil Sangam poetry and epics."
  },
  {
    "id": "ch-cult-08",
    "subjectId": "gk-culture",
    "number": 8,
    "title": "Six Orthodox Schools of Philosophy (Shad-Darshana)",
    "description": "Samkhya, Yoga, Nyaya, Vaisheshika, Mimamsa, Vedanta (Advaita, Vishishtadvaita), and heterodox philosophical systems."
  },
  {
    "id": "ch-cult-09",
    "subjectId": "gk-culture",
    "number": 9,
    "title": "Bhakti & Sufi Movements: Saints, Poetry & Syncretism",
    "description": "Alvars, Nayanars, Ramananda, Kabir, Tulsidas, Surdas, Mirabai, and the Chishti and Suhrawardi Sufi Silsilas."
  },
  {
    "id": "ch-cult-10",
    "subjectId": "gk-culture",
    "number": 10,
    "title": "Fairs, Festivals & Sacred Geography of Uttar Pradesh",
    "description": "Kumbh & Magh Mela, Bateshwar, Nauchandi, Shakumbhari, Lathmar Holi of Barsana, and Dev Deepawali of Varanasi."
  },
  {
    "id": "ch-cult-11",
    "subjectId": "gk-culture",
    "number": 11,
    "title": "Handicrafts, Traditional Textiles & GI Tags of UP",
    "description": "Banarasi Brocade, Lucknow Chikankari, Zardozi, Bhadohi Carpets, Moradabad Brassware, and UP GI crafts."
  },
  {
    "id": "ch-cult-12",
    "subjectId": "gk-culture",
    "number": 12,
    "title": "Indian Languages, Scripts & Classical Languages",
    "description": "Major language families, script evolution from Brahmi, Eighth Schedule, and criteria for Classical Languages of India."
  }
];

  global.CULTURE_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
