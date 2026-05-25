# Project LAKSHYA (ಲಕ್ಷ್ಯ)

> **Track:** APK Threat Analysis with C2 Detection  
> **Team Name:** Team Kavacha  
> **Institution:** PES University (EC Campus)  
> **Development Lifecycle:** 24–48 Hour Prototype Scale  

An automated, evasion-resistant Android mobile forensics pipeline designed for frontline law enforcement. LAKSHYA safely decompiles suspicious, brand-spoofed APKs, calculates dynamic threat confidence scores, maps code genealogy to track recycled malware strains, and visualizes shared Command-and-Control (C2) syndicates on an interactive dashboard with bilingual (English/Kannada) automated reporting.

---

## Key Platform Architecture

### 1. Automated Static Reverse-Engineering & Phishing Detection
To defeat advanced banking trojans that deploy anti-analysis or emulator-evasion tricks (instantly freezing or crashing when a sandbox environment is detected), LAKSHYA utilizes a 100% static forensic extraction pipeline built on top of `Androguard` and `Apktool`.
* **APK Analysis & Metadata Extraction:** Safely unpacks raw binary attributes and parses compiled `.dex` bytecode without runtime execution risks.
* **Permission & Manifest Analysis:** Automatically scans the structural definitions inside `AndroidManifest.xml` to flag malicious, high-risk access combinations (e.g., pairing background `INTERNET` socket access with sensitive `RECEIVE_SMS` privileges).
* **UI Spoofing Detection & Brand Security:** Executes string and regex matching algorithms through decompiled layout assets (`res/layout`). If an application targets trademarked keywords (e.g., *"State Bank of India Login"*, *"YONO Validation"*) but fails to match the institution's authentic cryptographic developer signature, a definitive mathematical brand-impersonation trace is flagged.

### 2. Statistical Validation Engine (Precision Tuning)
To protect law enforcement operations from disruptive alert fatigue, the platform implements a deterministic, weighted risk matrix to evaluate threats:
* **True Positive (TP) Maximization:** High-severity flags are isolated with maximum precision by combining cryptographic signature mismatches with explicit asset-spoof flags.
* **False Positive (FP) Mitigation (Contextual Triage):** If a standard utility application requests a sensitive permission but possesses an authorized institutional digital certificate and zero unauthorized trademark layout fragments, the system flags it as safe, dropping the false alarm rate to near 0%.

### 3. Code DNA Tracking & Call-Graph Fingerprinting
Malware syndicates constantly recycle codebase frameworks across separate campaigns. LAKSHYA treats software structural patterns like code DNA:
* **Function Call Graphs (FCG):** Maps out the internal architectural execution flowchart showing how code methods link and interact, converting this graph topology into a unique structural vector fingerprint.
* **Genealogy Comparison:** Even if developers rename variables, heavily obfuscate class files, or switch domain endpoints, LAKSHYA cross-checks the structural skeleton against a historical database to instantly link the sample to a known parent crime syndicate.

### 4. Cross-Case C2 Infrastructure Clustering
* **Forensic Artifact Extraction:** Automatically isolates and strips hardcoded domains, server IP addresses, and communication ports directly out of the decompiled configuration settings.
* **Network Flow Visualization:** Extracted Indicators of Compromise (IOCs) are cross-referenced with live threat intelligence feeds (`URLhaus`, `ThreatFox`, `AbuseIPDB`). Using `NetworkX` graph modeling, independent malware samples submitted from completely separate geographic districts are visually clustered together on a map if they communicate with overlapping IP blocks, identical registrars, or shared hosting networks.

### 5. Investigator Dashboard & Last-Mile Vernacular Reporting
* **Behavior Timeline:** Displays a logical, chronological visualization on the frontend, mapping exactly what actions the malware attempts sequentially based on its structural layout.
* **Bilingual Translation Gateway:** Erases technical boundaries for non-technical field constables by converting dense binary indicators into intuitive risk badges and plain-language summaries in both English and Kannada (*"ಈ ಅಪ್ಲಿಕೇಶನ್ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಒಟಿಪಿ (OTP) ಮತ್ತು ಸಂದೇಶಗಳನ್ನು ಕದ್ದು ಹ್ಯಾಕರ್‌ಗೆ ಕಳುಹಿಸುತ್ತದೆ"*).
* **Structured Forensic Reports:** Generates download-ready, legally sound technical summary PDFs formatted to be attached directly to an official First Information Report (FIR) or charge sheet, removing paperwork delays.

---

## Our Tech Stack & Dependencies

* **Frontend Dashboard:** ReactJS (TailwindCSS, to make interactive network graph rendering, timeline components)
* **Forensic Pipeline Backend:** Python (FastAPI / Flask framework)
* **Binary Processing Engines:** Androguard, Apktool
* **Graph Analytics Modeling:** NetworkX (for the Topology vector calculations and C2 node linkage)
* **Document Compilation Engine:** RAG-augmented deterministic language processing templates / PDF asset generators to make the FIR.

---

##  Project Repository Structure
```
├── README.md                        # Master Technical Documentation
├── docs/                            # Holds all registration and architectural design documents
│   ├── CIDECODE_2026_Abstract.pdf   # Final Formatted Abstract PDF for Registration
│   └── system_architecture_flow.pdf # Visual Forensic Pipeline & Feature Area Blueprints
├── src/                             # Main Source Directory wrapping all application code
│   ├── backend/                     # Python Forensic Extraction Backend (FastAPI/Flask)
│   │   ├── core_parsers/            # Manifest, Layout Resources & Artifact Extraction Logics
│   │   ├── genealogy/               # Function Call Graph (FCG) Extraction & Vectorization
│   │   └── clustering_engine/       # NetworkX Cross-Case Infrastructure Linkage Arrays
│   └── frontend/                    # ReactJS Investigator Triage Dashboard
│       ├── components/              # Interactive Network Flow Graphs & Malware Behavior Timelines
│       └── localization/            # English and Kannada Legal Phrase Data Dictionaries
└── templates/                       # Pre-formatted Layout Blueprints
    └── export_formats/              # FIR-Ready Structured Forensic Report Export Forms
```
