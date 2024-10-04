import json
from typing import Optional
from pydantic import BaseModel
from . import scrap
from . import cli_args_model


class Product (BaseModel):
    allergens: Optional[str] = None
    sku: Optional[int] = None
    vegan: Optional[bool] = None
    kosher: Optional[bool] = None
    organic: Optional[bool] = None
    vegetarian: Optional[bool] = None
    gluten_free: Optional[bool] = None
    lactose_free: Optional[bool] = None
    package_quantity: Optional[int] = None
    unit_size: Optional[float] = None
    net_weight: Optional[float] = None

def __parseRawProducts(json_prods: dict) -> Product:
    product_info:dict = {}
    fields: dict = Product.model_fields
    for key in fields.keys():
        #SOME PRODUCTS HAVE THEIS NAME INSIDE A VALUE KEY
        #IF VALUE IS LIST
        try:
            val: any = json_prods[key]["value"][0]["name"]
        except:
            val: any = json_prods[key]["value"]

        product_info[key] = val
    return Product(**product_info)    


def getProducts(parse: scrap.ParsingStatus) -> Product:
    json_needed_attr: list = parse.jsonResponse["allVariants"][0]["attributesRaw"]
    #SEARCH THE KEY "custom_attributes"
    custom_attributes: dict = [obj for obj in json_needed_attr if obj["name"]=="custom_attributes"][0]
    raw_products:str = custom_attributes["value"]["en-CR"]
    json_products = json.loads(raw_products)
    return __parseRawProducts(json_products)

    
def outputCSV(product: Product, cli_values: cli_args_model.CLIArgs) ->list:
    csv: list = []
    prod_list = product.__dict__
    headers = prod_list.keys()
    values = prod_list.values()
    csv = [headers, values]
    str_csv = ""
    for line in csv:
        str_csv = str_csv+",".join([str(element) for element in line])+"\n"
    
    with open(f"{cli_values.csv_output_path}/test_output.csv", mode="w") as file:
        file.write(str_csv)


