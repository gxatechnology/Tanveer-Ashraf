const fs = require('fs');
const path = require('path');

global.window = global;
require(path.join(__dirname, '../assets/data/questions.js'));
const allQ = global.PCSJ_QUESTIONS;

// Load topics
require(path.join(__dirname, '../assets/learning/data/criminal/criminal-topics.js'));
require(path.join(__dirname, '../assets/learning/data/crpc/crpc-topics.js'));
require(path.join(__dirname, '../assets/learning/data/evidence/evidence-topics.js'));

// -----------------------------------------------------------------------------
// 1. CRIMINAL LAW (Penal Law) MAPPINGS (78 PYQs)
// -----------------------------------------------------------------------------
const penalQ = allQ.filter(q => q.topic === 'Penal Law');
console.log('Penal Law PYQs found:', penalQ.length);

const penalMappings = penalQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-crim-01';
  let topId = 'top-crim-01-01';
  let rat = 'General principles and application of penal law';

  if (text.includes('jurisdiction') || text.includes('extra-territorial') || text.includes('territorial') || text.includes('high seas')) {
    chId = 'ch-crim-01'; topId = 'top-crim-01-01'; rat = 'Territorial and extra-territorial jurisdiction under Section 1-4 IPC / S. 1 BNS';
  } else if (text.includes('movable property') || text.includes('document') || text.includes('dishonestly') || text.includes('fraudulently') || text.includes('public servant') || text.includes('valuable security')) {
    chId = 'ch-crim-01'; topId = 'top-crim-01-02'; rat = 'Statutory definitions under Section 2 BNS / Sections 6-52A IPC';
  } else if (text.includes('mens rea') || text.includes('actus reus') || text.includes('strict liability') || text.includes('actus non facit')) {
    chId = 'ch-crim-01'; topId = 'top-crim-01-03'; rat = 'Actus Reus, Mens Rea, and Strict Liability in criminal law';
  } else if (text.includes('punishment') || text.includes('death penalty') || text.includes('life imprisonment') || text.includes('solitary') || text.includes('community service') || text.includes('fine')) {
    chId = 'ch-crim-02'; topId = 'top-crim-02-01'; rat = 'Sentencing framework and types of punishments under S. 4 BNS / S. 53 IPC';
  } else if (text.includes('mistake') || text.includes('ignorantia') || text.includes('76') || text.includes('79') || text.includes('judicial act')) {
    chId = 'ch-crim-03'; topId = 'top-crim-03-01'; rat = 'Mistake of fact versus mistake of law and judicial immunity';
  } else if (text.includes('insan') || text.includes('unsound') || text.includes('m\'naghten') || text.includes('84') || text.includes('child') || text.includes('infan') || text.includes('doli') || text.includes('82') || text.includes('83')) {
    chId = 'ch-crim-03'; topId = 'top-crim-03-02'; rat = 'Infancy (Doli incapax) and insanity defense (M\'Naghten rules)';
  } else if (text.includes('intoxicat') || text.includes('drunk') || text.includes('basdev') || text.includes('85') || text.includes('86')) {
    chId = 'ch-crim-03'; topId = 'top-crim-03-03'; rat = 'Involuntary vs voluntary intoxication under S. 23-24 BNS / S. 85-86 IPC';
  } else if (text.includes('consent') || text.includes('de minimis') || text.includes('95') || text.includes('good faith') || text.includes('harm') || text.includes('87') || text.includes('88') || text.includes('89')) {
    chId = 'ch-crim-03'; topId = 'top-crim-03-04'; rat = 'Consent, good faith medical acts, and trivial acts under General Exceptions';
  } else if (text.includes('private defence') || text.includes('self defence') || text.includes('96') || text.includes('97') || text.includes('99')) {
    if (text.includes('property') || text.includes('103') || text.includes('104') || text.includes('105')) {
      chId = 'ch-crim-04'; topId = 'top-crim-04-03'; rat = 'Right of private defence of property and causing death';
    } else if (text.includes('body') || text.includes('100') || text.includes('101') || text.includes('102') || text.includes('acid') || text.includes('rape')) {
      chId = 'ch-crim-04'; topId = 'top-crim-04-02'; rat = 'Right of private defence of body and when it extends to causing death';
    } else {
      chId = 'ch-crim-04'; topId = 'top-crim-04-01'; rat = 'Nature, scope, and statutory limitations of right of private defence';
    }
  } else if (text.includes('common intention') || text.includes('section 34') || text.includes('joint liability') || text.includes('barendra') || text.includes('mehboob') || text.includes('common object') || text.includes('149')) {
    chId = 'ch-crim-05'; topId = 'top-crim-05-01'; rat = 'Common intention (S. 3(5) BNS / S. 34 IPC) vs common object (S. 190 BNS / S. 149 IPC)';
  } else if (text.includes('abet') || text.includes('instigat') || text.includes('aid') || text.includes('107') || text.includes('108') || text.includes('109')) {
    chId = 'ch-crim-05'; topId = 'top-crim-05-02'; rat = 'Abetment by instigation, conspiracy, and intentional aiding';
  } else if (text.includes('conspiracy') || text.includes('120a') || text.includes('120b')) {
    chId = 'ch-crim-05'; topId = 'top-crim-05-03'; rat = 'Criminal conspiracy agreement and proof under S. 61 BNS / S. 120A IPC';
  } else if (text.includes('attempt') || text.includes('511') || text.includes('preparation')) {
    chId = 'ch-crim-05'; topId = 'top-crim-05-04'; rat = 'Criminal attempt, proximity test, and incomplete offences';
  } else if (text.includes('culpable homicide') || text.includes('299') || text.includes('300') || text.includes('murder') || text.includes('govinda') || text.includes('virsa singh')) {
    if (text.includes('provocation') || text.includes('exception') || text.includes('sudden fight') || text.includes('nanavati')) {
      chId = 'ch-crim-06'; topId = 'top-crim-06-02'; rat = 'The Five Exceptions to Murder and grave and sudden provocation';
    } else {
      chId = 'ch-crim-06'; topId = 'top-crim-06-01'; rat = 'Distinction between Culpable Homicide and Murder (Reg v. Govinda)';
    }
  } else if (text.includes('negligen') || text.includes('rash') || text.includes('304a') || text.includes('hit and run') || text.includes('106')) {
    chId = 'ch-crim-06'; topId = 'top-crim-06-03'; rat = 'Causing death by rash and negligent act and S. 106 BNS framework';
  } else if (text.includes('dowry death') || text.includes('304b') || text.includes('suicide') || text.includes('306') || text.includes('lynch')) {
    chId = 'ch-crim-06'; topId = 'top-crim-06-04'; rat = 'Dowry death (S. 80 BNS / S. 304B IPC) and abetment of suicide';
  } else if (text.includes('hurt') || text.includes('grievous') || text.includes('319') || text.includes('320') || text.includes('acid') || text.includes('emasculation')) {
    chId = 'ch-crim-07'; topId = 'top-crim-07-01'; rat = 'Hurt and the eight statutory clauses of Grievous Hurt (S. 116 BNS / S. 320 IPC)';
  } else if (text.includes('restraint') || text.includes('confinement') || text.includes('339') || text.includes('340')) {
    chId = 'ch-crim-07'; topId = 'top-crim-07-02'; rat = 'Wrongful restraint versus wrongful confinement';
  } else if (text.includes('kidnap') || text.includes('abduct') || text.includes('359') || text.includes('361') || text.includes('362') || text.includes('traffick')) {
    chId = 'ch-crim-07'; topId = 'top-crim-07-03'; rat = 'Kidnapping versus abduction and age thresholds';
  } else if (text.includes('rape') || text.includes('375') || text.includes('376') || text.includes('consent') || text.includes('sexual')) {
    chId = 'ch-crim-08'; topId = 'top-crim-08-01'; rat = 'Rape definition, statutory consent, and aggravated penalties';
  } else if (text.includes('modesty') || text.includes('354') || text.includes('voyeur') || text.includes('stalk') || text.includes('harass')) {
    chId = 'ch-crim-08'; topId = 'top-crim-08-02'; rat = 'Assault on woman, outraging modesty, voyeurism, and stalking';
  } else if (text.includes('cruelty') || text.includes('498a') || text.includes('husband') || text.includes('marriage') || text.includes('bigamy') || text.includes('494')) {
    chId = 'ch-crim-08'; topId = 'top-crim-08-03'; rat = 'Cruelty by husband/relatives (S. 85-86 BNS / S. 498A IPC) and marriage offences';
  } else if (text.includes('theft') || text.includes('378') || text.includes('379') || text.includes('extortion') || text.includes('383') || text.includes('robbery') || text.includes('390') || text.includes('dacoity') || text.includes('391')) {
    chId = 'ch-crim-09'; topId = 'top-crim-09-01'; rat = 'Gradation spectrum of theft, extortion, robbery, and dacoity';
  } else if (text.includes('misappropriation') || text.includes('403') || text.includes('breach of trust') || text.includes('405') || text.includes('406') || text.includes('409')) {
    chId = 'ch-crim-09'; topId = 'top-crim-09-02'; rat = 'Dishonest misappropriation of property and criminal breach of trust';
  } else if (text.includes('cheat') || text.includes('415') || text.includes('420') || text.includes('mischief') || text.includes('425') || text.includes('trespass') || text.includes('441') || text.includes('house-breaking')) {
    chId = 'ch-crim-09'; topId = 'top-crim-09-03'; rat = 'Cheating, mischief, criminal trespass, and house-breaking';
  } else if (text.includes('sedition') || text.includes('124a') || text.includes('sovereignty') || text.includes('152') || text.includes('war against') || text.includes('121')) {
    chId = 'ch-crim-10'; topId = 'top-crim-10-01'; rat = 'Acts endangering sovereignty and integrity of India (S. 152 BNS)';
  } else if (text.includes('terror') || text.includes('organised crime') || text.includes('gang')) {
    chId = 'ch-crim-10'; topId = 'top-crim-10-02'; rat = 'Terrorism and organised crime provisions in BNS';
  } else if (text.includes('unlawful assembly') || text.includes('141') || text.includes('riot') || text.includes('146') || text.includes('affray') || text.includes('159')) {
    chId = 'ch-crim-10'; topId = 'top-crim-10-03'; rat = 'Unlawful assembly, rioting, and affray under penal law';
  } else if (text.includes('false evidence') || text.includes('perjury') || text.includes('191') || text.includes('192') || text.includes('193')) {
    chId = 'ch-crim-11'; topId = 'top-crim-11-01'; rat = 'Giving and fabricating false evidence and perjury';
  } else if (text.includes('forgery') || text.includes('463') || text.includes('464') || text.includes('false document') || text.includes('electronic record')) {
    chId = 'ch-crim-12'; topId = 'top-crim-12-01'; rat = 'Forgery and making false documents/electronic records';
  } else if (text.includes('defamation') || text.includes('499') || text.includes('500') || text.includes('intimidation') || text.includes('503') || text.includes('506')) {
    chId = 'ch-crim-12'; topId = 'top-crim-12-02'; rat = 'Defamation exceptions and criminal intimidation';
  }

  return {
    questionId: q.id,
    year: q.year,
    paper: q.paper,
    questionNumber: q.no,
    chapterId: chId,
    topicId: topId,
    stem: q.stem || q.text.split('\n')[0],
    answer: q.answer,
    rationale: rat
  };
});

const crimFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Law Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 78 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.CRIMINAL_PYQ_MAPPING = ${JSON.stringify(penalMappings, null, 2)};

})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
`;

fs.writeFileSync('assets/learning/data/criminal/criminal-pyq-mapping.js', crimFileContent, 'utf8');
console.log('Successfully written assets/learning/data/criminal/criminal-pyq-mapping.js (78 PYQs)');


// -----------------------------------------------------------------------------
// 2. CRIMINAL PROCEDURE MAPPINGS (49 PYQs)
// -----------------------------------------------------------------------------
const crpcQ = allQ.filter(q => q.topic === 'Criminal Procedure');
console.log('Criminal Procedure PYQs found:', crpcQ.length);

const crpcMappings = crpcQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-crpc-01';
  let topId = 'top-crpc-01-01';
  let rat = 'Hierarchy and jurisdiction of criminal courts';

  if (text.includes('court') || text.includes('hierarchy') || text.includes('separation') || text.includes('executive magistrate')) {
    chId = 'ch-crpc-01'; topId = 'top-crpc-01-01'; rat = 'Hierarchy and classes of criminal courts in BNSS & CrPC';
  } else if (text.includes('sentence') || text.includes('cjm') || text.includes('sessions judge') || text.includes('magistrate first class') || text.includes('fine')) {
    chId = 'ch-crpc-01'; topId = 'top-crpc-01-02'; rat = 'Sentencing jurisdiction and maximum fines of Magistrates';
  } else if (text.includes('prosecutor') || text.includes('public prosecutor') || text.includes('assistant') || text.includes('24') || text.includes('25')) {
    chId = 'ch-crpc-01'; topId = 'top-crpc-01-03'; rat = 'Directorate of Prosecution and appointment of Public Prosecutors';
  } else if (text.includes('arrest') || text.includes('41') || text.includes('41a') || text.includes('without warrant') || text.includes('arnesh')) {
    chId = 'ch-crpc-02'; topId = 'top-crpc-02-01'; rat = 'Arrest without warrant and notice of appearance under S. 35 BNSS';
  } else if (text.includes('handcuff') || text.includes('search of arrested') || text.includes('medical exam') || text.includes('53') || text.includes('54')) {
    chId = 'ch-crpc-02'; topId = 'top-crpc-02-02'; rat = 'Arrest procedure, medical examination, and handcuff regulations';
  } else if (text.includes('24 hours') || text.includes('57') || text.includes('rights of arrested') || text.includes('basu') || text.includes('grounds of arrest')) {
    chId = 'ch-crpc-02'; topId = 'top-crpc-02-03'; rat = 'Rights of arrested persons and mandatory 24-hour production rule';
  } else if (text.includes('summons') || text.includes('warrant of arrest') || text.includes('service') || text.includes('61') || text.includes('70')) {
    chId = 'ch-crpc-03'; topId = 'top-crpc-03-01'; rat = 'Processes to compel appearance: summons and warrants';
  } else if (text.includes('proclamation') || text.includes('attachment') || text.includes('82') || text.includes('83') || text.includes('abscond')) {
    chId = 'ch-crpc-03'; topId = 'top-crpc-03-02'; rat = 'Proclamation and attachment of property for absconders';
  } else if (text.includes('search warrant') || text.includes('production') || text.includes('91') || text.includes('93') || text.includes('impound')) {
    chId = 'ch-crpc-03'; topId = 'top-crpc-03-03'; rat = 'Search warrants and summons to produce documents';
  } else if (text.includes('security') || text.includes('peace') || text.includes('good behaviour') || text.includes('106') || text.includes('107') || text.includes('110')) {
    chId = 'ch-crpc-04'; topId = 'top-crpc-04-01'; rat = 'Security for keeping peace and good behaviour proceedings';
  } else if (text.includes('unlawful assembly') || text.includes('129') || text.includes('144') || text.includes('urgent') || text.includes('nuisance')) {
    chId = 'ch-crpc-04'; topId = 'top-crpc-04-02'; rat = 'Maintenance of public order and urgent injunctions under S. 144 CrPC / S. 163 BNSS';
  } else if (text.includes('immovable property') || text.includes('possession') || text.includes('145') || text.includes('146') || text.includes('dispute')) {
    chId = 'ch-crpc-04'; topId = 'top-crpc-04-03'; rat = 'Disputes as to immovable property and possession inquiries under S. 145 CrPC';
  } else if (text.includes('maintenance') || text.includes('125') || text.includes('wife') || text.includes('child') || text.includes('parents') || text.includes('shah bano')) {
    chId = 'ch-crpc-05'; topId = 'top-crpc-05-01'; rat = 'Maintenance of wives, children, and parents under S. 144 BNSS / S. 125 CrPC';
  } else if (text.includes('fir') || text.includes('154') || text.includes('first information') || text.includes('zero fir') || text.includes('lalita kumari')) {
    chId = 'ch-crpc-06'; topId = 'top-crpc-06-01'; rat = 'First Information Report (FIR), Zero FIR, and preliminary inquiries';
  } else if (text.includes('witness') || text.includes('161') || text.includes('162') || text.includes('investigation') || text.includes('police officer')) {
    chId = 'ch-crpc-06'; topId = 'top-crpc-06-02'; rat = 'Police powers of investigation and witness examination under S. 161 CrPC';
  } else if (text.includes('confession') || text.includes('164') || text.includes('recording') || text.includes('magistrate statement')) {
    chId = 'ch-crpc-06'; topId = 'top-crpc-06-03'; rat = 'Recording of confessions and statements by Magistrate under S. 164 CrPC / S. 183 BNSS';
  } else if (text.includes('remand') || text.includes('167') || text.includes('custody') || text.includes('default bail') || text.includes('187')) {
    chId = 'ch-crpc-07'; topId = 'top-crpc-07-01'; rat = 'Remand, police custody in parts, and default bail rights';
  } else if (text.includes('inquest') || text.includes('174') || text.includes('charge-sheet') || text.includes('final report') || text.includes('173')) {
    chId = 'ch-crpc-07'; topId = 'top-crpc-07-02'; rat = 'Inquest reports and police final report (charge-sheet) under S. 173 CrPC';
  } else if (text.includes('cognizance') || text.includes('190') || text.includes('sanction') || text.includes('197') || text.includes('jurisdiction') || text.includes('177')) {
    chId = 'ch-crpc-08'; topId = 'top-crpc-08-02'; rat = 'Cognizance of offences by Magistrates and statutory sanctions';
  } else if (text.includes('complaint') || text.includes('200') || text.includes('202') || text.includes('204') || text.includes('issue of process')) {
    chId = 'ch-crpc-08'; topId = 'top-crpc-08-03'; rat = 'Complaints to Magistrates and examination of complainant';
  } else if (text.includes('charge') || text.includes('211') || text.includes('alteration') || text.includes('joinder') || text.includes('218') || text.includes('223')) {
    chId = 'ch-crpc-09'; topId = 'top-crpc-09-01'; rat = 'Form, contents, and alteration of charge and joinder rules';
  } else if (text.includes('sessions trial') || text.includes('225') || text.includes('discharge') || text.includes('227')) {
    chId = 'ch-crpc-10'; topId = 'top-crpc-10-01'; rat = 'Trial before Court of Session: opening, discharge, and framing';
  } else if (text.includes('warrant case') || text.includes('238') || text.includes('244')) {
    chId = 'ch-crpc-10'; topId = 'top-crpc-10-02'; rat = 'Trial of warrant cases by Magistrates (police vs complaint)';
  } else if (text.includes('summons case') || text.includes('251') || text.includes('summary trial') || text.includes('260')) {
    chId = 'ch-crpc-10'; topId = 'top-crpc-10-03'; rat = 'Summons trials and summary trials procedure and distinction';
  } else if (text.includes('plea bargaining') || text.includes('265a') || text.includes('absentia') || text.includes('356')) {
    chId = 'ch-crpc-10'; topId = 'top-crpc-10-04'; rat = 'Plea bargaining and trial in absentia of proclaimed offenders';
  } else if (text.includes('double jeopardy') || text.includes('300') || text.includes('autrefois') || text.includes('pardon') || text.includes('306') || text.includes('313') || text.includes('319') || text.includes('482') || text.includes('inherent')) {
    if (text.includes('482') || text.includes('inherent') || text.includes('319') || text.includes('summoning')) {
      chId = 'ch-crpc-11'; topId = 'top-crpc-11-03'; rat = 'Inherent powers of High Court (S. 482 CrPC / S. 528 BNSS) and S. 319 CrPC';
    } else {
      chId = 'ch-crpc-11'; topId = 'top-crpc-11-01'; rat = 'General trial provisions: double jeopardy and examination of accused';
    }
  } else if (text.includes('bail') || text.includes('436') || text.includes('437') || text.includes('438') || text.includes('439') || text.includes('appeal') || text.includes('revision') || text.includes('reference')) {
    if (text.includes('anticipatory') || text.includes('438')) {
      chId = 'ch-crpc-12'; topId = 'top-crpc-12-03'; rat = 'Anticipatory bail jurisprudence and conditions (S. 482 BNSS / S. 438 CrPC)';
    } else if (text.includes('undertrial') || text.includes('436a') || text.includes('479')) {
      chId = 'ch-crpc-12'; topId = 'top-crpc-12-02'; rat = 'Undertrial prisoner rights and release under S. 479 BNSS';
    } else if (text.includes('appeal') || text.includes('revision') || text.includes('reference') || text.includes('judgment')) {
      chId = 'ch-crpc-12'; topId = 'top-crpc-12-04'; rat = 'Judgments, appeals, reference, and revision powers';
    } else {
      chId = 'ch-crpc-12'; topId = 'top-crpc-12-01'; rat = 'Bailable vs non-bailable offences and general bail principles';
    }
  }

  return {
    questionId: q.id,
    year: q.year,
    paper: q.paper,
    questionNumber: q.no,
    chapterId: chId,
    topicId: topId,
    stem: q.stem || q.text.split('\n')[0],
    answer: q.answer,
    rationale: rat
  };
});

const crpcFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Procedure Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 49 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.CRPC_PYQ_MAPPING = ${JSON.stringify(crpcMappings, null, 2)};

})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
`;

