# 🌟 Bhuvanashree - Django Developer Portfolio & Web Application

[![Python](https://img.shields.io/badge/Python-3.15%20%7C%203.12-blue?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.1-green?logo=django&logoColor=white)](https://djangoproject.com)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)](https://render.com)
[![Status](https://img.shields.io/badge/Status-Active%20%26%20Production%20Ready-success)](#)

A modern, responsive full-stack web portfolio built with **Python**, **Django 6**, **HTML5/CSS3**, and **SQLite**. Featuring dynamic views, template inheritance, a database-backed contact form with admin review, and cloud deployment configuration for Render.

---

## 🚀 Live Demo & Preview
- **Live URL**: *(Deploying to Render - See instructions below)*
- **GitHub**: [github.com/bhuvanashreekr-del](https://github.com/bhuvanashreekr-del)

---

## ✨ Features

- 🎨 **Modern Glassmorphic UI**: High-contrast, sleek developer theme styled with custom responsive CSS, Google Font (*Plus Jakarta Sans*), subtle gradients, and micro-animations.
- ⚡ **Django MVT Architecture**: Clean separation of Models, Views, and Templates with an extensible `base.html` layout.
- 📱 **Fully Responsive**: Mobile-first fluid layout with a collapsible mobile navigation drawer.
- 📬 **Database-Backed Contact System**:
  - Validates user input with CSRF protection.
  - Automatically stores messages into SQLite via Django `ContactMessage` model.
  - Success alert feedback to user.
- 🛡️ **Django Admin Integration**: View, filter, and manage incoming messages via `/admin`.
- ☁️ **Production Cloud Ready**:
  - Configured with `gunicorn` WSGI server.
  - Static file compression & serving via `WhiteNoise`.
  - Automated deployment build script (`build.sh`) and `render.yaml` specification for Render.

---

## 📂 Project Structure

```text
myproject/
├── myproject/             # Django project settings & core routing
│   ├── asgi.py
│   ├── settings.py        # Configured for WhiteNoise, CSRF, and staticfiles
│   ├── urls.py            # Root URL dispatcher
│   └── wsgi.py            # WSGI entrypoint for Gunicorn
├── myapp/                 # Portfolio application
│   ├── admin.py           # ContactMessage registered in Admin
│   ├── models.py          # ContactMessage database model
│   ├── urls.py            # Application routes: '', 'about/', 'contact/'
│   ├── views.py           # Views for Home, About, Contact
│   ├── templates/myapp/   # Semantic Django templates
│   │   ├── base.html      # Shared header, navigation, and footer
│   │   ├── home.html      # Hero, stats, tech stack, feature cards
│   │   ├── about.html     # Biography, timeline, technical competencies
│   │   └── contact.html   # Direct info cards & interactive form
│   └── static/myapp/css/  # Custom styles
│       └── style.css      # Glassmorphism, animations, responsive design
├── build.sh               # Render build script (pip, collectstatic, migrate)
├── render.yaml            # Render infrastructure specification
├── requirements.txt       # Production dependencies
├── manage.py
└── README.md
```

---

## 🛠️ Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/bhuvanashreekr-del/django-practice.git
cd django-practice
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for Django Admin)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser!

---

## ☁️ Deploying to Render (Free Hosting)

1. Sign in to **[Render.com](https://render.com)** using your GitHub account (`bhuvanashreekr-del`).
2. Click **New +** > **Web Service**.
3. Select your GitHub repository (`django-practice`).
4. Configure the settings:
   - **Name**: `bhuvanashree-portfolio`
   - **Language**: `Python 3`
   - **Build Command**: `./build.sh` *(or `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`)*
   - **Start Command**: `gunicorn myproject.wsgi:application`
5. Click **Create Web Service**. Render will automatically build and publish your live website!

---

## 👤 Author
- **Bhuvanashree K R**
- GitHub: [@bhuvanashreekr-del](https://github.com/bhuvanashreekr-del)
- Email: [bhuvanashreekr@gmail.com](mailto:bhuvanashreekr@gmail.com)
