/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Culture Topics Metadata Module (Paper I — General Knowledge)
 * Covers 28 Topics across 12 Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "top-cult-01-01",
    "chapterId": "ch-cult-01",
    "subjectId": "gk-culture",
    "title": "Nagara Temple Architecture & Regional Sub-Schools: Khajuraho, Odisha, Solanki & Deogarh (UP)"
  },
  {
    "id": "top-cult-01-02",
    "chapterId": "ch-cult-01",
    "subjectId": "gk-culture",
    "title": "Dravida Temple Architecture: Cholas, Pallavas, Nayakas, Gopurams & Mandapas"
  },
  {
    "id": "top-cult-01-03",
    "chapterId": "ch-cult-01",
    "subjectId": "gk-culture",
    "title": "Vesara Style: Hoysala Stellate Plans, Belur, Halebidu & Chalukya Prototypes"
  },
  {
    "id": "top-cult-02-01",
    "chapterId": "ch-cult-02",
    "subjectId": "gk-culture",
    "title": "Major Ancient Sculptural Schools: Gandhara, Mathura, Sarnath Gupta & Amaravati"
  },
  {
    "id": "top-cult-02-02",
    "chapterId": "ch-cult-02",
    "subjectId": "gk-culture",
    "title": "Chola Bronze Sculptures & Nataraja Iconography: Lost-Wax Metallurgy, Mudras & Cosmic Symbolism"
  },
  {
    "id": "top-cult-03-01",
    "chapterId": "ch-cult-03",
    "subjectId": "gk-culture",
    "title": "The Eight Classical Dances of India (Sangeet Natak Akademi) & Natyashastra Foundations"
  },
  {
    "id": "top-cult-03-02",
    "chapterId": "ch-cult-03",
    "subjectId": "gk-culture",
    "title": "Kathak of Uttar Pradesh: Lucknow, Banaras & Jaipur Gharanas, Birju Maharaj & Dance Elements"
  },
  {
    "id": "top-cult-03-03",
    "chapterId": "ch-cult-03",
    "subjectId": "gk-culture",
    "title": "Folk Dances, Ballads & Theatrical Traditions of UP: Nautanki, Raslila, Charkula & Kajri"
  },
  {
    "id": "top-cult-04-01",
    "chapterId": "ch-cult-04",
    "subjectId": "gk-culture",
    "title": "Hindustani vs Carnatic Music Systems: Ragas, Talas, Dhrupad, Khayal & Classical Instruments"
  },
  {
    "id": "top-cult-04-02",
    "chapterId": "ch-cult-04",
    "subjectId": "gk-culture",
    "title": "Musical Gharanas of Uttar Pradesh: Lucknow, Banaras, Kirana, Agra & Vocal Lineages"
  },
  {
    "id": "top-cult-04-03",
    "chapterId": "ch-cult-04",
    "subjectId": "gk-culture",
    "title": "Semi-Classical Music of UP: Thumri, Dadra, Chaiti, Hori, Kajri & Wajid Ali Shah Court"
  },
  {
    "id": "top-cult-05-01",
    "chapterId": "ch-cult-05",
    "subjectId": "gk-culture",
    "title": "Ancient Rock-Cut Cave Murals: Ajanta (Frescoes), Ellora, Bagh & Sittanavasal"
  },
  {
    "id": "top-cult-05-02",
    "chapterId": "ch-cult-05",
    "subjectId": "gk-culture",
    "title": "Indian Miniature Painting Schools: Mughal, Rajasthani (Kishangarh Bani Thani) & Pahari (Kangra)"
  },
  {
    "id": "top-cult-06-01",
    "chapterId": "ch-cult-06",
    "subjectId": "gk-culture",
    "title": "UNESCO World Heritage Cultural Sites in India: Taj Mahal, Agra Fort, Fatehpur Sikri & Beyond"
  },
  {
    "id": "top-cult-06-02",
    "chapterId": "ch-cult-06",
    "subjectId": "gk-culture",
    "title": "UNESCO Intangible Cultural Heritage: Kumbh Mela (Prayagraj UP), Ramlila & National List"
  },
  {
    "id": "top-cult-07-01",
    "chapterId": "ch-cult-07",
    "subjectId": "gk-culture",
    "title": "Classical Sanskrit Literature: Epics, Puranas & Masterpieces of Kalidasa, Bhasa & Bhavabhuti"
  },
  {
    "id": "top-cult-07-02",
    "chapterId": "ch-cult-07",
    "subjectId": "gk-culture",
    "title": "Ancient Tamil Sangam Literature: Tolkappiyam, Eight Anthologies & Epics (Silappadikaram)"
  },
  {
    "id": "top-cult-08-01",
    "chapterId": "ch-cult-08",
    "subjectId": "gk-culture",
    "title": "The Six Orthodox Schools (Shad-Darshana): Samkhya, Yoga, Nyaya, Vaisheshika, Mimamsa & Vedanta"
  },
  {
    "id": "top-cult-08-02",
    "chapterId": "ch-cult-08",
    "subjectId": "gk-culture",
    "title": "Vedantic Sub-Schools (Advaita, Vishishtadvaita) & Heterodox Traditions (Charvaka, Ajivika)"
  },
  {
    "id": "top-cult-09-01",
    "chapterId": "ch-cult-09",
    "subjectId": "gk-culture",
    "title": "The Bhakti Movement: Alvars, Nayanars, Ramananda, Mirabai, Guru Nanak & Chaitanya"
  },
  {
    "id": "top-cult-09-02",
    "chapterId": "ch-cult-09",
    "subjectId": "gk-culture",
    "title": "Sufism in Medieval India: Chishti (Ajmer, Delhi, Salim Chishti UP), Suhrawardi & Syncretism"
  },
  {
    "id": "top-cult-09-03",
    "chapterId": "ch-cult-09",
    "subjectId": "gk-culture",
    "title": "Great Bhakti Poets of Uttar Pradesh: Sant Kabir Das of Varanasi, Goswami Tulsidas & Surdas"
  },
  {
    "id": "top-cult-10-01",
    "chapterId": "ch-cult-10",
    "subjectId": "gk-culture",
    "title": "Major Fairs of Uttar Pradesh: Kumbh & Magh Mela (Prayagraj), Bateshwar, Shakumbhari & Nauchandi"
  },
  {
    "id": "top-cult-10-02",
    "chapterId": "ch-cult-10",
    "subjectId": "gk-culture",
    "title": "Distinctive Festivals & Cultural Celebrations: Lathmar Holi (Barsana), Dev Deepawali (Varanasi)"
  },
  {
    "id": "top-cult-11-01",
    "chapterId": "ch-cult-11",
    "subjectId": "gk-culture",
    "title": "Traditional Textiles & Embroidery of UP: Banarasi Brocade & Silk, Lucknow Chikankari, Zardozi"
  },
  {
    "id": "top-cult-11-02",
    "chapterId": "ch-cult-11",
    "subjectId": "gk-culture",
    "title": "Handicrafts & Geographical Indication (GI) Clusters of UP: Moradabad, Firozabad, Bhadohi, Kannauj"
  },
  {
    "id": "top-cult-12-01",
    "chapterId": "ch-cult-12",
    "subjectId": "gk-culture",
    "title": "Linguistic Families of India, Script Evolution (Brahmi to Devanagari) & Eighth Schedule"
  },
  {
    "id": "top-cult-12-02",
    "chapterId": "ch-cult-12",
    "subjectId": "gk-culture",
    "title": "Classical Languages of India: Statutory Criteria & The 11 Conferred Classical Languages"
  }
];

  global.CULTURE_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
