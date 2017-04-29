from UserString import MutableString
from sqlbuilder.smartsql import Q, T, compile
from sqlbuilder.smartsql.queries import Query

def convertToQueryString(input):

    if type(input) is Query:
        input = compile(input)

    if type(input) is not tuple:
        return None

    if len(input) < 2:
        return None

    chars = list(input[0])
    argsList = input[1]

    query = MutableString()

    iChar = 0
    iArg = 0

    while iChar < len(chars):
        if chars[iChar] == '%' and iChar + 1 < len(chars) and chars[iChar + 1] == 's':
            if iArg >= len(argsList):
                return None

            if type(argsList[iArg]) is str:
                argsList[iArg] = '\'' + argsList[iArg] + '\''

            query.append(argsList[iArg])
            iArg += 1
            iChar += 1
        elif chars[iChar] != '\"':
            query.append(chars[iChar])

        iChar += 1

    return str(query)