fs.writeFileSync('assets/learning/data/crpc/crpc-pyq-mapping.js', crpcFileContent, 'utf8');
console.log('Successfully written assets/learning/data/crpc/crpc-pyq-mapping.js (49 PYQs)');


// -----------------------------------------------------------------------------
// 3. EVIDENCE LAW MAPPINGS (73 PYQs)
// -----------------------------------------------------------------------------
const eviQ = allQ.filter(q => q.topic === 'Evidence');
console.log('Evidence PYQs found:', eviQ.length);

const eviMappings = eviQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-evi-01';
  let topId = 'top-evi-01-01';
  let rat = 'Cardinal definitions and standard of proof in evidence law';

  if (text.includes('court') || text.includes('fact in issue') || text.includes('affidavit') || text.includes('arbitrat') || text.includes('extent')) {
    chId = 'ch-evi-01'; topId = 'top-evi-01-01'; rat = 'Scope of Evidence Act, Court, Fact, and Fact in Issue';
  } else if (text.includes('document') || text.includes('electronic record') || text.includes('relevant fact')) {
    chId = 'ch-evi-01'; topId = 'top-evi-01-02'; rat = 'Document and electronic records definition under BSA Section 2';
  } else if (text.includes('proved') || text.includes('disproved') || text.includes('not proved') || text.includes('may presume') || text.includes('shall presume') || text.includes('conclusive proof')) {
    chId = 'ch-evi-01'; topId = 'top-evi-01-03'; rat = 'Standards of proof and classification of statutory presumptions';
  } else if (text.includes('res gestae') || text.includes('section 6') || text.includes('same transaction') || text.includes('ratten') || text.includes('bedingfield')) {
    chId = 'ch-evi-02'; topId = 'top-evi-02-01'; rat = 'Doctrine of Res Gestae: facts forming part of same transaction (S. 4 BSA / S. 6 IEA)';
  } else if (text.includes('occasion') || text.includes('cause') || text.includes('effect') || text.includes('opportunity') || text.includes('section 7') || text.includes('motive') || text.includes('preparation') || text.includes('conduct') || text.includes('section 8') || text.includes('abdullah')) {
    chId = 'ch-evi-02'; topId = 'top-evi-02-02'; rat = 'Occasion, cause, effect, motive, preparation, and previous/subsequent conduct';
  } else if (text.includes('identification') || text.includes('tip') || text.includes('section 9')) {
    chId = 'ch-evi-02'; topId = 'top-evi-02-03'; rat = 'Test Identification Parade (TIP) and explanatory facts under Section 9 IEA';
  } else if (text.includes('conspiracy') || text.includes('section 10') || text.includes('common intention') || text.includes('alibi') || text.includes('section 11')) {
    chId = 'ch-evi-02'; topId = 'top-evi-02-04'; rat = 'Conspiracy evidence (S. 10 IEA) and plea of alibi (S. 11 IEA)';
  } else if (text.includes('admission') || text.includes('section 17') || text.includes('section 18') || text.includes('section 21')) {
    chId = 'ch-evi-03'; topId = 'top-evi-03-01'; rat = 'Admissions defined and persons qualified to make admissions';
  } else if (text.includes('inducement') || text.includes('threat') || text.includes('promise') || text.includes('section 24') || text.includes('person in authority')) {
    chId = 'ch-evi-03'; topId = 'top-evi-03-02'; rat = 'Confession caused by inducement, threat, or promise (S. 22 BSA / S. 24 IEA)';
  } else if (text.includes('police officer') || text.includes('section 25') || text.includes('section 26') || text.includes('police custody')) {
    chId = 'ch-evi-03'; topId = 'top-evi-03-03'; rat = 'Bar on confessions to police officers or in police custody';
  } else if (text.includes('section 27') || text.includes('pulukuri') || text.includes('discovery') || text.includes('so much of information') || text.includes('kottaya')) {
    chId = 'ch-evi-03'; topId = 'top-evi-03-04'; rat = 'Discovery of fact in consequence of information from accused (Pulukuri Kottaya)';
  } else if (text.includes('dying declaration') || text.includes('section 32') || text.includes('32(1)') || text.includes('cause of death') || text.includes('pakala')) {
    chId = 'ch-evi-04'; topId = 'top-evi-04-01'; rat = 'Dying declarations principles and admissibility under S. 26(a) BSA / S. 32(1) IEA';
  } else if (text.includes('business') || text.includes('against interest') || text.includes('32(2)') || text.includes('32(3)') || text.includes('section 33')) {
    chId = 'ch-evi-04'; topId = 'top-evi-04-02'; rat = 'Statements in ordinary course of business and against pecuniary interest';
  } else if (text.includes('judgment') || text.includes('section 40') || text.includes('section 41') || text.includes('res judicata') || text.includes('probate') || text.includes('matrimonial')) {
    chId = 'ch-evi-05'; topId = 'top-evi-05-01'; rat = 'Relevancy of judgments in rem and in personam';
  } else if (text.includes('expert') || text.includes('section 45') || text.includes('handwriting') || text.includes('fingerprint') || text.includes('science') || text.includes('foreign law')) {
    chId = 'ch-evi-05'; topId = 'top-evi-05-02'; rat = 'Expert opinions on science, art, handwriting, and digital evidence';
  } else if (text.includes('character') || text.includes('section 52') || text.includes('section 53') || text.includes('section 54') || text.includes('bad character')) {
    chId = 'ch-evi-05'; topId = 'top-evi-05-03'; rat = 'Character evidence in civil and criminal proceedings';
  } else if (text.includes('judicial notice') || text.includes('section 56') || text.includes('section 57') || text.includes('section 58') || text.includes('admitted')) {
    chId = 'ch-evi-06'; topId = 'top-evi-06-01'; rat = 'Facts judicially noticeable and facts admitted need not be proved';
  } else if (text.includes('oral evidence') || text.includes('direct') || text.includes('section 59') || text.includes('section 60') || text.includes('hearsay')) {
    chId = 'ch-evi-06'; topId = 'top-evi-06-02'; rat = 'Oral evidence must be direct and exclusion of hearsay evidence';
  } else if (text.includes('primary evidence') || text.includes('secondary evidence') || text.includes('section 61') || text.includes('section 62') || text.includes('section 63') || text.includes('section 65')) {
    chId = 'ch-evi-07'; topId = 'top-evi-07-01'; rat = 'Primary versus secondary documentary evidence and grounds for admissibility';
  } else if (text.includes('65b') || text.includes('electronic record') || text.includes('certificate') || text.includes('anvar') || text.includes('arjun panditrao')) {
    chId = 'ch-evi-07'; topId = 'top-evi-07-02'; rat = 'Admissibility of electronic records and mandatory certification under S. 63 BSA / S. 65B IEA';
  } else if (text.includes('public document') || text.includes('section 74') || text.includes('certified copy') || text.includes('section 76') || text.includes('30 years') || text.includes('section 90')) {
    chId = 'ch-evi-07'; topId = 'top-evi-07-03'; rat = 'Public documents, certified copies, and 30-year old document presumption';
  } else if (text.includes('section 91') || text.includes('best evidence') || text.includes('terms of contract')) {
    chId = 'ch-evi-08'; topId = 'top-evi-08-01'; rat = 'Exclusion of oral evidence of terms of contracts/grants (Best Evidence Rule)';
  } else if (text.includes('section 92') || text.includes('proviso') || text.includes('contradict') || text.includes('vary')) {
    chId = 'ch-evi-08'; topId = 'top-evi-08-02'; rat = 'Exclusion of evidence of oral agreement and the six statutory provisos';
  } else if (text.includes('burden of proof') || text.includes('section 101') || text.includes('section 102') || text.includes('onus')) {
    chId = 'ch-evi-09'; topId = 'top-evi-09-01'; rat = 'Legal burden of proof (S. 101) versus evidential onus of proof (S. 102)';
  } else if (text.includes('section 106') || text.includes('especially within knowledge') || text.includes('shambhu nath')) {
    chId = 'ch-evi-09'; topId = 'top-evi-09-01'; rat = 'Burden of proving fact especially within knowledge (S. 106 IEA / S. 109 BSA)';
  } else if (text.includes('section 112') || text.includes('legitimacy') || text.includes('access') || text.includes('280 days') || text.includes('dowry death') || text.includes('113b') || text.includes('113a')) {
    chId = 'ch-evi-09'; topId = 'top-evi-09-02'; rat = 'Conclusive proof of legitimacy (S. 112 IEA) and dowry death presumption (S. 113B IEA)';
  } else if (text.includes('section 114') || text.includes('presume existence') || text.includes('accomplice') || text.includes('114a') || text.includes('rape consent')) {
    chId = 'ch-evi-09'; topId = 'top-evi-09-03'; rat = 'Court presumptions under Section 114 IEA / Section 117 BSA and absence of consent';
  } else if (text.includes('estoppel') || text.includes('section 115') || text.includes('tenant') || text.includes('116') || text.includes('promissory')) {
    chId = 'ch-evi-10'; topId = 'top-evi-10-01'; rat = 'Doctrine of Estoppel (S. 115 IEA / S. 121 BSA) and tenant estoppel';
  } else if (text.includes('competent') || text.includes('section 118') || text.includes('dumb') || text.includes('119') || text.includes('privilege') || text.includes('122') || text.includes('126')) {
    chId = 'ch-evi-10'; topId = 'top-evi-10-02'; rat = 'Witness competency, dumb witnesses, and professional privileged communications';
  } else if (text.includes('examination') || text.includes('cross') || text.includes('chief') || text.includes('leading question') || text.includes('141') || text.includes('142') || text.includes('143')) {
    chId = 'ch-evi-10'; topId = 'top-evi-10-03'; rat = 'Stages of witness examination and permissible leading questions';
  } else if (text.includes('hostile') || text.includes('section 154') || text.includes('impeach') || text.includes('155') || text.includes('refresh') || text.includes('159')) {
    chId = 'ch-evi-10'; topId = 'top-evi-10-04'; rat = 'Hostile witnesses (S. 154 IEA / S. 157 BSA) and refreshing memory';
  }

  return {
    questionId: q.id,
    year: q.year,
    paper: q.paper,
    questionNumber: q.no,
    chapterId: chId,
    topicId: topId,
    stem: q.stem || q.text.split('\n')[0],
    answer: q.answer,
    rationale: rat
  };
});

const eviFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Law of Evidence Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 73 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.EVIDENCE_PYQ_MAPPING = ${JSON.stringify(eviMappings, null, 2)};

})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
`;

fs.writeFileSync('assets/learning/data/evidence/evidence-pyq-mapping.js', eviFileContent, 'utf8');
console.log('Successfully written assets/learning/data/evidence/evidence-pyq-mapping.js (73 PYQs)');
