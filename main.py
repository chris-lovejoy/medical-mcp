from mcp.server.fastmcp import FastMCP

mcp = FastMCP("medical-mcp")


@mcp.tool()
def get_bmi(height: float, weight: float) -> float:
    """
    Calculate the Body Mass Index (BMI) of a person.

    Args:
        height (float): The height of the person in meters.
        weight (float): The weight of the person in kilograms.

    Returns:
        float: The BMI of the person.
    """
    return weight / (height ** 2)


# def main():
#     print("Hello from medical-mcp!")


if __name__ == "__main__":

    print("Starting medical-mcp server...")
    
    # Start the server - this is what was missing
    mcp.run()


    # main()
