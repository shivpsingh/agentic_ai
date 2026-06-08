import asyncio
from mcp import stdio_client
from mcp.client.stdio import StdioServerParameters
from mcp.client.session import ClientSession
from contextlib import AsyncExitStack


class MCPClient:

    def __init__(self, command, args):
        self.command = command
        self.args = args
        self.exit_stack = AsyncExitStack()
        self.session = None

    async def connect(self):
        server_parameters = StdioServerParameters(
            command=self.command,
            args=self.args,
        )
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_parameters))
        self.session = await self.exit_stack.enter_async_context(ClientSession(stdio_transport[0], stdio_transport[1]))
        await self.session.initialize()

    def session(self):
        if self.session is None:
            raise ValueError("Session not connected")
        return self.session

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.exit_stack.aclose()
        self.session = None

    async def list_tools(self):
        return await self.session.list_tools()

    async def call_tool(self, tool_name, *args, **kwargs):
        return await self.session.call_tool(tool_name, *args, **kwargs)


async def main():
    async with MCPClient("python", ["mcp_server.py"]) as client:
        tools = await client.list_tools()
        print(tools)
        result = await client.call_tool("read_file", {"file": "file1.txt"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())