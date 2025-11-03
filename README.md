# 🤖 AI Career Companion

## 🚀 Overview
**AI Career Companion** is an intelligent platform that helps users **plan, grow, and manage their professional careers automatically**.  
It analyzes resumes and online profiles, identifies skill gaps, recommends personalized learning paths, updates LinkedIn and other professional accounts, and even automates job applications — with full user consent.

### 🎯 Mission
To bridge the gap between **learning** and **employment** by using AI to guide, track, and promote a user’s professional growth in real time.

---

## 🧩 Core Features
| Feature | Description |
|----------|--------------|
| **Smart Profile Analyzer** | Parses resumes and LinkedIn profiles to extract skills, achievements, and goals. |
| **Career Gap Detection** | Identifies missing skills or experiences compared to targeted job roles. |
| **AI-Generated Roadmap** | Creates a step-by-step personalized learning and project plan. |
| **LinkedIn Integration** | Updates profile data, skills, and summaries using official LinkedIn APIs (partner permissions required). |
| **Job Discovery Engine** | Recommends suitable job openings based on user skills and goals. |
| **Auto-Apply Agent** | Applies to selected jobs automatically or semi-automatically (user approval required). |
| **Cover Letter Generator** | Uses LLMs to generate tailored application documents. |
| **Learning Integration** | Suggests relevant courses from Coursera, Udemy, and LinkedIn Learning APIs. |

---

## 🏗️ System Architecture

```

+------------------------------------------------------+
|                     FRONTEND                         |
|  React / Next.js / Tailwind / Redux / OAuth UI        |
+------------------------------------------------------+
| REST / GraphQL API calls
v
+------------------------------------------------------+
|                    BACKEND (API)                     |
|  FastAPI / Node.js + Express                         |
|  Auth, Resume Parser, AI Engine, Integrations         |
+------------------------------------------------------+
|                   |
+--------+--------+    +-----+----------------+
|  AI & ML SERVICES |  | EXTERNAL INTEGRATIONS|
| Resume Parser (spaCy) | LinkedIn API (OAuth) |
| Roadmap Generator (LLM)| Indeed / Coursera API |
| Job Matcher (SBERT)    | GitHub API (optional) |
+------------------------+----------------------+
|
v
+------------------------------------------------------+
|                  DATABASE LAYER                      |
| PostgreSQL (Core Data) + Redis (Cache) + S3 (Storage)|
| Pinecone/Milvus (Vector DB for embeddings)           |
+------------------------------------------------------+

```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | Next.js, React, TailwindCSS, Redux Toolkit |
| **Backend** | FastAPI (Python) or Node.js (Express) |
| **AI/ML** | OpenAI API / Hugging Face Transformers, spaCy, Sentence-BERT |
| **Database** | PostgreSQL, Redis, Pinecone (vector search) |
| **Authentication** | OAuth 2.0 (LinkedIn, Google), JWT |
| **Integrations** | LinkedIn, Indeed, Coursera, GitHub APIs |
| **Infrastructure** | Docker, AWS EC2, S3, CloudFront, GitHub Actions (CI/CD) |

---

## 🧠 AI Components

1. **Resume Parser** – Extracts skills, experience, education, and achievements using NLP.
2. **Skill Gap Analyzer** – Compares extracted skills to target role requirements.
3. **Roadmap Generator** – Uses LLM to build a personalized learning plan.
4. **Job Recommender** – Matches user profile embeddings with job posting embeddings.
5. **Auto-Apply Assistant** – Fills forms and sends applications after user approval.
6. **Cover Letter Generator** – Generates customized job applications with context awareness.

---

## 🔐 API Integrations

| Platform | Purpose | Access Method |
|-----------|----------|----------------|
| **LinkedIn** | Read profile data, suggest updates | OAuth 2.0 (`r_liteprofile`, `r_emailaddress`), partner write access |
| **Indeed / Glassdoor** | Job search & apply | Partner API (requires registration) |
| **Coursera / Udemy / LinkedIn Learning** | Fetch learning resources | REST APIs or affiliate integrations |
| **GitHub** | Pull repositories/projects for portfolio insights | OAuth integration |
| **OpenAI / Hugging Face** | AI text generation & embeddings | API key authentication |

> ⚠️ *Certain integrations (e.g., LinkedIn write access, auto-apply) require partnership approval.*

---

