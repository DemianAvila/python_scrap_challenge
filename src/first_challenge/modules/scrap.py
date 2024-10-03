import requests
import json
from . import cli_args_model
from bs4 import BeautifulSoup
from pydantic import BaseModel


class ParsingStatus(BaseModel):
    hasError: bool
    errorDescription: str
    htmlResponse: str



def __request_from_page(const_values: cli_args_model.CLIArgs) -> ParsingStatus:
    try_num = 0
    while try_num<const_values.retries:
        try:
            response: requests.Response = requests.get(
                f"http://{const_values.URL}"
            )
            return ParsingStatus(
                hasError=False,
                errorDescription="",
                htmlResponse=response.text,
            )
        except Exception as e:
            if try_num==const_values.retries:
                return ParsingStatus(
                    hasError=True,
                    errorDescription=f"Error in request {e.with_traceback}",
                    htmlResponse="", 
                )
            else:
                try_num+=1


def __parse(raw_html:ParsingStatus):

    # NOTE
    """
    NORMALY, WHEN SCRAPPING, I WOULD USE BEAUTIFUL SOUP TO PARSE 
    THE OBTAINED INFO FROM THE HTML, BUT, SINCE THE URL IS ALREADY RETURNING 
    JSON INFORMATION, I'LL JUST PARSE IT IN  DICT
    """
    #soup = BeautifulSoup(raw_html.htmlResponse)
    #print(soup.prettify())

def scrap(const_values: cli_args_model.CLIArgs):
    raw_text_response: ParsingStatus = __request_from_page(const_values)
    if raw_text_response.hasError:
        return raw_text_response
    
    html_parse: ParsingStatus = __parse(raw_text_response)

    return raw_text_response