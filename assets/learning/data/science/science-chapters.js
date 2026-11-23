/**
 * Tanveer Ashraf Judicial Prep - General Science Chapters (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var SCIENCE_CHAPTERS = [
  {
    "id": "ch-sci-01",
    "subjectId": "gk-science",
    "number": 1,
    "order": 1,
    "title": "Mechanics, Motion, Gravitation & Work-Energy",
    "description": "Newton's laws of motion, universal law of gravitation, planetary motion, circular motion, friction, work, power, kinetic & potential energy.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-02",
    "subjectId": "gk-science",
    "number": 2,
    "order": 2,
    "title": "Wave Motion, Sound & Acoustic Phenomena",
    "description": "Longitudinal vs transverse waves, speed of sound in media, Doppler effect, ultrasonic waves, sonar, resonance, and audible frequency range.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-sci-03",
    "subjectId": "gk-science",
    "number": 3,
    "order": 3,
    "title": "Optics: Reflection, Refraction, Dispersion & Human Eye",
    "description": "Mirrors, lenses, total internal reflection, optical fibers, atmospheric refraction, dispersion through prism, scattering, defects of vision.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-04",
    "subjectId": "gk-science",
    "number": 4,
    "order": 4,
    "title": "Heat, Thermodynamics & Thermal Physics",
    "description": "Temperature scales, specific heat capacity, latent heat, thermal expansion, modes of heat transfer (conduction, convection, radiation), laws of thermodynamics.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-sci-05",
    "subjectId": "gk-science",
    "number": 5,
    "order": 5,
    "title": "Electricity, Circuits, Magnetism & Electromagnetism",
    "description": "Ohm's law, series and parallel circuits, heating effect of current, magnetic field of current, electromagnetic induction, Faraday's laws, transformers.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-06",
    "subjectId": "gk-science",
    "number": 6,
    "order": 6,
    "title": "Atomic Structure, Chemical Bonding & Periodic Classification",
    "description": "Subatomic particles (electrons, protons, neutrons), isotopes, isobars, ionic and covalent bonds, Modern Periodic Table periodic trends.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-sci-07",
    "subjectId": "gk-science",
    "number": 7,
    "order": 7,
    "title": "Acids, Bases, Salts, pH Scale & Everyday Chemistry",
    "description": "Arrhenius and Bronsted concepts, pH scale, common salts (baking soda, washing soda, plaster of Paris, bleaching powder), soaps and detergents.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-sci-08",
    "subjectId": "gk-science",
    "number": 8,
    "order": 8,
    "title": "Metals, Non-Metals, Metallurgy & Important Alloys",
    "description": "Reactivity series of metals, extraction of metals, corrosion and rust prevention, important alloys (brass, bronze, steel, solder, amalgam).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-sci-09",
    "subjectId": "gk-science",
    "number": 9,
    "order": 9,
    "title": "Cell Biology, Organelles, Genetics & Molecular Basis of Life",
    "description": "Prokaryotic vs eukaryotic cells, cell organelles (mitochondria, ribosomes, Golgi, chloroplasts), mitosis and meiosis, DNA and RNA structure, Mendel's laws.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-10",
    "subjectId": "gk-science",
    "number": 10,
    "order": 10,
    "title": "Human Physiology: Organ Systems & Biological Coordination",
    "description": "Circulatory system (blood groups, heart structure), digestive system, respiratory system, nervous system (brain parts), endocrine glands and hormones.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-11",
    "subjectId": "gk-science",
    "number": 11,
    "order": 11,
    "title": "Human Health, Diseases, Vitamins & Nutritional Disorders",
    "description": "Vitamins and deficiency diseases, communicable bacterial/viral/protozoan diseases (malaria, tuberculosis, dengue, COVID-19), immunity and vaccines.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-sci-12",
    "subjectId": "gk-science",
    "number": 12,
    "order": 12,
    "title": "Plant Biology, Photosynthesis & Ecosystem Dynamics",
    "description": "Plant tissues (xylem, phloem), photosynthesis light/dark reactions, plant hormones (auxins, gibberellins), trophic levels, food chains, ecological pyramids.",
    "estimatedMinutes": 45
  }
];
  global.SCIENCE_CHAPTERS = SCIENCE_CHAPTERS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: SCIENCE_CHAPTERS, SCIENCE_CHAPTERS: SCIENCE_CHAPTERS };
  }
})(typeof window !== 'undefined' ? window : global);
