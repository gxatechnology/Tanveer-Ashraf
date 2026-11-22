# Tune classifications to have ~25 'depends' items across all subjects
import json
import re

# We will read the generated legal-myths.js or update the parts.
# Let's inspect which IDs can naturally be 'depends' with clear conditional statements:

depends_map = {
    # Part 1 (Constitutional Law, BNS, IPC vs BNS)
    "myth-012": { # Art 143 advisory opinion
        # already depends
    },
    "myth-011": { # Ordinance force
        "statement": "An Ordinance promulgated by the President has the same legal force and permanent duration as an Act of Parliament.",
        "classification": "depends",
        "explanation": "Under Article 123(2), an Ordinance has the same legal force as an Act while in operation, but it lacks permanent duration: it lapses 6 weeks from reassembly of Parliament, and repeated re-promulgation without placing before legislature is an unconstitutional fraud (D.C. Wadhwa / Krishna Kumar Singh).",
        "exceptions": "Valid only during Parliamentary recess and ceases after six weeks from reassembly."
    },
    "myth-025": { # Preventive detention
        "statement": "A person can be detained under preventive detention without reference to an Advisory Board.",
        "classification": "depends",
        "explanation": "Under Article 22(4), detention up to 3 months is permissible without reference to an Advisory Board. However, continued detention beyond 3 months strictly requires the confirmation of an Advisory Board.",
        "exceptions": "Permissible for initial three months only."
    },
    "myth-046": { # BNS Private defence property
        "statement": "Under the Bharatiya Nyaya Sanhita, 2023, the right of private defence of property extends to causing the death of the wrongdoer.",
        "classification": "depends",
        "explanation": "Under Section 41 BNS (old IPC 103), private defence of property extends to causing death only for robbery, house-breaking by night, mischief by fire to human dwellings, or theft/mischief/trespass causing reasonable apprehension of death or grievous hurt. For other property offences, Section 42 limits defence to causing harm short of death.",
        "exceptions": "Extends to death only for the four aggravated offences listed in Section 41 BNS."
    },
    "myth-049": { # Involuntary vs voluntary intoxication
        "statement": "The state of intoxication provides a valid general defence against criminal liability under the Bharatiya Nyaya Sanhita, 2023.",
        "classification": "depends",
        "explanation": "Under Section 23 BNS, involuntary intoxication administered without knowledge or against one's will is a complete defence. However, voluntary intoxication is governed by Section 24 BNS, where the accused is dealt with as if they had the same knowledge as an unintoxicated person.",
        "exceptions": "Defence applies exclusively to involuntary intoxication under Section 23."
    },
    "myth-054": { # Criminal conspiracy overt act
        "statement": "An agreement to commit an unlawful act constitutes criminal conspiracy without proof of any overt act.",
        "classification": "depends",
        "explanation": "Under Section 61(1) BNS (old IPC 120A), if the agreement is to commit an offence, the agreement alone constitutes the conspiracy without an overt act. However, if the agreement is to do an illegal act that is not an offence, an overt act in pursuance is an essential requirement.",
        "exceptions": "Overt act required only where the agreed act is not a penal offence."
    },
    "myth-051": { # Causing death by negligence punishment
        "statement": "Causing death by rash or negligent act is punished with imprisonment of up to five years under Section 106 of the BNS.",
        "classification": "depends",
        "explanation": "Under Section 106(1) BNS, general rash or negligent act carries up to 5 years. However, medical practitioners carry up to 2 years under 106(1) proviso, and escaping the scene without reporting (hit-and-run) carries up to 10 years under Section 106(2).",
        "exceptions": "Medical negligence is capped at 2 years; hit-and-run extends up to 10 years."
    },

    # Part 2 (BSA, IEA vs BSA, BNSS, CPC)
    "myth-125": { # Confession in custody
        "statement": "A confession made by an accused person while in police custody is inadmissible in evidence.",
        "classification": "depends",
        "explanation": "Under Section 23(1) BSA (old IEA 25/26), confessions made to a police officer or in police custody are inadmissible as a general rule. However, so much as relates distinctly to a fact discovered thereby is admissible under Section 23(2) proviso, and confessions made in the immediate presence of a Magistrate are admissible.",
        "exceptions": "Admissible to the extent of facts discovered under Section 23(2) proviso."
    },
    "myth-130": { # Secondary evidence
        "statement": "Secondary evidence of the contents of a document is admissible in a court of law.",
        "classification": "depends",
        "explanation": "Under Section 59 and 60 BSA (old IEA 64/65), documents must be proved by primary evidence as a general rule. Secondary evidence is admissible only under the specific conditions enumerated in Section 60 (e.g. original lost, destroyed, in adversary possession, or public document).",
        "exceptions": "Admissible only when conditions under Section 60 BSA are satisfied."
    },
    "myth-133": { # Oral evidence for written contracts
        "statement": "Oral evidence is admissible to prove the terms of a contract reduced to the form of a document.",
        "classification": "depends",
        "explanation": "Under Section 94 BSA (old IEA 91), oral evidence is excluded as a general rule. However, oral evidence may be given if secondary evidence is admissible under Section 60, or to prove invalidating factors like fraud, illegality, or failure of consideration under Section 95 provisos.",
        "exceptions": "Admissible where secondary evidence is permissible or under Section 95 proviso exceptions."
    },
    "myth-136": { # Leading questions
        "statement": "Leading questions can be asked to a witness during examination in court.",
        "classification": "depends",
        "explanation": "Under Section 146 BSA (old IEA 142/143), leading questions must not be asked in examination-in-chief or re-examination if objected to, unless permitted by the court. Conversely, leading questions may be asked as of right by the adverse party in cross-examination.",
        "exceptions": "Permissible in cross-examination as of right; requires court leave in examination-in-chief."
    },
    "myth-140": { # Accomplice testimony
        "statement": "The uncorroborated testimony of an accomplice is sufficient to sustain a criminal conviction.",
        "classification": "depends",
        "explanation": "Under Section 138 BSA (old IEA 133), an accomplice is a competent witness and a conviction is not illegal merely because it proceeds upon uncorroborated testimony. However, under Section 119 illustration (b) BSA (old 114(b)), the Court presumes an accomplice unworthy of credit unless corroborated in material particulars as a mandatory rule of judicial prudence.",
        "exceptions": "Legally valid under Section 138, but prudence requires corroboration under Section 119(b)."
    },
    "myth-161": { # BNSS arrest without warrant
        "statement": "A police officer can arrest an accused person without a warrant from a Magistrate.",
        "classification": "depends",
        "explanation": "Under Section 35 BNSS (old CrPC 41), a police officer can arrest without warrant in cognizable offences. For non-cognizable offences, a warrant is mandatory under Section 174(2), unless the person refuses their name and address under Section 39 BNSS.",
        "exceptions": "Permissible for cognizable offences; requires warrant for non-cognizable offences."
    },
    "myth-164": { # Bail as a matter of right
        "statement": "An accused person is entitled to be released on bail as a matter of absolute right.",
        "classification": "depends",
        "explanation": "Under Section 478 BNSS (old CrPC 436), bail is an absolute statutory right in bailable offences. In non-bailable offences, bail is discretionary under Section 480 and 483 BNSS and cannot be claimed as an absolute right.",
        "exceptions": "Absolute right in bailable offences; discretionary in non-bailable offences."
    },
    "myth-166": { # Compounding of offences
        "statement": "A criminal case can be settled and compounded between the parties.",
        "classification": "depends",
        "explanation": "Under Section 359 BNSS (old CrPC 320), offences listed in Table I can be compounded without court leave; offences in Table II require permission of the Court; offences not listed in either table are legally non-compoundable.",
        "exceptions": "Permitted only for offences enumerated in Section 359 BNSS tables."
    },
    "myth-168": { # e-FIR registration
        "statement": "An FIR can be registered through electronic communication (e-FIR).",
        "classification": "depends",
        "explanation": "Under Section 173(1) proviso BNSS, information given electronically is taken on record, but it can only be formally registered and investigated after it is signed by the informant within three days.",
        "exceptions": "Formal registration requires physical or verified signature within three days."
    },
    "myth-170": { # Undertrial bail
        "statement": "An undertrial prisoner is entitled to mandatory release on bail upon completing one-third of the maximum sentence.",
        "classification": "depends",
        "explanation": "Under Section 479(1) proviso BNSS, release after one-third period is mandatory for first-time offenders who have never been convicted before. For repeat offenders, the threshold remains one-half of the maximum period, and undertrials charged with offences punishable with death or life imprisonment are excluded entirely.",
        "exceptions": "Applies strictly to first-time offenders not facing capital or life imprisonment charges."
    },
    "myth-195": { # CPC Amendment of pleadings
        "statement": "The Court can permit a party to alter or amend their pleadings at any stage of the proceedings.",
        "classification": "depends",
        "explanation": "Under Order VI Rule 17 CPC, amendments are liberally granted before trial begins. However, under the proviso to Rule 17, no amendment is allowed after trial has commenced unless the court concludes the party could not have raised the matter earlier despite due diligence.",
        "exceptions": "Pre-trial amendments are liberally granted; post-trial amendments require proof of due diligence."
    },
    "myth-200": { # CPC Injunction
        "statement": "A civil court can grant a temporary injunction restraining a defendant during the pendency of a suit.",
        "classification": "depends",
        "explanation": "Under Order XXXIX Rules 1 and 2 CPC, the court can grant an injunction only if the plaintiff proves all three cumulative requirements: (1) prima facie case, (2) balance of convenience, and (3) irreparable injury. If any one pillar is lacking, the injunction must be refused.",
        "exceptions": "Granted only when prima facie case, balance of convenience, and irreparable injury concur."
    },
    "myth-204": { # CPC Arrest in execution
        "statement": "A money decree passed by a civil court can be executed by the arrest and detention of the judgment-debtor in civil prison.",
        "classification": "depends",
        "explanation": "Under Section 51(c) CPC, arrest in civil prison is a recognized mode of execution against male judgment-debtors who possess means to pay but refuse to do so. However, Section 56 CPC totally prohibits the arrest and detention of women in execution of a money decree.",
        "exceptions": "Permissible against males with means under Section 51; strictly prohibited for women under Section 56."
    },

    # Part 3 (Contract, TPA, Torts, Jurisprudence, Maxims)
    "myth-232": { # Contract without consideration
        "statement": "An agreement entered into without consideration is void under Indian contract law.",
        "classification": "depends",
        "explanation": "Under Section 25 ICA, an agreement without consideration is void as a general rule. However, it is valid and enforceable if it falls within the three statutory exceptions: registered natural love and affection, promise to compensate for past voluntary service, or written promise to pay a time-barred debt.",
        "exceptions": "Enforceable if falling within Section 25(1), 25(2), or 25(3) ICA."
    },
    "myth-235": { # Silence as fraud
        "statement": "Silence maintained by a contracting party regarding vital facts constitutes actionable fraud.",
        "classification": "depends",
        "explanation": "Under Section 17 Explanation ICA, mere silence as to facts likely to affect willingness to contract is not fraud as a general rule (caveat emptor). However, silence amounts to fraud where there is a legal duty to speak (fiduciary relation or insurance) or where silence is in itself equivalent to speech.",
        "exceptions": "Amounts to fraud only when a legal duty to speak exists or silence equals speech."
    },
    "myth-243": { # Frustration of contract
        "statement": "A contract becomes void when performance becomes physically or commercially impossible after formation.",
        "classification": "depends",
        "explanation": "Under Section 56 ICA, supervening physical or legal impossibility beyond the control of parties discharges the contract by frustration (Satyabrata Ghose). However, mere commercial difficulty, unexpected price increase, or strikes do not frustrate the contract (Energy Watchdog).",
        "exceptions": "Discharges contract for supervening physical/legal impossibility; commercial hardship does not frustrate."
    },
    "myth-256": { # Oral transfer of property
        "statement": "A transfer of property can be made orally without any written instrument under the Transfer of Property Act, 1882.",
        "classification": "depends",
        "explanation": "Under Section 9 TPA, oral transfer is valid in all cases in which a writing is not expressly required by law. However, written and registered instruments are mandatory for sales of immovable property valued Rs. 100+ (Sec 54), simple mortgages (Sec 58), leases for 1+ years (Sec 107), gifts of immovable property (Sec 123), and actionable claims (Sec 130).",
        "exceptions": "Permitted where writing is not expressly required; written/registered deed mandatory for major transactions."
    },
    "myth-263": { # Part performance shield
        "statement": "A person who has taken possession of immovable property under an unregistered contract for sale can protect their possession against the transferor.",
        "classification": "depends",
        "explanation": "Under Section 53A TPA, the transferee can protect their possession as a shield if there is a contract in writing signed by transferor, possession was taken in part performance, and transferee is willing to perform their contractual obligations. If any statutory condition is unfulfilled, protection is denied.",
        "exceptions": "Available strictly as a shield if all statutory requirements of Section 53A are satisfied."
    },
    "myth-276": { # Vicarious liability of employer
        "statement": "An employer is vicariously liable for torts and wrongful acts committed by their employees.",
        "classification": "depends",
        "explanation": "Under the doctrine of respondeat superior, an employer is vicariously liable for torts committed by an employee if done in the course of employment. However, the employer is not liable if the employee was acting outside their authorized duties on a frolic of their own.",
        "exceptions": "Liable only for acts committed within the authorized course of employment."
    },
    "myth-278": { # Volenti non fit injuria
        "statement": "Consent given by the plaintiff to undergo a risk provides a complete defence against an action in tort.",
        "classification": "depends",
        "explanation": "Under the maxim Volenti non fit injuria, free consent given with full knowledge of the nature and extent of the risk is a complete defence. However, consent provides no defence in rescue cases (Haynes v. Harwood), where consent was obtained through fraud or coercion, or where the act is illegal.",
        "exceptions": "Valid defence only when consent is voluntary with full knowledge; inapplicable in rescue cases."
    }
}

