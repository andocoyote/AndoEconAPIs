from ..Common import Calculations as calc
import json
import logging
import sympy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    symbols = ''
    fx = ''

    try:
        req_body = req.get_json()

        # Example symbols = 'x'
        symbols = req_body.get('symbols')

        # Example: fx = 'x**5 + 7*x**4 + 3'
        fx = req_body.get('fx')
    except ValueError:
        pass
    
    if symbols and fx:
        # Differentiate it.  Should yield: 5*x**4 + 28*x**3
        derivative = calc.Differentiate(symbols, fx)

        if derivative:
            result = json.dumps({'fx': str(fx), 'derivative': str(derivative)})
            return func.HttpResponse(str(result))
            status_code=200
        else:
            return func.HttpResponse('Error: failed to calculate derivative from symbols {0} and fx {1}'.format(symbols, fx))
            status_code=400
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Supply symbols and fx.",
             status_code=200
        )
        