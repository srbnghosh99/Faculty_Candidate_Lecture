---
form: Project Monthly Input Form
form_reference: DI-MGMT-80368A
project_title: "Development of Analytical Capabilities for Information Campaign Assessment (TDAC-AC)"
project_short_name: TDAC-AC
project_lead: "Steven Schneider (PI), SUNY Polytechnic Institute"
team_members:
  - "William Thistleton, SUNY Poly"
  - "Asela Abeya, SUNY Poly"
  - "Shrabani Ghosh, SUNY Poly"
sponsor_poc: "Peter J. Grazaitis (DEVCOM/DAC)"
reporting_period:
  start: 2026-06-15
  end: 2026-07-15
date_submitted: 2026-07-29
source_note: >
  Drafted from repository meeting records and project-planning documents in
  sunypolyaix/tdac-ac (Meetings/Meeting_Record_June16_2026.md,
  Meetings/Meeting_Record_June17_2026.md,
  Meetings/TDAC-AC_Paper_Replication_Meeting_Report_2026-07-13.md,
  Meetings/Project_Summary_AI_Paper_Replication-July10_2026.md,
  project-calendar.md, project-mgmt/defense-analyst-pm/pm1/level1.md).
  Percent-complete figures are estimates inferred from these sources, not
  from a formal tracker — verify before submitting. Man-hours/cost and
  contact fields are not tracked anywhere in the repo and are left as
  placeholders.
---

# Project Monthly Input Form

*Feeds the consolidated Monthly Status Report (DI-MGMT-80368A). Complete all sections; enter "None this period" or "N/A" rather than leaving items blank.*

## A. Project Identification

| Field | Value |
|---|---|
| Project Title | Development of Analytical Capabilities for Information Campaign Assessment (TDAC-AC) |
| Project Lead | Steven Schneider (PI), SUNY Polytechnic Institute |
| Reporting Period | June 15, 2026 – July 15, 2026 |
| Date Submitted | July 29, 2026 |

## B. Project Summary

This project develops and evaluates AI/LLM-assisted analytical capabilities for intelligence-style reporting on socio-cultural instability and information campaigns. The core research question is whether an AI-generated analytic product — given the same temporally bounded open-source information environment as a human analyst — can produce a reliable expert outcome comparable to a human analyst's output, and under what conditions (model choice, information delivery method, analytical framework) that fidelity is highest.

This period was foundational:  the project team selected a case study paper as the target for analysis and completed collection of the associated data. The task was defined as a comparison of AI-generated versus human-generated papers, using three evaluation methods: semantic similarity, named entity extraction, and causal relation extraction. Initial groundwork for the comparison pipeline is in place, and analysis is done using these three methods next period. No major problems were encountered this period.

## C. Schedule and Milestone Status

**Overall Schedule Status:** On schedule. The project is in Months 1–2 ("Foundation") of the 12-month calendar (start May 25, 2026). Formal team kickoff with the sponsor is scheduled for July 20, 2026 — just after the close of this reporting period — so several Level-1 "Alignment" milestones are still open by design.

| Milestone / Task | Planned Date | Forecast / Actual Date | % Complete | Remarks |
|---|---|---|---|---|
| A1. Kickoff meeting with TDAC team completed | Jul 2026 | Scheduled Jul 20, 2026 |100% | Completed |
| A2. Project plan document agreed and candidate paper selction process | Jun–Jul 2026 | In progress | ~60% | Multiple project-plan   |
| L1. Literature-review process calibrated | Jul–Aug 2026 | In progress | ~20% | Reference-management workflow (Zotero categorization/filtering) defined; not yet run at scale. |
| C1. Replication case-study design agreed | Jun–Jul 2026 | In progress | ~70% | task-schedule drafts (v0–v3) produced |
| C2. Human-produced analytic artifact selected | Jun–Jul 2026 | Substantially complete | ~80% | Ghana economic-growth paper selected as Case Study Zero ("Cub"); Burkina Faso seed paper selected as the primary coup case; a COVID-timing paper used as a separate pilot for toolkit development. |
| C3. Context and method specified | Jul–Aug 2026 | In progress | ~40% |  |
| T1. Toolkit input structure defined | Jul 2026 | In progress | ~50% | PDF-vs-Markdown conversion |
| T2. Toolkit evaluation method defined | Jul 2026 | In progress | ~60% | Multi-metric evaluation framework drafted (semantic similarity, NER, SPO/fact extraction, knowledge/causal graphs, hallucination detection). |
| T3. Toolkit applied to case-study output | Jul 2026 | Preliminery analysis done | ~65% | Semantic-similarity and NER metrics already run against pilot AI-generated candidate papers (Versions 0–5). |

