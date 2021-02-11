# Errors
class Error(Exception):
    """Base class for other exceptions"""
    pass


class SameUnitsError(Error):
    """Current unit and unit to convert are the same"""
    pass


class UnrecognisedCurrentUnit(Error):
    """Current unit is unrecognized by script"""
    pass


class UnrecognisedConversionUnit(Error):
    """Current unit is unrecognized by script"""
    pass


def mass(massValue, currentUnit="kilogram", conversionUnit="gram"):
    """

    :param massValue: Mass variable (For example 4)
    :param currentUnit: Current unit [milligram, mg, gram, g, kilogram, kg, tonne, t, ounce, oz, pound, lb, stone, st]
    :param conversionUnit: Convert to unit [m/s, km/h]
    :return: Mass converted to another unit
    """
    try:
        # Check for errors in code
        if currentUnit.lower() == conversionUnit.lower():
            raise SameUnitsError

        # Convert meters per second
        if currentUnit.lower() == "gram" or currentUnit.lower() == "g":
            massValue *= 1000
        elif currentUnit.lower() == "kilogram" or currentUnit.lower() == "kg":
            massValue *= 1000 ** 2
        elif currentUnit.lower() == "tonne" or currentUnit.lower() == "t":
            massValue *= 1000 ** 3
        elif currentUnit.lower() == "ounce" or currentUnit.lower() == "oz":
            massValue *= 28349.5
        elif currentUnit.lower() == "pound" or currentUnit.lower() == "lb":
            massValue *= 453592
        elif currentUnit.lower() == "stone" or currentUnit.lower() == "st":
            massValue *= 6350290
        else:
            raise UnrecognisedConversionUnit

        # Convert milligrams to convertValue
        if conversionUnit.lower() == "gram" or conversionUnit.lower() == "g":
            return massValue / 1000
        elif conversionUnit.lower() == "kilogram" or conversionUnit.lower() == "kg":
            return massValue / 1000 ** 2
        elif conversionUnit.lower() == "tonne" or conversionUnit.lower() == "t":
            return massValue / 1000 ** 3
        elif conversionUnit.lower() == "ounce" or conversionUnit.lower() == "oz":
            return massValue / 28349.5
        elif conversionUnit.lower() == "pound" or conversionUnit.lower() == "lb":
            return massValue / 453592
        elif conversionUnit.lower() == "stone" or conversionUnit.lower() == "st":
            return massValue / 6350290
        else:
            raise UnrecognisedConversionUnit

    # Check for raised errors
    except SameUnitsError:
        print("==================== ERROR ====================\n"
              "Current unit and unit to convert are the same\n"
              "===============================================")
        return "ERROR"

    except UnrecognisedCurrentUnit:
        print(f"==================== ERROR ====================\n"
              f"Unit {currentUnit} is unrecognized by script\n"
              f"===============================================")
        return "ERROR"

    except UnrecognisedConversionUnit:
        print(f"==================== ERROR ====================\n"
              f"Unit {conversionUnit} is unrecognized by script\n"
              f"===============================================")
        return "ERROR"
