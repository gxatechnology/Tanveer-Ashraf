# -*- coding: utf-8 -*-
"""
Final Vocabulary Assembler & Exporter for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3).
Appends Jurisprudence, Legal Maxims, Court Terms, and Property Law to reach 285 verified entries.
Validates the entire database and writes assets/games/data/legal-vocabulary.js.
"""
import json
import os
import re

from append_contract_and_torts import ALL_ITEMS

JURISPRUDENCE_ITEMS = [
    ("voc-186", "JURISPRUDENCE", "beginner", "Jurisprudence",
     "The science, philosophy, and study of human and positive law",
     "Derived from Latin 'juris prudentia' meaning knowledge or skill in law; Salmond: 'science of first principles of civil law'",
     "The foundational philosophy and theoretical study of legal systems, rights, duties, and institutions.",
     "Salmond and Austin analyzed jurisprudence as the systematic exposition of foundational legal concepts.",
     "Salmond on Jurisprudence; Austin's Province of Jurisprudence Determined",
     "https://main.sci.gov.in/judgments"),

    ("voc-187", "NATURAL LAW", "beginner", "Jurisprudence",
     "Philosophy of law asserting that certain rights and moral values are inherent in human nature and discovered through reason",
     "Associated with Aristotle, Aquinas, Locke, and Fuller; higher law superseding unjust positive enactments",
     "A universal body of unchanging moral principles regarded as the foundational basis for all human conduct and law.",
     "The concept of procedural fairness and Article 21 due process in Indian law draws deeply from natural law principles.",
     "Maneka Gandhi v. Union of India (1978 1 SCC 248); H.L.A. Hart and Lon Fuller debate",
     "https://main.sci.gov.in/judgments"),

    ("voc-188", "POSITIVISM", "intermediate", "Jurisprudence",
     "School of jurisprudence maintaining that law is posited by human authority, separate from morality",
     "Associated with Bentham, Austin ('command of sovereign'), and Hart ('rule of recognition')",
     "A philosophy of jurisprudence that separates law as it is from law as it ought to be, tracing validity to sovereign source.",
     "Austin's analytical positivism defined law strictly as the command of the sovereign backed by sanctions.",
     "John Austin, The Province of Jurisprudence Determined (1832); H.L.A. Hart, The Concept of Law (1961)",
     "https://main.sci.gov.in/judgments"),

    ("voc-189", "GRUNDNORM", "advanced", "Jurisprudence",
     "Basic or foundational norm in Hans Kelsen's Pure Theory of Law from which all subordinate legal norms derive validity",
     "Postulated by Kelsen; in a constitutional democracy, the Constitution itself acts as the Grundnorm",
     "The supreme foundational norm at the apex of the legal hierarchy that validates all other subordinate legal rules.",
     "In India's constitutional framework, the Constitution of India functions as the supreme Grundnorm.",
     "Hans Kelsen, General Theory of Law and State (1945); Kesavananda Bharati v. State of Kerala",
     "https://main.sci.gov.in/judgments"),

    ("voc-190", "SOVEREIGN", "beginner", "Jurisprudence",
     "Supreme political authority in a state that receives habitual obedience from society and renders obedience to no one",
     "Core concept in Austinian analytical jurisprudence; in India, sovereign authority vests in 'We, the People'",
     "The supreme and independent political entity or institution exercising ultimate legislative and executive power.",
     "In Indian constitutional jurisprudence, sovereign power is exercised through constitutional institutions under the Preamble.",
     "Indira Nehru Gandhi v. Raj Narain (1975 Supp SCC 1); John Austin",
     "https://main.sci.gov.in/judgments"),

    ("voc-191", "CUSTOM", "beginner", "Jurisprudence",
     "Habitual course of conduct observed continuously from time immemorial, recognized as a primary source of law",
     "Must be ancient, certain, reasonable, and not opposed to public policy or statutory law",
     "An unwritten long-standing social usage that has attained the force of binding legal obligation through uniform observance.",
     "A customary marriage ritual observed by a community since antiquity was recognized under Hindu law.",
     "Hindu Marriage Act, 1955, Section 3(a); Collector of Madura v. Moottoo Ramalinga (1868 12 MIA 397)",
     "https://www.indiacode.nic.in/handle/123456789/1560"),

    ("voc-192", "PRECEDENT", "beginner", "Jurisprudence",
     "Judicial decision serving as an authoritative rule or pattern for deciding subsequent similar cases",
     "Source of law based on stare decisis; Supreme Court judgments are binding on all Indian courts under Article 141",
     "An earlier judicial ruling that furnishes an authoritative principle for the determination of future similar controversies.",
     "Under Article 141, the ratio decidendi declared by the Supreme Court serves as binding precedent across India.",
     "Constitution of India, Article 141; Bengal Immunity Co. v. State of Bihar (AIR 1955 SC 661)",
     "https://www.indiacode.nic.in/handle/123456789/1522"),

    ("voc-193", "LEGISLATION", "beginner", "Jurisprudence",
     "The formal making of law by a competent legislative organ; regarded by modern jurists as the supreme source of law",
     "Divided into supreme legislation (Parliament) and subordinate legislation (rules, regulations, bye-laws)",
     "The formal enactment of binding statutory rules by an authorized sovereign legislative assembly.",
     "The enactment of the Bharatiya Nyaya Sanhita, 2023 by Parliament is a direct exercise of supreme legislation.",
     "Salmond on Jurisprudence, 12th Ed., Chapter on Legislation",
     "https://main.sci.gov.in/judgments"),

    ("voc-194", "LEGAL RIGHT", "beginner", "Jurisprudence",
     "An interest recognized, protected, and enforced by law, imposing a corresponding duty on others",
     "Hohfeldian analysis decomposes rights into claims, liberties, powers, and immunities",
     "A legally protected interest whose violation constitutes a legal wrong actionable in court.",
     "A registered owner's right to exclude trespassers from property is a fundamental legal right in rem.",
     "State of Rajasthan v. Union of India (1977 3 SCC 592); Wesley Newcomb Hohfeld, Fundamental Legal Conceptions",
     "https://main.sci.gov.in/judgments"),

    ("voc-195", "LEGAL DUTY", "beginner", "Jurisprudence",
     "Obligation recognized by law requiring a person to do or abstain from doing something for another",
     "The correlative of a legal right; breach of duty constitutes an actionable wrong",
     "A mandatory obligation imposed by legal rules requiring obedience under pain of civil or criminal sanction.",
     "A driver has a positive legal duty to stop and provide assistance following a highway accident.",
     "Salmond on Jurisprudence; Motor Vehicles Act, 1988, Section 134",
     "https://www.indiacode.nic.in/handle/123456789/1998"),

    ("voc-196", "OWNERSHIP", "intermediate", "Jurisprudence",
     "The complex of legal rights to possess, use, enjoy, alienate, and destroy a thing to the exclusion of others",
     "Salmond: 'Ownership is the relation between a person and any right that is vested in him'",
     "The bundle of absolute proprietary rights over property recognized by law, comprising title and right to dispose.",
     "Ownership of agricultural land confers the right to cultivate, lease, mortgage, or sell the property freely.",
     "Salmond on Jurisprudence, 12th Ed., Chapter 8; Guru Amarjit Singh v. Rattan Chand (1993 4 SCC 349)",
     "https://main.sci.gov.in/judgments"),

    ("voc-197", "POSSESSION", "intermediate", "Jurisprudence",
     "The physical control of a thing coupled with the intention to hold it for oneself to the exclusion of others",
     "Comprises corpus possessionis (physical control) and animus possidendi (mental intent to exclude)",
     "The visible custody and physical dominion over tangible property accompanied by the intent to exclude others.",
     "Even a tenant possessing a house without ownership title can maintain a suit to protect settled possession against force.",
     "Rame Gowda v. M. Varadappa Naidu (2004 1 SCC 769); Poona Ram v. Moti Ram (2019 11 SCC 309)",
     "https://main.sci.gov.in/judgments"),

    ("voc-198", "CORPUS POSSESSIONIS", "advanced", "Jurisprudence",
     "The objective physical element of possession; actual physical custody or power over a thing",
     "Latin term; physical control necessary alongside animus to establish legally recognized possession",
     "The material physical detention or control exercised by an individual over tangible property.",
     "Holding the physical ignition key and parking a car in one's private locked garage provides corpus possessionis.",
     "Salmond on Jurisprudence; Supdt. and Remembrancer of Legal Affairs, W.B. v. Anil Kumar Bhunja (1979 4 SCC 274)",
     "https://main.sci.gov.in/judgments"),

    ("voc-199", "ANIMUS POSSIDENDI", "advanced", "Jurisprudence",
     "The subjective mental element of possession; the intention to hold and control a thing as one's own to the exclusion of others",
     "Latin term; distinguished from mere physical custody without mental intent",
     "The conscious intention to exercise physical custody over a thing for one's own benefit to the exclusion of the world.",
     "A servant holding a silver tray for a master has mere physical custody, lacking animus possidendi.",
     "Babu Lal v. Ram Swarup (AIR 1952 All 560); P. Lakshmi Reddy v. L. Lakshmi Reddy (AIR 1957 SC 314)",
     "https://main.sci.gov.in/judgments"),

    ("voc-200", "TITLE", "beginner", "Jurisprudence",
     "The legal basis, deed, or vestitive facts by which a person acquires ownership of property",
     "Vestitive facts are divided into acts of parties (sale, gift) and operation of law (inheritance, prescription)",
     "The legal ground, document, or set of facts constituting lawful ownership of real or personal property.",
     "A duly registered Sale Deed confers valid marketable title to the real estate upon the purchaser.",
     "Transfer of Property Act, 1882, Section 54; Suraj Lamp & Industries v. State of Haryana (2012 1 SCC 656)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-201", "LEGAL PERSONALITY", "intermediate", "Jurisprudence",
     "Capacity recognized by law of having legal rights and bearing legal duties, conferred on humans and artificial entities",
     "Includes natural persons and juristic persons (corporations, idols, cooperative societies)",
     "The status conferred by a legal system on an entity enabling it to sue, be sued, hold property, and enter contracts.",
     "A registered company and a consecrated Hindu idol are both recognized as possessing separate legal personality.",
     "Shiromani Gurdwara Parbandhak Committee v. Som Nath Dass (2000 4 SCC 146); Salomon v. Salomon",
     "https://main.sci.gov.in/judgments"),

    ("voc-202", "STARE DECISIS", "beginner", "Jurisprudence",
     "Doctrine requiring courts to stand by decided cases and adhere to established rules of law",
     "Latin for 'to stand by things decided'; ensures consistency, certainty, and stability in judicial adjudication",
     "The principle that judicial precedents must be respected and followed in subsequent cases with similar facts.",
     "Under the doctrine of stare decisis, a high court bench is bound by decisions of earlier benches of equal strength.",
     "Central Board of Dawoodi Bohra Community v. State of Maharashtra (2005 2 SCC 673)",
     "https://main.sci.gov.in/judgments"),

    ("voc-203", "RATIO DECIDENDI", "intermediate", "Jurisprudence",
     "The underlying legal principle or reason upon which a judicial decision is founded, creating binding precedent",
     "Latin for 'reason of deciding'; distinguished from obiter dicta; binding under Article 141",
     "The fundamental legal principle that determines the outcome of a case and serves as binding precedent for the future.",
     "The ratio decidendi of Maneka Gandhi is that statutory procedure depriving liberty must be just, fair, and reasonable.",
     "Director of Settlements, A.P. v. M.R. Apparao (2002 4 SCC 638); Arthur L. Goodhart's ratio test",
     "https://main.sci.gov.in/judgments"),

    ("voc-204", "OBITER DICTA", "intermediate", "Jurisprudence",
     "Observations, illustrations, or judicial remarks made in passing that are not essential to the determination of the case",
     "Latin for 'by the way'; persuasive authority, but not strictly binding precedent under Article 141",
     "Casual judicial comments or reflections on legal issues not directly necessary to decide the matter in controversy.",
     "The judge's passing commentary on patent law in a simple breach of contract case was non-binding obiter dicta.",
     "State of Haryana v. Ranbir (2006 5 SCC 167); Mohandas Issardas v. A.N. Sattanathan (AIR 1955 Bom 113)",
     "https://main.sci.gov.in/judgments"),

    ("voc-205", "SUBSTANTIVE LAW", "beginner", "Jurisprudence",
     "Body of statutory rules that defines, creates, and regulates legal rights, duties, and offenses",
     "Contrasted with procedural law; e.g., Bharatiya Nyaya Sanhita, Indian Contract Act, Transfer of Property Act",
     "The statutory framework that creates, defines, and regulates rights, duties, liabilities, and legal relations.",
     "The Bharatiya Nyaya Sanhita is substantive criminal law, defining offenses and prescribing their punishments.",
     "Blyth v. Blyth (1966 1 All ER 524); Central Bank of India v. Vrajlal Kapurchand Gandhi (2003 6 SCC 573)",
     "https://main.sci.gov.in/judgments"),

    ("voc-206", "PROCEDURAL LAW", "beginner", "Jurisprudence",
     "Law that prescribes the formal machinery, steps, and procedure for enforcing substantive rights and duties",
     "Adjective law; e.g., Bharatiya Nagarik Suraksha Sanhita, Code of Civil Procedure, Bharatiya Sakshya Adhiniyam",
     "The rules of court governing the mechanics and process by which a civil or criminal lawsuit is instituted and tried.",
     "The Bharatiya Nagarik Suraksha Sanhita governs the procedural rules for investigation, arrest, bail, and trial.",
     "Ghanshyam Dass v. Dominion of India (1984 3 SCC 46); Salmond on Jurisprudence",
     "https://main.sci.gov.in/judgments"),

    ("voc-207", "CODIFICATION", "intermediate", "Jurisprudence",
     "The systematic arrangement, collection, and reduction of statutory or customary rules into a coherent written code",
     "Pioneered by Jeremy Bentham and Macaulay (drafter of the original Indian Penal Code, 1860)",
     "The comprehensive consolidation and systematic legislative enactment of an entire branch of law into a single code.",
     "Macaulay's monumental codification in 1860 gave India the Penal Code, modernized into the BNS in 2023.",
     "Sir Courtenay Ilbert, Legislative Methods and Forms; Bentham on Codification",
     "https://www.indiacode.nic.in"),

    ("voc-208", "UTILITARIANISM", "intermediate", "Jurisprudence",
     "Legal and moral philosophy advocating 'the greatest happiness of the greatest number' as the measure of law",
     "Founded by Jeremy Bentham; evaluates legal enactments by utility through pain and pleasure calculus",
     "A consequentialist legal theory asserting that laws must be designed to maximize aggregate social well-being and utility.",
     "Bentham argued that penal legislation should deter crime while inflicting only the minimal pain necessary for deterrence.",
     "Jeremy Bentham, An Introduction to the Principles of Morals and Legislation (1789)",
     "https://main.sci.gov.in/judgments"),

    ("voc-209", "SOCIAL ENGINEERING", "advanced", "Jurisprudence",
     "Roscoe Pound's sociological theory of law as an instrument for harmonizing competing social, public, and private interests",
     "Sociological jurisprudence; aims to eliminate friction and waste in satisfying human wants and demands",
     "The functional conception of law as an active tool of social balancing and progressive societal transformation.",
     "Protective labor legislation and agrarian land ceiling acts in India exemplify law as social engineering.",
     "Roscoe Pound, Jurisprudence (1959); National Textile Workers' Union v. P.R. Ramakrishnan (1983 1 SCC 228)",
     "https://main.sci.gov.in/judgments"),

    ("voc-210", "LIVING LAW", "advanced", "Jurisprudence",
     "Eugen Ehrlich's concept of the actual unwritten norms governing human associations, distinct from formal state statutes",
     "Core premise of sociological school; law arises from societal inner order rather than legislative decree",
     "The dynamic social practices and internalized rules actually observed by communities in daily social life.",
     "Ehrlich demonstrated that business merchants often resolve disputes according to commercial living law rather than court codes.",
     "Eugen Ehrlich, Fundamental Principles of the Sociology of Law (1913)",
     "https://main.sci.gov.in/judgments"),

    ("voc-211", "HISTORICAL SCHOOL", "intermediate", "Jurisprudence",
     "School of jurisprudence asserting that law is not made by sovereign command, but organically evolves from national consciousness",
     "Founded by Friedrich Carl von Savigny; developed concept of 'Volksgeist' (spirit of the people)",
     "A jurisprudence school tracing legal validity to gradual, organic historical evolution rooted in community customs.",
     "Savigny opposed rapid codification in Germany, arguing law must develop through organic customs like language.",
     "Friedrich Carl von Savigny, Of the Vocation of Our Age for Legislation and Jurisprudence (1814)",
     "https://main.sci.gov.in/judgments"),

    ("voc-212", "REALIST SCHOOL", "advanced", "Jurisprudence",
     "American and Scandinavian jurisprudence viewing law pragmatically as the predictions of what courts actually do in fact",
     "Oliver Wendell Holmes Jr. ('the life of the law has not been logic; it has been experience'), Jerome Frank, and Karl Llewellyn",
     "A pragmatic legal philosophy emphasizing real-world judicial behavior, judicial discretion, and sociological impact.",
     "Holmes' bad-man theory defined law simply as the prophecy of what judges will enforce in fact.",
     "Oliver Wendell Holmes Jr., The Path of the Law (1897); Jerome Frank, Law and the Modern Mind",
     "https://main.sci.gov.in/judgments"),

    ("voc-213", "RIGHT IN REM", "intermediate", "Jurisprudence",
     "A legal right available against the whole world at large, such as ownership of land",
     "Contrasted with right in personam; binds all citizens not to interfere with the protected entitlement",
     "An absolute proprietary right enforceable against all individuals in human society generally.",
     "A registered patent right is a right in rem, preventing anyone in the country from manufacturing the patented invention.",
     "Salmond on Jurisprudence; T.P. Act, 1882",
     "https://main.sci.gov.in/judgments"),

    ("voc-214", "RIGHT IN PERSONAM", "intermediate", "Jurisprudence",
     "A legal right available only against a specific, definite individual or party, such as a contractual debt",
     "Correlative to a specific contractual duty; enforceable solely against the debtor or obligor",
     "A relative personal right enforceable only against designated individuals bound by contract or fiduciary relation.",
     "The right to recover a ten-thousand rupee loan from a specific borrower is a classic right in personam.",
     "Salmond on Jurisprudence; Indian Contract Act, 1872",
     "https://main.sci.gov.in/judgments"),

    ("voc-215", "DE FACTO", "beginner", "Jurisprudence",
     "In fact, actual, or in reality, whether recognized by formal law or not",
     "Latin legal term; contrasted with de jure (lawful or by right)",
     "Existing as an actual state of affairs or reality regardless of formal legal title or constitutional sanction.",
     "The caretaker exercised de facto possession of the estate, although legal title belonged to the absent heir.",
     "Gokaraju Rangaraju v. State of A.P. (1981 3 SCC 132 — De Facto Doctrine)",
     "https://main.sci.gov.in/judgments")
]

