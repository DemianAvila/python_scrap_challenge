import modules

if __name__ == "__main__":
    #GET VALUES FROM ARGUMENTS, OR ENV FILE OR DEFAULT IN THAT ORDER
    args: any = modules.cli_args_model.set_values_from_arg()
    values: modules.cli_args_model.CLIArgs = modules.cli_args_model.open_env_file(args)

    #SCRAP URL
    json_parsed: modules.scrap.ParsingStatus = modules.scrap.scrap(values)
    if json_parsed.hasError:
        raise BaseException(json_parsed.errorDescription)
    
    #OUTPUT THE JSON INFO IN THE CSV
    product: modules.ouput_csv.Product =  modules.ouput_csv.getProducts(json_parsed)
    csv: list = modules.ouput_csv.outputCSV(product, values)

