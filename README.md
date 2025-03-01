# Social Media Platform

A Django-based social media platform where users can create profiles, upload posts, follow other users, and interact with content.

---

## Features

- **User Authentication**:
  - Sign up, log in, and log out functionality.
  - Password validation and secure storage.

- **User Profiles**:
  - Customizable profiles with bio, profile picture, and location.
  - Display follower and following counts.

- **Posts**:
  - Upload images with captions.
  - View posts from other users.
  - Like posts.

- **Follow System**:
  - Follow and unfollow other users.
  - Display followers and following lists.

- **Responsive Design**:
  - Works seamlessly on desktop and mobile devices.

---

## Technologies Used

- **Backend**:
  - Django (Python web framework)
  - Django ORM for database management
  - SQLite (default database for development)

- **Frontend**:
  - HTML, CSS, JavaScript
  - Bootstrap for styling

- **Other Tools**:
  - Pillow for image handling
  - Django Allauth (optional for advanced authentication)

---

## Installation

Follow these steps to set up the project locally.

1. Ensure you have Python and `pipenv` installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/milad-2003/SocialBook/
   cd SocialBook
   ```
3. Create a virtual environment and activate it:
   ```bash
   pipenv shell
   ```
4. Install dependencies:
   ```bash
   pipenv install
   ```
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
7. Access the admin panel at `http://127.0.0.1:8000/admin`
8. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
---

## Contributing

We welcome contributions to SocialBook! Here's how you can contribute:

1. **Fork the repository** to your GitHub account.
2. **Clone your fork** to your local machine:
   ```bash
   git clone <your_forked_repo_url>
   ```
3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b <branch_name>
   ```
4. Make your changes and commit them with descriptive messages:
   ```bash
   git commit -m "Add/Update/Remove <feature_description>"
   ```
5. Push your branch to your fork:
   ```bash
   git push origin <branch_name>
   ```
6. Open a pull request on the main repository and describe your changes.

---

For any queries or issues, feel free to open an issue in the repository.
