from controller import start_cypher
from config import CypherConfig
from logger import enable_logging, disable_logging

def main():
    user_choice_logger = input("Would you like to enable logging? (y/n): ").strip().lower()
    if user_choice_logger == 'y':
        enable_logging()
    else:
        disable_logging()

    config = CypherConfig(min_shift=1, max_shift=9)
    start_cypher(config)

if __name__ == "__main__":
    main()