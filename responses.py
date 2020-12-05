def braspag_mocked_response():
    response = {
        "Status": "0",
        "Amount": 2000,
        "ReturnCode": "00011",
        "Nsu": "100"
    }
    return response


def ingenico_mocked_response():
    response = {
        "transaction_status_code": "1",
        "amount": 2000,
        "code": "0222",
        "complement": "10",
        "unit_code": "200"
    }

    return response

