import os
import argparse
from pydantic import BaseModel

class CLIArgs(BaseModel):
    URL: str
    retries: int

def open_env_file(cli_args)-> CLIArgs:
    default_values = {
        "URL": "storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json",
        "retries": 3
    }
    args_name = [arg for arg in dir(cli_args) if not arg.startswith("_")]
    setCLIArgs = CLIArgs(
        URL="",
        retries=0
    )
    for key in args_name:
        if not cli_args.__getattribute__(key):
            setCLIArgs.__setattr__(
                key,
            os.environ.get(
                key,
                default_values[key]
            )      
            )
        else:
            setCLIArgs.__setattr__(key, cli_args.__getattribute__(key))
    return setCLIArgs


def set_values_from_arg():
    # Create the parser
    parser = argparse.ArgumentParser(description="Program that inputs a JSON file via scrapping\
                                     and outputs a csv")

    parser.add_argument("--URL", type=str, default=None,
                        help="Set the URL where the program will scrap")
    
    parser.add_argument("--retries", type=str, default=None,
                        help="In case of internet failure, how many times \
                            should the program retry the connection")

    args = parser.parse_args()
    return args

