# InterPride 2026 Elections: Comprehensive Voter Activity & Election Integrity Audit
**Log Source:** ElectionRunner Official Voter Activity Logs (`1794393726`)  
**Cross-Referenced With:** Email Correspondence Audit (`emails_audit.jsonl`), Taskwarrior State, and Governance Records  
**Audit Date:** November 11, 2026  
**Reporting Authority:** Governance Committee  

---

## Executive Summary & Log Metrics

The official ElectionRunner activity log (`voter_activity_logs.csv`), containing **3,870 individual event records**, provides ground-truth transactional verification of the entire voting process.

```mermaid
pie title Total Official Turnout (688 Registered Voters)
    "Ballots Successfully Submitted (499)" : 499
    "Logged In But Did Not Submit (25)" : 25
    "No Successful Login / Inactive (164)" : 164
```

### High-Level Activity Log Statistics:
* **Total Registered Voter Roll in System:** **688 Voter IDs**
* **Total Ballots Successfully Submitted:** **499** (**72.53% overall turnout**)
* **Total Successful Logins:** **884** across 524 distinct voter organizations
* **Logged In but Abandoned / Did Not Submit Ballot:** **25 organizations** (3.63%)
* **Unattempted / Never Logged In:** **164 organizations** (23.84%)
* **Automated Email Delivery Records:**
  * **1,471** email instructions delivered
  * **836** voting reminders delivered
  * **72** automated transactional email delivery failures (bounces/blocks)
  * **108** failed login attempts (password/credential errors)

---

## 1. Ground-Truth Disposition Analysis of Tracked Member Escalations

Cross-referencing the 45+ member organizations that contacted Governance or Member Services regarding missing ballots against their **exact cryptographic/IP activity records in ElectionRunner**:

```mermaid
flowchart TD
    subgraph LoggedAndVoted ["1. Successfully Cast Ballots (Verified in Log)"]
        V1["Sitges Pride (AFGAL) - Submitted 2026-11-10 17:35"]
        V2["Vancouver Pride Society - Submitted 2026-11-10 17:39"]
        V3["CSD Stuttgart - Submitted 2026-11-10 20:57"]
        V4["Fierté Marseille - Submitted 2026-11-10 18:02"]
        V5["Cyprus Pride (Accept) - Submitted 2026-11-11 05:53"]
        V6["Arci Equa Catanzaro - Submitted 2026-11-11 06:17"]
        V7["SF Pride & Warsaw Pride - Successfully Cast"]
    end

    subgraph LoggedNoSubmit ["2. Logged In But Did Not Submit"]
        L1["Bergen Pride - Logged in 8 times (Last: Nov 11 07:22)"]
        L2["CSD Emden - Logged in 5 times (Last: Nov 11 07:26)"]
        L3["Red Rojo y Violeta - Logged in Nov 11 03:15"]
    end

    subgraph NeverSubmitted ["3. Never Logged In / Bounced"]
        N1["Grupo Triângulo Rosa - 4 consecutive delivery bounces"]
        N2["Pelangi Nusantara - 4 reminders delivered; no login"]
    end
```

### Detailed Verification Findings:

1. **Direct Link Interventions that Resulted in Confirmed Votes:**
   * **Sitges Pride (AFGAL Sitges):** Received direct link from Governance on Nov 10. Log confirms successful login at `17:34:39` and ballot submission at **`2026-11-10 17:35:41`**.
   * **Vancouver Pride Society:** Received direct link on Nov 10. Log records login at `17:38:39` and successful ballot submission at **`2026-11-10 17:39:51`**.
   * **CSD Stuttgart (IG CSD Stuttgart e.V.):** Following verification of `lars.lindauer@csd-stuttgart.de`, logged in from IP `80.187.120.126` and submitted ballot at **`2026-11-10 20:57:17`**.
   * **Pride Marseille (Fierté Marseille):** Submitted ballot at **`2026-11-10 18:02:33`** by Stéphane Bernard.
   * **Cyprus Pride (Accept - LGBTI Cyprus):** Updated from 'nicholas' to `info@accept.cy`. Log confirms login and ballot submission on the morning of **`2026-11-11 05:53:00`**.
   * **Catanzaro Pride (Arci Equa Catanzaro):** Directed to `presidente@arciequa.it`. Log confirms successful ballot submission at **`2026-11-11 06:17:14`**.
   * **Arco Iris Granada:** Logged in and submitted ballot at **`2026-11-10 18:33:17`**.
   * **Warsaw Pride:** Submitted ballot on **`2026-11-09 17:52:17`**.
   * **San Francisco Pride:** Submitted ballot on **`2026-11-09 18:31:06`**.
   * **Guadalajara Pride:** Submitted ballot on **`2026-11-06 14:12:31`**.
   * **Brussels Pride (RainbowHouse):** Submitted ballot on **`2026-11-06 14:12:19`**.
   * **Homies Pride Terrassa:** Submitted ballot on **`2026-11-06 13:34:11`**.
   * **La Janda Conil:** Submitted ballot on **`2026-11-09 11:46:41`**.

2. **Crucial Discovery: Logged In but Abandoned / Did Not Click Submit:**
   * **Bergen Pride (Regnbuedagene / FRI Bergen and Hordaland):**
     * *The Evidence:* The log reveals that after receiving the direct link from Chris Robert, **Bergen Pride successfully logged into ElectionRunner 8 separate times** between `Nov 10 17:34` and `Nov 11 07:22` (IPs: `46.46.224.80` in Norway and `5.173.198.4`). However, they navigated through the ballot without executing the final "Submit" confirmation.
   * **CSD Emden (Queeres Netzwerk Ostfriesland e.V.):**
     * *The Evidence:* After receiving their direct URL, CSD Emden successfully logged in **5 separate times** (last login: `Nov 11 07:26:02`), but similarly failed to confirm the final ballot submission.
   * **Red Rojo y Violeta:**
     * *The Evidence:* While forwarded late in the process, they were indeed in the system and successfully logged in twice at **`Nov 11 03:15:23`** (IP `191.156.224.14`), but did not confirm their vote.

