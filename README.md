# Redis Distributed Lock Demo

This project demonstrates a simple distributed locking mechanism using Redis and Flask.

## Problem
When multiple processes try to access the same resource simultaneously, race conditions may occur.

## Solution
Redis is used as a centralized locking system to ensure that only one process can access the resource at a time.

## Tech Stack
- Python
- Flask
- Redis

## Run the Project

1. Install Redis and start the server.
2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

python app.py

4. Open in browser:

http://127.0.0.1:5000/process

Try opening the endpoint from multiple tabs to observe locking behavior.
