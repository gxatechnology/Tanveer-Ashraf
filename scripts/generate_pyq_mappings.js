const fs = require('fs');
const path = require('path');

global.window = global;
require(path.join(__dirname, '../assets/data/questions.js'));
const allQ = global.PCSJ_QUESTIONS;

// Load topics for reference
require(path.join(__dirname, '../assets/learning/data/jurisprudence/jurisprudence-topics.js'));
require(path.join(__dirname, '../assets/learning/data/contract/contract-topics.js'));
require(path.join(__dirname, '../assets/learning/data/tpa/tpa-topics.js'));

const jurTopics = global.JURISPRUDENCE_TOPICS;
const cntTopics = global.CONTRACT_TOPICS;
const tpaTopics = global.TPA_TOPICS;

// 1. Jurisprudence Mappings
const jurQ = allQ.filter(q => q.topic === 'Jurisprudence');
console.log('Jurisprudence PYQs found:', jurQ.length);

const jurMappings = jurQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-jur-01';
  let topId = 'top-jur-01-01';
  let rat = 'Nature, definition and scope of jurisprudence';

  if (text.includes('austin') || text.includes('command') || text.includes('sovereign') || text.includes('imperative')) {
    chId = 'ch-jur-02'; topId = 'top-jur-02-01'; rat = "Austin's imperative command theory of law";
  } else if (text.includes('bentham') || text.includes('utilitarian') || text.includes('utility')) {
    chId = 'ch-jur-02'; topId = 'top-jur-02-02'; rat = "Bentham's utilitarianism and expository jurisprudence";
  } else if (text.includes('hart') || text.includes('rule of recognition') || text.includes('primary and secondary')) {
    chId = 'ch-jur-02'; topId = 'top-jur-02-03'; rat = "HLA Hart's union of primary and secondary rules";
  } else if (text.includes('kelsen') || text.includes('grundnorm') || text.includes('pure theory')) {
    chId = 'ch-jur-02'; topId = 'top-jur-02-04'; rat = "Hans Kelsen's Pure Theory of Law and Grundnorm";
  } else if (text.includes('savigny') || text.includes('volksgeist') || text.includes('historical')) {
    chId = 'ch-jur-03'; topId = 'top-jur-03-01'; rat = "Savigny's Volksgeist and historical jurisprudence";
  } else if (text.includes('henry maine') || text.includes('status to contract') || text.includes('maine')) {
    chId = 'ch-jur-03'; topId = 'top-jur-03-02'; rat = "Sir Henry Maine's legal evolution: status to contract";
  } else if (text.includes('roscoe pound') || text.includes('social engineering') || text.includes('jural postulate')) {
    chId = 'ch-jur-04'; topId = 'top-jur-04-01'; rat = "Roscoe Pound's sociological jurisprudence and social engineering";
  } else if (text.includes('ihereing') || text.includes('ihering') || text.includes('interest') || text.includes('duguit') || text.includes('social solidarity')) {
    chId = 'ch-jur-04'; topId = 'top-jur-04-02'; rat = "Sociological theory: Duguit's social solidarity and Ihering's purpose";
  } else if (text.includes('natural law') || text.includes('stammler') || text.includes('fuller') || text.includes('aquinas') || text.includes('morality') || text.includes('philosophical')) {
    chId = 'ch-jur-05'; topId = 'top-jur-05-01'; rat = "Natural Law revival, Fuller's inner morality, Stammler";
  } else if (text.includes('realist') || text.includes('holmes') || text.includes('frank') || text.includes('llewellyn')) {
    chId = 'ch-jur-05'; topId = 'top-jur-05-02'; rat = "Legal Realism: American and Scandinavian Realist Schools";
  } else if (text.includes('precedent') || text.includes('stare decisis') || text.includes('ratio decidendi') || text.includes('obiter')) {
    chId = 'ch-jur-06'; topId = 'top-jur-06-01'; rat = "Precedent as a source of law, ratio decidendi, stare decisis";
  } else if (text.includes('custom') || text.includes('immemorial') || text.includes('opinio juris')) {
    chId = 'ch-jur-06'; topId = 'top-jur-06-02'; rat = "Custom as a source of law and essential requisites";
  } else if (text.includes('legislation') || text.includes('statute') || text.includes('codification')) {
    chId = 'ch-jur-06'; topId = 'top-jur-06-03'; rat = "Legislation: supreme and subordinate legislation";
  } else if (text.includes('right') || text.includes('duty') || text.includes('hohfeld') || text.includes('jural correlative')) {
    chId = 'ch-jur-07'; topId = 'top-jur-07-01'; rat = "Legal rights, duties, and Hohfeldian analysis";
  } else if (text.includes('ownership') || text.includes('corpus') || text.includes('animus') || text.includes('possession') || text.includes('savigny possession')) {
    if (text.includes('ownership')) {
      chId = 'ch-jur-08'; topId = 'top-jur-08-01'; rat = "Concept and characteristics of ownership";
    } else {
      chId = 'ch-jur-08'; topId = 'top-jur-08-02'; rat = "Concept of possession: corpus possessionis and animus possidendi";
    }
  } else if (text.includes('personality') || text.includes('person') || text.includes('corporate') || text.includes('unborn') || text.includes('idol') || text.includes('dead man')) {
    chId = 'ch-jur-09'; topId = 'top-jur-09-01'; rat = "Legal personality: status of unborn, dead, animals, and corporations";
  } else if (text.includes('property') || text.includes('corporeal') || text.includes('incorporeal')) {
    chId = 'ch-jur-10'; topId = 'top-jur-10-01'; rat = "Concept of legal property, corporeal and incorporeal property";
  } else if (text.includes('liability') || text.includes('strict liability') || text.includes('vicarious') || text.includes('mens rea') || text.includes('negligence') || text.includes('motive') || text.includes('intention')) {
    chId = 'ch-jur-11'; topId = 'top-jur-11-01'; rat = "Legal liability: civil and criminal liability, fault and strict liability";
  } else if (text.includes('salmond') || text.includes('holland') || text.includes('definition')) {
    chId = 'ch-jur-01'; topId = 'top-jur-01-02'; rat = "Definitions of Jurisprudence: Austin, Salmond, Holland, Ulpian";
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

const jurFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Jurisprudence Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 45 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.JURISPRUDENCE_PYQ_MAPPING = ${JSON.stringify(jurMappings, null, 2)};

})(typeof window !== 'undefined' ? window : global);
`;

fs.writeFileSync('assets/learning/data/jurisprudence/jurisprudence-pyq-mapping.js', jurFileContent, 'utf8');
console.log('Successfully written assets/learning/data/jurisprudence/jurisprudence-pyq-mapping.js');


// 2. Contract Law Mappings
const cntQ = allQ.filter(q => q.topic === 'Contract Law');
console.log('Contract Law PYQs found:', cntQ.length);

const cntMappings = cntQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-cnt-01';
  let topId = 'top-cnt-01-01';
  let rat = 'Formation of contract and essentials under Section 10';

  if (text.includes('proposal') || text.includes('offer') || text.includes('invitation to offer') || text.includes('invitation to treat') || text.includes('tender') || text.includes('general offer') || text.includes('carlill') || text.includes('harvey')) {
    chId = 'ch-cnt-01'; topId = 'top-cnt-01-02'; rat = "Proposal, essentials, offer vs invitation to treat";
  } else if (text.includes('acceptance') || text.includes('communication') || text.includes('postal') || text.includes('revocation') || text.includes('section 4') || text.includes('section 5') || text.includes('section 7') || text.includes('bhagwandas')) {
    chId = 'ch-cnt-01'; topId = 'top-cnt-01-03'; rat = "Acceptance, postal communication rule and revocation";
  } else if (text.includes('intention') || text.includes('balfour')) {
    chId = 'ch-cnt-01'; topId = 'top-cnt-01-04'; rat = "Intention to create legal relations";
  } else if (text.includes('consideration') || text.includes('privity') || text.includes('chinnaya') || text.includes('stranger') || text.includes('quid pro quo') || text.includes('section 25') || text.includes('time-barred') || text.includes('natural love')) {
    if (text.includes('privity') || text.includes('chinnaya') || text.includes('stranger')) {
      chId = 'ch-cnt-02'; topId = 'top-cnt-02-02'; rat = "Privity of contract vs privity of consideration";
    } else if (text.includes('section 25') || text.includes('without consideration') || text.includes('time-barred') || text.includes('natural love')) {
      chId = 'ch-cnt-02'; topId = 'top-cnt-02-03'; rat = "Agreements without consideration and Section 25 exceptions";
    } else {
      chId = 'ch-cnt-02'; topId = 'top-cnt-02-01'; rat = "Consideration essentials under Section 2(d)";
    }
  } else if (text.includes('minor') || text.includes('mohori') || text.includes('competent') || text.includes('capacity') || text.includes('unsound') || text.includes('lunatic') || text.includes('necessaries') || text.includes('section 68') || text.includes('section 11') || text.includes('section 12')) {
    if (text.includes('necessaries') || text.includes('section 68')) {
      chId = 'ch-cnt-03'; topId = 'top-cnt-03-03'; rat = "Necessaries supplied to incompetent persons (Section 68)";
    } else if (text.includes('unsound') || text.includes('lunatic') || text.includes('section 12')) {
      chId = 'ch-cnt-03'; topId = 'top-cnt-03-02'; rat = "Persons of unsound mind and disqualifications (Section 12)";
    } else {
      chId = 'ch-cnt-03'; topId = 'top-cnt-03-01'; rat = "Competency to contract and minor's agreement (Mohori Bibee)";
    }
  } else if (text.includes('consent') || text.includes('coercion') || text.includes('undue influence') || text.includes('fraud') || text.includes('misrepresentation') || text.includes('mistake') || text.includes('section 14') || text.includes('section 15') || text.includes('section 16') || text.includes('section 17') || text.includes('section 18') || text.includes('section 19') || text.includes('section 20') || text.includes('section 21') || text.includes('section 22')) {
    if (text.includes('coercion') || text.includes('section 15') || text.includes('suicide')) {
      chId = 'ch-cnt-04'; topId = 'top-cnt-04-02'; rat = "Coercion: statutory definition and effect (Section 15)";
    } else if (text.includes('undue influence') || text.includes('section 16') || text.includes('fiduciary') || text.includes('pardanashin')) {
      chId = 'ch-cnt-04'; topId = 'top-cnt-04-03'; rat = "Undue influence and unconscionable bargains (Section 16)";
    } else if (text.includes('fraud') || text.includes('section 17') || text.includes('silence')) {
      chId = 'ch-cnt-04'; topId = 'top-cnt-04-04'; rat = "Fraud and active concealment (Section 17)";
    } else if (text.includes('misrepresentation') || text.includes('section 18')) {
      chId = 'ch-cnt-05'; topId = 'top-cnt-05-01'; rat = "Misrepresentation types and remedies (Sections 18, 19)";
    } else if (text.includes('mistake') || text.includes('section 20') || text.includes('section 21') || text.includes('section 22')) {
      chId = 'ch-cnt-05'; topId = 'top-cnt-05-02'; rat = "Mistake of fact and law (Sections 20, 21, 22)";
    } else {
      chId = 'ch-cnt-04'; topId = 'top-cnt-04-01'; rat = "Free consent and consensus ad idem (Sections 13, 14)";
    }
  } else if (text.includes('unlawful') || text.includes('public policy') || text.includes('section 23') || text.includes('restraint of trade') || text.includes('restraint of marriage') || text.includes('wager') || text.includes('section 26') || text.includes('section 27') || text.includes('section 28') || text.includes('section 29') || text.includes('section 30')) {
    if (text.includes('restraint') || text.includes('wager') || text.includes('section 27') || text.includes('section 28') || text.includes('section 30')) {
      chId = 'ch-cnt-06'; topId = 'top-cnt-06-02'; rat = "Specific void agreements: restraint of trade, marriage, wagers";
    } else {
      chId = 'ch-cnt-06'; topId = 'top-cnt-06-01'; rat = "Unlawful consideration and public policy (Section 23)";
    }
  } else if (text.includes('contingent') || text.includes('quasi') || text.includes('unjust enrichment') || text.includes('section 31') || text.includes('section 69') || text.includes('section 70') || text.includes('section 72')) {
    if (text.includes('contingent') || text.includes('section 31')) {
      chId = 'ch-cnt-07'; topId = 'top-cnt-07-01'; rat = "Contingent contracts rules and enforcement (Sections 31–36)";
    } else {
      chId = 'ch-cnt-07'; topId = 'top-cnt-07-02'; rat = "Quasi-contracts and unjust enrichment (Sections 68–72)";
    }
  } else if (text.includes('performance') || text.includes('frustration') || text.includes('impossible') || text.includes('novation') || text.includes('remission') || text.includes('section 56') || text.includes('section 62') || text.includes('section 63')) {
    if (text.includes('frustration') || text.includes('section 56') || text.includes('satyabrata')) {
      chId = 'ch-cnt-08'; topId = 'top-cnt-08-02'; rat = "Doctrine of frustration and impossibility (Section 56)";
    } else if (text.includes('novation') || text.includes('remission') || text.includes('section 62') || text.includes('section 63')) {
      chId = 'ch-cnt-08'; topId = 'top-cnt-08-03'; rat = "Novation, rescission, and alteration (Sections 62–67)";
    } else {
      chId = 'ch-cnt-08'; topId = 'top-cnt-08-01'; rat = "Performance of contracts and reciprocal promises";
    }
  } else if (text.includes('breach') || text.includes('damages') || text.includes('penalty') || text.includes('liquidated') || text.includes('section 73') || text.includes('section 74') || text.includes('hadley')) {
    if (text.includes('liquidated') || text.includes('penalty') || text.includes('section 74')) {
      chId = 'ch-cnt-09'; topId = 'top-cnt-09-03'; rat = "Liquidated damages vs penalty (Section 74)";
    } else if (text.includes('anticipatory') || text.includes('section 39')) {
      chId = 'ch-cnt-09'; topId = 'top-cnt-09-01'; rat = "Anticipatory breach of contract (Section 39)";
    } else {
      chId = 'ch-cnt-09'; topId = 'top-cnt-09-02'; rat = "Damages for breach: rule in Hadley v Baxendale (Section 73)";
    }
  } else if (text.includes('indemnity') || text.includes('guarantee') || text.includes('surety') || text.includes('bailment') || text.includes('bailee') || text.includes('pledge') || text.includes('pawnee') || text.includes('section 124') || text.includes('section 126') || text.includes('section 148') || text.includes('section 172')) {
    if (text.includes('indemnity') || text.includes('guarantee') || text.includes('surety') || text.includes('section 124') || text.includes('section 126')) {
      chId = 'ch-cnt-10'; topId = 'top-cnt-10-01'; rat = "Contracts of indemnity and guarantee (Sections 124–147)";
    } else if (text.includes('pledge') || text.includes('pawnee') || text.includes('section 172')) {
      chId = 'ch-cnt-10'; topId = 'top-cnt-10-03'; rat = "Pledge and rights of pawnee (Sections 172–181)";
    } else {
      chId = 'ch-cnt-10'; topId = 'top-cnt-10-02'; rat = "Bailment duties and bailee's lien (Sections 148–171)";
    }
  } else if (text.includes('agent') || text.includes('agency') || text.includes('principal') || text.includes('section 182')) {
    chId = 'ch-cnt-11'; topId = 'top-cnt-11-01'; rat = "Contract of agency: creation and authority (Sections 182–238)";
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

const cntFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Law of Contract Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 82 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.CONTRACT_PYQ_MAPPING = ${JSON.stringify(cntMappings, null, 2)};

})(typeof window !== 'undefined' ? window : global);
`;