*(Milestones L2/L3, C4/C5, T4/T5, P1–P3 have not yet started and are omitted above; see Level-1 plan for full list.)*

## D. Technical Accomplishments This Period

- **Project architecture:** Confirmed GitHub repository structure (AIX Private → `projects/` + `tools/`); established README-for-every-directory norm; agreed raw data stays in SharePoint ("AIX Data Vault"), never in GitHub, while synthesized/structured data and documents live in GitHub.
- **Case-study scope:** Confirmed the five-country West African case-study framework (2019–2022): Mali, Guinea, Burkina Faso (coup occurred — active cases) vs. Senegal, Ghana (no coup — stable comparison cases), for quasi-experimental validity.
- **Alpha/validation run:** Selected "Determinants of Economic Growth in Ghana" (ARDL model, World Bank data) as Case Study Zero ("Cub") to validate the full pipeline at low risk before committing to the harder Burkina Faso corpus; plan agreed with summer RA Sabrita to redo her prior replication attempt using the correct data vintage and the project's full process.
- **Data collection:** Began ACLED conflict-event data download (Africa scope, 2013–present, excluding US/Canada) and Afrobarometer/fragility-barometer data; identified SAV→CSV conversion as a required preprocessing step; agreed the "synthesis before model" principle (raw structured data must be interpreted/summarized before any LLM ingestion).
- **Web scraping / cost pipeline:** Settled on HTTrack/Python-based scraping to separate text from images before any model involvement, and a cost-reduction pipeline (free preprocessing → cheap models to validate pipeline shape → Claude/GPT only for production runs), driven by real per-article cost estimates (~$5/article via API).
- **Analytic Toolkit (Deliverable 1.2) — pilot metrics built:**
  - Semantic-similarity metric (sentence-transformer embeddings, cosine similarity, document/section/sentence level) — implemented and demoed against a pilot candidate paper ("COVID Timing 2019" replication), achieving a 79% document-level baseline similarity with no additional context provided.
  - Named-entity-recognition (NER) metric — implemented and demoed.
  - Subject-predicate-object (fact/triplet) extraction — scoped as the next metric; identified as the basis from which causal-graph comparison will be derived rather than building a separate causal extractor.
  - Hallucination-detection approach — converged on comparing extracted facts against the original document as a grounding source (with the caveat that legitimately-introduced facts from added context are not automatically hallucinations); designed an information-availability matrix (full/partial/zero references) to isolate model capability from information-availability effects.
- **Methodology documents:** Reviewed and iterated V7/V8 experimental-design documents; confirmed data-leakage mitigation (favor open-weight models with pre-2019 training cutoffs for the predictive-test conditions); flagged need for an 8th analytic-register type to classify the Burkina Faso source document.
- **Reproducibility:** Noted a hyperparameter-control limitation of proprietary/commercial LLMs and proposed replicating select experiments with an open-source model (e.g., a DeepSeek-class model) on local/HPC resources for direct comparability.

## E. Status of Previously Reported Problems

N/A — this is the first Project Monthly Input Form filed for this project; no problems were reported in a prior monthly cycle.

## F. New or Anticipated Problems

