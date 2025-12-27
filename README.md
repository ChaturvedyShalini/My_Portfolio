# Shalini Chaturvedy - Portfolio Website

A modern, animated, professional portfolio website built with Django for a Computer Science graduate specializing in Data Analysis, Cloud, and Machine Learning.

![Portfolio Preview](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.0-38B2AC.svg)

## Features

### Visual Design
- Clean, modern tech + data analytics theme
- Dark mode / Light mode toggle
- Glassmorphism cards with soft gradients
- Responsive mobile-first design

### Animations
- Page load animations (fade + slide)
- Scroll-based reveal animations (AOS.js)
- Animated progress bars for skills
- Typing effect for hero section
- Count-up stats animation
- Hover effects on cards
- Timeline animation for experience
- Certification card flip effect

### Sections
1. **Hero Section** - Animated introduction with typing effect
2. **About Section** - Professional summary with animated counters
3. **Skills Section** - Categorized skills with progress bars
4. **Experience Timeline** - Vertical timeline with alternating cards
5. **Projects Section** - Project cards with hover effects
6. **Certifications Section** - Grid layout with badge cards
7. **Achievements Section** - Research highlights
8. **Contact Section** - Django form with SMTP integration

### Tech Stack
- **Backend**: Django 4.2+
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Animations**: GSAP, AOS.js
- **Database**: SQLite (development) / PostgreSQL (production)

## Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/shalini-portfolio.git
cd shalini-portfolio
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Populate sample data**
```bash
python manage.py populate_dataread this 
```

7. **Create admin superuser**
```bash
python manage.py createsuperuser
```

8. **Run the development server**
```bash
python manage.py runserver
```

9. **Open in browser**
- Website: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin

## Project Structure

```
shalini_portfolio/
├── portfolio/              # Main Django project settings
├── core/                   # Core app (home, about, settings)
├── projects/               # Projects app
├── experience/             # Experience/Timeline app
├── certifications/         # Certifications app
├── contact/                # Contact form app
├── templates/              # HTML templates
│   ├── base.html
│   ├── includes/
│   │   ├── navbar.html
│   │   └── footer.html
│   ├── core/
│   ├── projects/
│   ├── contact/
│   └── ...
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                  # User uploaded files
├── requirements.txt
└── manage.py
```

## Admin Panel

Access the admin panel at `/admin` to manage:
- **Site Settings**: Personal info, social links, SEO
- **Skills**: Add/edit skills with categories and proficiency
- **Experience**: Manage work history and internships
- **Projects**: Add portfolio projects with descriptions
- **Certifications**: Manage professional certifications
- **Achievements**: Add research and achievements
- **Contact Messages**: View submitted contact forms

## Customization

### Updating Content
1. Log into the admin panel
2. Navigate to the section you want to update
3. Add/edit content as needed

### Changing Colors
Edit the Tailwind config in `templates/base.html`:
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: { /* your colors */ },
                accent: { /* your colors */ }
            }
        }
    }
}
```

### Adding New Sections
1. Create a new template file
2. Include it in `core/home.html`
3. Add corresponding model/view if needed

## Deployment

### Render
1. Create a new Web Service
2. Connect your GitHub repository
3. Set environment variables
4. Build command: `pip install -r requirements.txt && python manage.py migrate`
5. Start command: `gunicorn portfolio.wsgi:application`

### Railway
1. Create new project from GitHub
2. Add environment variables
3. Deploy automatically

### AWS (Elastic Beanstalk)
1. Install AWS CLI and EB CLI
2. Initialize EB application
3. Configure environment variables
4. Deploy using `eb deploy`

## Email Configuration (Contact Form)

For Gmail SMTP:
1. Enable 2-factor authentication
2. Generate an App Password
3. Add to `.env`:
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Performance Optimizations

- Lazy loading images
- CSS/JS minification (via CDN)
- Whitenoise for static files
- Database query optimization
- Browser caching headers

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- **Design & Development**: AI-assisted development
- **Icons**: Font Awesome
- **Animations**: GSAP, AOS.js
- **CSS Framework**: Tailwind CSS
- **JS Framework**: Alpine.js

---

Made with love for Shalini Chaturvedy's Portfolio