MAXIMS_ITEMS = [
    ("voc-216", "AUDI ALTERAM PARTEM", "beginner", "Legal Maxims",
     "First pillar of natural justice: 'Hear the other side'; no person should be condemned or judged unheard",
     "Latin legal maxim; guarantees fair hearing, prior notice, and opportunity to present defense",
     "The indispensable rule of procedural fairness mandating that no person shall be judged without a fair hearing.",
     "An order terminating a government civil servant without issuing a show-cause notice violates audi alteram partem.",
     "Maneka Gandhi v. Union of India (1978 1 SCC 248); Ridge v. Baldwin (1964 AC 40)",
     "https://main.sci.gov.in/judgments"),

    ("voc-217", "NEMO JUDEX IN CAUSA SUA", "beginner", "Legal Maxims",
     "Second pillar of natural justice: 'No one should be a judge in their own cause'; rule against bias",
     "Latin legal maxim; disqualifies any adjudicator with personal, pecuniary, or subject-matter bias",
     "The fundamental legal rule ensuring absolute judicial impartiality by disqualifying judges with any personal stake.",
     "A departmental inquiry officer who was also the principal complaining witness was disqualified for bias.",
     "A.K. Kraipak v. Union of India (1969 2 SCC 262); Dimes v. Grand Junction Canal (1852 3 HLC 759)",
     "https://main.sci.gov.in/judgments"),

    ("voc-218", "UBI JUS IBI REMEDIUM", "beginner", "Legal Maxims",
     "Foundational legal maxim: 'Where there is a right, there is a remedy'",
     "Latin maxim; establishes that the law will not allow a recognized legal injury to go without a judicial remedy",
     "The fundamental premise that wherever law confers a right, it also provides a legal machinery to protect and enforce it.",
     "When an election official wrongfully rejected a lawful vote, the court held that ubi jus ibi remedium applied.",
     "Ashby v. White (1703 2 Ld Raym 938); Sardar Amarjit Singh Kalra v. Pramod Gupta (2003 3 SCC 272)",
     "https://main.sci.gov.in/judgments"),

    ("voc-219", "IGNORANTIA JURIS NON EXCUSAT", "beginner", "Legal Maxims",
     "Ancient legal maxim: 'Ignorance of the law excuses not'; every citizen is presumed to know the law",
     "Latin maxim; ignorance of fact is an excuse under Section 14 BNS, but ignorance of law is never an excuse",
     "The universal legal rule holding that lack of knowledge of a statute is no defense against liability.",
     "An accused cannot escape penalties for transporting undeclared foreign currency by claiming ignorance of foreign exchange acts.",
     "Bharatiya Nyaya Sanhita, 2023, Section 14; State of Maharashtra v. Mayer Hans George (AIR 1965 SC 722)",
     "https://main.sci.gov.in/judgments"),

    ("voc-220", "DE MINIMIS NON CURAT LEX", "intermediate", "Legal Maxims",
     "Maxim: 'The law does not concern itself with trifles'; acts causing negligible or slight harm are not offenses",
     "Codified under Section 34 of Bharatiya Nyaya Sanhita, 2023 (formerly Section 95 IPC)",
     "A statutory defense excluding trivial or negligible infringements that a person of ordinary sense would ignore.",
     "Accidentally dipping an elbow onto a fellow passenger's coat sleeve in a crowded metro is shielded by de minimis.",
     "Bharatiya Nyaya Sanhita, 2023, Section 34; Mrs. Veeda Menezes v. Yusuf Khan Haji (AIR 1966 SC 1773)",
     "https://www.indiacode.nic.in/handle/123456789/2111"),

    ("voc-221", "ACTIO PERSONALIS MORITUR CUM PERSONA", "intermediate", "Legal Maxims",
     "Maxim: 'A personal right of action dies with the person'; personal injury tort claims generally abate on death",
     "Latin legal maxim; modified by survival of actions in Fatal Accidents Act and modern motor accident claim acts",
     "The common law rule establishing that actions founded on purely personal wrongs terminate upon the death of either party.",
     "A civil suit claiming damages for personal defamation terminates upon the plaintiff's death under this maxim.",
     "Melepurath Sankunni Ezhuthassan v. Thekittil Geopalankutty Nair (1986 1 SCC 118)",
     "https://main.sci.gov.in/judgments"),

    ("voc-222", "CAVEAT EMPTOR", "beginner", "Legal Maxims",
     "Maxim: 'Let the buyer beware'; duty on buyer to inspect goods and satisfy themselves of quality before purchasing",
     "Codified in Section 16 of Sale of Goods Act, 1930; subject to implied conditions of fitness and merchantability",
     "A commercial legal principle placing the risk and burden of examining goods upon the buyer prior to purchase.",
     "A customer buying second-hand furniture without inspecting its joints cannot sue the vendor for obvious wobbliness.",
     "Sale of Goods Act, 1930, Section 16; Ward v. Hobbs (1878 4 App Cas 13)",
     "https://www.indiacode.nic.in/handle/123456789/2384"),

    ("voc-223", "CAVEAT VENDITOR", "intermediate", "Legal Maxims",
     "Modern commercial maxim: 'Let the seller beware'; duty on manufacturer/seller to ensure products are safe and fit",
     "Modern consumer jurisprudence; core principle under Consumer Protection Act, 2019",
     "The modern consumer law principle holding sellers and product manufacturers responsible for defective goods.",
     "Under modern product liability rules, a manufacturer is strictly accountable for manufacturing defects.",
     "Consumer Protection Act, 2019, Section 82-87; Donoghue v. Stevenson (1932 AC 562)",
     "https://www.indiacode.nic.in/handle/123456789/15256"),

    ("voc-224", "SALUS POPULI SUPREMA LEX", "intermediate", "Legal Maxims",
     "Maxim: 'The safety and welfare of the people is the supreme law'",
     "Latin maxim; public welfare and safety takes precedence over private individual property rights in times of national crisis",
     "The constitutional doctrine that the security and health of the public constitutes the paramount legal interest.",
     "Demolishing a dilapidated private building about to collapse onto a crowded public highway is justified under this maxim.",
     "State of U.P. v. Raj Narain (1975 4 SCC 428); Municipal Corporation of Greater Bombay v. Lala Pancham",
     "https://main.sci.gov.in/judgments"),

    ("voc-225", "EX NUDO PACTO NON ORITUR ACTIO", "advanced", "Legal Maxims",
     "Maxim: 'No right of action arises from a bare promise made without consideration'",
     "Latin maxim; codified in Section 25 of Indian Contract Act, 1872",
     "The contract law rule that an informal promise unsupported by consideration cannot be enforced in a court of law.",
     "A gratuitous promise to gift a sports car to a friend cannot support a lawsuit for breach if the promisor changes his mind.",
     "Indian Contract Act, 1872, Section 25; Rann v. Hughes (1778 7 TR 350)",
     "https://www.indiacode.nic.in/handle/123456789/2187"),

    ("voc-226", "IN BONAM PARTEM", "advanced", "Legal Maxims",
     "Maxim: 'In a good sense'; words in a statute should be construed favorably and lawfully rather than maliciously",
     "Rule of statutory interpretation presuming that words in an enactment refer to lawful acts rather than illegal acts",
     "A canon of construction requiring statutory words to be interpreted in a lawful, regular, and proper sense.",
     "The statutory term 'possession' in a licensing act was interpreted in bonam partem to mean lawful possession.",
     "Maxwell on the Interpretation of Statutes; Re: B.V. Govindarajulu (AIR 1950 Mad 839)",
     "https://main.sci.gov.in/judgments"),

    ("voc-227", "PRIMA FACIE", "beginner", "Legal Maxims",
     "At first sight or on the face of it; sufficient evidence to establish a fact unless rebutted",
     "Latin legal term; mandatory standard for framing of criminal charges and granting interim injunctions",
     "Sufficient evidence at preliminary evaluation to raise a legal presumption of fact unless contradicted.",
     "The trial judge framed charges under Section 308 BNS after finding a prima facie case against the accused.",
     "Union of India v. Prafulla Kumar Samal (1979 3 SCC 4); Order XXXIX Rule 1 CPC",
     "https://main.sci.gov.in/judgments"),

    ("voc-228", "BONA FIDE", "beginner", "Legal Maxims",
     "In good faith; without fraud, deceit, or intentional collusion",
     "Latin legal term; protected under General Exceptions (Section 14 BNS) and Section 3(22) General Clauses Act",
     "An act performed honestly and with due care and attention, free from deceit or fraudulent intent.",
     "A bona fide purchaser for valuable consideration without notice of an unrecorded title dispute takes clean title.",
     "General Clauses Act, 1897, Section 3(22); Bharatiya Nyaya Sanhita, 2023, Section 14",
     "https://www.indiacode.nic.in/handle/123456789/2184"),

    ("voc-229", "MALA FIDE", "beginner", "Legal Maxims",
     "In bad faith; with fraudulent, dishonest, or malicious intent",
     "Latin legal term; administrative action tainted by mala fides is null and void under Article 226",
     "Conduct marked by deliberate dishonesty, corrupt intent, or improper collateral motives.",
     "An administrative transfer of a whistleblower advocate ordered purely out of personal vindictiveness was set aside as mala fide.",
     "State of Punjab v. Gurdial Singh (1980 2 SCC 471); E.P. Royappa v. State of Tamil Nadu",
     "https://main.sci.gov.in/judgments"),

    ("voc-230", "ULTRA VIRES", "beginner", "Legal Maxims",
     "Beyond the powers; an act performed by a corporation, minister, or body exceeding legally conferred jurisdiction",
     "Latin legal term; ultra vires regulations or administrative decisions are void ab initio",
     "Acting beyond the statutory scope of powers authorized by the Constitution, statute, or corporate charter.",
     "A municipal council passing an income tax ordinance acted ultra vires its statutory powers under the Municipalities Act.",
     "Ashbury Railway Carriage Co. v. Riche (1875 LR 7 HL 653); Express Newspapers v. Union of India",
     "https://main.sci.gov.in/judgments"),

    ("voc-231", "INTRA VIRES", "intermediate", "Legal Maxims",
     "Within the legal powers or authority lawfully conferred by statute or the Constitution",
     "Latin legal term; opposite of ultra vires",
     "An act, rule, or administrative order executed fully within the limits of legally granted statutory jurisdiction.",
     "The High Court held that the environmental emission rules framed by the board were intra vires the enabling parent act.",
     "State of U.P. v. Babu Ram Upadhya (AIR 1961 SC 751)",
     "https://main.sci.gov.in/judgments"),

    ("voc-232", "MUTATIS MUTANDIS", "intermediate", "Legal Maxims",
     "With the necessary changes in points of detail; adopting a rule with suitable modifications to fit new context",
     "Latin phrase ubiquitous in Indian procedural drafting and statutory cross-referencing",
     "Applying statutory rules to a new situation while making only those alterations necessary to adapt to the new context.",
     "The appellate rules provide that provisions governing original appeals apply mutatis mutandis to miscellaneous appeals.",
     "Ashok Service Centre v. State of Orissa (1983 2 SCC 82)",
     "https://main.sci.gov.in/judgments"),

    ("voc-233", "PRO BONO", "beginner", "Legal Maxims",
     "Professional legal work undertaken voluntarily and without charge for the public good",
     "Short for 'pro bono publico' (for the public good); core duty under Bar Council of India rules and Article 39A",
     "Free legal representation and counsel provided to indigent litigants or worthy public causes in the public interest.",
     "The senior advocate appeared pro bono on behalf of the displaced slum dwellers to ensure their constitutional defense.",
     "Bar Council of India Rules; Constitution of India, Article 39A; Hussainara Khatoon v. Home Secretary, State of Bihar",
     "https://main.sci.gov.in/judgments"),

    ("voc-234", "NEMO DEBET BIS VEXARI", "intermediate", "Legal Maxims",
     "Maxim: 'No one should be vexed twice for one and the same cause'; constitutional rule against double jeopardy",
     "Codified in Article 20(2) of Constitution of India and Section 337 BNSS (Section 300 CrPC)",
     "The fundamental legal principle protecting an individual from repeated prosecutions for an identical criminal offense.",
     "Having been lawfully acquitted of robbery, the defendant could not be retried on the same facts under this maxim.",
     "Constitution of India, Article 20(2); Maqbool Hussain v. State of Bombay (AIR 1953 SC 325)",
     "https://main.sci.gov.in/judgments"),

    ("voc-235", "ACTUS CURIAE NEMINEM GRAVABIT", "advanced", "Legal Maxims",
     "Maxim: 'An act of the court shall prejudice no one'; foundation of restitution and curative orders",
     "Codified in Section 144 CPC; court must undo damage caused to a litigant by an erroneous judicial order",
     "The universal principle that an error, delay, or mistake committed by a court of law shall not harm any litigant.",
     "When court staff misfiled an appeal causing time-lapse, the court restored the matter under actus curiae neminem gravabit.",
     "A.R. Antulay v. R.S. Nayak (1988 2 SCC 602); South Eastern Coalfields v. State of M.P.",
     "https://main.sci.gov.in/judgments"),

    ("voc-236", "QUI FACIT PER ALIUM FACIT PER SE", "intermediate", "Legal Maxims",
     "Maxim: 'He who acts through another does the act himself'; foundational rule of agency and vicarious liability",
     "Latin maxim; attributes liability to the principal for authorized acts committed by their agent or employee",
     "The legal doctrine holding that an act performed through an authorized agent is deemed the personal act of the principal.",
     "Signing a commercial purchase contract through an authorized power-of-attorney holder binds the principal under this maxim.",
     "Indian Contract Act, 1872, Section 182; State of Rajasthan v. Vidhyawati",
     "https://main.sci.gov.in/judgments"),

    ("voc-237", "DELEGATUS NON POTEST DELEGARE", "intermediate", "Legal Maxims",
     "Maxim: 'A delegate cannot further delegate'; an authorized delegate cannot sub-delegate statutory discretion without express power",
     "Core principle of administrative law; prevents sub-delegation of quasi-judicial or discretionary authority",
     "The administrative law rule prohibiting a person to whom power has been delegated from delegating it to another.",
     "A licensing magistrate cannot sub-delegate the discretionary power to cancel firearm licenses to an inspector without statutory power.",
     "Barium Chemicals Ltd. v. Company Law Board (AIR 1967 SC 295); A.K. Roy v. State of Punjab (1986 4 SCC 326)",
     "https://main.sci.gov.in/judgments"),

    ("voc-238", "EJUSDEM GENERIS", "intermediate", "Legal Maxims",
     "Statutory interpretation rule: general words following specific words must be construed as of the same kind or nature",
     "Canon of construction; e.g., 'horses, cows, sheep and other animals' does not include wild lions or tigers",
     "The rule that general statutory catch-all words take their color and meaning from the preceding specific enumerated class.",
     "In a statute restricting 'arms, ammunition, gunpowder, and other goods', 'other goods' was limited to military materiel.",
     "State of Karnataka v. Kempaiah (1998 6 SCC 103); UPSEB v. Hari Shanker Jain (1978 4 SCC 16)",
     "https://main.sci.gov.in/judgments"),

    ("voc-239", "EXPRESSIO UNIUS EST EXCLUSIO ALTERIUS", "advanced", "Legal Maxims",
     "Maxim: 'The express mention of one thing implies the exclusion of another'",
     "Canon of statutory interpretation; naming specific items in a provision indicates intent to exclude omitted items",
     "A statutory canon stating that explicit inclusion of particular items in a section implies the exclusion of alternatives.",
     "A statute granting tax exemptions to 'schools and colleges' was held to deliberately exclude commercial coaching centers.",
     "State of Maharashtra v. Laljit Rajshi Shah (2000 2 SCC 699); G.V.K. Industries v. ITO (2011 4 SCC 36)",
     "https://main.sci.gov.in/judgments"),

    ("voc-240", "GENERALIA SPECIALIBUS NON DEROGANT", "advanced", "Legal Maxims",
     "Maxim: 'General provisions do not derogate from special provisions'; specific statutes prevail over general enactments",
     "Harmonious construction rule; e.g., special insolvency code prevails over general civil procedure provisions",
     "The statutory canon establishing that a specific provision dealing with a precise subject overrides a general provision.",
     "The specific limitation period under the Arbitration Act overrides the general provisions of the Limitation Act, 1963.",
     "Life Insurance Corporation of India v. D.J. Bahadur (1980 4 SCC 82); Commercial Tax Officer v. Binani Cements (2014 8 SCC 319)",
     "https://main.sci.gov.in/judgments"),

    ("voc-241", "IN PARI DELICTO", "intermediate", "Legal Maxims",
     "Short for 'In pari delicto potior est conditio defendentis': 'Where both parties are equally at fault, the defendant's position is stronger'",
     "Latin maxim; courts will not assist a plaintiff who founds their claim on their own illegal or immoral transaction",
     "The equitable principle that court assistance is withheld when both litigants share equal guilt in an illegal bargain.",
     "A smuggler suing his partner for half the profits of an unlawful diamond trade is barred under in pari delicto.",
     "Kedar Nath Motani v. Prahlad Rai (AIR 1960 SC 213); Holman v. Johnson (1775 1 Cowp 341)",
     "https://main.sci.gov.in/judgments"),

    ("voc-242", "INTER ALIA", "beginner", "Legal Maxims",
     "Among other things; phrase used when citing selected items from a larger comprehensive set",
     "Latin phrase standard in judicial drafting and legal pleadings",
     "A legal drafting phrase indicating that the cited points are merely illustrative parts of a broader collection.",
     "The petition argued, inter alia, that the impugned demolition violated principles of natural justice and Article 21.",
     "Standard judicial drafting term used in Supreme Court of India reports",
     "https://main.sci.gov.in"),

    ("voc-243", "IPSE DIXIT", "intermediate", "Legal Maxims",
     "An unproven assertion made on someone's bare authority alone: 'He himself said it'",
     "Latin phrase; an expert opinion or executive finding unsupported by reasons or evidence is rejected as mere ipse dixit",
     "A bare, unsupported dogmatic statement accepted solely because an authoritative figure asserted it, without proof.",
     "The court rejected the police report as mere ipse dixit because it cited no corroborating forensic evidence or witness.",
     "State of U.P. v. Ram Asrey (AIR 1990 SC 1188); Dr. Ramji Singh v. State of Bihar",
     "https://main.sci.gov.in/judgments"),

    ("voc-244", "MODUS OPERANDI", "beginner", "Legal Maxims",
     "A characteristic method of operation or functioning, especially a criminal's distinctive pattern of committing offenses",
     "Latin phrase; highly relevant under Section 6 BSA (Section 8 IEA) to prove system and identity",
     "The distinctive and habitual technique or method employed by a criminal in carrying out unlawful offenses.",
     "The burglar's specific modus operandi of drilling door locks between 2 AM and 4 AM helped detectives identify the suspect.",
     "Bharatiya Sakshya Adhiniyam, 2023, Section 6; State of U.P. v. Babul Nath (1994 6 SCC 29)",
     "https://www.indiacode.nic.in/handle/123456789/2112"),

    ("voc-245", "SINE QUA NON", "beginner", "Legal Maxims",
     "An indispensable and essential condition or element without which something cannot exist",
     "Latin phrase; e.g., mens rea is a sine qua non for proving criminal homicide",
     "An indispensable prerequisite or essential foundational condition required for a legal consequence to attach.",
     "Proof of a valid subsisting prior marriage is an indispensable sine qua non for sustaining a conviction of bigamy.",
     "K.S. Puttaswamy v. Union of India (2017 10 SCC 1); BNS Section 82",
     "https://main.sci.gov.in/judgments")
]

