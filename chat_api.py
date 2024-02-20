from fastapi import FastAPI, HTTPException
from crud import read_thread, update_thread, delete_thread, create_thread
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class ThreadCreate(BaseModel):
    message: str

class ThreadUpdate(ThreadCreate, BaseModel):
    thread_id: str

class ThreadDelete(BaseModel):
    thread_id: str

app = FastAPI()
DATABASE_NAME = 'chat.db'

@app.get("/threads")
async def read_threads():
    threads_data = read_thread.get_threads(DATABASE_NAME)
    if not threads_data:
        raise HTTPException(status_code=404, detail="Threads not found")

    return JSONResponse(status_code=200, content={"threads": threads_data})

@app.get("/threads/{thread_id}")
async def get_thread(thread_id: str):
    thread_data = read_thread.get_thread_messages(thread_id, DATABASE_NAME)
    if not thread_data:
        raise HTTPException(status_code=404, detail="Threads not found")

    return JSONResponse(status_code=200, content={"thread": thread_data})

@app.post("/threads/")
async def write_thread(thread: ThreadCreate):
    thread_id, response = create_thread.create_thread(thread.message, DATABASE_NAME)
    if not thread_id:
        raise HTTPException(status_code=404, detail="Threads not found")
    return JSONResponse(status_code=200, content={"thread_id": thread_id, "user_msg": thread.message, "response": response})


@app.put("/update-threads")
async def update_threads(thread: ThreadUpdate):
    messages_data = read_thread.get_thread_messages(thread.thread_id, database=DATABASE_NAME)
    history = []
    for each_message in messages_data:
        history.append({"role": each_message[1], "content": each_message[2]})
    message = thread.message
    response = update_thread.update_thread(
        thread.thread_id, database=DATABASE_NAME, message=message, history=history
    )
    return JSONResponse(status_code=200, content={"thread_id": thread.thread_id, "user_msg": message, "response": response})

@app.delete("/delete-thread")
async def thread_delete(thread: ThreadDelete):
    delete_thread.delete_thread(thread.thread_id, database=DATABASE_NAME)
    return JSONResponse(status_code=200, content={"thread_id": thread.thread_id, "user_msg": "Thread deleted."})