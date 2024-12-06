# Cheltenham Festival Racing Website

A Django-based web application dedicated to showcasing the Cheltenham Festival—one of the premier events in the National Hunt racing calendar. This site highlights daily race information, results, historical data, and leverages an external API to fetch the latest race cards in real-time.

## Features

- **API Integration:** Fetches daily race cards from an external API to ensure up-to-date information.
- **Historical Results & Top Runners:** Access past winners and track records.
- **Responsive UI:** Built with HTML, CSS, and Bootstrap for a seamless desktop and mobile experience.
- **Caching for Improved Performance:** Integrates Redis for server-side caching of frequently accessed data.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite or PostgreSQL  
  *(Originally used PostgreSQL; switched to SQLite for cost-free alternative.)*
- **Caching:** Redis (via `django_redis`)
- **External API:** Used to retrieve the latest race cards

## Getting Started

### Prerequisites

- **Python 3.8+**
- **pipenv** or **virtualenv** (optional but recommended)
- **PostgreSQL or SQLite** installed and configured
- **Redis** running locally or remotely

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dyson1664/cheltenham-festival-website.git
   cd cheltenham-festival-website
   venv/scripts/activate

2. **Install Dependencies**
```
    pip install -r requirements.txt
```

3. **Configure the Database**
- **For SQLite, the default Django settings often work out-of-the-box.**
- **For PostgreSQL, update DATABASES in** ```settings.py```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. **Set up Redis Caching (Optional but Recommended)**
- **Make sure Redis is running locally or specify an external ```REDIS_URL``` in your environment:**

```
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
```

## Environment Variables

Create a `.env` file in the project’s root directory and add your credentials:

```bash
RACING_API_USERNAME=your_username
RACING_API_PASSWORD=your_password
REDIS_URL=redis://localhost:6379
```

## Run Migrations
```python manage.py runserver```

## Running the Server
```python manage.py runserver```
