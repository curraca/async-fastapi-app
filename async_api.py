from fastapi import FastAPI, Request, Depends, HTTPException, UploadFile, File, BackgroundTasks
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import asyncio
import aiofiles
import requests
import time
import logging

app = FastAPI(title="Async API with Issues")

# Hardcoded secrets
SECRET_KEY = "async-secret-789"  # FASTAPI-HARDCODED-SECRETS
DATABASE_URL = "postgresql://user:password@localhost/db"  # FASTAPI-HARDCODED-SECRETS

# Missing CORS configuration
# FASTAPI-MISSING-CORS

class UserRequest(BaseModel):
    name: str
    email: str
    password: str  # FASTAPI-PLAINTEXT-PASSWORD

class LoginRequest(BaseModel):
    username: str
    password: str  # FASTAPI-PLAINTEXT-PASSWORD

# Global in-memory storage (insecure)
users_db = {}  # FASTAPI-WEAK-SESSION
sessions_db = {}  # FASTAPI-WEAK-SESSION

@app.post("/api/users")  # FASTAPI-MISSING-RESP-MODEL, FASTAPI-MISSING-STATUS-CODE
async def create_user(user: UserRequest):
    # No authentication required
    # Plaintext password storage
    users_db[user.email] = {
        "name": user.name,
        "password": user.password,  # FASTAPI-PLAINTEXT-PASSWORD
        "created_at": time.time()
    }
    
    return {"message": "User created", "email": user.email}

@app.post("/api/login")  # FASTAPI-MISSING-AUTH
async def login(login_req: LoginRequest):
    # No rate limiting
    # Plaintext password comparison
    if login_req.username in users_db:
        stored_password = users_db[login_req.username]["password"]
        if login_req.password == stored_password:  # FASTAPI-PLAINTEXT-PASSWORD
            # Insecure session creation
            session_id = f"session_{login_req.username}_{time.time()}"
            sessions_db[session_id] = {"username": login_req.username}  # FASTAPI-WEAK-SESSION
            return {"token": session_id, "message": "Login successful"}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/api/profile")  # FASTAPI-MISSING-AUTH
async def get_profile(request: Request):
    # No authentication check
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    
    if token not in sessions_db:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    username = sessions_db[token]["username"]
    user_data = users_db.get(username, {})
    
    return {"username": username, "data": user_data}

@app.post("/api/upload")  # FASTAPI-FILE-UPLOAD-SIZE
async def upload_file(file: UploadFile = File(...)):
    # No file size limits
    # No file type validation
    contents = await file.read()
    
    # Unsafe file saving
    async with aiofiles.open(f"/tmp/{file.filename}", "wb") as f:  # FASTAPI-UNSAFE-FILE-ACCESS
        await f.write(contents)
    
    return {"filename": file.filename, "size": len(contents)}

@app.get("/api/files/{filename}")
async def get_file(filename: str):
    # Path traversal vulnerability
    file_path = f"/tmp/{filename}"  # FASTAPI-UNSAFE-FILE-ACCESS
    
    async with aiofiles.open(file_path, "r") as f:
        content = await f.read()
    
    return {"filename": filename, "content": content}

@app.post("/api/external")  # FASTAPI-BLOCKING-REQUESTS-IN-ASYNC
async def call_external_api():
    # Blocking requests in async handler
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")  # FASTAPI-BLOCKING-REQUESTS-IN-ASYNC
    return response.json()

@app.post("/api/process")
async def process_data(request: Request):
    # Unsafe JSON parsing
    body = await request.body()
    data = json.loads(body)  # FASTAPI-UNSAFE-JSON-PARSE
    
    # Process without validation
    return {"processed": data}

@app.get("/api/search")
async def search_data(request: Request):
    # Unvalidated query parameters
    search_term = request.query_params.get('q')  # FASTAPI-MISSING-VALIDATION
    limit = request.query_params.get('limit', '10')  # FASTAPI-MISSING-VALIDATION
    
    # Simulate database query
    query = f"SELECT * FROM data WHERE content LIKE '%{search_term}%' LIMIT {limit}"
    
    return {"search_term": search_term, "query": query}

@app.get("/api/redirect")
async def redirect_user(request: Request):
    # Unsafe redirect
    url = request.query_params.get('url')
    return RedirectResponse(url=url)  # FASTAPI-UNSAFE-REDIRECT

@app.post("/api/webhook")
async def webhook_handler(request: Request, background_tasks: BackgroundTasks):
    # No authentication for webhook
    # No rate limiting
    data = await request.json()
    
    # Process webhook without validation
    background_tasks.add_task(process_webhook, data)
    
    return {"status": "accepted"}

async def process_webhook(data: dict):
    # Background task without proper error handling
    # FASTAPI-MISSING-ERROR-HANDLER
    await asyncio.sleep(1)
    logging.info(f"Processing webhook: {data}")

@app.get("/api/config")
async def get_config():
    # Exposing sensitive configuration
    return {
        "secret_key": SECRET_KEY,  # FASTAPI-HARDCODED-SECRETS
        "database_url": DATABASE_URL,  # FASTAPI-HARDCODED-SECRETS
        "debug": True
    }

@app.get("/api/logs")
async def get_logs():
    # No authentication
    # Exposing log files
    async with aiofiles.open("/var/log/app.log", "r") as f:  # FASTAPI-UNSAFE-FILE-ACCESS
        logs = await f.read()
    
    return {"logs": logs}

@app.get("/api/sessions")
async def list_sessions():
    # No authentication
    # Exposing all sessions
    return {"sessions": list(sessions_db.keys())}

@app.delete("/api/sessions/{session_id}")
async def delete_session(session_id: str):
    # No authentication
    if session_id in sessions_db:
        del sessions_db[session_id]
        return {"message": "Session deleted"}
    
    return {"message": "Session not found"}

@app.get("/api/health")
async def health_check():
    # No authentication
    # Exposing internal health data
    return {
        "status": "healthy",
        "users_count": len(users_db),
        "sessions_count": len(sessions_db),
        "uptime": time.time()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)  # REPLIT-UVICORN-RELOAD
