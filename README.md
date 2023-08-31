# CRUD app using a Svelte frontend and a Django backend

Here is my take on a svelte-django web app. I made this mostly to get some experience with full stack development, but also to learn how Svelte and Django integrate together. I've gotten to the point where I can run my Svelte web server on port 5173 and my Django web server on port 8000, and the frontend can call fetch requests to the Django backend that will go on to interface with the database and so on. Ideally if I was going to deploy this to a real production environment I would want to package my svelte project into a static bundle and have Django serve those files, consolidating the two servers into one. For now as I am just playing around with the tech stack the two servers will suffice!

If you would like to try running the web app yourself, you could clone the repository (or make a codespace), run ```make install``` and in two separate terminals run ```make start-dev``` and ```make start-backend```.
