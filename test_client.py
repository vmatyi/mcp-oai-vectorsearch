import asyncio
from fastmcp import Client

async def main():
    # Create a client that connects to the deployed server
    client = Client("https://mcp-oai-vectorsearch-78058204125.europe-central2.run.app/sse", auth="1Pv7NSdxXahkZmFliwaUMDugptCavl7nn/SlSzSMm1pzIrnLdthAsgajZRBf2rRXwe778iSGzaKAKLeiOzspHQ==")

    async with client:
        print("Client connected to FastMCP server.")

        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())