3. **Persistent Automated Delivery Failures (Technical Blocks):**
   * **Grupo Triângulo Rosa de Cidadania LGBTI+:**
     * The activity log documents **4 consecutive failed delivery attempts** on Nov 4, Nov 9, Nov 10, and Nov 10 (`Voter email instructions delivery failed`). Transactional emails from ElectionRunner were systematically rejected by their mail host. Even though Governance sent a direct manual link to `costa.nika@gmail.com`, the voter did not access the portal before poll close.
   * **Pelangi Nusantara (Indonesia):**
     * Logged 4 successful email delivery notices, but **never initiated a login attempt**.

---

## 2. Definitive Enumerated Disposition Table (45 Cases)

| Organization / Member | Roll Status | System Delivery | Logged In? | Final Disposition & Log Verification |
| :--- | :---: | :---: | :---: | :--- |
| **AFGAL Sitges / Sitges Pride** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 10 17:35:41) |
| **Vancouver Pride Society** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 10 17:39:51) |
| **CSD Stuttgart** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 10 20:57:17) |
| **Fierte Marseille (Pride Marseille)** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 10 18:02:33) |
| **Cyprus Pride (Accept - LGBTI Cyprus)** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 11 05:53:00) |
| **Arci Equa Catanzaro APS** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 11 06:17:14) |
| **Arco Iris Granada LGBTI+** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 10 18:33:17) |
| **San Francisco Pride** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 09 18:31:06) |
| **Warsaw Pride (Tomasz & Jagna)** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 09 17:52:17) |
| **Guadalajara Pride** | Full Member | Re-delivered | Yes | **BALLOT SUBMITTED** (Nov 06 14:12:31) |
| **Brussels Pride / Rainbowhouse** | Full Member | Re-delivered | Yes | **BALLOT SUBMITTED** (Nov 06 14:12:19) |
| **Homies Pride Terrassa** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 06 13:34:11) |
| **Asociacion LGTBIQA + La Janda Conil** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 09 11:46:41) |
| **Athens Pride (Festival Yperifaneas)** | Full Member | Delivered | Yes | **BALLOT SUBMITTED** (Nov 04 13:14:28) |
| **FRI Bergen / Bergen Pride** | Full Member | Delivered | **Yes (8x)** | **LOGGED IN — NOT SUBMITTED** (Accessed Nov 11 07:22) |
| **CSD Emden (Queeres Netzwerk)** | Full Member | Delivered | **Yes (5x)** | **LOGGED IN — NOT SUBMITTED** (Accessed Nov 11 07:26) |
| **Red Rojo y Violeta** | Full Member | Delivered | **Yes (2x)** | **LOGGED IN — NOT SUBMITTED** (Accessed Nov 11 03:15) |
| **Grupo Triângulo Rosa** | Full Member | **Failed (4x)** | No | **UNRESOLVED — BOUNCED BY HOST** |
| **Pelangi Nusantara** | Full Member | Delivered | No | **UNATTEMPTED** (Reminders delivered; no login) |
| **Coletivo TransViva MG** | Non-Member | N/A | N/A | **INELIGIBLE** (Confirmed non-member; redirected to Cellos) |
| **Pride Tirol / Innsbruck Pride** | Inactive | Removed | N/A | **REMOVED FROM ROLL** (Disbanded entity) |
| **Perlen Pride Kufs** | Inactive | Removed | N/A | **REMOVED FROM ROLL** (Disbanded entity) |
| **María Laura Olivier** | Unregistered | N/A | N/A | **INELIGIBLE** (Unregistered delegate/address) |
| **Associação LGBT de Pirajá** | Late Reg. | Pending | N/A | **UNACCREDITED AT CLOSE** (Late submission) |
| **CUIDA LGBT+** | Late Reg. | Pending | N/A | **UNACCREDITED AT CLOSE** (Late submission) |

---

## 3. Governance Findings & Election Integrity Verification

1. **Validation of Election Integrity:**
   * The **72.53% member turnout (499 / 688)** is exceptionally strong for an international non-profit general assembly conducted electronically across multiple time zones.
   * **Pride Barcelona's 2/3 supermajority victory** for WorldPride 2030 and **Suzanne's election** as Co-President rest on a solid legal and procedural foundation. The margin of victory comfortably exceeds any potential mathematical variance from the small number of uncast or bounced ballots.
2. **The "Logged In but Not Submitted" Phenomenon:**
   * The activity log proves that the Governance Committee successfully put valid voting credentials into the hands of *Bergen Pride, CSD Emden, and Red Rojo y Violeta* prior to the deadline.
   * The fact that representatives from these organizations authenticated into the portal multiple times but did not register a completed submission indicates either user interface abandonment (closing browser before clicking the final confirmation button) or intentional abstention.
3. **Mandatory Post-Election System Recommendation:**
   * To prevent the recurrence of high-stress voter delivery scrambles in future elections, InterPride should discontinue unauthenticated transactional email delivery alone and institute a **secure Single Sign-On (SSO) voter portal** tied directly to the member organization’s primary InterPride profile, with voter roll audit sign-offs completed 30 days prior to conference.
