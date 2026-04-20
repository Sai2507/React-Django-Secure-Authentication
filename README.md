# React Django Login

A full-stack web application demonstrating user authentication with React frontend and Django backend.

## Project Structure

```
react-django-login/
├── frontend/          # React.js application
│   ├── public/       # Static assets
│   ├── src/          # React components and pages
│   ├── package.json  # Frontend dependencies
│   └── README.md     # Frontend-specific documentation
└── backend/          # Django application
    ├── accounts/     # User authentication app
    ├── config/       # Django configuration
    ├── manage.py     # Django management script
    └── db.sqlite3    # SQLite database
```

## Tech Stack

- **Frontend**: React.js
- **Backend**: Django (Python)
- **Database**: SQLite
- **Authentication**: Django built-in auth system

## Features

- User login/logout
- Dashboard after authentication
- Session management
- RESTful API integration

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

## Available Pages

- **Login** (`/login`) - User authentication page
- **Dashboard** (`/dashboard`) - Protected page for authenticated users

## API Endpoints

- `POST /api/login/` - User login
- `POST /api/logout/` - User logout
- `GET /api/user/` - Get current user information

## Development

Both frontend and backend support hot-reloading during development. Make sure both servers are running:

1. Backend: `python manage.py runserver` (port 8000)
2. Frontend: `npm start` (port 3000)

## Building for Production

### Backend
No additional build step required. Configure Django settings for production.

### Frontend
```bash
cd frontend
npm run build
```

This creates an optimized production build in the `build/` directory.

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - feel free to use this project as a template.
