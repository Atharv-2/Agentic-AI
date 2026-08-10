from mcp.server.fastmcp import FastMCP

#Initialize the fastmcp
mcp=FastMCP("weather")#Tool name is weather

async def get_weather(location:str)->str:
    """Get the Weather Location"""
    return "It's Raining in Delhi"


if __name__=="__main__":
    mcp.run(transport="streamable-http")