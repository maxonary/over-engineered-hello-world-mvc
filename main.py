from controller import start_cypher
from config import CypherConfig

if __name__ == "__main__":
    config = CypherConfig(min_shift=1, max_shift=9)
    start_cypher(config)