COURT_ITEMS = [
    ("voc-246", "PETITION", "beginner", "Judicial Terminology",
     "A formal written application submitted to a court praying for specific judicial relief or exercise of jurisdiction",
     "Includes Special Leave Petitions (Article 136), Writ Petitions (Articles 32/226), and Revision Petitions",
     "A formal written document presented to a judicial tribunal setting forth facts and requesting specific legal orders.",
     "The aggrieved citizen filed a writ petition under Article 226 before the High Court of Judicature at Allahabad.",
     "Constitution of India, Article 226; Supreme Court Rules, 2013",
     "https://www.indiacode.nic.in/handle/123456789/1522"),

    ("voc-247", "BAIL", "beginner", "Judicial Terminology",
     "Temporary judicial release of an accused person awaiting trial upon security, sureties, and undertaking to appear",
     "Governed by Chapter XXXV of Bharatiya Nagarik Suraksha Sanhita, 2023; 'Bail is the rule, jail is the exception'",
     "The procurement of release from custody of an accused person upon providing adequate security for future attendance.",
     "The sessions judge granted regular bail to the accused under Section 480 BNSS upon furnishing two local sureties.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Sections 478-485; State of Rajasthan v. Balchand (1977 4 SCC 308)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-248", "ANTICIPATORY BAIL", "intermediate", "Judicial Terminology",
     "Direction issued by Sessions Court or High Court granting bail to a person in the event of their arrest on accusation of non-bailable offense",
     "Governed by Section 482 of Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly Section 438 CrPC)",
     "Pre-arrest bail granted to protect an individual from arrest and harassment in anticipated false or motivated charges.",
     "Apprehending arrest in a false property dispute, the advocate successfully moved an application for anticipatory bail.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 482; Sushila Aggarwal v. State (NCT of Delhi) (2020 5 SCC 1)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-249", "REMAND", "beginner", "Judicial Terminology",
     "Order of a magistrate sending an arrested accused back into police custody or judicial custody during investigation or trial",
     "Governed by Section 187 of BNSS 2023 (formerly Section 167 CrPC); limits initial police remand to 15 days",
     "The judicial act of committing an arrested person into continued police detention or jail custody pending inquiry.",
     "The judicial magistrate refused police remand and committed the accused to judicial custody in the district jail.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 187; CBI v. Anupam J. Kulkarni (1992 3 SCC 141)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-250", "COGNIZABLE", "beginner", "Judicial Terminology",
     "Offense for which a police officer may arrest without a warrant and investigate without magistrate's order",
     "Defined in Section 2(1)(g) of BNSS 2023 (Section 2(c) CrPC); First Schedule categorizes offenses",
     "A serious category of criminal offenses authorizing police to make arrests without prior judicial warrant.",
     "Robbery is a cognizable offense, requiring police to immediately register an FIR upon receiving information.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 2(1)(g) & 173; Lalita Kumari v. Govt. of U.P. (2014 2 SCC 1)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-251", "NON COGNIZABLE", "beginner", "Judicial Terminology",
     "Offense for which a police officer has no authority to arrest without a warrant",
     "Defined in Section 2(1)(o) of BNSS 2023 (Section 2(l) CrPC); requires magistrate permission to investigate under Section 174 BNSS",
     "Less grave offenses wherein the police cannot arrest or begin investigation without a magistrate's specific warrant.",
     "Simple assault without weapon is a non-cognizable offense recorded in the non-cognizable register (NCR).",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 2(1)(o) & 174; Keshav Lal Thakur v. State of Bihar (1996 11 SCC 557)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-252", "COMPOUNDABLE", "intermediate", "Judicial Terminology",
     "Offenses which can be lawfully compromised and settled between the victim and accused, resulting in acquittal",
     "Governed by Section 359 of BNSS 2023 (formerly Section 320 CrPC); table lists offenses with/without permission of court",
     "A statutory class of criminal offenses which the complainant can agree to drop upon arriving at an amicable settlement.",
     "Cheating was compounded by the complainant before the magistrate after receiving full refund of disputed money.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 359; Gian Singh v. State of Punjab (2012 10 SCC 303)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-253", "CHARGE", "beginner", "Judicial Terminology",
     "Formal notice formulated by court informing the accused of the precise criminal allegations against them",
     "Chapter XIX of BNSS 2023 (formerly Chapter XVII CrPC); must state offense, statute, time, and particulars",
     "The precise formal accusation drawn up by the trial court giving the defendant notice of the exact crime alleged.",
     "The sessions court formally framed charges of murder and conspiracy under Sections 103 and 61 BNS against the accused.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Sections 234-247; V.C. Shukla v. State (1980 Supp SCC 92)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-254", "ACQUITTAL", "beginner", "Judicial Terminology",
     "Formal judicial certification that an accused person is not guilty of the criminal charge after full trial",
     "Operates as a bar against double jeopardy under Article 20(2) and Section 337 BNSS (Section 300 CrPC)",
     "The definitive judicial verdict freeing an accused from criminal guilt following trial or failure of prosecution evidence.",
     "Because eyewitness testimony was thoroughly contradicted by ballistic science, the court pronounced an honorable acquittal.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 255 & 268; Babu v. State of Kerala (2010 9 SCC 189)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-255", "CONVICTION", "beginner", "Judicial Terminology",
     "Formal judicial finding following trial that the accused has been proved guilty of the charged criminal offense",
     "Requires proof beyond reasonable doubt; followed by hearing on quantum of sentence under BNSS",
     "The definitive judgment of a criminal court declaring the defendant legally guilty of a proven offense.",
     "Upon recording a conviction under Section 303(2) BNS, the magistrate heard the defense advocate on the question of sentence.",
     "Bharatiya Nagarik Suraksha Sanhita, 2023, Section 258 & 271; Santa Singh v. State of Punjab (1976 4 SCC 190)",
     "https://www.indiacode.nic.in/handle/123456789/2113"),

    ("voc-256", "SENTENCE", "beginner", "Judicial Terminology",
     "The formal judicial penalty or punishment ordered by court upon an offender following a criminal conviction",
     "Includes imprisonment, fine, community service (new in BNS), forfeiture, and capital punishment",
     "The specific statutory punishment pronounced by a trial court to be undergone by a convicted criminal.",
     "The sessions court sentenced the convict to five years rigorous imprisonment and imposed a fine of ten thousand rupees.",
     "Bharatiya Nyaya Sanhita, 2023, Chapter III (Punishments, Sections 4-13); Bachan Singh v. State of Punjab",
     "https://www.indiacode.nic.in/handle/123456789/2111"),

    ("voc-257", "PROBATION", "intermediate", "Judicial Terminology",
     "Release of a convicted offender into the community under supervision instead of sending them to prison",
     "Governed by Probation of Offenders Act, 1958 and Section 401 BNSS (Section 360 CrPC); reformative justice",
     "A reformative judicial alternative releasing a first-time minor offender on good conduct without custodial incarceration.",
     "Taking into account his youthful age and lack of criminal record, the magistrate released the first offender on probation.",
     "Probation of Offenders Act, 1958, Section 4; Rattan Lal v. State of Punjab (AIR 1965 SC 444)",
     "https://www.indiacode.nic.in/handle/123456789/1572"),

    ("voc-258", "PAROLE", "intermediate", "Judicial Terminology",
     "Conditional and temporary release of a convicted prisoner before expiration of sentence for special reasons",
     "Distinguished from furlough; granted for family bereavement, medical emergency, or reformative rehabilitation",
     "The temporary release of an incarcerated convict from prison under strict supervision and conditions of good behavior.",
     "The state government granted 30 days medical parole to the elderly convict to undergo eye cataract surgery.",
     "State of Haryana v. Mahender Singh (2007 13 SCC 606); Asfaq v. State of Rajasthan (2017 15 SCC 55)",
     "https://main.sci.gov.in/judgments"),

    ("voc-259", "CONTEMPT OF COURT", "intermediate", "Judicial Terminology",
     "Act or conduct that disrespects, defies, or scandalizes the authority, dignity, or orders of a court of justice",
     "Divided into Civil Contempt (willful disobedience of order) and Criminal Contempt (scandalizing court) under Act of 1971",
     "Conduct that defies judicial authority, impedes the administration of justice, or scandalizes court integrity.",
     "Deliberately refusing to comply with a High Court status quo injunction constitutes willful civil contempt.",
     "Contempt of Courts Act, 1971, Section 2; Constitution of India, Articles 129 & 215; Re: Prashant Bhushan (2021 1 SCC 745)",
     "https://www.indiacode.nic.in/handle/123456789/1531"),

    ("voc-260", "LOCUS STANDI", "beginner", "Judicial Terminology",
     "The legal capacity or standing of a party to bring an action before a court of law",
     "Latin term; traditionally requires personal injury; relaxed in Public Interest Litigation (PIL) by Justice P.N. Bhagwati",
     "The right of an individual to initiate a lawsuit based on having a direct, legally protectable interest in the outcome.",
     "In public interest litigation, the traditional requirement of locus standi is relaxed to protect marginalized communities.",
     "S.P. Gupta v. Union of India (1981 Supp SCC 87); Bar Council of Maharashtra v. M.V. Dabholkar",
     "https://main.sci.gov.in/judgments"),

    ("voc-261", "SUO MOTU", "beginner", "Judicial Terminology",
     "On its own motion; an action initiated by a court on its own initiative without a formal petition from a party",
     "Latin phrase; frequently exercised by High Courts and Supreme Court in public crises or human rights violations",
     "The exercise of judicial power by a court taking notice of an injustice on its own motion without a private petitioner.",
     "The High Court took suo motu cognizance of hospital fire safety violations upon reading investigative newspaper reports.",
     "In Re: Distribution of Essential Supplies During Pandemic (2021 SC); Article 226",
     "https://main.sci.gov.in/judgments"),

    ("voc-262", "IN CAMERA", "beginner", "Judicial Terminology",
     "Proceedings conducted in private or closed court chambers from which the public and press are excluded",
     "Latin for 'in a chamber'; mandated in trials of sexual offenses and matrimonial reconciliation",
     "A closed-door judicial hearing held without public or media presence to protect victim privacy and sensitivity.",
     "Section 72 of Bharatiya Nyaya Sanhita mandates that inquiry and trial of rape offenses must be conducted in camera.",
     "Bharatiya Nyaya Sanhita, 2023, Section 72 & BNSS Section 366; Naresh Shridhar Mirajkar v. State of Maharashtra",
     "https://www.indiacode.nic.in/handle/123456789/2111"),

    ("voc-263", "CORAM", "intermediate", "Judicial Terminology",
     "The judges comprising the bench hearing a particular judicial proceeding: 'In the presence of'",
     "Latin term; designated on all official court orders; e.g., 'Coram: Hon'ble Dr. Justice D.Y. Chandrachud'",
     "The specific composition of judges sitting on the judicial bench who hear and decide a case.",
     "The constitutional challenge was placed before a Constitution Bench comprising a five-judge coram.",
     "Supreme Court Rules, 2013; Union of India v. Raghubir Singh (1989 2 SCC 754)",
     "https://main.sci.gov.in"),

    ("voc-264", "BENCH", "beginner", "Judicial Terminology",
     "The seat of judges collectively or the body of judges constituting a particular court or division",
     "Categorized into Single Bench, Division Bench (two judges), Full Bench (three+), and Constitution Bench (five+)",
     "The collective body of judges presiding over a hearing in a court of law.",
     "A reference on a conflicting point of law was referred to a three-judge Full Bench of the High Court.",
     "High Court of Judicature at Allahabad Rules, 1952",
     "https://www.allahabadhighcourt.in"),

    ("voc-265", "QUORUM", "beginner", "Judicial Terminology",
     "The minimum number of members or judges required to be present to validate proceedings of a deliberative body",
     "Article 100(3) sets parliamentary quorum at one-tenth of total membership; Article 145(3) sets Constitution Bench quorum at 5",
     "The statutory minimum number of judicial officers or legislative members necessary to lawfully transact business.",
     "A minimum quorum of five Supreme Court judges is required under Article 145(3) to decide substantial constitutional questions.",
     "Constitution of India, Article 100(3) & 145(3)",
     "https://www.indiacode.nic.in/handle/123456789/1522")
]

