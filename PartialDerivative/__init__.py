from ..Common import Calculations as calc
import json
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
        # Calcule the partial deriviatve
        pd = calc.PartialDerivative(symbols, fx, variable)

        if pd:
            result = json.dumps({'fx': str(fx), 'PartialDerivative': str(pd)})
            return func.HttpResponse(result)
            status_code=200
        else:
            return func.HttpResponse('Error: failed to calculate the partial derivative from symbols {0}, fx {1}, and variable {2}'
            .format(symbols, fx, variable))

            status_code=400
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Supply symbols, fx, and variable.",
             status_code=200
        )
        