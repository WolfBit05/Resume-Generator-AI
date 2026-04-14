# Resume-Generator-Ai

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

**Resume-Generator-Ai** is a modern, responsive, and schema-compliant frontend application designed to collect professional resume data. It features a sleek interface with Dark/Light mode support, dynamic form fields, and strictly structured JSON output optimized for backend processing.

## 🚀 Features

### 🎨 UI/UX Design
- **Professional Aesthetic:** Built with a "Glassmorphism" inspired dark mode and a clean, high-contrast light mode.
- **Theme Toggle:** Persistent Dark/Light mode switch (saves preference to LocalStorage).
- **Responsive Layout:** Fully optimized for desktop and mobile devices.
- **Micro-interactions:** Smooth animations for adding/removing rows and transitioning between modes.

### 🛠 Functional Capabilities
- **Two Entry Modes:**
  - **Detailed Builder:** Structured form with validation.
  - **Quick Sync:** Raw text paste or file upload for parsing.
- **Dynamic Sections:** Add or remove unlimited rows for *Experience*, *Education*, *Projects*, *Skills*, and *Certificates*.
- **Smart Input:** Typing a comma (`,`) in specific fields (e.g., Company Name) automatically adds a new entry row.
- **Passport Photo Module:** Instant image preview for profile headshots.
- **Schema Validation:** The final output is a structured JSON object strictly matching the backend `schema.py`.

---

## 📂 Project Structure

```text
/ResumAI-Pro
│
├── index.html      # Main HTML structure and layout
├── style.css       # CSS variables, animations, and responsive design
├── script.js       # Logic for dynamic rows, theme toggle, and JSON generation
└── README.md       # Project documentation
📦 Output Data Schema
When the user clicks "Generate JSON", the application logs an object to the browser console matching the following structure:

JSON

{
  "personal_info": {
    "full_name": "String",
    "phone_number": "String",
    "email": "String"
  },
  "objective": "String",
  "skills": [
    {
      "skill_type": "String",  // e.g., "Frontend"
      "skills": ["String", "String"] // e.g., ["React", "Vue"]
    }
  ],
  "experience": [
    {
      "company": "String",
      "role": "String",
      "description": "String"
    }
  ],
  "projects": [
    {
      "name": "String",
      "description": "String"
    }
  ],
  "education": [
    {
      "institution": "String",
      "degree": "String"
    }
  ],
  "certificates": ["String"]
}
⚡ Quick Start
Clone or Download the repository.

Ensure index.html, style.css, and script.js are in the same directory.

Open index.html in any modern web browser (Chrome, Firefox, Edge).

Test the Output:

Fill in the form details.

Click Generate JSON.

Open Developer Tools (F12 or Ctrl+Shift+I) and check the Console tab to see the output object.

🔧 Customization
Changing the Color Scheme
Open style.css and modify the CSS variables in the :root (for Dark Mode) or [data-theme="light"] block.

CSS

:root {
    --accent: #6366f1; /* Indigo - Primary Action Color */
    --bg: #0b0f1a;     /* Background Color */
}
Modifying Form Fields
To add new fields, update the HTML in index.html and ensure you capture the value in the resumeForm.addEventListener block inside script.js.

🤝 Contributing
Contributions, issues, and feature requests are welcome!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

Happy Building! 🚀