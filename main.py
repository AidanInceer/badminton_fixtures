from badminton_fixtures.generator import Generator
from badminton_fixtures.ingestor import Ingestor
from badminton_fixtures.utils.config import Config

if __name__ == '__main__':
    i = Ingestor()
    g = Generator()
    config = Config().create_config()
    print(config)

    i.ingest()