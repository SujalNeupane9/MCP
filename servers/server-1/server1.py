import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")
DEFAULT_WORKSPACE = os.path.expanduser("./mcp/workspace")

# Ensure the workspace directory exists
os.makedirs(DEFAULT_WORKSPACE, exist_ok=True)

@mcp.tool()
def run_command(command: str) -> str:
    """Run a shell command inside the default workspace directory. Can be used to create files, read files, or execute any valid shell command."""
    try:
        # Ensure the workspace directory exists before each command
        if not os.path.exists(DEFAULT_WORKSPACE):
            os.makedirs(DEFAULT_WORKSPACE, exist_ok=True)
            
        result = subprocess.run(command, shell=True, cwd=DEFAULT_WORKSPACE, capture_output=True, text=True)
        if result.returncode != 0 and result.stderr:
            return f"Error: {result.stderr}"
        return result.stdout or result.stderr
    except Exception as e:
        return f"Exception occurred: {str(e)}"
    
if __name__ == "__main__":
    mcp.run(transport='stdio')