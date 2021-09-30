"""
Calculator API
"""
from flask_validation_extended import Validator, Query
from flask_validation_extended import ValidationRule
from app.api import response_200, bad_request
from app.api.api_v1 import api_v1 as api
from app.api.decorator import timer
from controller import calculator


@api.route('/add')
@Validator(bad_request)
@timer
def add_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.add(a, b))


@api.route('/subtract')
@Validator(bad_request)
@timer
def subtract_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.subtract(a, b))


@api.route('/multiply')
@Validator(bad_request)
@timer
def multiply_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.multiply(a, b))


class NotZero(ValidationRule):

    def invalid_str(self):
        return "Must Not be Zero."

    def is_valid(self, data) -> bool:
        return data != 0


@api.route('/divide')
@Validator(bad_request)
@timer
def divide_api(
    a=Query(int),
    b=Query(int, rules=NotZero())
):
    return response(calculator.divide(a, b))