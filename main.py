from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("medical-mcp")

SERPER_URL = "https://google.serper.dev/search"

urls = {
    "NICE": "https://www.nice.org.uk/"
}




def search_web(query: str) -> str:  
    """
    Search the web for information on a given topic.
    """
    # TODO: implement this
    return "TODO"


def fetch_url(url: str) -> str:
    """
    Fetch a URL and return the content.
    """
    # TODO: implement this
    return "TODO"



@mcp.tool()
def get_nice_guidance(query: str) -> str:
    """
    Get guidance from NICE on a given topic.
    """
    # TODO: implement this
    return "TODO"


if __name__ == "__main__":

    print("Starting medical-mcp server...")
    
    mcp.run()
