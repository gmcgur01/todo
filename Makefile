start-dev:
	cd frontend && npm run dev

start-backend:
	cd backend && python3 manage.py runserver

install:
	pip install -r requirements.txt
	cd frontend && npm install