# Apply to legal-myths.js
import os
myths_path = os.path.join("assets", "games", "data", "legal-myths.js")
with open(myths_path, "r", encoding="utf-8") as f:
    text = f.read()

# Load json items from file
# The file has: const ARENA_MYTHS = [...];
match = re.search(r'const ARENA_MYTHS = (\[.*?\]);\s*const ARENA_MYTHS_BY_ID', text, re.DOTALL)
if not match:
    print("Could not find ARENA_MYTHS array in legal-myths.js")
    exit(1)

items = json.loads(match.group(1))
print(f"Loaded {len(items)} items from legal-myths.js")

updated_count = 0
for it in items:
    mid = it["id"]
    if mid in depends_map and depends_map[mid]:
        patch = depends_map[mid]
        if "statement" in patch:
            it["statement"] = patch["statement"]
        it["classification"] = "depends"
        if "explanation" in patch:
            it["explanation"] = patch["explanation"]
        if "exceptions" in patch:
            it["exceptions"] = patch["exceptions"]
        it["errorPhrase"] = None
        it["correction"] = None
        updated_count += 1

print(f"Updated {updated_count} items to 'depends'.")

# Re-compile
by_id = {item["id"]: item for item in items}
by_subject = {}
for item in items:
    by_subject.setdefault(item["subject"], []).append(item["id"])

