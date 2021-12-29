from ..Common import Calculations as calc
import json
import logging
import sympy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    symbols = ''
    fx = ''
    cx = ''

    try:
        req_body = req.get_json()

        # Example symbols = 'x'
        symbols = req_body.get('symbols')

        # Example: fx = '10 - 0.001*x'
        fx = req_body.get('fx')

        # Example: cx = '5000 + 2*x'
        cx = req_body.get('cx')
    
        if symbols and fx and cx:
            demandFunction = fx
            costFunction = cx

            # Revenue is quantity x * price p which is given by the demand function (price function)
            revenueFunction = symbols + ' * (' + demandFunction + ')'

            # Profit is revenue minus cost
            profitFunction = '(' + revenueFunction + ')' + '-(' + costFunction + ')'

            # MP is the derivative of the profit function
            marginalProfitFunction = calc.Derivative(symbols, profitFunction)

            # Solve the equation set to zero and obtain the result
            optimumQuantitySet = calc.Solve(symbols, marginalProfitFunction)
            optimumQuantity = [float(num) for num in optimumQuantitySet]

            # Evaluate the demand function using optimum quantity to obtain price per item
            itemPrice = calc.Evalutate(symbols, demandFunction, {'x': optimumQuantity[0]})

            # Evaluate the revenue function using optimum quantity to obtain total revenue
            totalRevenue = calc.Evalutate(symbols, revenueFunction, {'x': optimumQuantity[0]})

            # Format the response body JSON
            response = json.dumps(
                {'demandFunction': str(demandFunction),
                'costFunction': str(costFunction),
                'revenueFunction': str(revenueFunction),
                'profitFunction': str(profitFunction),
                'marginalProfitFunction': str(marginalProfitFunction),
                'optimumQuantity': float(optimumQuantity[0]),
                'itemPrice': float(itemPrice),
                'totalRevenue': float(totalRevenue)})

            return func.HttpResponse(response)
            status_code=200
            
        else:
            return func.HttpResponse(
                "This HTTP triggered function executed successfully. Supply symbols and fx.",
                status_code=200
            )
    except:
        return func.HttpResponse('Error: failed to calculate result from symbols {0} and fx {1}'
        .format(symbols, fx))

        status_code=400