| Problem / Risk | Effect on Project | Corrective Action |
|---|---|---|
| Billing for AI tool usage is currently running through the AIX Center account rather than the TDAC research-funding account; TDAC account number not yet issued. | Cost tracking is not attributable to the correct funding line. | Obtain TDAC account number from PI and complete billing transition (in progress since Jun 16). |
| Project budget line is coded "grad student," blocking hiring of qualified undergraduate/non-grad research assistants. | Constrains available research-assistant labor pool. | Identify and pursue the correct escalation path through the grants/venue office to request a budget-line change. |
| Data-leakage risk: frontier LLMs (Claude, GPT-4+) were almost certainly trained on news coverage of the target coup events. | Could invalidate the AI-vs-human predictive comparison for the core case studies. | Mitigate by using open-weight models with training cutoffs prior to 2019 for the experimental (predictive) comparison conditions; V7 methods document details the mitigation. |
| API-based LLM usage has no session cost cap, unlike the flat-rate Pro subscription tier. | Risk of unplanned, potentially large compute costs if scaled prematurely. | Team policy: prototype on cheap/free tooling and the Pro subscription tier; reserve API calls for production-quality runs only. |
| PDF-to-Markdown conversion quality is unverified (no ground truth) and AI-generated candidates are natively "clean" Markdown while human-authored originals carry conversion noise. | Risk of systematically biased fact/entity-extraction comparisons that look like content gaps but are really format-quality artifacts. | Isolate the conversion step for independent evaluation; prioritize cross-tool conversion comparisons; treat AI-version-vs-AI-version comparisons as more reliable than AI-vs.-noisy-original comparisons in the interim. |

## G. Conferences, Trips, and Directives

None this period requiring sponsor notice. Internal team working sessions were held June 16, June 17, and July 13, 2026. Formal kickoff meeting with the sponsor team is scheduled for July 20, 2026 (next period).

## H. Plans for Next Period

- Hold the formal TDAC-AC kickoff meeting with the sponsor team (July 20, 2026).
- Have Sabrita complete the Ghana ("Cub") replication case study end-to-end using the corrected World Bank data vintage and the project's full pipeline, as validation of the methodology before committing to the Burkina Faso corpus.
- Continue ACLED and Afrobarometer data collection and preprocessing (SAV→CSV conversion, synthesis layer).
- Build the subject-predicate-object (fact/triplet) extraction metric and derive the causal-graph comparison from it.
- Run the information-availability matrix experiment (full/partial/zero external references) to isolate hallucination causes from model capability.
- Define the 8th analytic-register type needed to classify the Burkina Faso seed document.
- Resolve open administrative items: TDAC billing-account transition and the grad-student budget-line restriction.
- Audit the original task-order proposal against current work to confirm no sponsor deliverable commitments (including monthly reporting) are being missed.

## I. Man-Hours and Costs

Not tracked in a form suitable for this report as of period close — no timesheet/cost-ledger data available in the project repository. *TBD — fill in before submission if required by the sponsor.*

| Task / Category | Man-Hours (Period) | Man-Hours (Cumulative) | Cost (Period) | Cost (Cumulative) |
|---|---|---|---|---|
| *TBD* | | | | |

## J. Deliverables Status

No formal deliverables are due during this reporting period. Per the project calendar, the first deliverables (1.1 Case Studies and Experimental Results; 1.2 Analytical Tools) are due at Month 9 (~February 2027); 1.3 Publications and Analyses is due at Month 12 (~May 2027).

| Deliverable | Due Date | Submitted / Shipped? | Acceptance Status |
|---|---|---|---|
| 1.1 Case Studies and Experimental Results | Month 9 (~Feb 2027) | Not yet due | N/A |
| 1.2 Analytical Tools | Month 9 (~Feb 2027) | Not yet due | N/A |
| 1.3 Publications and Analyses | Month 12 (~May 2027) | Not yet due | N/A |