subjects = {}
classifications = {}
for item in items:
    s = item["subject"]
    subjects[s] = subjects.get(s, 0) + 1
    c = item["classification"]
    classifications[c] = classifications.get(c, 0) + 1

print("New Classifications:", classifications)

subject_list = sorted(list(subjects.keys()))

# Get existing modes list
modes_match = re.search(r'const ARENA_MYTHS_MODES = (\[.*?\]);\s*// Expose to global window', text, re.DOTALL)
modes_list = json.loads(modes_match.group(1))

new_js = f"""/**
 * Tanveer Ashraf Judicial Prep - Game 7: Legal Myth Buster Database
 * Version 3.0 Phase 4 - Chamber of Truth
 * Total Verified Legal Statements: {len(items)}
 * Verification Date: 2026-11-22
 * Author: Tauqeer Ashraf
 */

(function() {{
  'use strict';

  const ARENA_MYTHS = {json.dumps(items, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_BY_ID = {json.dumps(by_id, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_BY_SUBJECT = {json.dumps(by_subject, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_SUBJECTS = {json.dumps(subject_list, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_MODES = {json.dumps(modes_list, indent=2, ensure_ascii=False)};

  // Expose to global window
  if (typeof window !== 'undefined') {{
    window.ARENA_MYTHS = ARENA_MYTHS;
    window.ARENA_MYTHS_BY_ID = ARENA_MYTHS_BY_ID;
    window.ARENA_MYTHS_BY_SUBJECT = ARENA_MYTHS_BY_SUBJECT;
    window.ARENA_MYTHS_SUBJECTS = ARENA_MYTHS_SUBJECTS;
    window.ARENA_MYTHS_MODES = ARENA_MYTHS_MODES;
  }}

  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = {{
      ARENA_MYTHS,
      ARENA_MYTHS_BY_ID,
      ARENA_MYTHS_BY_SUBJECT,
      ARENA_MYTHS_SUBJECTS,
      ARENA_MYTHS_MODES
    }};
  }}
}})();
"""

with open(myths_path, "w", encoding="utf-8") as f:
    f.write(new_js)

print("Saved updated legal-myths.js successfully!")
