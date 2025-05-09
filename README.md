# ShowYourSpot

**Live Demo:** [https://www.showyourspot.com](https://www.showyourspot.com)

*A social platform to share images of the places you love, built with Django.*

Developer: Diane Corriette - [GitHub](https://github.com/djangify) & [Website](https://www.djangify.com/)

---

## 📋 Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Testing](#testing)
* [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## ✨ Features

* 🔐 **Authentication:** User registration, login/logout, password reset
* 👤 **Profiles:** Avatar upload, bio, and profile editing
* 📸 **Photo Sharing:** Upload, edit, and delete spot photos
* 🗺️ **Geolocation:** Tag spots on an interactive map
* 🔍 **Discovery:** Browse by location, tags, or popularity
* ❤️ **Engagement:** Like, comment, and follow other users
* 📝 **Blog Posts:** Create and browse travel stories

---

## 🏗️ Tech Stack

| Layer        | Technology                        |
| ------------ | --------------------------------- |
| **Backend**  | Django                            |
| **Frontend** | Django Templates, HTML5, CSS3, JS |
| **Database** | MariaDB (dev), MariaDB (prod)   |
| **Storage**  | Local Filesystem / Django        |
| **Server**   | Gunicorn / Passenger WSGI         |
| **Testing**  | Pytest                            |

Dependencies are listed in [requirements.txt](requirements.txt).

---

## 🚀 Prerequisites

* Python 3.8+
* pip
* virtualenv (recommended)

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/djangify/our-spot.git
   cd our-spot
   ```
2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\\Scripts\\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```
5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```
6. **Collect static assets**

   ```bash
   python manage.py collectstatic
   ```
7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to see the app in action.

---

## ⚙️ Configuration

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```
2. Update the following in `.env`:

   ```text
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3  # or your production DB URL

   ```

---

## 🎯 Usage

1. Register or log in.
2. Upload your favorite spots and tag them on the map.
3. Browse, like, comment, and follow other explorers.
4. Write and share travel stories in the blog section.

Admin panel available at `/admin/`.

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

---

## 🚢 Deployment

This app can be deployed on cpanel or on platforms like Railway. Key steps:

1. Set environment variables in your host.
2. Use PostgreSQL for production database.
3. Configure settings for static/media files.
4. Ensure `DEBUG=False` and proper `ALLOWED_HOSTS`.

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repo.
2. Create a branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add YourFeature'`.
4. Push: `git push origin feature/YourFeature`.
5. Open a Pull Request to `main`.

Ensure tests pass and code is linted before submitting.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📫 Contact

* 🌐 Website: [showyourspot.com](https://www.showyourspot.com)
* 📂 Repo: [djangify/our-spot](https://github.com/djangify/our-spot)
* 👩‍💻 Developer: Diane Corriette ([@todiane](https://github.com/djangify))


Live Demo: https://www.showyourspot.com



<p align="right">(<a href="#table-of-content">back to top</a>)</p>

