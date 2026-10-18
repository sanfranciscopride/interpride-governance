# InterPride Governance & Resources Master Index

This document indexes the **140 governing, policy, strategic, and financial PDF documents** downloaded from `https://www.interpride.org/` (via the WordPress REST API `wp-json/wp/v2/media`) into [`resources/`](file:///Users/chris/Developer/interpride/governance/resources), along with their plain-text extractions in [`resources/extracted_text/`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text).

---

## 1. Why `interpride.org/resources/` Looked Empty (and How We Recovered Everything)

When visiting `https://www.interpride.org/resources/`, the page currently renders only a single post (`2025_embassy_support_report`) and a footer link to the 2025–2027 Strategic Plan because the WordPress `Policy` category (`id: 13`) has `0` published posts. However, querying the WordPress REST API (`https://www.interpride.org/wp-json/wp/v2/media?mime_type=application/pdf`) revealed **205 PDFs** still hosted in `/wp-content/uploads/` (across media folders `PDF`, `WP Forms`, and `ZZZ_ARCHIVE`).

All 205 items are cataloged in [`resources_manifest.json`](file:///Users/chris/Developer/interpride/governance/resources_manifest.json), and all **140 governance, policy, strategy, and financial documents** have been downloaded by [`download_resources.py`](file:///Users/chris/Developer/interpride/governance/download_resources.py) into 7 structured directories under [`resources/`](file:///Users/chris/Developer/interpride/governance/resources).

---

## 2. Directory Structure & Core Governing Documents

### [`01_bylaws/`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws) (18 PDFs — English, Spanish, French, Portuguese)
- **Latest Website Version (Updated Jan 20, 2024):**
  - PDF: [`IP_Bylaws_Approved_English_01.20.2024.pdf`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_English_01.20.2024.pdf) | Text: [`IP_Bylaws_Approved_English_01.20.2024.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/01_bylaws/IP_Bylaws_Approved_English_01.20.2024.txt)
  - Translations: [`Spanish`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_Spanish_01.20.2024.pdf), [`French`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_French_01.20.2024.pdf), [`Portuguese`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_Portuguese_01.20.2024.pdf)
- **Prior Versions (Sept 29, 2023 & Dec 2022):**
  - [`IP_Bylaws_Approved_English_09.29.2023_V1.pdf`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_English_09.29.2023_V1.pdf), [`IP_Bylaws_Approved_English_09.29.2023.pdf`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_English_09.29.2023.pdf), [`IP_Bylaws_Approved_English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/01_bylaws/IP_Bylaws_Approved_English.pdf)

### [`02_bylaw_amendments/`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments) (7 PDFs)
- [`Bylaws-Amendment-Purpose-e55e3e4a907826c9ae607483369b9bf4.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Bylaws-Amendment-Purpose-e55e3e4a907826c9ae607483369b9bf4.pdf) (Article III Purpose update)
- [`Bylaws-Amendment-Emeritus-Council-f61eb9430944b04585a5401e10f9c25c.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Bylaws-Amendment-Emeritus-Council-f61eb9430944b04585a5401e10f9c25c.pdf) & [`Bylaws-Amendment-and-standing-rules-amendment-Emeritus-Council-a55c10533dcea59cf65147f45ac1071b.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Bylaws-Amendment-and-standing-rules-amendment-Emeritus-Council-a55c10533dcea59cf65147f45ac1071b.pdf) (Article V Sec 1 & SR 01.03 Emeritus Council)
- [`Bylaws-Amendment-Plenary-2.final_-ce58a02ad4c0ddadb7b1b6d59cf167f2.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Bylaws-Amendment-Plenary-2.final_-ce58a02ad4c0ddadb7b1b6d59cf167f2.pdf) (Article VIII Sec 3 Plenary scheduling)
- [`Pride-Winnipeg-Bylaw-signed-a181735a92d4f4318c34b2b00ec1e6c1.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Pride-Winnipeg-Bylaw-signed-a181735a92d4f4318c34b2b00ec1e6c1.pdf) (Separating VPDIA into VP of Diversity & Inclusion and VP of Accessibility)
- [`Bylaw_Amendment_Form_English_2023.pdf`](file:///Users/chris/Developer/interpride/governance/resources/02_bylaw_amendments/Bylaw_Amendment_Form_English_2023.pdf) (Blank form)

### [`03_standing_rules_and_ethics/`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics) (14 PDFs)
- **Standing Rules (Updated Oct 11, 2023):**
  - PDF: [`IP_Standing-Rules_English_10.11.23.pdf`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_English_10.11.23.pdf) | Text: [`IP_Standing-Rules_English_10.11.23.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/03_standing_rules_and_ethics/IP_Standing-Rules_English_10.11.23.txt)
  - Translations: [`Spanish`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Spanish_10.11.23.pdf), [`French`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_French_10.11.23.pdf), [`Portuguese`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Portuguese_10.11.23.pdf)
- **Code of Ethics and Conduct (SR 08.04, Nov 2023 standalone booklet):**
  - PDF: [`IP_Standing-Rules_Code-of-Ethics-Conduct_2023-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Code-of-Ethics-Conduct_2023-English.pdf) | Text: [`IP_Standing-Rules_Code-of-Ethics-Conduct_2023-English.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/03_standing_rules_and_ethics/IP_Standing-Rules_Code-of-Ethics-Conduct_2023-English.txt)
  - Translations: [`Spanish`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Code-of-Ethics-Conduct_2023-Spanish.pdf), [`French`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Code-of-Ethics-Conduct_2023-French.pdf), [`Portuguese`](file:///Users/chris/Developer/interpride/governance/resources/03_standing_rules_and_ethics/IP_Standing-Rules_Code-of-Ethics-Conduct_2023-Portuguese.pdf)

### [`04_resolutions/`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions) (18 PDFs)
- **Resolutions Compendium (Updated Dec 2023):**
  - PDF: [`IP_Resolutions_12.03.22-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/IP_Resolutions_12.03.22-English.pdf) | Text: [`IP_Resolutions_12.03.22-English.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/04_resolutions/IP_Resolutions_12.03.22-English.txt)
  - Translations: [`Spanish`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/IP_Resolutions_12.03.22-Spanish.pdf), [`French`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/IP_Resolutions_12.03.22-French.pdf), [`Portuguese`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/IP_Resolutions_12.03.22-Portuguese.pdf)
- **2023 Resolution Submissions & Forms:**
  - [`Resolution-Gala-Costs-aab94e0efbe3ee6aca6c97e77e0d2b46.pdf`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/Resolution-Gala-Costs-aab94e0efbe3ee6aca6c97e77e0d2b46.pdf) (Recouping April 2023 Gala financial losses)
  - [`Resolution_Proposal_Form_English_2023-be3f9b89f01ea631b8ee9b7a355e441d.pdf`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/Resolution_Proposal_Form_English_2023-be3f9b89f01ea631b8ee9b7a355e441d.pdf) (Communications Committee operational independence — Resolution 23-01)
  - [`Resolution_Proposal_Form_English_2023.pdf`](file:///Users/chris/Developer/interpride/governance/resources/04_resolutions/Resolution_Proposal_Form_English_2023.pdf) (Blank form)

### [`05_gac_rules_and_regulations/`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations) (12 PDFs)
- **Global Advisory Council (GAC) Rules and Regulations (Updated Jan 31, 2024):**
  - PDF: [`IP_GAC_Rules-and-Regulations_English_01.31.24.pdf`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/IP_GAC_Rules-and-Regulations_English_01.31.24.pdf) | Text: [`IP_GAC_Rules-and-Regulations_English_01.31.24.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/05_gac_rules_and_regulations/IP_GAC_Rules-and-Regulations_English_01.31.24.txt)
  - Translations: [`Spanish`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/IP_GAC_Rules-and-Regulations_Spanish_01.31.24.pdf), [`French`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/IP_GAC_Rules-and-Regulations_French_01.31.24.pdf), [`Portuguese`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/IP_GAC_Rules-and-Regulations_Portuguese_01.31.24.pdf)
- **GAC & Pride Platform Transition Plan:**
  - PDF: [`IP_GAC_PridePlatform_TransitionPlan_English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/IP_GAC_PridePlatform_TransitionPlan_English.pdf) | Text: [`IP_GAC_PridePlatform_TransitionPlan_English.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/05_gac_rules_and_regulations/IP_GAC_PridePlatform_TransitionPlan_English.txt)
- **Humanitarian Aid Fund Policy (formerly Legacy Fund, May 2022):**
  - PDF: [`Humanitarian-Aid-Fund-Policy-formerly-Legacy-Fund-_-MAY-22-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/05_gac_rules_and_regulations/Humanitarian-Aid-Fund-Policy-formerly-Legacy-Fund-_-MAY-22-English.pdf) | Text: [`Humanitarian-Aid-Fund-Policy-formerly-Legacy-Fund-_-MAY-22-English.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/05_gac_rules_and_regulations/Humanitarian-Aid-Fund-Policy-formerly-Legacy-Fund-_-MAY-22-English.txt)

### [`06_policies_and_board_governance/`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance) (17 PDFs)
- **Board Duties & Responsibilities (SR 12.01):**
  - PDF: [`12-Board-Duties-Responsibilities.pdf`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance/12-Board-Duties-Responsibilities.pdf) | Text: [`12-Board-Duties-Responsibilities.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/06_policies_and_board_governance/12-Board-Duties-Responsibilities.txt)
- **InterPride Values Statement (2023):**
  - PDF: [`InterPride-Values-Statement-2023-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance/InterPride-Values-Statement-2023-English.pdf) | Text: [`InterPride-Values-Statement-2023-English.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/06_policies_and_board_governance/InterPride-Values-Statement-2023-English.txt)
- **Program & Fund Policies:**
  - [`Scholarship-Fund-Policy-_-APRIL-22-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance/Scholarship-Fund-Policy-_-APRIL-22-English.pdf) (Pam O'Brien Memorial Scholarship Fund Policy)
  - [`Solidarity-Fund-Policy-_-May-22-English.pdf`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance/Solidarity-Fund-Policy-_-May-22-English.pdf) (Solidarity Fund Policy)
  - [`Member-Benefit-Partner-Policy-MAY-2022.pdf`](file:///Users/chris/Developer/interpride/governance/resources/06_policies_and_board_governance/Member-Benefit-Partner-Policy-MAY-2022.pdf) (Member Benefit Partner Program Policy)

### [`07_strategy_reports_and_990s/`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s) (50 PDFs)
- **Strategic Plans:**
  - [`InterPride_Strategic_Plan_2025-2027.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/InterPride_Strategic_Plan_2025-2027.pdf) | Text: [`InterPride_Strategic_Plan_2025-2027.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/07_strategy_reports_and_990s/InterPride_Strategic_Plan_2025-2027.txt)
  - [`InterPride-Strategic-Plan-2022-2024-English-1.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/InterPride-Strategic-Plan-2022-2024-English-1.pdf) & [`StrategicPlanFindings2022.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/StrategicPlanFindings2022.pdf)
- **Annual Reports (2008–2024):**
  - [`2024_IPAnnual-Report_FINAL.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/2024_IPAnnual-Report_FINAL.pdf), [`AR23.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/AR23.pdf) (2023), [`IP-Annual-Report-2022_FINAL-WEBSITE.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/IP-Annual-Report-2022_FINAL-WEBSITE.pdf), plus 2008–2021.
- **IRS Form 990s:** `IP_990_2013.pdf` through [`IP_990_2021.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/IP_990_2021.pdf).
- **Special Reports & Bidding:** [`WP28-Bidding-Process.pptx.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/WP28-Bidding-Process.pptx.pdf), [`2502-Report-Embassy-engagement-with-Prides.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/2502-Report-Embassy-engagement-with-Prides.pdf), [`GALA-REPORT.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/GALA-REPORT.pdf), [`Global-Gala-2nd-Report-September-2023.pdf`](file:///Users/chris/Developer/interpride/governance/resources/07_strategy_reports_and_990s/Global-Gala-2nd-Report-September-2023.pdf).

---

## 3. Executive Digest of InterPride's Governing Framework (for Governance Co-Chairs)

### A. Core Governance Committee Mandate (`SR 01.11`)
Under [`SR 01.11 – Governance Committee`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/03_standing_rules_and_ethics/IP_Standing-Rules_English_10.11.23.txt#L622-L680), the Governance Committee is responsible for the health, compliance, and functioning of the Board:
1. **Board & GAC Education:** New Board Member & GAC Representative orientations; coordinating mentors.
2. **Accountability & Compliance:** Administering the annual Board Member, GAC, and Committee Co-Chairs Agreement; tracking Board attendance and compliance (`SR 02.02 Sec 3` requires Governance Co-Chairs + Co-Presidents to verify "active" status: >=75% voting participation, timely reports, monthly regional communications).
3. **Elections & Candidate Verification (`SR 03.09`, `Bylaws Art V Sec 12–14`, `GAC Rules Sec 2`):**
   - Verifying Officer nominees (must be affiliated with & endorsed by a Full Member in good standing, present at the GM&WC or per current rules, and have attended 1 of the 2 prior GM&WCs).
   -Endorsing Full Member organizations for both **Board Officers** (`Bylaws Art V Sec 12.B`) and **Committee Co-Chairs** (`SR 01.01 Sec 5.F`) must complete payment of their annual dues within the **first 60 days of the fiscal year (by March 1)** or the individual forfeits their position.
   - Co-administering GAC Board Representative elections (7-day electronic ballot requiring a **2/3 supermajority** of GAC to be seated).
4. **Grievance, Conflict Resolution & Disciplinary Inquiry (`SR 03.04` & `Bylaws Art V Sec 18`):**
   - **Grievance Intake (`SR 03.04 Sec 2.D`):** Governance Co-Chairs have **14 calendar days** from receipt of a grievance to determine whether it is within scope and supported by evidence, and notify the Complainant (and forward to the Subject if moving forward).
   - **ADR vs. Committee Decision (`SR 03.04 Sec 3`):** Parties may consent to Mediation or Restorative Justice (except grievances against InterPride itself, which must go to the Governance Committee). If referred to the Governance Committee: Subject has **10 days** to respond -> Committee meets within **5–30 days** -> renders decision/recommendations -> either party may appeal to the Board within **7 working days** -> Board renders final decision within **20 calendar days**.
   - **Removal for Cause (`Bylaws Art V Sec 18.G`):** Fair and reasonable removal requires:
     1. Investigation conducted by the Board in partnership with the GAC;
     2. Motion to accuse, citing Charges and Specifications, approved by the **Governance Committee**;
     3. Member is heard orally and in writing within **10 days maximum** after the Governance Committee passes its motion;
     4. Motion to carry out disciplinary action approved by a **2/3 majority vote of the Board of Directors**;
     5. Written notification within **24 hours** after the Board vote.

### B. Bylaws & Standing Rules Amendment Thresholds
- **Bylaw Amendments (`Bylaws Art XII`):**
  - May be proposed by **>= 5 representatives from different Full Member Organizations**, OR by a **majority vote of the Board or GAC**.
  - Must include an implementation plan.
  - Requires a **simple majority vote (51%+)** at the GM where presented, followed by a **two-thirds (67%+) ratification vote** of the Membership within **60 days** of the first vote.
- **Standing Rules (`SR 01.01`, `SR 03.06`):**
  - Adopted or amended by a majority vote of the Board of Directors (or Membership).
- **GAC Rules & Regulations (`GAC Rules Sec 3.A.18`):**
  - Modified by a majority (`50% + 1`) of Quorum (`50% + 1` of elected GAC Representatives), **pending review by Governance** to ensure no conflicts with policies, and approval by the InterPride Board.

---

## 4. 2025–2026 Governing Documents Downloaded from Email Archive ([`00_2025_2026_email_versions/`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions))

All **42 unique 2025–2026 governing, policy, financial, and meeting minute attachments** from `chris.robert@interpride.org` have been downloaded into [`resources/00_2025_2026_email_versions/`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions) with plain-text extractions in [`resources/extracted_text/00_2025_2026_email_versions/`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions):

1. **Bylaws (Dec 12, 2025):** [`IP_Bylaws_Approved_English_12.12.2025.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Bylaws_Approved_English_12.12.2025.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Bylaws_Approved_English_12.12.2025.txt))
2. **Standing Rules (April 6, 2026 & Dec 13, 2025):**
   - [`IP_Standing Rules_English_04.06.26.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Standing%20Rules_English_04.06.26.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Standing%20Rules_English_04.06.26.txt))
   - [`IP_Standing Rules_English_12.13.25.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Standing%20Rules_English_12.13.25.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Standing%20Rules_English_12.13.25.txt))
   - [`IP_Standing Rule 02.07_English_03.13.26.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Standing%20Rule%2002.07_English_03.13.26.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Standing%20Rule%2002.07_English_03.13.26.txt), plus ES/FR/PT)
   - [`IP_Standing Rules_Role Descriptions.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Standing%20Rules_Role%20Descriptions.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Standing%20Rules_Role%20Descriptions.txt))
3. **Resolutions (March 20, 2026 & Dec 12, 2025):**
   - [`IP_Resolutions_English_03.20.26.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Resolutions_English_03.20.26.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Resolutions_English_03.20.26.txt))
   - [`IP_Resolutions_English_12.12.25.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Resolutions_English_12.12.25.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Resolutions_English_12.12.25.txt))
4. **Code of Ethics & Conduct (Oct 31, 2025):**
   - [`IP_Code of Ethics & Conduct_English_10.31.25.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Code%20of%20Ethics%20%26%20Conduct_English_10.31.25.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Code%20of%20Ethics%20%26%20Conduct_English_10.31.25.txt), plus ES/FR/PT)
5. **GAC Rules & Regulations (July 17, 2026):**
   - [`IP_GAC_Rules and Regulations_English_07.17.26.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_GAC_Rules%20and%20Regulations_English_07.17.26.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_GAC_Rules%20and%20Regulations_English_07.17.26.txt))
6. **Campaigning Policy (2026) & Organization Agreement/Directory (June 2026):**
   - [`IP_Campaigning Policy_English_2026.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Campaigning%20Policy_English_2026.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Campaigning%20Policy_English_2026.txt), plus ES/FR/PT)
   - [`IP_Agreement_Board_Chair_GAC_2026.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/IP_Agreement_Board_Chair_GAC_2026.pdf) ([`.txt`](file:///Users/chris/Developer/interpride/governance/resources/extracted_text/00_2025_2026_email_versions/IP_Agreement_Board_Chair_GAC_2026.txt))
7. **2026 Governance Committee Minutes:**
   - [`Governance Meeting Minutes – April 2026 pt-BR.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/Governance%20Meeting%20Minutes%20%E2%80%93%20April%202026%20pt-BR.pdf), [`May 2026.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/Governance%20Meeting%20Minutes%20%E2%80%93%20May%202026.pdf), [`August 2026.pdf`](file:///Users/chris/Developer/interpride/governance/resources/00_2025_2026_email_versions/Governance%20Meeting%20Minutes%20%E2%80%93%20August%202026.pdf)

> **See [`COMPREHENSIVE_VERSION_ANALYSIS.md`](file:///Users/chris/Developer/interpride/governance/COMPREHENSIVE_VERSION_ANALYSIS.md) for the complete section-by-section diff across all 2022–2026 versions and the Governance Audit of textual corruptions and contradictions.**
