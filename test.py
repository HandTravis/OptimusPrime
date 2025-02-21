from dotenv import load_dotenv
import os

load_dotenv()

PAT = os.getenv('PAT')
print("Hello automated workflow!")
