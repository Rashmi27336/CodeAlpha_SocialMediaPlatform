# 🌐 SocialConnect – Social Media Platform

A professional mini social media platform developed as part of the **CodeAlpha Full Stack Development Internship – Task 2**.

SocialConnect allows users to create accounts, log in, create posts, like posts, comment on posts, view profiles, and follow or unfollow other users.

---

## 📌 Project Overview

**SocialConnect** is a full-stack social media web application built using **Python and Django** for the backend and **HTML, CSS, and JavaScript** for the frontend.

The application demonstrates important full-stack development concepts such as:

- User authentication
- Database management
- CRUD operations
- Social interactions
- Django models and views
- Responsive frontend design
- JavaScript-based user interface enhancements

---

## ✨ Features

### 🔐 User Authentication

- User registration
- User login
- User logout
- Password validation
- Secure Django authentication
- Automatic profile creation for new users

### 📝 Posts

- Create new posts
- Display posts in the latest-first order
- Show username and post creation time
- Clean and responsive post interface

### ❤️ Likes

- Like posts
- Unlike posts
- Display total number of likes
- Prevent duplicate likes from the same user

### 💬 Comments

- Add comments to posts
- Display comments below posts
- Show the commenting user's username
- Display comment creation time

### 👤 User Profiles

- View personal profile
- Display username
- Display profile information
- Display followers count
- Display following count

### 👥 Follow System

- Discover other users
- Follow users
- Unfollow users
- Display follower and following relationships

### 🎨 User Interface

- Professional and modern design
- Responsive layout
- Clean navigation
- User-friendly forms
- Responsive cards and buttons
- Mobile-friendly styling

### ⚡ JavaScript Enhancements

- Post character counter
- Form submission loading state
- Logout confirmation
- Automatic message handling
- Mobile navigation support

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

## 🏗️ Project Structure

```text
CodeAlpha_SocialMediaPlatform/
│
├── core/
│   ├── migrations/
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   │
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
