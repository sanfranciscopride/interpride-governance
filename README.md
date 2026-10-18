# InterPride Governance Repository & Canonical Digital Portal (`2022–2026`)

Welcome to the **InterPride Governance Committee Repository**. This repository houses:

1. **[`docs/` — The Canonical "Just the Docs" Jekyll Static Site](docs/index.md):**
   - **90+ structured Markdown pages** providing a searchable, deep-linkable digital edition of all current InterPride governing documents (`Bylaws 12.12.2025`, `Standing Rules 04.06.2026`, `Resolutions 03.20.2026`, `GAC Rules & Regulations 07.17.2026`, `2026 Organization Agreement & Confidentiality Matrix`, `June 7, 2026 Contact & Shared Drive Directory`, Grant Fund Policies, and Strategic Plan).
   - **Inline Governance Audit Errata & Restored Text Callouts:** Displays both the exact adopted PDF text and the restored canonical text where late-2025/2026 desktop-publishing layout corruptions occurred (e.g., [`Bylaws Article V, Section 12.B & Section 14`](docs/bylaws/article-05.md) and [`Bylaws Article II.R`](docs/bylaws/article-02.md)).
   - **Automated Longitudinal Diffs (`2022` → `2023` → `2024` → `2025` → `2026`):** Article-by-article and rule-by-rule historical diffs on every page.
   - **[Governance Committee Co-Chair Hub](docs/governance-hub/index.md):** Operational playbooks for [Ethics, Progressive Discipline, Grievance & Whistleblower Workflows](docs/governance-hub/ethics-and-grievance-playbook.md), [Board & GAC Candidate Verification & Elections](docs/governance-hub/elections-and-verification-playbook.md), and the [2026 Governance Committee Minutes & Workplan (`Apr–Aug 2026`)](docs/governance-hub/2026-minutes-and-workplan.md).
   - **[11-Point Governance Audit & Sept 30, 2026 Redline Tracker](docs/audit/index.md):** Ready-to-submit redline fixes for the Governance Committee's September 30, 2026 Standing Rules overhaul.

2. **[`COMPREHENSIVE_VERSION_ANALYSIS.md`](COMPREHENSIVE_VERSION_ANALYSIS.md):**
   - Complete standalone longitudinal analysis across all `2022–2026` versions of the Bylaws, Standing Rules, Resolutions, GAC Rules, Policies, and Agreements, plus the 11-point Governance Audit.

3. **[`GOVERNANCE_DOCS_INDEX.md`](GOVERNANCE_DOCS_INDEX.md) & [`resources/`](resources/):**
   - Complete local archive of **182 governing documents & financial filings** (**140 PDFs** from `interpride.org/resources/` across `01_bylaws/` through `07_strategy_reports_and_990s/` + **42 updated 2025–2026 attachments** in `resources/00_2025_2026_email_versions/`), along with full plaintext extractions in `resources/extracted_text/`.

---

## Site Architecture (`docs/`)

| Section | Path | Contents |
| :--- | :--- | :--- |
| **Portal Home** | [`docs/index.md`](docs/index.md) | Constitutional hierarchy diagram, currency matrix (`Website 2022–2024` vs. `Canonical 2025–2026`), and topic quick-links. |
| **Bylaws (`12.12.2025`)** | [`docs/bylaws/index.md`](docs/bylaws/index.md) | Overview + **13 individual Article pages** ([`article-01.md`](docs/bylaws/article-01.md) – [`article-13.md`](docs/bylaws/article-13.md)) with restored text callouts and `2022–2025` diffs. |
| **Standing Rules (`04.06.2026`)** | [`docs/standing-rules/index.md`](docs/standing-rules/index.md) | Overview + **52 individual Standing Rule pages** ([`sr-01-01.md`](docs/standing-rules/sr-01-01.md) – [`sr-12-01.md`](docs/standing-rules/sr-12-01.md)) with commentary, audit flags, and `2022–2026` diffs. |
| **Resolutions (`03.20.2026`)** | [`docs/resolutions/index.md`](docs/resolutions/index.md) | Overview + **6 thematic category pages** covering all active resolutions (`1983–2025`), including the restored Medellín Plenary floor amendments to `Resolution 24-02`. |
| **GAC Rules (`07.17.2026`)** | [`docs/gac/index.md`](docs/gac/index.md) | Full `07.17.2026` GAC Rules & Regulations (including the new 8-step Regional Representative election workflow), diff vs. `01.31.2024`, and the [2023 Transition Plan](docs/gac/transition-plan.md). |
| **Policies, Agreements & Funds** | [`docs/policies/index.md`](docs/policies/index.md) | [2026 Organization Agreement & 4-Tier Confidentiality Matrix](docs/policies/organization-agreement.md), [June 7, 2026 Contact & Shared Drive Directory](docs/policies/contact-and-storage-directory.md), [Values Statement](docs/policies/values-statement.md), [Grant Fund Policies](docs/policies/fund-policies.md), and [Strategic Plan (2025–2027) & Form 990s](docs/policies/strategic-plan-and-financials.md). |
| **Governance Committee Hub** | [`docs/governance-hub/index.md`](docs/governance-hub/index.md) | [Ethics, Grievance & Whistleblower Playbook](docs/governance-hub/ethics-and-grievance-playbook.md), [Elections & Candidate Verification Playbook](docs/governance-hub/elections-and-verification-playbook.md), and [2026 Committee Minutes & Workplan](docs/governance-hub/2026-minutes-and-workplan.md). |
| **11-Point Governance Audit** | [`docs/audit/index.md`](docs/audit/index.md) | Master Errata & Redline Action Tracker for the **September 30, 2026** Standing Rules overhaul. |

---

## Running or Deploying the Jekyll Site (`docs/`)

### Option 1: GitHub Pages (Zero Local Setup)
1. Push this repository to GitHub.
2. In **Settings → Pages**, set **Build and deployment** source to **Deploy from a branch**, select your branch (`main`), and select the **`/docs`** folder.
3. GitHub Pages will automatically build the site using [`docs/_config.yml`](docs/_config.yml) (`remote_theme: just-the-docs/just-the-docs@v0.10.0`).

### Option 2: Local Preview with Jekyll & Bundler
From the `docs/` directory:
```bash
bundle install
bundle exec jekyll serve --livereload
```
Then open `http://localhost:4000` in your browser.
