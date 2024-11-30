from dotenv import load_dotenv
import os
# initational enviroment

class Config:
    def __init__(self,env_path_file:str):
        self.env_path_file = load_dotenv(env_path_file)
        self.country = os.getenv("COUNTRY")
        self.state = os.getenv("STATE")
        self.city = os.getenv("CITY")
        self.start_date = os.getenv("START_DATE")
        self.end_date = os.getenv("END_DATE")
        self.api_key = os.getenv("API_KEY")
    def __call__(self):
        print(f"Country: {self.country}")
        print(f"State: {self.state}")
        print(f"City: {self.city}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"API Key: {self.api_key}")


if __name__=="__main__":
    config = Config('src\dotenv_test.env')
    print(config())