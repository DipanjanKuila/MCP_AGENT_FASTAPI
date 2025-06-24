# MCP_AGENT_FASTAPI
# 🚀 MCP Agent with FastAPI Integration

## 📹 Demo Video

[▶️ Watch the Demo](./assets/demo.mp4)


This project demonstrates how to **easily convert your FastAPI APIs into an MCP (Modular Command Protocol) server** using `fastapi-mcp`. It includes:

- Multiple CRUD endpoints
- Integration with `MCPClient` and `MCPAgent`
- Selective endpoint exposure as MCP tools
- Built-in schema flexibility (robust against schema changes)
- Persistent storage using a `mockdata.json` file

---

## 📦 Features

✅ Simple FastAPI app integrated with `FastApiMCP`  
✅ Endpoints automatically available as MCP tools  
✅ Schema changes do **not break** the MCP server  
✅ Custom control to **exclude** specific endpoints from MCP (like `delete_user`)  
✅ Works out-of-the-box with `MCPAgent` using a config file  
✅ Video demo available 

---

## 📁 Project Structure
```
├── main.py # FastAPI app + MCP mounting
├── client.py # Asynchronous memory chat using MCPAgent
├── config.json # MCP server configuration
├── MOCK_DATA.json # Local data store for user records
└── README.md # Project documentation
```


## How MCP Works with FastAPI
- The FastApiMCP class wraps your FastAPI app.
- All valid routes (except the ones you exclude) are turned into MCP tools.
- You can use these tools with an MCPAgent, allowing LLMs to interact with your app programmatically.

## Benefits
- 🔧 Turn any FastAPI route into an LLM tool instantly.
- 🔒 Secure control by excluding sensitive endpoints.
-🧠 Built-in memory and reasoning with MCPAgent.
-🛠️ Schema-agnostic: your server won't break due to model changes.

## ▶️ How to Run
### Install dependencies
pip install fastapi uvicorn pydantic fastapi-mcp langchain_openai
### Start the FastAPI MCP server
uvicorn main:app --reload
### Run the memory-based interactive chat (client)
python client.py

