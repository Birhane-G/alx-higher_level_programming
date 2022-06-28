def http_error(Status):
    match Status:
        case 400:
            return "1o"
        case 404:
            return "20"
        case _:
            return "_"