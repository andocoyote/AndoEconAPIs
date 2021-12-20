from ..Common import Calculations as calc
import logging
import sympy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    symbols = ''
    fx = ''
    variable = ''

    try:
        req_body = req.get_json()

        # Example symbols = 'c p'
        symbols = req_body.get('symbols')

        # Example: fx = 'sqrt(p * c)'
        fx = req_body.get('fx')

        #Example: c
        variable = req_body.get('variable')
    except ValueError:
        pass
    
    if symbols and fx and variable:
        # Calcule the Marginal Utility
        MU = calc.MarginalUtility(symbols, fx, variable)

        if MU:
            return func.HttpResponse(str(MU))
            status_code=200
        else:
            return func.HttpResponse('Error: failed to calculate Marginal Utility from symbols {0}, fx {1}, and variable {2}'
            .format(symbols, fx, variable))

            status_code=400
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Supply symbols, fx, and variable.",
             status_code=200
        )
        