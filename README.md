# Kremlin Voices (Голоса Кремля)

> A high-performance, bilingual open-source intelligence (OSINT) data visualization platform tracking political figures and state media personnel.

![Kremlin Voices Preview](https://img.shields.io/badge/UI-Dark_Mode_First-1a1a1a?style=flat-square)
![Performance](https://img.shields.io/badge/Lighthouse-100%2F100-brightgreen?style=flat-square)
![Zero Dependencies](https://img.shields.io/badge/Frontend_Dependencies-0-blue?style=flat-square)
![Bilingual](https://img.shields.io/badge/i18n-EN%20%7C%20RU-orange?style=flat-square)

## 📖 Overview

**Kremlin Voices** is a data journalism and civic tech project designed to systematically archive, structure, and visualize public data regarding individuals associated with Russian state media and political propaganda. 

Operating at the intersection of **web development** and **OSINT (Open Source Intelligence)**, the platform aggregates biographies, verifiable quotes, familial/financial connections, and international sanction histories (EU, US, UK, Canada, etc.) into comprehensive, easy-to-navigate dossiers.

This project was built with a strict focus on **performance, accessibility, and resilience**. By utilizing a static architecture without a heavy JavaScript framework, the site ensures instantaneous load times and robust resistance to traffic spikes or potential DDoS attacks.

## ✨ Key Features

- **High-Performance Static Architecture:** Fully vanilla HTML/CSS/JS frontend. Zero render-blocking requests, resulting in perfect Core Web Vitals and a 100/100 Lighthouse performance score.
- **Bilingual by Design (i18n):** Every single dossier and informational page is fully available in both English and Russian, expanding global reach.
- **OSINT Data Structuring:** Complex relational data (e.g., sanction timelines, inter-personal connections) is mapped out using semantic HTML and custom CSS Grids.
- **Advanced CSS Visuals:** Uses native SVG masking, radial gradients, CSS grid layouts, and typography (`Playfair Display` + `Inter`) to create a serious, editorial "investigative" UI—no Tailwind or Bootstrap required.
- **Automated Generation Pipeline:** Python scripting is utilized to parse data arrays, inject localized text, and programmatically generate over 70+ HTML pages, ensuring consistency across the platform.
- **SEO & Social Ready:** Fully integrated Schema.org microdata, OpenGraph tags, dynamic XML sitemaps, and RSS feeds for optimal search engine indexing.

## 🛠 Tech Stack

**Frontend:**
- **HTML5:** Semantic, accessible markup.
- **CSS3:** Advanced Grid/Flexbox layouts, CSS variables for theming (Light/Dark mode), native `@media` queries for responsive design, inline critical CSS for FCP optimization.
- **Vanilla JavaScript (ES6+):** Lightweight DOM manipulation, theme toggling, and keyboard navigation.

**Automation & Tooling:**
- **Python 3:** Build scripts (`/scripts`) used to parse text templates, map assets, and batch-generate HTML files.
- **Regex Parsing:** Extensive use of regular expressions to safely modify and refactor hundreds of DOM nodes across the codebase.

## 📂 Architecture & Project Structure

The project relies on a static generation approach, where Python scripts act as a primitive Static Site Generator (SSG), outputting ready-to-serve HTML.

```text
├── index.html, index-en.html        # Main catalog / landing pages
├── sanctions.html, quotes.html      # Data aggregation views
├── [person].html, [person]-en.html  # 70+ Individual bilingual dossiers
├── templates/                       # Localized, optimized media assets
└── scripts/                         # Python automation & generation scripts
```

## 🚀 Why Vanilla HTML/CSS/JS?

In an ecosystem dominated by heavy SPA frameworks (React, Vue), this project intentionally takes a "return to basics" approach:
1. **Resilience:** Static files hosted on Edge CDNs are virtually un-crashable.
2. **Speed:** By inlining critical CSS and removing JS bundle overhead, the site achieves sub-second First Contentful Paint (FCP).
3. **Engineering Depth:** Demonstrates a deep understanding of browser rendering, DOM APIs, and native CSS capabilities (like CSS-only theme variables and responsive clamp typography) without relying on abstractions.

## 🤝 Contributing

This is an open-source data archival project. If you spot a factual inaccuracy or wish to add verifiable, cited sources to an existing dossier, please open an Issue or submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
