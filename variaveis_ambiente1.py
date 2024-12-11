from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()


print(os.getenv('BD_USER'))
print(os.getenv('BD_SENHA'))
print(os.getenv('BD_PORTA'))
print(os.getenv('BD_HOST'))
