from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel, EmailStr
from pathlib import Path
import json

app = FastAPI()
mcp = FastApiMCP(app,exclude_operations=["delete_user"])


MOCK_DATA_FILE = Path("MOCK_DATA.json")


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    ip_address: str


# Utility function to read data from file
def read_data():
    if not MOCK_DATA_FILE.exists():
        return []
    try:
        with MOCK_DATA_FILE.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding mock data file")


# Utility function to write data to file
def write_data(data):
    with MOCK_DATA_FILE.open("w") as file:
        json.dump(data, file, indent=4)


@app.post("/add")
async def add_user(payload: User):
    """
    Add new records in the mock JSON file.
    """
    data = read_data()

    if any(user["id"] == payload.id for user in data):
        raise HTTPException(status_code=400, detail="User with this ID already exists")

    data.append(payload.dict())
    write_data(data)
    return {"message": "User added successfully", "user": payload}


@app.delete("/delete/{id}",operation_id="delete_user")
async def delete_user(id: int):
    """
    Delete records matching the provided id from the mock JSON file.
    """
    data = read_data()
    updated_data = [user for user in data if user["id"] != id]

    if len(updated_data) == len(data):
        raise HTTPException(status_code=404, detail="User with this ID not found")

    write_data(updated_data)
    return {"message": f"User with id {id} deleted successfully"}


@app.get("/all")
async def get_all_users():
    """
    Fetch all records  from the mock JSON file.
    """
    data = read_data()
    return {"data": data}

class NameRequest(BaseModel):
    first_name: str

@app.post("/data")
async def get_data_by_first_name(payload: NameRequest):
    """
    Fetch records matching the provided first_name from the mock JSON file.
    """
    if not MOCK_DATA_FILE.exists():
        raise HTTPException(status_code=404, detail="Mock data file not found")

    try:
        with MOCK_DATA_FILE.open("r") as file:
            data = json.load(file)

        matched_data = [item for item in data if item.get("first_name") == payload.first_name]

        if not matched_data:
            raise HTTPException(status_code=404, detail="No records found for the given first_name")

        return {"data": matched_data}
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding mock data file")

#mcp.setup_server()
mcp.mount()
mcp.setup_server()

def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()