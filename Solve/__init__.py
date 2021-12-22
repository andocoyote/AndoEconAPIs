from ..Common import Calculations as calc
import json
import logging
import sympy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    symbols = ''
    fx = ''
    subs = {}

    try:
        req_body = req.get_json()

        # Example symbols = 'x y'
        symbols = req_body.get('symbols')

        # Example: fx = 'sqrt(x y)'
        fx = req_body.get('fx')

        # Example: {'x':2, 'y':5}
        subs = req_body.get('subs')

    except ValueError:
        pass
    
    if symbols and fx and subs:
        # Solve the equation and obtain the result
        result = calc.Solve(symbols, fx, subs)

        if result:
            result = json.dumps({'fx': str(fx), 'result': str(result)})
            return func.HttpResponse(str(result))
            status_code=200
        else:
            return func.HttpResponse('Error: failed to calculate result from symbols {0}, fx {1}, and subs {2}'
            .format(symbols, fx, subs))

            status_code=400
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Supply symbols and fx.",
             status_code=200
        )
        