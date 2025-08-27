# 🚀TweetApp in Django

## 📌 Introduction

**TweetApp in Django** is a simple yet powerful web application that replicates the basic functionalities of Twitter. Users can sign up, log in, create tweets, view tweets, like them, and manage their profiles. The project is built using the **Django framework** and follows the MVC (Model-View-Controller) pattern, ensuring scalability and clean code organization.

This project is suitable for learning purposes and can be extended into a more feature-rich social media platform.

---

## ✨ Features

* **User Authentication**

  * User Registration & Login/Logout
  * Profile management with profile picture support

* **Tweet Management**

  * Create new tweets
  * View tweets from all users
  * Like/unlike tweets

* **User Profile**

  * View user’s personal tweets
  * Edit profile details
  * Upload profile picture

* **Responsive UI**

  * Styled with **Bootstrap** for mobile and desktop compatibility

---

## ⚙️ Workflow

1. **User Registration / Authentication**

   * A new user signs up with their details.
   * Login is required to access tweeting and liking features.

2. **Tweet Creation**

   * Authenticated users can create tweets (short posts).
   * Tweets are displayed in the feed for all users.

3. **Interacting with Tweets**

   * Users can like/unlike tweets.
   * Tweets are linked to the user’s profile.

4. **Profile Management**

   * Users can view and update their profile, including uploading a profile picture.
   * Logout option is provided for account security.

---

## 📚 Libraries & Technologies Used

* **Backend**: Django (Python Web Framework)
* **Frontend**: HTML, CSS, Bootstrap
* **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
* **Authentication**: Django’s built-in authentication system
* **Static Files & Media**: Django static and media handling

---

## 🚀 Future Enhancements

* Add comment functionality on tweets
* Implement hashtags and search feature
* Real-time updates with Django Channels
* Notification system for likes and new followers

