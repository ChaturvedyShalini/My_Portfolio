from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from core.models import SiteSettings, Skill, Achievement
from projects.models import Project
from experience.models import Experience
from certifications.models import Certification


class Command(BaseCommand):
    help = 'Populates the database with sample data for Shalini Chaturvedy portfolio'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')

        # Create Site Settings
        self.create_site_settings()

        # Create Skills
        self.create_skills()

        # Create Experience
        self.create_experience()

        # Create Projects
        self.create_projects()

        # Create Certifications
        self.create_certifications()

        # Create Achievements
        self.create_achievements()

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))

    def create_site_settings(self):
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        settings.name = "Shalini Chaturvedy"
        settings.title = "Data Analyst | Cloud & ML Enthusiast"
        settings.email = "shalini.chaturvedy@example.com"
        settings.location = "Bengaluru, Karnataka, India"
        settings.hero_subtitle = "Transforming raw data into meaningful insights. Passionate about leveraging cloud technologies and machine learning to solve real-world problems."
        settings.typing_texts = "Data Analyst,Cloud & ML Enthusiast,Python Developer,Problem Solver"
        settings.about_text = """I am a Computer Science graduate with a strong passion for data analysis, cloud computing, and machine learning. With hands-on experience from multiple internships at leading organizations, I specialize in transforming complex datasets into actionable insights that drive business decisions.

My expertise spans across Python programming, SQL databases, Power BI visualization, and AWS cloud services. I have successfully completed projects ranging from IPL analytics dashboards to crime rate prediction systems using machine learning.

I'm constantly learning and exploring new technologies to stay at the forefront of the data science field. My goal is to leverage data-driven solutions to create meaningful impact in organizations."""
        settings.github_url = "https://github.com/shalini-chaturvedy"
        settings.linkedin_url = "https://linkedin.com/in/shalini-chaturvedy"
        settings.projects_count = 3
        settings.internships_count = 4
        settings.certifications_count = 5
        settings.meta_description = "Shalini Chaturvedy - Data Analyst specializing in Cloud Computing, Machine Learning, and Data Visualization. View my portfolio showcasing projects in Python, AWS, Power BI, and more."
        settings.meta_keywords = "Data Analyst, Machine Learning, Cloud Computing, Python, AWS, Power BI, SQL, Data Science, Bengaluru"
        settings.save()
        self.stdout.write(f'  Created/Updated Site Settings')

    def create_skills(self):
        skills_data = [
            # Programming & Data
            {'name': 'Python', 'category': 'programming', 'proficiency': 90, 'icon_class': 'fab fa-python', 'order': 1},
            {'name': 'SQL / MySQL', 'category': 'programming', 'proficiency': 85, 'icon_class': 'fas fa-database', 'order': 2},
            {'name': 'Pandas / NumPy', 'category': 'programming', 'proficiency': 88, 'icon_class': 'fas fa-table', 'order': 3},
            {'name': 'Scikit-learn / TensorFlow', 'category': 'programming', 'proficiency': 75, 'icon_class': 'fas fa-brain', 'order': 4},
            {'name': 'ETL & Data Cleaning', 'category': 'programming', 'proficiency': 82, 'icon_class': 'fas fa-broom', 'order': 5},

            # Cloud & Systems
            {'name': 'AWS (EC2, S3, IAM)', 'category': 'cloud', 'proficiency': 80, 'icon_class': 'fab fa-aws', 'order': 1},
            {'name': 'Linux', 'category': 'cloud', 'proficiency': 75, 'icon_class': 'fab fa-linux', 'order': 2},
            {'name': 'VPC & Networking', 'category': 'cloud', 'proficiency': 70, 'icon_class': 'fas fa-network-wired', 'order': 3},
            {'name': 'Git & Version Control', 'category': 'cloud', 'proficiency': 78, 'icon_class': 'fab fa-git-alt', 'order': 4},

            # Visualization
            {'name': 'Power BI', 'category': 'visualization', 'proficiency': 90, 'icon_class': 'fas fa-chart-bar', 'order': 1},
            {'name': 'Excel (Advanced)', 'category': 'visualization', 'proficiency': 92, 'icon_class': 'fas fa-file-excel', 'order': 2},
            {'name': 'Matplotlib / Seaborn', 'category': 'visualization', 'proficiency': 85, 'icon_class': 'fas fa-chart-line', 'order': 3},
            {'name': 'Data Storytelling', 'category': 'visualization', 'proficiency': 88, 'icon_class': 'fas fa-book-open', 'order': 4},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.update_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} Skill: {skill.name}')

    def create_experience(self):
        experiences_data = [
            {
                'title': 'AWS Trainee',
                'company': 'Magic Bus Foundation',
                'experience_type': 'training',
                'location': 'Remote',
                'start_date': date(2024, 6, 1),
                'end_date': date(2024, 8, 31),
                'description': 'Comprehensive training program focused on AWS cloud services and infrastructure management.',
                'responsibilities': '''Configured and managed EC2 instances for various workloads
Implemented S3 storage solutions with proper access controls
Set up IAM policies and user management
Designed VPC architectures for secure networking
Gained hands-on experience with AWS CLI and CloudWatch''',
                'technologies': 'AWS EC2, S3, IAM, VPC, CloudWatch',
                'icon_class': 'fab fa-aws',
                'order': 1,
            },
            {
                'title': 'Data Analysis Intern',
                'company': 'Cognifyz Technologies',
                'experience_type': 'internship',
                'location': 'Remote',
                'start_date': date(2024, 4, 1),
                'end_date': date(2024, 5, 31),
                'description': 'Performed comprehensive data analysis tasks including data cleaning, exploration, and visualization to derive actionable business insights.',
                'responsibilities': '''Cleaned and preprocessed large datasets using Python and Pandas
Created interactive dashboards and reports using Power BI
Performed statistical analysis to identify trends and patterns
Collaborated with team members to present findings to stakeholders
Automated data processing workflows using Python scripts''',
                'technologies': 'Python, Pandas, Power BI, Excel, SQL',
                'icon_class': 'fas fa-chart-line',
                'order': 2,
            },
            {
                'title': 'Machine Learning Intern',
                'company': 'Codveda Technologies',
                'experience_type': 'internship',
                'location': 'Remote',
                'start_date': date(2024, 2, 1),
                'end_date': date(2024, 3, 31),
                'description': 'Developed and trained machine learning models for predictive analytics and classification problems.',
                'responsibilities': '''Built and trained ML models using Scikit-learn and TensorFlow
Performed feature engineering and data preprocessing
Evaluated model performance using various metrics
Implemented cross-validation and hyperparameter tuning
Documented ML pipelines and model architectures''',
                'technologies': 'Python, Scikit-learn, TensorFlow, Pandas, NumPy',
                'icon_class': 'fas fa-brain',
                'order': 3,
            },
            {
                'title': 'Big Data Intern',
                'company': 'Samsung Innovation Campus',
                'experience_type': 'internship',
                'location': 'Bengaluru',
                'start_date': date(2023, 10, 1),
                'end_date': date(2024, 1, 31),
                'description': 'Participated in an intensive Big Data program focusing on data engineering, processing, and analytics at scale.',
                'responsibilities': '''Learned big data processing concepts and technologies
Worked with large datasets using SQL and Python
Implemented ETL pipelines for data transformation
Collaborated on team projects involving data analysis
Completed capstone project on data analytics''',
                'technologies': 'Python, SQL, Big Data, Data Engineering',
                'icon_class': 'fas fa-database',
                'order': 4,
            },
        ]

        for exp_data in experiences_data:
            exp, created = Experience.objects.update_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} Experience: {exp.title} at {exp.company}')

    def create_projects(self):
        projects_data = [
            {
                'title': 'IPL Analysis Dashboard',
                'slug': 'ipl-analysis-dashboard',
                'short_description': 'Interactive Power BI dashboard analyzing IPL cricket data with player performance metrics and team statistics.',
                'description': '''A comprehensive Power BI dashboard that provides in-depth analysis of Indian Premier League (IPL) cricket data. This project showcases my ability to work with large datasets and create meaningful visualizations.

Key Features:
- Player performance tracking across seasons
- Team comparison and head-to-head analysis
- Match-wise statistics and trends
- Interactive filters for custom analysis
- Predictive insights based on historical data

The dashboard helps cricket enthusiasts and analysts understand patterns in player performances, team strategies, and match outcomes.''',
                'tech_stack': 'Power BI, SQL, Excel, Python',
                'github_url': 'https://github.com/shalini-chaturvedy/ipl-dashboard',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Business Cost Insight Dashboard',
                'slug': 'business-cost-insight-dashboard',
                'short_description': 'Comprehensive dashboard for analyzing business costs, profit margins, and financial KPIs.',
                'description': '''An enterprise-grade Power BI dashboard designed to provide businesses with actionable insights into their cost structures and profitability.

Key Features:
- Cost breakdown by department/category
- Profit margin analysis and trends
- Budget vs. actual comparisons
- Key financial KPIs at a glance
- Drill-down capabilities for detailed analysis

This project demonstrates my ability to translate business requirements into effective data visualization solutions that support decision-making.''',
                'tech_stack': 'Power BI, Excel, SQL, Data Analysis',
                'github_url': 'https://github.com/shalini-chaturvedy/cost-insight',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Crime Rate Prediction System',
                'slug': 'crime-rate-prediction-system',
                'short_description': 'Machine learning model to predict crime rates using historical data and socioeconomic factors.',
                'description': '''A machine learning project that uses historical crime data and socioeconomic indicators to predict crime rates in different regions. This project was presented at a national technical symposium.

Key Features:
- Data preprocessing and feature engineering
- Multiple ML algorithms comparison
- Model evaluation and validation
- Visualization of predictions
- API endpoint for real-time predictions

The system helps law enforcement and policymakers understand crime patterns and allocate resources effectively.''',
                'tech_stack': 'Python, Scikit-learn, Pandas, NumPy, Flask',
                'github_url': 'https://github.com/shalini-chaturvedy/crime-prediction',
                'is_featured': True,
                'order': 3,
            },
        ]

        for proj_data in projects_data:
            proj, created = Project.objects.update_or_create(
                slug=proj_data['slug'],
                defaults=proj_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} Project: {proj.title}')

    def create_certifications(self):
        certifications_data = [
            {
                'title': 'AWS Cloud Practitioner',
                'issuer': 'Amazon Web Services',
                'issue_date': date(2024, 7, 1),
                'description': 'Foundational understanding of AWS Cloud concepts, services, and terminology.',
                'icon_class': 'fab fa-aws',
                'order': 1,
            },
            {
                'title': 'Google Data Analytics Professional',
                'issuer': 'Google',
                'issue_date': date(2024, 5, 1),
                'description': 'Professional certification in data analytics, covering data cleaning, analysis, and visualization.',
                'icon_class': 'fab fa-google',
                'order': 2,
            },
            {
                'title': 'Python for Data Science',
                'issuer': 'IBM',
                'issue_date': date(2024, 3, 1),
                'description': 'Comprehensive Python programming for data science applications.',
                'icon_class': 'fab fa-python',
                'order': 3,
            },
            {
                'title': 'Machine Learning Specialization',
                'issuer': 'Stanford Online (Coursera)',
                'issue_date': date(2024, 4, 1),
                'description': 'In-depth machine learning concepts including supervised and unsupervised learning.',
                'icon_class': 'fas fa-brain',
                'order': 4,
            },
            {
                'title': 'Power BI Data Analyst',
                'issuer': 'Microsoft',
                'issue_date': date(2024, 2, 1),
                'description': 'Professional certification in creating and managing Power BI dashboards and reports.',
                'icon_class': 'fas fa-chart-bar',
                'order': 5,
            },
        ]

        for cert_data in certifications_data:
            cert, created = Certification.objects.update_or_create(
                title=cert_data['title'],
                issuer=cert_data['issuer'],
                defaults=cert_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} Certification: {cert.title}')

    def create_achievements(self):
        achievements_data = [
            {
                'title': 'Conference Presentation',
                'description': 'Presented research paper on "Crime Rate Prediction Using Machine Learning" at a national technical symposium, receiving recognition for innovative approach.',
                'icon_class': 'fas fa-microphone-alt',
                'date': date(2024, 3, 15),
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Samsung Innovation Campus Graduate',
                'description': 'Successfully completed the prestigious Big Data program at Samsung Innovation Campus with distinction, demonstrating expertise in data engineering and analytics.',
                'icon_class': 'fas fa-award',
                'date': date(2024, 1, 31),
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Academic Excellence',
                'description': 'Maintained consistent academic performance throughout Computer Science degree with focus on data science and analytics coursework.',
                'icon_class': 'fas fa-graduation-cap',
                'is_featured': False,
                'order': 3,
            },
        ]

        for ach_data in achievements_data:
            ach, created = Achievement.objects.update_or_create(
                title=ach_data['title'],
                defaults=ach_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} Achievement: {ach.title}')