fs.writeFileSync('assets/learning/data/contract/contract-pyq-mapping.js', cntFileContent, 'utf8');
console.log('Successfully written assets/learning/data/contract/contract-pyq-mapping.js');


// 3. Property Law (TPA) Mappings
const tpaQ = allQ.filter(q => q.topic === 'Property Law');
console.log('Property Law PYQs found:', tpaQ.length);

const tpaMappings = tpaQ.map(q => {
  const text = (q.text + ' ' + (q.stem || '')).toLowerCase();
  let chId = 'ch-tpa-01';
  let topId = 'top-tpa-01-01';
  let rat = 'General principles of transfer of property inter vivos';

  if (text.includes('section 6') || text.includes('spes successionis') || text.includes('transferable') || text.includes('right to sue')) {
    chId = 'ch-tpa-01'; topId = 'top-tpa-01-02'; rat = "What may be transferred and non-transferable property (Section 6)";
  } else if (text.includes('section 7') || text.includes('section 8') || text.includes('competent') || text.includes('legal incident')) {
    chId = 'ch-tpa-01'; topId = 'top-tpa-01-03'; rat = "Competency to transfer and legal incidents (Sections 7, 8)";
  } else if (text.includes('section 10') || text.includes('restraint on alienation') || text.includes('repugnant') || text.includes('section 11')) {
    chId = 'ch-tpa-02'; topId = 'top-tpa-02-01'; rat = "Conditions restraining alienation and enjoyment (Sections 10, 11)";
  } else if (text.includes('section 13') || text.includes('unborn') || text.includes('prior interest') || text.includes('tagore')) {
    chId = 'ch-tpa-02'; topId = 'top-tpa-02-02'; rat = "Transfer for benefit of unborn person (Section 13)";
  } else if (text.includes('section 14') || text.includes('perpetuity') || text.includes('accumulation') || text.includes('section 17')) {
    chId = 'ch-tpa-02'; topId = 'top-tpa-02-03'; rat = "Rule against perpetuity and accumulation (Sections 14, 17)";
  } else if (text.includes('vested') || text.includes('contingent') || text.includes('section 19') || text.includes('section 21')) {
    chId = 'ch-tpa-03'; topId = 'top-tpa-03-01'; rat = "Vested interest vs contingent interest (Sections 19, 21)";
  } else if (text.includes('conditional transfer') || text.includes('condition precedent') || text.includes('condition subsequent') || text.includes('section 25') || text.includes('section 26') || text.includes('section 28') || text.includes('section 29')) {
    chId = 'ch-tpa-03'; topId = 'top-tpa-03-02'; rat = "Conditional transfers: precedent vs subsequent (Sections 25–34)";
  } else if (text.includes('election') || text.includes('section 35')) {
    chId = 'ch-tpa-03'; topId = 'top-tpa-03-03'; rat = "Doctrine of Election under Section 35";
  } else if (text.includes('notice') || text.includes('constructive notice') || text.includes('section 3') || text.includes('priority') || text.includes('section 48')) {
    chId = 'ch-tpa-04'; topId = 'top-tpa-04-01'; rat = "Doctrine of notice (actual and constructive) under Section 3";
  } else if (text.includes('ostensible') || text.includes('section 41') || text.includes('benami')) {
    chId = 'ch-tpa-04'; topId = 'top-tpa-04-02'; rat = "Transfer by ostensible owner under Section 41";
  } else if (text.includes('feeding the grant') || text.includes('section 43') || text.includes('estoppel')) {
    chId = 'ch-tpa-04'; topId = 'top-tpa-04-03'; rat = "Doctrine of feeding the grant by estoppel (Section 43)";
  } else if (text.includes('lis pendens') || text.includes('section 52') || text.includes('pendente lite')) {
    chId = 'ch-tpa-05'; topId = 'top-tpa-05-01'; rat = "Doctrine of Lis Pendens under Section 52";
  } else if (text.includes('fraudulent transfer') || text.includes('section 53') || text.includes('creditors')) {
    chId = 'ch-tpa-05'; topId = 'top-tpa-05-02'; rat = "Fraudulent transfer to defeat creditors under Section 53";
  } else if (text.includes('part performance') || text.includes('section 53a')) {
    chId = 'ch-tpa-05'; topId = 'top-tpa-05-03'; rat = "Doctrine of part performance under Section 53A";
  } else if (text.includes('sale') || text.includes('section 54') || text.includes('contract for sale')) {
    chId = 'ch-tpa-06'; topId = 'top-tpa-06-01'; rat = "Sale of immovable property and essentials under Section 54";
  } else if (text.includes('section 55') || text.includes('seller') || text.includes('buyer') || text.includes('covenant for title') || text.includes('unpaid vendor')) {
    chId = 'ch-tpa-06'; topId = 'top-tpa-06-02'; rat = "Rights and liabilities of buyer and seller (Section 55)";
  } else if (text.includes('exchange') || text.includes('section 118')) {
    chId = 'ch-tpa-06'; topId = 'top-tpa-06-03'; rat = "Exchange of immovable property (Sections 118–121)";
  } else if (text.includes('mortgage') || text.includes('section 58') || text.includes('usufructuary') || text.includes('simple mortgage') || text.includes('conditional sale') || text.includes('english mortgage')) {
    if (text.includes('redemption') || text.includes('section 60') || text.includes('clog')) {
      chId = 'ch-tpa-07'; topId = 'top-tpa-07-02'; rat = "Right of redemption and clog on equity of redemption (Section 60)";
    } else if (text.includes('subrogation') || text.includes('section 92') || text.includes('charge') || text.includes('section 100')) {
      chId = 'ch-tpa-07'; topId = 'top-tpa-07-03'; rat = "Subrogation (s.92) and charges (s.100)";
    } else {
      chId = 'ch-tpa-07'; topId = 'top-tpa-07-01'; rat = "Concept and 6 statutory forms of mortgage (Section 58)";
    }
  } else if (text.includes('lease') || text.includes('section 105') || text.includes('section 106') || text.includes('section 107') || text.includes('section 111') || text.includes('holding over') || text.includes('forfeiture')) {
    chId = 'ch-tpa-08'; topId = 'top-tpa-08-01'; rat = "Lease of immovable property and determination (Sections 105–117)";
  } else if (text.includes('gift') || text.includes('section 122') || text.includes('section 123') || text.includes('section 126') || text.includes('onerous')) {
    chId = 'ch-tpa-08'; topId = 'top-tpa-08-02'; rat = "Gifts: essentials, onerous gift, and revocation (Sections 122–129)";
  } else if (text.includes('actionable claim') || text.includes('section 130')) {
    chId = 'ch-tpa-08'; topId = 'top-tpa-08-03'; rat = "Transfer of actionable claims (Sections 130–137)";
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

const tpaFileContent = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Transfer of Property Act Module — Historical UP PCS-J PYQ Topic Mapping
 * Total Mapped PYQs: 47 authentic questions across 2012–2023 examinations
 * Zero modification to base questions.js; non-destructive overlay registry
 */

(function (global) {
  'use strict';

  global.TPA_PYQ_MAPPING = ${JSON.stringify(tpaMappings, null, 2)};

})(typeof window !== 'undefined' ? window : global);
`;

fs.writeFileSync('assets/learning/data/tpa/tpa-pyq-mapping.js', tpaFileContent, 'utf8');
console.log('Successfully written assets/learning/data/tpa/tpa-pyq-mapping.js');
