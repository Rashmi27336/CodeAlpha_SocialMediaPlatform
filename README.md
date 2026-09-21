# CodeAlpha Social Media Platform

A full-stack social media platform developed as part of the CodeAlpha Full Stack Development Internship.

The application allows users to create accounts, connect with other users, share posts, like and comment on posts, and manage their social connections.

---

## 🚀 Features

### 👤 User Authentication
- User registration
- User login
- User logout
- Secure password handling using Django authentication

### 📝 Posts
- Create posts
- Display latest posts
- View posts from different users

### ❤️ Likes
- Like posts
- Unlike posts
- Display total likes

### 💬 Comments
- Add comments to posts
- Display comments
- Display comment count

### 👥 Follow System
- View other users
- Follow users
- Unfollow users
- Display followers and following counts

### 👤 User Profiles
- Personal profile page
- Username display
- Followers count
- Following count
- Profile information

### 🎨 User Interface
- Professional and clean design
- Responsive layout
- Mobile-friendly interface
- Navigation between pages
- Interactive buttons and cards

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

## 📂 Project Structure

```text
CodeAlpha_SocialMediaPlatform/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── users.html
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── socialmedia/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── db.sqlite3
├── README.md
└── requirements.txt