from mcp.server.fastmcp import FastMCP

#Initialize the fastmcp
mcp=FastMCP("math")#Tool name is math


def add(a:int,b:int)->int:
    """Sum of Two Numbers"""
    return a+b


def multiply(a:int,b:int)->int:
    """Product of two numbers"""
    return a*b


if __name__=="__main__":
    mcp.run(transport="stdio")