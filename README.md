# 🌐 SocialConnect – Social Media Platform

A mini social media platform developed as part of the **CodeAlpha Full Stack Development Internship – Task 2**.

SocialConnect is a full-stack web application that allows users to create accounts, log in, create posts, like and comment on posts, view profiles, and follow or unfollow other users.

---

## 📌 Project Overview

The **SocialConnect** platform is designed as a simple social networking application.

Users can:

- Create an account
- Log in and log out
- Create and view posts
- Like and unlike posts
- Add comments
- View their profile
- Discover other users
- Follow and unfollow users
- View followers and following counts

The project uses **HTML, CSS, and JavaScript** for the frontend and **Python with Django** for the backend. **SQLite** is used as the database.

---

## ✨ Features

- 🔐 User Registration
- 🔑 User Login and Authentication
- 🚪 User Logout
- 📝 Create Posts
- ❤️ Like and Unlike Posts
- 💬 Add Comments
- 👤 User Profiles
- 👥 Follow and Unfollow Users
- 🔎 Discover Other Users
- 📊 Followers and Following Counts
- 🎨 Responsive and Professional UI
- ⚡ JavaScript UI Enhancements
- 🛠️ Django Admin Panel

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Django

### Database

- SQLite

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
CodeAlpha_SocialMediaPlatform/
│
├── core/
│   ├── migrations/
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── users.html
│   │
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── socialmedia/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
└── README.md
```

---

## 🗄️ Database Models

The application uses **Django ORM** with **SQLite**.

### Profile

Stores additional profile information associated with a user.

### Post

Stores posts created by users.

### Comment

Stores comments made by users on posts.

### Like

Stores likes given by users to posts.

### Follow

Stores the relationship between followers and the users they follow.

---

## 🏠 Main Pages

### 🏡 Home

The Home page allows users to:

- Create posts
- View recent posts
- Like and unlike posts
- Add comments
- View post information

### 🔐 Login

Registered users can securely log in using their username and password.

### 📝 Register

New users can create a SocialConnect account.

### 👤 Profile

The Profile page displays:

- Username
- Profile information
- Followers count
- Following count

### 👥 People

The People page allows users to:

- Discover other registered users
- Follow users
- Unfollow users

### ⚙️ Admin

The Django Admin panel allows administrators to manage:

- Users
- Profiles
- Posts
- Comments
- Likes
- Follows

---

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Rashmi27336/CodeAlpha_SocialMediaPlatform.git
```

### 2. Navigate to the Project Folder

```bash
cd CodeAlpha_SocialMediaPlatform
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Django Superuser

```bash
python manage.py createsuperuser
```

Enter the required username, email, and password when prompted.

### 8. Start the Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Django Admin Panel

The Django Admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

Administrators can use the panel to manage application data such as:

- Users
- Profiles
- Posts
- Comments
- Likes
- Follow relationships

---

## 🧪 Testing

The following features were tested during development:

- ✅ User Registration
- ✅ User Login
- ✅ User Logout
- ✅ Create Post
- ✅ Like Post
- ✅ Unlike Post
- ✅ Add Comments
- ✅ View Profile
- ✅ Follow User
- ✅ Unfollow User
- ✅ Discover Users
- ✅ Followers and Following Counts
- ✅ Django Admin Panel
- ✅ JavaScript Enhancements
- ✅ Responsive User Interface

---

## 🔒 GitHub Security

Sensitive and unnecessary local files are excluded from the GitHub repository using `.gitignore`.

The following files and folders are excluded:

```text
venv/
__pycache__/
*.pyc
db.sqlite3
.env
.vscode/
```

No passwords or authentication credentials are included in the repository.

---

## 🎓 CodeAlpha Internship

**Internship:** CodeAlpha Full Stack Development Internship

**Project:** Social Media Platform

**Task:** Task 2

This project was developed as part of the CodeAlpha Full Stack Development Internship.

The project demonstrates a full-stack social media application with:

- User profiles
- Posts
- Comments
- Likes
- Follow system
- User authentication

The application was developed using **HTML, CSS, JavaScript, Python, Django, and SQLite**.

---

## 🔮 Future Improvements

The following features can be added in future versions:

- 🖼️ Profile picture uploads
- 📷 Image uploads for posts
- ✏️ Edit posts
- 🗑️ Delete posts
- ✏️ Edit profile
- 🔔 Notifications
- 🔎 Search functionality
- 💬 Direct messaging
- 🌐 REST API integration
- ☁️ Cloud deployment

---

## 👩‍💻 Author

**V. Rashmi**

Information Science Engineering Student

GitHub:  
https://github.com/Rashmi27336

---

## 🙏 Acknowledgement

Thanks to **CodeAlpha** for providing the opportunity to develop this project as part of the **Full Stack Development Internship**.

---

## 📄 License

This project was created for **educational and internship purposes**.
