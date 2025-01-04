# Hate Speech and Offensive Comment Detection Platform

This project is a web platform designed to detect and delete hate speech and offensive comments. The platform is built using **HTML**, **CSS**, **JavaScript**, and **Django**, providing features like user authentication (sign in/sign up), profile management, and content moderation.

## Features

1. **User Authentication**
   - Secure login and registration system with CSRF protection.
   - Passwords are hashed for security.

2. **Content Moderation**
   - Automatic detection of hate speech and offensive comments using a pre-trained machine learning model.
   - Offensive comments are flagged or deleted automatically.

3. **Profile Management**
   - Users can upload and update their profile pictures.
   - Users can edit their personal details (e.g., username, email, etc.).

## Technologies Used

### Frontend
- **HTML**: For structuring the web pages.
- **CSS (Tailwind CSS, Bootstrap)**: For styling and responsive design.
- **JavaScript**: For interactive features.

### Backend
- **Django**: For server-side logic and database management.
- **SQLite**: Default database for development.
- **Pre-trained Machine Learning Model**: Used for detecting hate speech and offensive comments.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Asmiadhikari/hate-speech-detection.git
   cd hate-speech-detection
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
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Sign Up**: Create an account using the sign-up page.
2. **Log In**: Log in with your credentials.
3. **Post Content**: Add posts or comments on the platform.
4. **Moderation**: Offensive content is detected and automatically deleted or flagged.
5. **Edit Profile**: Update your profile picture and personal details.

## Machine Learning Model
The platform uses a pre-trained hate speech detection model. The model is stored in an `.h5` file and is loaded during server startup. The model predicts whether a comment contains offensive or hate speech using natural language processing (NLP).

## Future Enhancements
- Add a user dashboard with analytics (e.g., number of flagged comments).
- Implement a warning system for users who post offensive content.
- Extend support for multiple languages in hate speech detection.
- Add email notifications for flagged comments.

## Contributing
Feel free to fork this repository and submit pull requests. Any contributions, suggestions, or bug reports are welcome!

## Acknowledgments
- **Django Documentation**: [Django Project](https://www.djangoproject.com/)
- **Tailwind CSS**: [Tailwind CSS](https://tailwindcss.com/)
- **Bootstrap**: [Bootstrap](https://getbootstrap.com/)
- **Machine Learning Model**: Pre-trained NLP model for hate speech detection.

---

