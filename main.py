from controller import start_cypher
from config import CypherConfig
from logger import enable_logging, disable_logging
from view import ask_logging_preference

def main():
    logging_enabled = ask_logging_preference()
    if logging_enabled == 'y':
        enable_logging()
    else:
        disable_logging()

    config = CypherConfig(min_shift=1, max_shift=9)
    start_cypher(config)

if __name__ == "__main__":
    main()