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

        # Example symbols = 'q'
        symbols = req_body.get('symbols')

        # Example: fx = '12 - 2/3*q'
        fx = req_body.get('fx')

    except ValueError:
        pass
    
    if symbols and fx:
        # Solve the equation set to zero and obtain the result
        result = calc.Solve(symbols, fx)

        if result:
            # The values in sympy sets are not native Python types and must be converted to float
            resultlist = [float(num) for num in result]
            result = json.dumps({'fx': str(fx), 'result': resultlist})
            return func.HttpResponse(result)
            status_code=200
        else:
            return func.HttpResponse('Error: failed to calculate result from symbols {0} and fx {1}'
            .format(symbols, fx))

            status_code=400
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Supply symbols and fx.",
             status_code=200
        )
        