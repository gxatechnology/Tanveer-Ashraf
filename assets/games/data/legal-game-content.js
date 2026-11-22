/**
 * LEGAL BRAIN ARENA — VERIFIED LEGAL DATASET
 * Curated specifically for UP PCS-J Examination Preparation
 * Modes: Legal Terms, Constitutional Articles, Landmark Case Laws
 */
(function() {
  'use strict';

  // Mode B: Legal Terms, Maxims and Fundamental Principles
  const LEGAL_TERMS = [
    {
      id: 'term-1',
      term: 'Res Ipsa Loquitur',
      definition: 'The thing speaks for itself',
      explanation: 'A doctrine of law that one is presumed to be negligent if he/she had exclusive control of whatever caused the injury.'
    },
    {
      id: 'term-2',
      term: 'Audi Alteram Partem',
      definition: 'Hear the other side',
      explanation: 'A fundamental principle of natural justice stating that no person should be judged unheard.'
    },
    {
      id: 'term-3',
      term: 'Nemo Judex In Causa Sua',
      definition: 'No one should be a judge in their own cause',
      explanation: 'Rule against bias in natural justice; ensures impartial adjudication without interest in the outcome.'
    },
    {
      id: 'term-4',
      term: 'Actus Non Facit Reum Nisi Mens Sit Rea',
      definition: 'The act does not make one guilty unless mind is guilty',
      explanation: 'Core maxim of criminal jurisprudence requiring both wrongful physical act (actus reus) and mental intent (mens rea).'
    },
    {
      id: 'term-5',
      term: 'Doli Incapax',
      definition: 'Incapable of committing a crime',
      explanation: 'Legal presumption of innocence by reason of age (e.g. child under seven years under BNS Section 20).'
    },
    {
      id: 'term-6',
      term: 'Volenti Non Fit Injuria',
      definition: 'To a willing person, injury is not done',
      explanation: 'General defense in tort law where a person who voluntarily consents to a known risk cannot claim damages.'
    },
    {
      id: 'term-7',
      term: 'Ubi Jus Ibi Remedium',
      definition: 'Where there is a right, there is a remedy',
      explanation: 'Fundamental premise establishing that legal rights must be backed by a corresponding remedy in court.'
    },
    {
      id: 'term-8',
      term: 'Damnum Sine Injuria',
      definition: 'Damage without legal injury',
      explanation: 'Actual monetary or physical loss suffered without infringement of an actionable legal right (e.g. Gloucester Grammar School case).'
    },
    {
      id: 'term-9',
      term: 'Injuria Sine Damno',
      definition: 'Legal injury without actual damage',
      explanation: 'Infringement of an absolute legal right causing no monetary loss, yet actionable per se (e.g. Ashby v. White).'
    },
    {
      id: 'term-10',
      term: 'Res Judicata',
      definition: 'A matter already judged',
      explanation: 'Bar against re-litigating a dispute conclusively adjudicated between the same parties (Section 11, CPC).'
    },
    {
      id: 'term-11',
      term: 'Caveat Emptor',
      definition: 'Let the buyer beware',
      explanation: 'Commercial law doctrine placing duty on buyer to examine goods before purchase, subject to statutory warranties.'
    },
    {
      id: 'term-12',
      term: 'Sub Judice',
      definition: 'Under judicial consideration',
      explanation: 'A case or matter that is currently pending decision before a court of law.'
    },
    {
      id: 'term-13',
      term: 'Locus Standi',
      definition: 'Right to appear or stand in court',
      explanation: 'The legal capacity or direct standing of a person to initiate judicial proceedings.'
    },
    {
      id: 'term-14',
      term: 'Stare Decisis',
      definition: 'To stand by decided matters',
      explanation: 'The doctrine of judicial precedent under which lower courts must follow binding decisions of superior courts.'
    },
    {
      id: 'term-15',
      term: 'Nemo Debet Bis Vexari',
      definition: 'No one ought to be twice vexed for the same cause',
      explanation: 'Constitutional and statutory protection against double jeopardy (Article 20(2), Constitution of India).'
    },
    {
      id: 'term-16',
      term: 'Ex Post Facto Law',
      definition: 'Retrospective criminal law',
      explanation: 'A law that penalizes an act committed prior to its enactment; prohibited under Article 20(1).'
    },
    {
      id: 'term-17',
      term: 'Pacta Sunt Servanda',
      definition: 'Agreements must be kept',
      explanation: 'Fundamental rule of contract law and public international law requiring obligations to be fulfilled in good faith.'
    },
    {
      id: 'term-18',
      term: 'Quid Pro Quo',
      definition: 'Something for something',
      explanation: 'Law of contract principle denoting lawful consideration given in exchange for a promise.'
    },
    {
      id: 'term-19',
      term: 'Ignorantia Juris Non Excusat',
      definition: 'Ignorance of the law is no excuse',
      explanation: 'Presumption that every person subject to the jurisdiction knows the applicable statutes.'
    },
    {
      id: 'term-20',
      term: 'In Pari Delicto',
      definition: 'In equal fault',
      explanation: 'When both parties are equally wrongful, court will not assist the plaintiff.'
    }
  ];

  // Mode C: Constitutional Articles & Core Subjects
  const CONSTITUTION_ARTICLES = [
    {
      id: 'art-14',
      article: 'Article 14',
      subject: 'Equality Before Law & Equal Protection of Laws',
      explanation: 'Guarantees equality before law and prohibits arbitrary state classification.'
    },
    {
      id: 'art-19',
      article: 'Article 19',
      subject: 'Protection of Six Fundamental Freedoms',
      explanation: 'Protects speech, peaceful assembly, association, movement, residence, and profession subject to reasonable restrictions.'
    },
    {
      id: 'art-21',
      article: 'Article 21',
      subject: 'Protection of Life and Personal Liberty',
      explanation: 'Heart of Fundamental Rights; no person deprived of life or personal liberty except by procedure established by law.'
    },
    {
      id: 'art-21a',
      article: 'Article 21A',
      subject: 'Right to Free and Compulsory Education (6–14 yrs)',
      explanation: 'Inserted by 86th Constitutional Amendment Act, 2002 as a Fundamental Right.'
    },
    {
      id: 'art-25',
      article: 'Article 25',
      subject: 'Freedom of Conscience & Profession of Religion',
      explanation: 'Guarantees individual freedom of conscience and right to freely profess, practice and propagate religion.'
    },
    {
      id: 'art-32',
      article: 'Article 32',
      subject: 'Remedies for Enforcement of Fundamental Rights',
      explanation: 'Dr. B.R. Ambedkar called this the "Heart and Soul" of the Constitution; empowers Supreme Court to issue prerogative writs.'
    },
    {
      id: 'art-44',
      article: 'Article 44',
      subject: 'Uniform Civil Code for the Citizens',
      explanation: 'Directive Principle of State Policy enjoining State to secure a UCC throughout the territory of India.'
    },
    {
      id: 'art-50',
      article: 'Article 50',
      subject: 'Separation of Judiciary from Executive',
      explanation: 'Directive Principle ensuring independent functioning of the judicial arm.'
    },
    {
      id: 'art-51a',
      article: 'Article 51A',
      subject: 'Fundamental Duties of Citizens',
      explanation: 'Inserted by 42nd Amendment 1976 on recommendations of Swaran Singh Committee; currently 11 duties.'
    },
    {
      id: 'art-124',
      article: 'Article 124',
      subject: 'Establishment and Constitution of Supreme Court',
      explanation: 'Provides for CJI, judges appointment, qualification, and removal mechanism by impeachment.'
    },
    {
      id: 'art-136',
      article: 'Article 136',
      subject: 'Special Leave to Appeal by the Supreme Court',
      explanation: 'Plenary discretionary appellate power to grant special leave against any judicial judgment or decree in India.'
    },
    {
      id: 'art-141',
      article: 'Article 141',
      subject: 'Law Declared by Supreme Court Binding on All Courts',
      explanation: 'Establishes binding doctrine of precedent across all courts within Indian territory.'
    },
    {
      id: 'art-226',
      article: 'Article 226',
      subject: 'Power of High Courts to Issue Prerogative Writs',
      explanation: 'Writ jurisdiction of High Courts for Fundamental Rights and "any other purpose" (wider than Article 32).'
    },
    {
      id: 'art-300a',
      article: 'Article 300A',
      subject: 'Persons Not to be Deprived of Property Save by Law',
      explanation: 'Right to Property shifted from Fundamental Right to Constitutional / Legal Right by 44th Amendment 1978.'
    },
    {
      id: 'art-324',
      article: 'Article 324',
      subject: 'Superintendence, Direction & Control of Elections',
      explanation: 'Vests complete election management in the independent Election Commission of India.'
    },
    {
      id: 'art-352',
      article: 'Article 352',
      subject: 'Proclamation of National Emergency',
      explanation: 'Imposed on grounds of war, external aggression or armed rebellion (44th Amendment).'
    },
    {
      id: 'art-356',
      article: 'Article 356',
      subject: 'President\'s Rule in Case of Failure of Constitutional Machinery',
      explanation: 'State Emergency invoked upon receipt of report from Governor or otherwise.'
    },
    {
      id: 'art-368',
      article: 'Article 368',
      subject: 'Power of Parliament to Amend Constitution & Procedure',
      explanation: 'Prescribes special majority amendment procedure, subject to the unamendable Basic Structure Doctrine.'
    }
  ];

  // Mode D: Landmark Judicial Precedents & Core Rulings
  const LANDMARK_CASES = [
    {
      id: 'case-1',
      caseName: 'Kesavananda Bharati v. State of Kerala (1973)',
      principle: 'Basic Structure Doctrine',
      explanation: 'Held that Parliament cannot alter the basic structure or essential framework of the Constitution under Article 368.'
    },
    {
      id: 'case-2',
      caseName: 'Maneka Gandhi v. Union of India (1978)',
      principle: 'Procedure Established by Law Must Be Just, Fair & Reasonable',
      explanation: 'Interlinked Articles 14, 19, and 21 (Golden Triangle), rejecting mechanical formalism in personal liberty.'
    },
    {
      id: 'case-3',
      caseName: 'K.S. Puttaswamy v. Union of India (2017)',
      principle: 'Fundamental Right to Privacy Under Article 21',
      explanation: 'A 9-judge bench unanimously affirmed privacy as an intrinsic component of life and personal liberty.'
    },
    {
      id: 'case-4',
      caseName: 'Navtej Singh Johar v. Union of India (2018)',
      principle: 'Decriminalization of Consensual Homosexual Acts',
      explanation: 'Read down Section 377 IPC to the extent of consensual adult intimacy, affirming constitutional morality.'
    },
    {
      id: 'case-5',
      caseName: 'Vishaka v. State of Rajasthan (1997)',
      principle: 'Guidelines Against Sexual Harassment at Workplace',
      explanation: 'Judicially formulated binding guidelines prior to the POSH Act, 2013 under Articles 14, 19, and 21.'
    },
    {
      id: 'case-6',
      caseName: 'D.K. Basu v. State of West Bengal (1997)',
      principle: 'Mandatory Safeguards and Guidelines for Arrest & Detention',
      explanation: 'Prescribed 11 mandatory guidelines to curb custodial torture and uphold human dignity.'
    },
    {
      id: 'case-7',
      caseName: 'M.C. Mehta v. Union of India (Oleum Gas Leak, 1987)',
      principle: 'Doctrine of Absolute Liability',
      explanation: 'Evolved strict absolute liability without exceptions for hazardous industries in India.'
    },
    {
      id: 'case-8',
      caseName: 'Bachan Singh v. State of Punjab (1980)',
      principle: 'Rarest of Rare Cases Doctrine for Death Penalty',
      explanation: 'Mandated balancing of aggravating and mitigating factors before sentencing to death.'
    },
    {
      id: 'case-9',
      caseName: 'Indra Sawhney v. Union of India (1992)',
      principle: '50% Rule and Creamy Layer Exclusion in Reservations',
      explanation: 'Upheld 27% OBC reservation subject to exclusion of creamy layer and general 50% quota ceiling.'
    },
    {
      id: 'case-10',
      caseName: 'Shayara Bano v. Union of India (2017)',
      principle: 'Talaq-e-Biddat (Triple Talaq) Declared Unconstitutional',
      explanation: 'Held instant triple talaq to be arbitrary and violative of Article 14.'
    },
    {
      id: 'case-11',
      caseName: 'Minerva Mills v. Union of India (1980)',
      principle: 'Balance Between Fundamental Rights & Directive Principles',
      explanation: 'Held the balance between Part III and Part IV to be an essential feature of the Basic Structure.'
    },
    {
      id: 'case-12',
      caseName: 'Hussainara Khatoon v. Home Secretary, Bihar (1979)',
      principle: 'Right to Speedy Trial as Fundamental Right',
      explanation: 'Recognized speedy justice as integral to personal liberty under Article 21 for undertrial prisoners.'
    }
  ];

  window.LEGAL_GAME_CONTENT = {
    terms: LEGAL_TERMS,
    articles: CONSTITUTION_ARTICLES,
    cases: LANDMARK_CASES
  };
})();