## 🧰 Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis
- Docker (optional)
- OpenAI API key (or any LLM provider)
- LinkedIn Developer Account (for OAuth setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ai-career-companion.git
cd ai-career-companion
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Update `.env`:

```
OPENAI_API_KEY=your_key
LINKEDIN_CLIENT_ID=your_id
LINKEDIN_CLIENT_SECRET=your_secret
DATABASE_URL=postgresql://user:pass@localhost:5432/career_ai
REDIS_URL=redis://localhost:6379
```

Run:

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The app runs on `http://localhost:3000`.

---

## 🧪 API Overview (Backend Endpoints)

| Endpoint            | Method | Description                            |
| ------------------- | ------ | -------------------------------------- |
| `/auth/linkedin`    | GET    | Initiate LinkedIn OAuth login          |
| `/users/me`         | GET    | Retrieve user profile                  |
| `/resume/upload`    | POST   | Upload and parse resume                |
| `/skills/gaps`      | GET    | Analyze skill gaps                     |
| `/roadmap/generate` | POST   | Generate personalized learning roadmap |
| `/jobs/search`      | GET    | Fetch relevant jobs                    |
| `/jobs/apply`       | POST   | Apply to job (requires user consent)   |
| `/profile/update`   | PUT    | Suggest LinkedIn profile updates       |

---

## 🧭 Development Workflow

1. **Branch naming:** `feature/<name>` or `fix/<issue>`
2. **Commit style:** Use [Conventional Commits](https://www.conventionalcommits.org/)
3. **Pull Requests:** Require 1 reviewer approval before merge
4. **Testing:**

   * Backend: `pytest`
   * Frontend: `jest`
   * Linting: `flake8`, `eslint`
5. **CI/CD:**

   * GitHub Actions for testing & deployment
   * Docker image auto-build to AWS ECR or Docker Hub

---

## 🧑‍💻 Contribution Guide

1. Fork the repository
2. Create a feature branch
3. Commit changes (`feat: added resume parser module`)
4. Push and open a Pull Request
5. Tag issues for maintainers to review

---

## 🧱 Folder Structure

```
ai-career-companion/
│
├── backend/
│   ├── app/
│   │   ├── api/              # API routes
│   │   ├── core/             # Config, logging
│   │   ├── models/           # Database models
│   │   ├── services/         # Business logic, AI integration
│   │   ├── utils/            # Helpers, parsers
│   │   └── main.py           # Entry point
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── store/
│   ├── utils/
│   └── package.json
│
├── docs/
│   ├── architecture.md
│   ├── api_spec.md
│   └── roadmap.md
│
└── README.md
```

---

## 🌱 Roadmap

| Phase       | Milestone                            | Status         |
| ----------- | ------------------------------------ | -------------- |
| **Phase 1** | Resume parsing & skill gap detection | ✅              |
| **Phase 2** | AI-generated learning roadmap        | 🟡 In progress |
| **Phase 3** | LinkedIn integration (read-only)     | 🔜             |
| **Phase 4** | Job discovery engine                 | 🔜             |
| **Phase 5** | Auto-apply assistant (partner APIs)  | 🔜             |
| **Phase 6** | Full multi-platform rollout          | ⏳ Future       |

---

## 🔒 Privacy & Compliance

* Follows **OAuth 2.0** standards for all integrations.
* Stores minimal user data.
* All third-party actions (profile update, job apply) require **explicit consent**.
* Complies with **GDPR**, **CCPA**, and **LinkedIn Partner Policy**.

---

## 💰 Monetization Plan

* **Freemium:** Core roadmap and analytics
* **Pro Tier:** Automated job applications + advanced AI roadmap
* **Enterprise:** Career dashboards for universities & bootcamps

---

## 📈 Future Enhancements

* AI career coach chat interface
* Real-time labor market analysis
* Cross-platform (GitHub, Kaggle, Behance) profile insights
* Skill certification via blockchain credentials

---

## 🧑‍🏫 Authors

**Founder:** [Tanshu](https://www.linkedin.com)
**Technical Lead:** OpenAI GPT-5 (assistant in architecture & design)
**License:** MIT

---

## 🧾 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🛠 Support

For technical support or integration help:
📧 Email: [support@careercompanion.ai](mailto:support@careercompanion.ai)
🌐 Website: [https://careercompanion.ai](https://careercompanion.ai)
