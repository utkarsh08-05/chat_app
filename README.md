# Vartalap

Vartalap is a backend-driven chat application inspired by modern messaging platforms.
It focuses on conversation management, message persistence, and user interaction using a web-based architecture.

This project is designed to explore how real-world chat systems are built on the backend, rather than focusing on UI polish.

---

## 🚀 What This Project Does (Version 1)

Vartalap (v1) supports:

- User authentication and profiles
- One-to-one conversations between users
- Sending and storing text messages
- Conversation history persistence
- User avatars and media handling
- Basic deployment-ready configuration

The system is built to be deployable, maintainable, and easy to extend.

---

## 🧠 Why I Built This

I built Vartalap to understand how communication platforms manage:

- Conversation state
- Message flow between users
- Data modeling for chats
- Backend structure beyond simple CRUD apps

The goal was to work on a realistic backend problem rather than isolated algorithms or tutorial projects.

---

## 🏗️ Tech Stack

- Language: Python  
- Framework: Django  
- Database: SQLite (development)  
- Media Storage: Cloudinary  
- Deployment: Render / Railway  

---

## 📁 Project Structure (Key Files)

Important files to review:

- `vartalap/models.py`  
  Defines users, conversations, and messages.

- `vartalap/views.py`  
  Core logic for message sending, conversation handling, and responses.

- `vartalap/urls.py`  
  Request routing and API-style endpoints.

These files contain the primary logic implemented by me, beyond framework boilerplate.

---

## 🔑 Key Design Decisions

- Django ORM for relational data modeling
- Server-side message persistence for reliability
- Lightweight views to keep logic readable
- Cloud-based media storage to avoid local file limitations
- Focus on clarity over complexity for version 1

---

## 📚 What I Learned

While building Vartalap, I learned:

- How to design backend systems for communication workflows
- Structuring Django projects to reduce tight coupling
- Managing state and data consistency across conversations
- Writing cleaner, modular backend logic
- Preparing applications for deployment and scalability
- Thinking in terms of tradeoffs instead of just features

---

## ⚠️ Limitations (Version 1)

- No real-time messaging (polling-based updates)
- SQLite is not ideal for production scale
- Limited edge-case handling
- No group chats

These limitations were intentional to keep version 1 focused and understandable.

---

## 🔮 Future Roadmap

### Version 2 (Planned)

- Real-time messaging using WebSockets
- PostgreSQL as the primary database
- Improved authentication and authorization
- Better validation and error handling
- Clear separation of service and view layers

### Version 3 (Planned)

- Group chats and role-based conversations
- Message delivery and read receipts
- Rate limiting and spam prevention
- Scalable backend architecture considerations
- API-first design for mobile or frontend clients

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/vartalap.git
cd vartalap
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