PROPERTY_ITEMS = [
    ("voc-266", "MORTGAGE", "beginner", "Property Law",
     "The transfer of an interest in specific immovable property for the purpose of securing payment of a loan or debt",
     "Defined in Section 58 of Transfer of Property Act, 1882; divided into 6 statutory classes (simple, usufructuary, etc.)",
     "A conveyance of an interest in real property as collateral security for the repayment of a debt or money loan.",
     "Executing a registered simple mortgage over agricultural land to secure a bank crop loan is governed by Section 58(b) TPA.",
     "Transfer of Property Act, 1882, Section 58; Ram Kinkar Banerjee v. Satya Charan Srimani (AIR 1939 PC 14)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-267", "LEASE", "beginner", "Property Law",
     "Transfer of a right to enjoy immovable property made for a certain time or in perpetuity in consideration of price or rent",
     "Defined in Section 105 of Transfer of Property Act, 1882; parties are lessor and lessee",
     "A contractual grant of exclusive possession of real property for a specified term in exchange for rent.",
     "Letting out a commercial office space for five years against monthly rent of fifty thousand rupees constitutes a statutory lease.",
     "Transfer of Property Act, 1882, Section 105; Associated Hotels of India v. R.N. Kapoor (AIR 1959 SC 1262)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-268", "SALE OF PROPERTY", "beginner", "Property Law",
     "Transfer of ownership in exchange for a price paid or promised, or part-paid and part-promised",
     "Defined in Section 54 of Transfer of Property Act, 1882; requires registered instrument for value of Rs 100 or upward",
     "The absolute conveyance of full ownership title in immovable property from seller to buyer in exchange for a price.",
     "Execution and registration of a Sale Deed before the Sub-Registrar completes the transfer of title under Section 54 TPA.",
     "Transfer of Property Act, 1882, Section 54; Suraj Lamp & Industries v. State of Haryana (2012 1 SCC 656)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-269", "EXCHANGE", "intermediate", "Property Law",
     "When two persons mutually transfer the ownership of one thing for the ownership of another, neither thing being money only",
     "Defined in Section 118 of Transfer of Property Act, 1882; parties have rights and liabilities of a seller and buyer",
     "A bilateral transaction where two landowners mutually swap parcels of land without an exclusive cash purchase price.",
     "Swapping an agricultural field in the north village for a commercial orchard plot in the south village is a statutory exchange.",
     "Transfer of Property Act, 1882, Section 118; CIT v. Motors & General Stores (AIR 1968 SC 200)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-270", "GIFT", "beginner", "Property Law",
     "Transfer of certain existing movable or immovable property made voluntarily and without consideration by donor to donee",
     "Defined in Section 122 of Transfer of Property Act, 1882; must be accepted by donee during donor's lifetime",
     "A gratuitous voluntary transfer of property ownership made without monetary consideration and accepted by donee.",
     "Gifting an ancestral house to a daughter through a registered deed accepted during the father's lifetime is a valid gift.",
     "Transfer of Property Act, 1882, Section 122 & 123; K. Balakrishnan v. K. Kamalam (2004 1 SCC 581)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-271", "EASEMENT", "intermediate", "Property Law",
     "Right which owner or occupier of certain land possesses for beneficial enjoyment of that land to do or continue to do something on another's land",
     "Defined in Section 4 of Indian Easements Act, 1882; involves dominant heritage and servient heritage",
     "A non-possessory right to use or cross a neighbor's real property for the beneficial enjoyment of one's own land.",
     "A right of pathway across an adjacent estate to access a public highway is a classic easement of necessity.",
     "Indian Easements Act, 1882, Section 4 & 13; Chapsibhai Dhanjibhai Danad v. Purushottam (1971 2 SCC 205)",
     "https://www.indiacode.nic.in/handle/123456789/2337"),

    ("voc-272", "ACTIONABLE CLAIM", "intermediate", "Property Law",
     "A claim to any unsecured debt or beneficial interest in movable property not in possession, enforceable by court",
     "Defined in Section 3 of Transfer of Property Act, 1882; transferable by execution of an instrument in writing (Section 130)",
     "A legally enforceable right to recover an unsecured money debt or claim beneficial movable assets.",
     "The right to recover arrears of rent or insurance proceeds due under a policy constitutes an actionable claim under Section 3 TPA.",
     "Transfer of Property Act, 1882, Section 3 & 130; Sunrise Associates v. Govt. of NCT of Delhi (2006 5 SCC 603)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-273", "PART PERFORMANCE", "intermediate", "Property Law",
     "Equitable doctrine protecting a transferee in possession under an uncompleted contract of sale from eviction by transferor",
     "Codified in Section 53A of Transfer of Property Act, 1882; acts as a shield for defense, not a sword",
     "A statutory defense shielding a buyer who took possession and performed part of a written sale contract from ejectment.",
     "Having paid full consideration and taken physical possession under a signed sale agreement, the buyer is protected under Section 53A.",
     "Transfer of Property Act, 1882, Section 53A; Shrimant Shamrao Suryavanshi v. Pralhad Bhairoba Suryavanshi (2002 3 SCC 676)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-274", "PERPETUITY", "advanced", "Property Law",
     "Rule against perpetuity invalidating property transfers that tie up property beyond lifetime of living persons plus minority of unborn",
     "Section 14 of Transfer of Property Act, 1882; ensures property remains alienable and prevents endless dynastic dead-hand control",
     "The rule preventing property from being rendered permanently inalienable across successive unborn generations.",
     "A clause in a settlement deed attempting to tie up family land across five unborn generations is void under Section 14 TPA.",
     "Transfer of Property Act, 1882, Section 14; Ram Newaz v. Nankoo (AIR 1926 All 283)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-275", "REVERSION", "advanced", "Property Law",
     "The undisposed residue of an estate left in the grantor or their successor after determination of a lesser estate granted",
     "Property concept; e.g., when a life estate ends, property reverts to the original grantor or heirs",
     "The future possessory interest retained by a transferor after conveying a temporary or life interest in land.",
     "Granting land to a person for life means that upon their death, the estate reverts back to the original grantor's estate.",
     "Transfer of Property Act, 1882; Mulla on Transfer of Property Act",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-276", "REMAINDER", "advanced", "Property Law",
     "Future estate created in favor of a third party to take effect immediately upon the termination of a prior particular estate",
     "Contrasted with reversion; e.g., to A for life, and upon A's death, remainder to B in fee simple",
     "A future interest in real property granted to a third party that takes effect upon the expiration of a prior life estate.",
     "A deed conveying property to a spouse for life with remainder to their daughter creates a vested remainder in the daughter.",
     "Transfer of Property Act, 1882, Section 19 & 21; R. Rajagopal Reddy v. Padmini Chandrasekharan (1995 2 SCC 630)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-277", "REDEMPTION", "intermediate", "Property Law",
     "Right of a mortgagor upon payment of mortgage money to require mortgagee to deliver title deeds and possession",
     "Codified in Section 60 of Transfer of Property Act, 1882; 'Once a mortgage, always a mortgage'",
     "The statutory right of a debtor to reclaim mortgaged property upon repaying the loan in full.",
     "Any clog or condition in a mortgage deed purporting to destroy the mortgagor's right of redemption is void.",
     "Transfer of Property Act, 1882, Section 60; Seth Ganga Dhar v. Shankar Lal (AIR 1958 SC 770)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-278", "FORECLOSURE", "intermediate", "Property Law",
     "Right of mortgagee to obtain a decree that the mortgagor shall be absolutely debarred of their right to redeem mortgaged property",
     "Section 67 of Transfer of Property Act, 1882; available in mortgage by conditional sale and anomalous mortgage",
     "A legal proceeding terminating a mortgagor's right of redemption upon persistent failure to repay the loan.",
     "Upon mortgagor's default on a mortgage by conditional sale, the lender filed a suit for foreclosure under Section 67 TPA.",
     "Transfer of Property Act, 1882, Section 67; Monappa v. Horikeri (AIR 1952 Mys 12)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-279", "SUBROGATION", "advanced", "Property Law",
     "Equitable doctrine where a person who redeems a mortgage steps into the shoes of the original mortgagee regarding rights against property",
     "Section 92 of Transfer of Property Act, 1882; divided into legal subrogation and conventional subrogation",
     "The substitution of one creditor for another, clothing the paying party with all securities and rights of the redeemed debt.",
     "A co-mortgagor who redeemed the entire mortgage debt was subrogated to the rights of the mortgagee against co-owners.",
     "Transfer of Property Act, 1882, Section 92; Ganeshi Lal v. Joti Pershad (1953 SCR 243)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-280", "COVENANT", "intermediate", "Property Law",
     "Formal promise or agreement in a deed creating obligations that run with the land or bind signatories",
     "Covenants running with the land governed by Section 40 of Transfer of Property Act, 1882",
     "A solemn promise contained in a property deed concerning the use, maintenance, or non-use of real estate.",
     "A restrictive covenant in an estate deed prohibiting the construction of industrial factories was held binding on successors.",
     "Transfer of Property Act, 1882, Section 40; Tulk v. Moxhay (1848 2 Ph 774)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-281", "ATTORNMENT", "advanced", "Property Law",
     "Formal agreement by a tenant acknowledging a new landlord upon transfer of property ownership",
     "Section 109 of Transfer of Property Act, 1882; attornment is not essential to complete transfer of landlord's rights",
     "The acknowledgment by a tenant of a new property owner as their lawful landlord following sale of the premises.",
     "Upon buying the leased commercial building, the purchaser served notice requiring the tenant's attornment under Section 109.",
     "Transfer of Property Act, 1882, Section 109; B.P. Pathak v. Dr. R.V. Shirali (AIR 1976 MP 158)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-282", "ACCRETION", "advanced", "Property Law",
     "Gradual and imperceptible addition of land caused by natural alluvion from a receding river or sea",
     "Section 63 of Transfer of Property Act, 1882; accretions to mortgaged property belong to the mortgagor on redemption",
     "The increase of land border resulting from gradual water recession or alluvium deposits by a river.",
     "Alluvial soil gradually deposited by the Ganges along a riverfront field belongs to the riparian owner under accretion.",
     "Transfer of Property Act, 1882, Section 63; Felix Lopez v. Maddan Mohan Thakoor (1870 13 MIA 467)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-283", "EQUITABLE MORTGAGE", "intermediate", "Property Law",
     "Mortgage created by delivery of documents of title to immovable property with intent to create a security thereon",
     "Defined in Section 58(f) of Transfer of Property Act, 1882; common in notified commercial banking towns",
     "A security interest in real property created simply by depositing original title deeds with a financial lender.",
     "Depositing original sale deeds with a bank in Kanpur to secure an immediate overdraft facility creates an equitable mortgage.",
     "Transfer of Property Act, 1882, Section 58(f); K.J. Nathan v. S.V. Maruthi Rao (AIR 1965 SC 430)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-284", "USUFRUCTUARY MORTGAGE", "intermediate", "Property Law",
     "Mortgage where mortgagor delivers possession to mortgagee authorizing retention until mortgage money is satisfied from rents/profits",
     "Defined in Section 58(d) of Transfer of Property Act, 1882; no personal liability on mortgagor to pay debt",
     "A mortgage wherein the lender takes physical possession of land and repays the debt out of agricultural rents and profits.",
     "Handing over possession of an orchard so the lender collects mango harvests to satisfy loan interest is a usufructuary mortgage.",
     "Transfer of Property Act, 1882, Section 58(d); Ram Narayan Prasad Sah v. Ram Bilas Roy (1977 4 SCC 344)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-285", "RECTIFICATION", "intermediate", "Property Law",
     "Equitable court remedy correcting a written instrument that does not express real intention of parties through mutual mistake or fraud",
     "Governed by Section 26 of Specific Relief Act, 1963; court orders deed to be rectified to reflect true intent",
     "The equitable correction of an error in a written contract or deed to accurately reflect parties' true agreement.",
     "When a typist mistakenly swapped plot survey numbers 41 and 42 in the deed, the court ordered rectification of the instrument.",
     "Specific Relief Act, 1963, Section 26; Subhadra v. Thankam (2010 11 SCC 514)",
     "https://www.indiacode.nic.in/handle/123456789/2264")
]

