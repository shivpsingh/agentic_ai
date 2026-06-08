from pydantic import Field
from mcp.server.fastmcp import FastMCP

app = FastMCP(name="Test MCP Server", instructions="Tool to be used when required to read and write to a listed file")

mock_data = {
    "file1.txt": "Hello, world!",
    "file2.txt": "This is the second file",
    "file3.txt": "This is the third file",
    "file4.txt": "This is the fourth file",
    "file5.txt": "This is the fifth file",
    "file6.txt": "This is the sixth file",
    "file7.txt": "This is the seventh file",
    "file8.txt": "This is the eighth file",
    "file9.txt": "This is the ninth file",
}

@app.tool(
    name="read_file",
    description="Read the contents of a file",
)
def read_file(file = Field(..., description="The path to the file to read")) -> str:
    return mock_data[file]

@app.tool(
    name="write_file",
    description="Write to a file"
)
def write_file(file = Field(..., description="The path to the file to write to"), content = Field(..., description="The content to write to the file")) -> str:
    mock_data[file] = content
    return "File written successfully"

@app.resource(
    uri="docs://documents",
)
def documents() -> list[str]:
    return list(mock_data.keys())

@app.resource(
    uri="docs://documents/{file}",
)
def document(file = Field(..., description="The path to the file to read")) -> str:
    return mock_data[file]


if __name__ == "__main__":
    app.run()