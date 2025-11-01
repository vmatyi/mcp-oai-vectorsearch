# Project Overview: MCP Server for ChatGPT Deep Research

This project is a sample Model Context Protocol (MCP) server that integrates with ChatGPT's Deep Research feature. It provides semantic search and document retrieval capabilities using OpenAI's Vector Store API.

## Key Information

*   **Purpose:** To demonstrate how to build a custom MCP server to extend ChatGPT with company-specific knowledge and tools.
*   **Technologies:**
    *   Python 3.8+
    *   `fastmcp`: For implementing the MCP protocol.
    *   `uvicorn`: As the ASGI server.
    *   `openai`: For interacting with the OpenAI Vector Store API.
*   **Core Functionality:**
    *   **Search Tool:** Performs semantic search on a configured OpenAI Vector Store and returns document chunks.
*   **Authorization:**
    *   The server uses a bearer token authentication mechanism.
    *   The token is passed in the `Authorization` header.
    *   The token is validated against the `SESSION_SECRET` environment variable.
*   **Entry Point:** The main application logic is in `main.py`.
*   **Dependencies:** Project dependencies are listed in `pyproject.toml` and `requirements.txt`.
*   **Vector Store:** The server is configured to use a specific vector store, which can be changed in `main.py`.

## My Role

My role is to assist with the development and maintenance of this MCP server. I can help with tasks such as:
*   Understanding the code in `main.py`.
*   Modifying the `search` tool.
*   Adding new tools to the MCP server.
*   Answering questions about the project's architecture and functionality.
