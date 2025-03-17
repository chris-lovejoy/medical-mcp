import httpx
import json
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

mcp = FastMCP("medical-mcp")

SERPER_URL = "https://google.serper.dev/search"

urls = {
    "NICE": "www.nice.org.uk/"
}



async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 3})
    
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}


async def fetch_url(url: str) -> str:
   async with httpx.AsyncClient() as client:
       try:
           response = await client.get(url, timeout=30.0)
           soup = BeautifulSoup(response.text, "html.parser")
           text = soup.get_text()
           return text
       except httpx.TimeoutException:
           return "Timeout error"


@mcp.tool()
async def get_nice_guidance(query: str) -> str:
    """
    Get guidance for a given topic from NICE.

    Args:
        query (str): The topic to get guidance for (eg. "high blood pressure")

    Returns:
        str: The guidance for the given topic.
    """

    query = f"site:{urls['NICE']} {query}"
    results = await search_web(query)
    if len(results["organic"]) == 0:
        return "No results found"
       
    text = ""
    for result in results["organic"]:
        text += await fetch_url(result["link"])
    return text


if __name__ == "__main__":

    print("Starting medical-mcp server...")
    
    mcp.run(transport="stdio")
