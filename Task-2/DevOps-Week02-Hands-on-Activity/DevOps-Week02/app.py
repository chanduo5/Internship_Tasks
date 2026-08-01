import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def greet(name):
    logger.info(f"Greeting requested for {name}")
    return f"Hello, {name}! Welcome to DevOps Week 02."

if __name__ == "__main__":
    print(greet("Team"))