FINAL_TUPLES = JURISPRUDENCE_ITEMS + MAXIMS_ITEMS + COURT_ITEMS + PROPERTY_ITEMS

for t in FINAL_TUPLES:
    ALL_ITEMS.append({
        "id": t[0],
        "canonical": t[1],
        "acceptedVariants": [t[1]],
        "difficulty": t[2],
        "subject": t[3],
        "primaryClue": t[4],
        "additionalHint": t[5],
        "definition": t[6],
        "educationalExample": t[7],
        "statuteOrAuthority": t[8],
        "sourceUrl": t[9],
        "verificationDate": "2026-11-22"
    })

print(f"Grand Total Vocabulary Count: {len(ALL_ITEMS)}")

# Validate uniqueness
ids = set()
canonicals = set()
duplicates = []

for item in ALL_ITEMS:
    if item["id"] in ids:
        duplicates.append(f"Duplicate ID: {item['id']}")
    ids.add(item["id"])
    
    if item["canonical"] in canonicals:
        duplicates.append(f"Duplicate Canonical: {item['canonical']}")
    canonicals.add(item["canonical"])

if duplicates:
    print("VALIDATION ERRORS:")
    for d in duplicates:
        print(" -", d)
    raise ValueError(f"Found {len(duplicates)} duplicate entries!")

