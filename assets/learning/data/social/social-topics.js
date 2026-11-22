/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Social Legislation Topics Metadata Module (Paper I — General Knowledge)
 * Covers 9 Prescribed Social Acts across 84 Topics.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "top-disab-01-01",
    "chapterId": "ch-soc-disab-01",
    "subjectId": "soc-disabilities",
    "title": "UNCRPD Background, Salient Features & Constitutional Underpinnings",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-disab-01-02",
    "chapterId": "ch-soc-disab-01",
    "subjectId": "soc-disabilities",
    "title": "Key Definitions: Disability, Benchmark Disability (40%), High Support Need & Discrimination",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-disab-01-03",
    "chapterId": "ch-soc-disab-01",
    "subjectId": "soc-disabilities",
    "title": "The 21 Specified Disabilities in the Schedule: Physical, Intellectual & Mental",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-disab-02-01",
    "chapterId": "ch-soc-disab-02",
    "subjectId": "soc-disabilities",
    "title": "Rights & Entitlements: Equality, Non-Discrimination, Community Life & Legal Capacity",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-disab-02-02",
    "chapterId": "ch-soc-disab-02",
    "subjectId": "soc-disabilities",
    "title": "Education & Employment Mandates: Inclusive Education, 4% Reservation & Equal Opportunity",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-disab-02-03",
    "chapterId": "ch-soc-disab-02",
    "subjectId": "soc-disabilities",
    "title": "Accessibility Architecture: Built Environment, Transport, ICT & Mandatory Audits",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-disab-03-01",
    "chapterId": "ch-soc-disab-03",
    "subjectId": "soc-disabilities",
    "title": "Central & State Advisory Boards: Composition, Functions & Tenure",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-disab-03-02",
    "chapterId": "ch-soc-disab-03",
    "subjectId": "soc-disabilities",
    "title": "Chief Commissioner & State Commissioners for PwD: Inquiries, Powers & Grievance Redressal",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-disab-03-03",
    "chapterId": "ch-soc-disab-03",
    "subjectId": "soc-disabilities",
    "title": "Special Courts, Special Public Prosecutors & Offences / Penalties (Sections 84\u201395)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 16
  },
  {
    "id": "top-parent-01-01",
    "chapterId": "ch-soc-parent-01",
    "subjectId": "soc-parents",
    "title": "Legislative History, Statement of Objects and Constitutional Directive (Art. 41)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-parent-01-02",
    "chapterId": "ch-soc-parent-01",
    "subjectId": "soc-parents",
    "title": "Statutory Definitions: Senior Citizen (60+), Parent, Children, Relative & Welfare",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-parent-01-03",
    "chapterId": "ch-soc-parent-01",
    "subjectId": "soc-parents",
    "title": "Duty to Maintain: Obligation of Children & Relatives Entitled to Inherit Property",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-parent-02-01",
    "chapterId": "ch-soc-parent-02",
    "subjectId": "soc-parents",
    "title": "Maintenance Application (S. 4\u20135): Filing, Interim Maintenance & Maximum Cap Evolution",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-parent-02-02",
    "chapterId": "ch-soc-parent-02",
    "subjectId": "soc-parents",
    "title": "Constitution and Procedure of Maintenance Tribunals (S. 7\u201314, SDO Adjudication)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-parent-02-03",
    "chapterId": "ch-soc-parent-02",
    "subjectId": "soc-parents",
    "title": "Appellate Tribunal (S. 15\u201318, District Magistrate) & Bar on Legal Practitioners (S. 17)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-parent-03-01",
    "chapterId": "ch-soc-parent-03",
    "subjectId": "soc-parents",
    "title": "Section 23: Invalidation of Property Transfers Conditioned on Maintenance & Landmark Precedents",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-parent-03-02",
    "chapterId": "ch-soc-parent-03",
    "subjectId": "soc-parents",
    "title": "Medical Care, Old Age Homes & State Welfare Safeguards (Sections 19\u201320)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-parent-03-03",
    "chapterId": "ch-soc-parent-03",
    "subjectId": "soc-parents",
    "title": "Section 24: Abandonment of Senior Citizens, Penalties & Summary Trial Procedures",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-dowry-01-01",
    "chapterId": "ch-soc-dowry-01",
    "subjectId": "soc-dowry",
    "title": "Legislative Scheme, Objectives and 1984/1986 Amendments",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-dowry-01-02",
    "chapterId": "ch-soc-dowry-01",
    "subjectId": "soc-dowry",
    "title": "Statutory Definition of 'Dowry' under Section 2 vs Traditional Presents / Stridhan",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dowry-01-03",
    "chapterId": "ch-soc-dowry-01",
    "subjectId": "soc-dowry",
    "title": "Section 3: Penalties for Giving or Taking Dowry & Statutory Exclusion for Customary Gifts",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-dowry-02-01",
    "chapterId": "ch-soc-dowry-02",
    "subjectId": "soc-dowry",
    "title": "Section 4 & 4A: Demanding Dowry and Ban on Advertisements Offering Property",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dowry-02-02",
    "chapterId": "ch-soc-dowry-02",
    "subjectId": "soc-dowry",
    "title": "Section 5: Agreements for Giving/Taking Dowry to be Void & Unenforceable",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-dowry-02-03",
    "chapterId": "ch-soc-dowry-02",
    "subjectId": "soc-dowry",
    "title": "Section 6: Dowry to be for Benefit of Wife / Heirs & Criminal Breach of Trust Interface",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-dowry-03-01",
    "chapterId": "ch-soc-dowry-03",
    "subjectId": "soc-dowry",
    "title": "Section 7: Cognizance of Offences, Competent Magistrates & Non-applicability of CrPC S. 468",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-dowry-03-02",
    "chapterId": "ch-soc-dowry-03",
    "subjectId": "soc-dowry",
    "title": "Section 8 & 8A: Offence Classification (Cognizable/Non-Bailable) & Reverse Burden of Proof",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dowry-03-03",
    "chapterId": "ch-soc-dowry-03",
    "subjectId": "soc-dowry",
    "title": "Section 8B: Dowry Prohibition Officers & Interplay with BNS 80/85 (IPC 304B/498A)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-dv-01-01",
    "chapterId": "ch-soc-dv-01",
    "subjectId": "soc-domestic-violence",
    "title": "Legislative Purpose, CEDAW Framework & Civil Remedy Architecture",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-dv-01-02",
    "chapterId": "ch-soc-dv-01",
    "subjectId": "soc-domestic-violence",
    "title": "Section 2 Definitions: Aggrieved Person, Respondent, Domestic Relationship & DIR",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-dv-01-03",
    "chapterId": "ch-soc-dv-01",
    "subjectId": "soc-domestic-violence",
    "title": "Section 3: Definition and Dimensions of Domestic Violence (Physical, Sexual, Emotional, Economic)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dv-02-01",
    "chapterId": "ch-soc-dv-02",
    "subjectId": "soc-domestic-violence",
    "title": "Section 17: Right to Reside in Shared Household (Satish Chander Ahuja & Prabha Tyagi Doctrines)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 24
  },
  {
    "id": "top-dv-02-02",
    "chapterId": "ch-soc-dv-02",
    "subjectId": "soc-domestic-violence",
    "title": "Protection Officers, Service Providers & Shelter Homes (Sections 8\u201311)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dv-02-03",
    "chapterId": "ch-soc-dv-02",
    "subjectId": "soc-domestic-violence",
    "title": "Procedure for Applications under Section 12, Notice (S. 13) & 60-Day Disposal Mandate (S. 12(5))",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  },
  {
    "id": "top-dv-03-01",
    "chapterId": "ch-soc-dv-03",
    "subjectId": "soc-domestic-violence",
    "title": "Section 18: Protection Orders & Section 19: Residence Orders (Restraining Dispossession)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-dv-03-02",
    "chapterId": "ch-soc-dv-03",
    "subjectId": "soc-domestic-violence",
    "title": "Monetary Relief (S. 20), Custody Orders (S. 21) & Ex-Parte / Interim Reliefs (S. 23)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-dv-03-03",
    "chapterId": "ch-soc-dv-03",
    "subjectId": "soc-domestic-violence",
    "title": "Section 31: Penalty for Breach of Protection Order, Cognizance & Section 29 Appeals",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-posh-01-01",
    "chapterId": "ch-soc-posh-01",
    "subjectId": "soc-posh",
    "title": "From Vishaka (1997) to POSH Act: Constitutional Foundations & International Obligations",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-posh-01-02",
    "chapterId": "ch-soc-posh-01",
    "subjectId": "soc-posh",
    "title": "Key Definitions: Aggrieved Woman, Employee, Workplace (Extended Workplace) & Employer",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-posh-01-03",
    "chapterId": "ch-soc-posh-01",
    "subjectId": "soc-posh",
    "title": "Section 3: Sexual Harassment Concepts: Quid Pro Quo vs Hostile Work Environment",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-posh-02-01",
    "chapterId": "ch-soc-posh-02",
    "subjectId": "soc-posh",
    "title": "Internal Committee (IC): Constitution, Presiding Officer, External Member & 10-Worker Threshold",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-posh-02-02",
    "chapterId": "ch-soc-posh-02",
    "subjectId": "soc-posh",
    "title": "Local Committee (LC): Constitution, District Officer & Unorganized Sector Coverage (S. 6\u20137)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  },
  {
    "id": "top-posh-02-03",
    "chapterId": "ch-soc-posh-02",
    "subjectId": "soc-posh",
    "title": "Complaint Mechanism (S. 9): 3-Month Limitation, Conciliation (S. 10) & Natural Justice Inquiry",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-posh-03-01",
    "chapterId": "ch-soc-posh-03",
    "subjectId": "soc-posh",
    "title": "Inquiry Report, Recommendations & Interim Measures (Leave, Transfer) during Pendency (S. 12\u201313)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-posh-03-02",
    "chapterId": "ch-soc-posh-03",
    "subjectId": "soc-posh",
    "title": "Section 16: Strict Prohibition of Publication of Contents of Complaint, Inquiry & Identity",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-posh-03-03",
    "chapterId": "ch-soc-posh-03",
    "subjectId": "soc-posh",
    "title": "Duties of Employer (S. 19), Penalties for Non-Compliance (S. 26) & Section 18 Appeals",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-pcpndt-01-01",
    "chapterId": "ch-soc-pcpndt-01",
    "subjectId": "soc-pcpndt",
    "title": "Historical Context, Declining Child Sex Ratio & 2003 Pre-Conception Amendments",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-pcpndt-01-02",
    "chapterId": "ch-soc-pcpndt-01",
    "subjectId": "soc-pcpndt",
    "title": "Key Definitions: Genetic Clinic, Laboratory, Pre-Natal Diagnostic Procedures & Sex Selection",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pcpndt-01-03",
    "chapterId": "ch-soc-pcpndt-01",
    "subjectId": "soc-pcpndt",
    "title": "Regulation of Pre-Natal Diagnostic Techniques: Permissible Indications & Strict Exclusions (S. 4)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-pcpndt-02-01",
    "chapterId": "ch-soc-pcpndt-02",
    "subjectId": "soc-pcpndt",
    "title": "Section 5 & 6: Absolute Ban on Sex Selection & Prohibition on Communicating Foetal Sex",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  },
  {
    "id": "top-pcpndt-02-02",
    "chapterId": "ch-soc-pcpndt-02",
    "subjectId": "soc-pcpndt",
    "title": "Mandatory Registration of Genetic Clinics & Ultrasound Machines (Sections 18\u201321)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pcpndt-02-03",
    "chapterId": "ch-soc-pcpndt-02",
    "subjectId": "soc-pcpndt",
    "title": "Record Maintenance Mandates (Form F), Preservation Periods (2 Years) & Sealing Powers",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 19
  },
  {
    "id": "top-pcpndt-03-01",
    "chapterId": "ch-soc-pcpndt-03",
    "subjectId": "soc-pcpndt",
    "title": "Central & State Supervisory Boards (CSB/SSB): Composition and Policy Mandates (Sections 7\u201316)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-pcpndt-03-02",
    "chapterId": "ch-soc-pcpndt-03",
    "subjectId": "soc-pcpndt",
    "title": "Appropriate Authorities & Advisory Committees: Inspection, Search & Seizure (Sections 17 & 30)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pcpndt-03-03",
    "chapterId": "ch-soc-pcpndt-03",
    "subjectId": "soc-pcpndt",
    "title": "Offences, Penalties (S. 23), Reverse Burden of Proof (S. 24) & Cognizance Safeguards (S. 28)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-mtp-01-01",
    "chapterId": "ch-soc-mtp-01",
    "subjectId": "soc-mtp",
    "title": "Legislative Scheme, Shantilal Shah Committee & Constitutional Privacy Protections",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-mtp-01-02",
    "chapterId": "ch-soc-mtp-01",
    "subjectId": "soc-mtp",
    "title": "Key Definitions: Registered Medical Practitioner (RMP), Guardian & Mentally Ill Person",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-mtp-01-03",
    "chapterId": "ch-soc-mtp-01",
    "subjectId": "soc-mtp",
    "title": "The 2021 Amendment Paradigm: Expanding Scope to Unmarried Women & Reproductive Autonomy",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 19
  },
  {
    "id": "top-mtp-02-01",
    "chapterId": "ch-soc-mtp-02",
    "subjectId": "soc-mtp",
    "title": "Gestational Tiers: Up to 20 Weeks (1 RMP) & 20\u201324 Weeks (2 RMPs for Vulnerable Categories)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-mtp-02-02",
    "chapterId": "ch-soc-mtp-02",
    "subjectId": "soc-mtp",
    "title": "Termination Beyond 24 Weeks: Substantial Foetal Abnormalities & Medical Board Certification",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-mtp-02-03",
    "chapterId": "ch-soc-mtp-02",
    "subjectId": "soc-mtp",
    "title": "Section 5: Emergency Exception (Life-Saving Termination Without Gestational Limits)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-mtp-03-01",
    "chapterId": "ch-soc-mtp-03",
    "subjectId": "soc-mtp",
    "title": "Consent Regime (S. 3(4)): Woman's Sole Consent vs Guardian Consent (Minor / Mentally Ill)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 19
  },
  {
    "id": "top-mtp-03-02",
    "chapterId": "ch-soc-mtp-03",
    "subjectId": "soc-mtp",
    "title": "Approved Places for Termination (S. 4) & Maintenance of Confidential Admission Register",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-mtp-03-03",
    "chapterId": "ch-soc-mtp-03",
    "subjectId": "soc-mtp",
    "title": "Offences and Penalties under Section 5A (Privacy Breach) & Interplay with BNS 90\u201392 (IPC 312\u2013314)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-irwa-01-01",
    "chapterId": "ch-soc-irwa-01",
    "subjectId": "soc-indecent-rep",
    "title": "Historical Context, Rajya Sabha Debates and Salient Features of Act No. 60 of 1986",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 16
  },
  {
    "id": "top-irwa-01-02",
    "chapterId": "ch-soc-irwa-01",
    "subjectId": "soc-indecent-rep",
    "title": "Section 2 Definitions: Indecent Representation of Women, Advertisement, Distribution & Package",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-irwa-01-03",
    "chapterId": "ch-soc-irwa-01",
    "subjectId": "soc-indecent-rep",
    "title": "Section 3: Absolute Prohibition on Advertisements Containing Indecent Representation of Women",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-irwa-02-01",
    "chapterId": "ch-soc-irwa-02",
    "subjectId": "soc-indecent-rep",
    "title": "Section 4: Prohibition on Publication, Sale, Hire, Distribution or Circulation of Indecent Material",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 19
  },
  {
    "id": "top-irwa-02-02",
    "chapterId": "ch-soc-irwa-02",
    "subjectId": "soc-indecent-rep",
    "title": "Statutory Exceptions: Scientific, Art, Literature, Religious Purposes & Ancient Monuments (S. 4 Proviso)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 19
  },
  {
    "id": "top-irwa-02-03",
    "chapterId": "ch-soc-irwa-02",
    "subjectId": "soc-indecent-rep",
    "title": "Digital Convergence: Application of IRWA to Electronic Media & Interplay with IT Act 2000 (S. 67)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-irwa-03-01",
    "chapterId": "ch-soc-irwa-03",
    "subjectId": "soc-indecent-rep",
    "title": "Section 5: Powers of Entry, Search, Seizure & Examination of Gazetted Officers",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  },
  {
    "id": "top-irwa-03-02",
    "chapterId": "ch-soc-irwa-03",
    "subjectId": "soc-indecent-rep",
    "title": "Section 6: Penalties for First & Subsequent Convictions (Imprisonment & Mandatory Fines)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 17
  },
  {
    "id": "top-irwa-03-03",
    "chapterId": "ch-soc-irwa-03",
    "subjectId": "soc-indecent-rep",
    "title": "Section 7 & 8: Offences by Companies, Cognizability, Bailability & Good Faith Protection",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-pocso-01-01",
    "chapterId": "ch-soc-pocso-01",
    "subjectId": "soc-pocso",
    "title": "UN Convention on the Rights of the Child (CRC) & Special Protective Paradigm",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-pocso-01-02",
    "chapterId": "ch-soc-pocso-01",
    "subjectId": "soc-pocso",
    "title": "Section 2 Definitions: 'Child' (Strict Age Cutoff under 18 Years) & Gender-Neutral Architecture",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 19
  },
  {
    "id": "top-pocso-01-03",
    "chapterId": "ch-soc-pocso-01",
    "subjectId": "soc-pocso",
    "title": "Statutory Interpretation: Primacy of Child Welfare, Strict Liability & Age Determination Standards",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-pocso-02-01",
    "chapterId": "ch-soc-pocso-02",
    "subjectId": "soc-pocso",
    "title": "Penetrative Sexual Assault (S. 3\u20134) & Aggravated Penetrative Sexual Assault (S. 5\u20136, 2019 Amendments)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 23
  },
  {
    "id": "top-pocso-02-02",
    "chapterId": "ch-soc-pocso-02",
    "subjectId": "soc-pocso",
    "title": "Sexual Assault (S. 7\u20138) & Aggravated Sexual Assault (S. 9\u201310)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  },
  {
    "id": "top-pocso-02-03",
    "chapterId": "ch-soc-pocso-02",
    "subjectId": "soc-pocso",
    "title": "Sexual Harassment (S. 11\u201312) & Child Pornography / Digital Exploitation (Sections 13\u201315)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  },
  {
    "id": "top-pocso-03-01",
    "chapterId": "ch-soc-pocso-03",
    "subjectId": "soc-pocso",
    "title": "Sections 19\u201321: Mandatory Duty to Report Offences & Penalties for Failure to Report",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pocso-03-02",
    "chapterId": "ch-soc-pocso-03",
    "subjectId": "soc-pocso",
    "title": "Investigation Procedures: Special Juvenile Police Unit (SJPU), Women Officers & Child-Friendly Setting",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pocso-03-03",
    "chapterId": "ch-soc-pocso-03",
    "subjectId": "soc-pocso",
    "title": "Medical Examination of Child (S. 27), Emergency Medical Treatment & Immediate Compensation",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-pocso-04-01",
    "chapterId": "ch-soc-pocso-04",
    "subjectId": "soc-pocso",
    "title": "Designation and Jurisdiction of Special Courts (S. 28) & Recording Evidence within 30 Days (S. 35)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-pocso-04-02",
    "chapterId": "ch-soc-pocso-04",
    "subjectId": "soc-pocso",
    "title": "Child-Friendly Court Procedures: In-Camera Trial, Video Link & No Direct Confrontation (S. 33\u201338)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 22
  },
  {
    "id": "top-pocso-04-03",
    "chapterId": "ch-soc-pocso-04",
    "subjectId": "soc-pocso",
    "title": "Statutory Presumptions (S. 29 Presumption of Guilt, S. 30 Culpable Mental State) & S. 42A Overriding Effect",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 21
  }
];

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  const root = typeof window !== "undefined" ? window : global;
  root.SOCIAL_TOPICS = DATA;
})(typeof window !== "undefined" ? window : global);
