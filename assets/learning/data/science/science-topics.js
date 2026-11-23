/**
 * Tanveer Ashraf Judicial Prep - General Science Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var SCIENCE_TOPICS = [
  {
    "id": "top-sci-01-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-01",
    "number": 1,
    "order": 1,
    "title": "Newton's Laws of Motion & Momentum",
    "summary": "First law (inertia), second law (F=ma, rate of change of momentum), third law (action-reaction), impulse, conservation of linear momentum.",
    "keyProvisions": [
      "Newton's First, Second and Third Laws",
      "Law of Conservation of Linear Momentum",
      "SI Units: Newton, Joule"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-01-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-01",
    "number": 2,
    "order": 2,
    "title": "Universal Gravitation & Planetary Motion",
    "summary": "Newton's law of gravitation (G value), acceleration due to gravity (g variations with altitude/depth), Kepler's laws of planetary motion, escape velocity.",
    "keyProvisions": [
      "Newton's Law of Gravitation (G = 6.674 x 10^-11 N m^2/kg^2)",
      "Earth escape velocity 11.2 km/s",
      "g variations at poles vs equator"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-01-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-01",
    "number": 3,
    "order": 3,
    "title": "Work, Energy, Power & Mechanical Principles",
    "summary": "Work done formula (W = F·d·cos θ), kinetic energy (1/2 mv^2), potential energy (mgh), law of conservation of mechanical energy, power (Watt).",
    "keyProvisions": [
      "Law of Conservation of Energy",
      "Power in Watts and Horsepower (1 hp = 746 W)",
      "Friction types"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-02-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-02",
    "number": 4,
    "order": 4,
    "title": "Wave Characteristics & Nature of Sound",
    "summary": "Mechanical waves vs electromagnetic waves, frequency, wavelength, amplitude, speed of sound in solids > liquids > gases, vacuum barrier.",
    "keyProvisions": [
      "Speed of sound in air ~343 m/s at 20°C",
      "Inaudibility in vacuum",
      "Pitch vs loudness vs quality"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-02-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-02",
    "number": 5,
    "order": 5,
    "title": "Ultrasonic Waves, Sonar & Doppler Effect",
    "summary": "Infrasonic (<20 Hz), audible (20 Hz - 20,000 Hz), ultrasonic (>20 kHz), SONAR working principle, echolocation in bats, Doppler frequency shift.",
    "keyProvisions": [
      "Audible frequency range: 20 Hz to 20,000 Hz",
      "SONAR: Sound Navigation and Ranging",
      "Doppler Effect applications"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-03-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-03",
    "number": 6,
    "order": 6,
    "title": "Reflection, Spherical Mirrors & Optical Applications",
    "summary": "Laws of reflection, concave mirrors (converging, shaving/headlights/solar furnaces), convex mirrors (diverging, rear-view vehicle mirrors), mirror formula.",
    "keyProvisions": [
      "Mirror formula: 1/f = 1/v + 1/u",
      "Concave vs convex mirror image formation",
      "Virtual and diminished images in convex mirror"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-03-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-03",
    "number": 7,
    "order": 7,
    "title": "Refraction, Snell's Law & Total Internal Reflection",
    "summary": "Refractive index, Snell's law (n1 sin θ1 = n2 sin θ2), critical angle, total internal reflection (optical fibers, mirage, diamond brilliance).",
    "keyProvisions": [
      "Snell's Law of Refraction",
      "Conditions for TIR (denser to rarer medium, angle > critical angle)",
      "Optical fiber technology"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sci-03-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-03",
    "number": 8,
    "order": 8,
    "title": "Dispersion, Atmospheric Optics & Defects of Vision",
    "summary": "Dispersion of white light (VIBGYOR), rainbow formation (refraction, dispersion, TIR), blue sky / red sunset (Rayleigh scattering), myopia & hypermetropia correction.",
    "keyProvisions": [
      "Rayleigh scattering (I ∝ 1/λ^4)",
      "Myopia corrected by concave lens",
      "Hypermetropia corrected by convex lens"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-04-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-04",
    "number": 9,
    "order": 9,
    "title": "Temperature Scales, Thermal Expansion & Specific Heat",
    "summary": "Celsius, Fahrenheit, and Kelvin conversion (C/5 = (F-32)/9 = (K-273)/5), anomalous expansion of water between 0°C and 4°C, latent heat of fusion/vaporization.",
    "keyProvisions": [
      "Anomalous expansion of water maximum density at 4°C",
      "Latent heat of steam vs boiling water burn severity",
      "Absolute zero (0 K or -273.15°C)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-04-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-04",
    "number": 10,
    "order": 10,
    "title": "Modes of Heat Transfer & Laws of Thermodynamics",
    "summary": "Conduction (solids), convection (fluids), radiation (vacuum/electromagnetic), Stefan's law, Newton's law of cooling, First and Second laws of thermodynamics.",
    "keyProvisions": [
      "Zeroth, First, and Second Laws of Thermodynamics",
      "Greenhouse effect thermal mechanism",
      "Thermos flask insulation design"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-05-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-05",
    "number": 11,
    "order": 11,
    "title": "Electric Current, Potential Difference & Ohm's Law",
    "summary": "Charge (Coulomb), current (Ampere = Q/t), potential difference (Volt), Ohm's law (V = IR), factors affecting resistance (length, area, resistivity), superconductivity.",
    "keyProvisions": [
      "Ohm's Law: V = IR",
      "Resistance factors: R = ρL/A",
      "Electric power: P = VI = I^2 R = V^2/R"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-05-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-05",
    "number": 12,
    "order": 12,
    "title": "Circuits, Heating Effect & Domestic Electric Wiring",
    "summary": "Resistors in series and parallel, Joule's heating effect (H = I^2 Rt), electric fuse (low melting point lead-tin alloy), earthing and circuit breakers (MCBs).",
    "keyProvisions": [
      "Domestic wiring: parallel connection at 220V, 50 Hz AC",
      "Electric fuse composition",
      "1 kWh = 3.6 x 10^6 Joules"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-05-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-05",
    "number": 13,
    "order": 13,
    "title": "Electromagnetism, Induction & Transformers",
    "summary": "Magnetic field around current-carrying conductor, Right-Hand Thumb Rule, Fleming's Left and Right Hand rules, Faraday's laws of induction, step-up/step-down transformers.",
    "keyProvisions": [
      "Faraday's Law of Electromagnetic Induction",
      "Fleming's Left-Hand Rule for electric motors",
      "Transformer operates on AC only"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-06-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-06",
    "number": 14,
    "order": 14,
    "title": "Atomic Structure & Subatomic Particles",
    "summary": "Thomson, Rutherford, and Bohr models, discovery of electron (J.J. Thomson), proton (Rutherford/Goldstein), neutron (Chadwick), atomic number and mass number.",
    "keyProvisions": [
      "Protons (+1), Neutrons (0), Electrons (-1)",
      "Chadwick discovered neutron (1932)",
      "Isotopes vs isobars"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-06-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-06",
    "number": 15,
    "order": 15,
    "title": "Radioactivity & Nuclear Fission / Fusion",
    "summary": "Henri Becquerel, alpha, beta, gamma rays, half-life, nuclear fission (uranium-235 chain reaction in nuclear reactors), nuclear fusion (stellar energy, hydrogen bomb).",
    "keyProvisions": [
      "Discovery of radioactivity by Henri Becquerel",
      "Nuclear fission vs fusion energy yield",
      "Moderators (heavy water D2O, graphite) in reactors"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-06-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-06",
    "number": 16,
    "order": 16,
    "title": "Chemical Bonding & Modern Periodic Table Trends",
    "summary": "Moseley's Modern Periodic Law (atomic number), groups and periods, electronegativity, ionization energy, atomic radius trends across periods and down groups.",
    "keyProvisions": [
      "Modern Periodic Law: properties are periodic functions of atomic numbers",
      "Valency and reactivity trends",
      "Noble gases inert electronic configuration"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-07-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-07",
    "number": 17,
    "order": 17,
    "title": "Acids, Bases, Indicators & The pH Scale",
    "summary": "Properties of acids and bases, litmus, phenolphthalein, universal indicator, Sorenson's pH scale (0 to 14), neutral pH 7, acid rain (pH < 5.6), digestive pH.",
    "keyProvisions": [
      "pH formula: -log[H+]",
      "Blood pH range: 7.35 to 7.45",
      "Natural acids: citric, tartaric, oxalic, acetic, formic (methanoic)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-07-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-07",
    "number": 18,
    "order": 18,
    "title": "Important Chemical Salts & Household Compounds",
    "summary": "Sodium chloride, caustic soda (NaOH), baking soda (NaHCO3), washing soda (Na2CO3·10H2O), bleaching powder (CaOCl2), plaster of Paris (CaSO4·1/2H2O), gypsum.",
    "keyProvisions": [
      "Plaster of Paris formula: CaSO4·0.5 H2O",
      "Baking soda vs baking powder",
      "Hardness of water removal via washing soda"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-08-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-08",
    "number": 19,
    "order": 19,
    "title": "Metals, Reactivity Series & Extraction",
    "summary": "Physical properties (malleability, ductility, conductivity), chemical reactivity series (K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Ag > Au), smelting, roasting, calcination.",
    "keyProvisions": [
      "Reactivity series of metals",
      "Aluminium extracted by Hall-Héroult electrolytic process from bauxite",
      "Mercury is liquid metal at room temperature"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-08-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-08",
    "number": 20,
    "order": 20,
    "title": "Corrosion, Rusting & Protection Methods",
    "summary": "Mechanism of iron rusting (presence of oxygen and water/moisture), galvanization (zinc coating), anodizing, sacrificial anode, stainless steel.",
    "keyProvisions": [
      "Rust chemical formula: hydrated ferric oxide (Fe2O3·xH2O)",
      "Galvanization uses zinc",
      "Rusting increases mass of iron"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-08-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-08",
    "number": 21,
    "order": 21,
    "title": "Important Alloys & Industrial Uses",
    "summary": "Brass (copper + zinc), bronze (copper + tin), stainless steel (iron + carbon + chromium + nickel), solder (lead + tin), duralumin, dental amalgams (mercury alloys).",
    "keyProvisions": [
      "Brass: Cu + Zn",
      "Bronze: Cu + Sn",
      "German Silver contains NO silver (Cu + Zn + Ni)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-09-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-09",
    "number": 22,
    "order": 22,
    "title": "Cell Structure, Organelles & Functions",
    "summary": "Cell theory (Schleiden, Schwann, Virchow), plant cell vs animal cell (cell wall, plastids, vacuoles), mitochondria (powerhouse, ATP), ribosomes (protein synthesis), lysosomes (suicide bags).",
    "keyProvisions": [
      "Mitochondria produce ATP via cellular respiration",
      "Ribosomes are protein factories",
      "Lysosomes contain hydrolytic digestive enzymes"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-09-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-09",
    "number": 23,
    "order": 23,
    "title": "Cell Division: Mitosis & Meiosis",
    "summary": "Cell cycle phases (G1, S, G2, M), mitosis (equational division, somatic growth, 2 diploid daughter cells), meiosis (reductional division, gametogenesis, crossing over, 4 haploid cells).",
    "keyProvisions": [
      "Mitosis produces 2 identical diploid (2n) cells",
      "Meiosis produces 4 genetically varied haploid (n) gametes",
      "Crossing over in pachytene stage of prophase I"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-09-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-09",
    "number": 24,
    "order": 24,
    "title": "Genetics, DNA/RNA Structure & Heredity",
    "summary": "Mendelian genetics (laws of segregation and independent assortment), Watson and Crick double helix model of DNA, nucleotides (adenine, thymine/uracil, guanine, cytosine), human chromosomes (23 pairs).",
    "keyProvisions": [
      "DNA double helix base pairing: A=T, G≡C",
      "RNA replaces thymine with uracil",
      "Human karyotype: 44 autosomes + 2 sex chromosomes (XX/XY)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sci-10-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-10",
    "number": 25,
    "order": 25,
    "title": "Human Circulatory System & Blood Groups",
    "summary": "Heart chambers, pulmonary and systemic circulation, components of blood (RBCs/erythrocytes, WBCs/leukocytes, platelets/thrombocytes, plasma), ABO blood grouping, Rh factor, universal donor (O-) and acceptor (AB+).",
    "keyProvisions": [
      "ABO blood group discovered by Karl Landsteiner",
      "Universal donor: O Rh-negative; Universal recipient: AB Rh-positive",
      "RBC lifespan ~120 days, hemoglobin transport of oxygen"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-10-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-10",
    "number": 26,
    "order": 26,
    "title": "Human Nervous System & Brain Anatomy",
    "summary": "Central nervous system (brain and spinal cord), cerebrum (memory, intelligence, reasoning), cerebellum (motor balance and posture), medulla oblongata (involuntary reflexes, respiration, heart rate).",
    "keyProvisions": [
      "Cerebrum: largest part, seat of intellect and voluntary motor actions",
      "Cerebellum: coordination and equilibrium",
      "Medulla oblongata: vital involuntary cardiac and respiratory centers"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-10-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-10",
    "number": 27,
    "order": 27,
    "title": "Endocrine Glands & Major Hormones",
    "summary": "Pituitary gland (master gland, growth hormone), thyroid (thyroxine, iodine deficiency goitre), pancreas (islets of Langerhans, insulin, glucagon, diabetes mellitus), adrenal glands (adrenaline/epinephrine, fight or flight).",
    "keyProvisions": [
      "Insulin produced by beta cells of islets of Langerhans",
      "Iodine essential for thyroxine synthesis",
      "Adrenaline: emergency hormone"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-11-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-11",
    "number": 28,
    "order": 28,
    "title": "Vitamins, Minerals & Nutritional Deficiency Diseases",
    "summary": "Fat-soluble vitamins (A, D, E, K), water-soluble vitamins (B-complex, C), deficiency disorders: Vitamin A (night blindness), B1 (beriberi), B3 (pellagra), C (scurvy), D (rickets), K (defective clotting), iron (anemia).",
    "keyProvisions": [
      "Fat-soluble vitamins: A, D, E, K",
      "Water-soluble: B and C",
      "Vitamin K essential for synthesis of prothrombin for blood clotting"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-11-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-11",
    "number": 29,
    "order": 29,
    "title": "Infectious Diseases: Bacterial, Viral & Protozoan Pathogens",
    "summary": "Bacterial (tuberculosis, cholera, typhoid, tetanus), viral (polio, rabies, dengue, influenza, AIDS/HIV), protozoan (malaria - Plasmodium via female Anopheles, amoebiasis, kala-azar via sandfly).",
    "keyProvisions": [
      "Malaria caused by protozoan Plasmodium, vector female Anopheles mosquito",
      "Tuberculosis caused by Mycobacterium tuberculosis (BCG vaccine)",
      "Dengue caused by Flavivirus, vector Aedes aegypti"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-11-03",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-11",
    "number": 30,
    "order": 30,
    "title": "Immunity, Antibodies & Vaccine Platforms",
    "summary": "Innate vs acquired immunity, active vs passive immunity, B-cells (humoral immunity, antibodies), T-cells (cell-mediated immunity), vaccine types (inactivated, live-attenuated, mRNA, viral vector).",
    "keyProvisions": [
      "Antigen-antibody specificity",
      "Active immunity produces memory cells",
      "Edward Jenner developed first vaccine (smallpox 1796)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-12-01",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-12",
    "number": 31,
    "order": 31,
    "title": "Plant Physiology, Transpiration & Photosynthesis",
    "summary": "Xylem (water and mineral transport upwards), phloem (bidirectional translocation of photoassimilates), photosynthesis (chlorophyll, 6CO2 + 6H2O -> C6H12O6 + 6O2), stomatal transpiration.",
    "keyProvisions": [
      "Xylem transports water unidirectionally",
      "Phloem translocates nutrients bidirectionally",
      "Oxygen released in photosynthesis derives from photolysis of water, not CO2"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sci-12-02",
    "subjectId": "gk-science",
    "chapterId": "ch-sci-12",
    "number": 32,
    "order": 32,
    "title": "Ecosystems, Food Chains & Bio-Geochemical Cycles",
    "summary": "Producers, consumers, decomposers, 10% energy transfer law (Lindeman), bioaccumulation and biomagnification of persistent pollutants (DDT, mercury), carbon and nitrogen cycles.",
    "keyProvisions": [
      "10 percent law of energy transfer (Raymond Lindeman 1942)",
      "Biomagnification increases concentration at higher trophic levels",
      "Pyramid of energy is always upright"
    ],
    "estimatedMinutes": 20
  }
];
  global.SCIENCE_TOPICS = SCIENCE_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: SCIENCE_TOPICS, SCIENCE_TOPICS: SCIENCE_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