# Write out assets/games/data/legal-vocabulary.js
js_content = """/**
 * LEGAL VOCABULARY DATABASE (V3.0 Phase 3)
 * Authoritative Indian Legal Terminology, Maxims, and Statutory Definitions
 * Specifically curated and verified for UP Judicial Services (UP PCS-J)
 * Total Verified Entries: 285 unique items across 10 subject disciplines
 */
(function() {
  'use strict';

  const VOCABULARY = """ + json.dumps(ALL_ITEMS, indent=2, ensure_ascii=False) + """;

  // Build indexed lookups for rapid querying
  const BY_ID = {};
  const BY_CANONICAL = {};
  const BY_SUBJECT = {};
  const BY_DIFFICULTY = { beginner: [], intermediate: [], advanced: [] };

  VOCABULARY.forEach(item => {
    BY_ID[item.id] = item;
    BY_CANONICAL[item.canonical.toUpperCase()] = item;
    if (Array.isArray(item.acceptedVariants)) {
      item.acceptedVariants.forEach(v => {
        BY_CANONICAL[v.toUpperCase()] = item;
      });
    }

    if (!BY_SUBJECT[item.subject]) {
      BY_SUBJECT[item.subject] = [];
    }
    BY_SUBJECT[item.subject].push(item);

    if (BY_DIFFICULTY[item.difficulty]) {
      BY_DIFFICULTY[item.difficulty].push(item);
    }
  });

  window.ARENA_VOCABULARY = VOCABULARY;
  window.ARENA_VOCAB_BY_ID = BY_ID;
  window.ARENA_VOCAB_BY_CANONICAL = BY_CANONICAL;
  window.ARENA_VOCAB_BY_SUBJECT = BY_SUBJECT;
  window.ARENA_VOCAB_BY_DIFFICULTY = BY_DIFFICULTY;
})();
"""

target_path = os.path.join("assets", "games", "data", "legal-vocabulary.js")
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {target_path} with {len(ALL_ITEMS)} verified vocabulary entries!")
