# 🌍 Mod Translation Manager: Community Master List

![License](https://img.shields.io/github/license/Zoonkky/Mod-Translation-Manager-Master-List?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![Data Integrity](https://img.shields.io/badge/Data-Validated-blue?style=flat-square)

> **The central brain of the Mod Translation Manager ecosystem.** > A decentralized, crowd-sourced database connecting Mod Hashes to their correct Translations across Nexus Mods.

---

## 🚀 The Mission

Modding should be about playing **in your language**, not spending hours hunting for the right translations.

Our primary goal is **Efficiency and Practicality**. We exist to eliminate the monotonous, repetitive process of manually searching, verifying versions, and downloading translations one by one on Nexus Mods.

**This project solves the chaos by automating the connection:**

* **⚡ Speed & Efficiency:** No more opening dozens of tabs. The Community List automatically detects which mods you have and instantly points to the correct translation.
* **🎯 Precision (Strict Hash Matching):** We don't just guess by ID. We identify your specific file (via MD5 Hash) to distinguish between Main Files, Patches, and optional downloads.
* **🛠️ Practicality:** Avoid broken games caused by installing the wrong translation on the wrong file. If the hash doesn't match, we warn you.

This repository collects the "Collective Intelligence" of the community, turning manual work into a seamless, automated experience for everyone.

## 📂 Repository Structure

* **`database/`**: The core memory. Contains validated JSON files for each language (e.g., `skyrimspecialedition_pt_br.json`).
* **`submissions/`**: The inbox. Community exports land here before being merged.
* **`scripts/`**: Automation tools for merging and validating data.

## 🎮 Supported Languages

We currently maintain active translation lists for:

| Code | Language | File |
| :--- | :--- | :--- |
| 🇧🇷 **PT-BR** | Portuguese (Brazil) | `..._pt_br.json` |
| 🇺🇸 **EN** | English | `..._en.json` |
| 🇫🇷 **FR** | French | `..._fr.json` |
| 🇩🇪 **DE** | German | `..._de.json` |
| 🇮🇹 **IT** | Italian | `..._it.json` |
| 🇪🇸 **ES** | Spanish | `..._es.json` |
| 🇷🇺 **RU** | Russian | `..._ru.json` |
| 🇨🇳 **ZH** | Chinese (Simp) | `..._zh_cn.json` |
| ... | And many others | (See database folder) |

## 🤝 How to Contribute

We believe in the power of the crowd. If your Mod Translation Manager has correct links that are missing here, share them!

1.  **Export:** In the app, click **"Export List"**.
2.  **Upload:** Fork this repo and upload your JSON to the `submissions/` folder.
3.  **PR:** Open a Pull Request.

👉 **[Read our Full Contribution Guide](CONTRIBUTING.md)**

## 🛡️ Data Policy & Quality

* **Strict Hash Matching:** We prioritize entries that include file hashes. This avoids "False Positives" on patches and optional files.
* **Version Sanitization:** Our scripts automatically clean up version numbers to ensure consistency.
* **Validation:** Every Pull Request passes through an automated check to ensure valid JSON syntax.

---

## ⚖️ License

This data is open for everyone.
Distributed under the **MIT License**. See `LICENSE` for more information.

Copyright © 2025 Zoonkky & Contributors.
