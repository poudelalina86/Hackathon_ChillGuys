# Hate Speech and Offensive Comment Detection Platform  

This project is a web-based platform designed to detect and manage hate speech and offensive comments effectively. Built using **HTML**, **CSS**, **JavaScript**, and **Django**, the platform offers user authentication, profile management, content moderation, and even a chatbot for user interaction.  

## Features  

### 1. **User Authentication**  
- Secure login and registration system with CSRF protection.  
- Passwords are hashed to ensure user security.  

### 2. **Content Moderation**  
- Automatic detection of hate speech and offensive comments using a pre-trained machine learning model.  
- Offensive comments are flagged or automatically deleted.  

### 3. **Profile Management**  
- Users can upload and update profile pictures.  
- Personal details (e.g., username, email) can be edited easily.  

### 4. **Interactive Chatbot**  
- A chatbot feature is included, allowing users to engage in conversations or ask platform-related queries.  

## Technologies Used  

### Frontend  
- **HTML**: Structuring web pages.  
- **CSS** (Tailwind CSS, Bootstrap): Styling and responsive design.  
- **JavaScript**: Adding interactivity and dynamic features.  

### Backend  
- **Django**: Server-side logic and database management.  
- **SQLite**: Default database for development.  
- **Pre-trained Machine Learning Model**: Detects hate speech and offensive comments using NLP.  

## Installation  

Set up the project locally with the following steps:  

1. **Clone the repository**  
   ```bash  
   git clone https://github.com/poudelalina86/HackathonChillGuys.git  
   cd HackathonChillGuys  
   ```  

2. **Set up a virtual environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Run migrations**  
   ```bash  
   python manage.py migrate  
   ```  

5. **Start the development server**  
   ```bash  
   python manage.py runserver  
   ```  

6. **Access the platform**  
   Open your browser and navigate to `http://127.0.0.1:8000/`.  

## Usage  

1. **Sign Up**: Create an account through the sign-up page.  
2. **Log In**: Access your account with your credentials.  
3. **Post Content**: Add posts or comments on the platform.  
4. **Moderation**: Offensive content is automatically flagged or deleted.  
5. **Chatbot**: Interact with the chatbot for assistance or casual conversations.  
6. **Edit Profile**: Update profile details and pictures.  

## Machine Learning Model  

The platform incorporates a pre-trained hate speech detection model stored in an `.pkl` file. The model leverages natural language processing (NLP) to predict whether a comment contains hate speech or offensive language.  

## Future Enhancements  

- Add a user dashboard with analytics, such as the number of flagged comments.  
- Implement a warning or penalty system for users who repeatedly post offensive content.  
- Extend support for detecting hate speech in multiple languages.  
- Send email notifications to users when their comments are flagged.  

## Contributing  

We welcome contributions! Fork the repository, create a feature branch, and submit a pull request. Suggestions and bug reports are encouraged.  

## Acknowledgments  

- **Django Documentation**: [Django Project](https://www.djangoproject.com/)  
- **Tailwind CSS**: [Tailwind CSS](https://tailwindcss.com/)  
- **Bootstrap**: [Bootstrap](https://getbootstrap.com/)  
- **Machine Learning Model**: NLP model for hate speech detection.  
