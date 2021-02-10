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


def speed(speedValue, currentUnit="m/s", conversionUnit="km/h"):
    """
    This function convert speed values to another speed values

    :param speedValue: Speed variable (For example 4)
    :param currentUnit: Current unit [m/s, km/h]
    :param conversionUnit: Convert to unit [m/s, km/h]
    :return: Speed converted to another unit
    """

    try:
        # Check for errors in code
        if currentUnit.lower() == conversionUnit.lower():
            raise SameUnitsError

        # Convert meters per second
        if currentUnit.lower() == "m/s":
            if conversionUnit.lower() == "km/h":
                return speedValue * 3.6
            elif conversionUnit.lower() == "ft/s":
                return speedValue * 3.28084
            elif conversionUnit.lower() == "mph":
                return speedValue * 2.23694
            else:
                raise UnrecognisedConversionUnit

        # Convert kilometers per hour
        elif currentUnit.lower() == "km/h":
            if conversionUnit.lower() == "m/s":
                return speedValue / 3.6
            elif conversionUnit.lower() == "ft/s":
                return speedValue * 0.911344
            elif conversionUnit.lower() == "mph":
                return speedValue * 0.621371
            else:
                raise UnrecognisedConversionUnit

        # Convert feet per second
        elif currentUnit.lower() == "ft/s":
            if conversionUnit.lower() == "mph":
                return speedValue * 0.681818
            elif conversionUnit.lower() == "m/s":
                return speedValue * 0.3048
            elif conversionUnit.lower() == "km/h":
                return speedValue * 1.09728
            else:
                raise UnrecognisedConversionUnit

        # Convert miles per hour
        elif currentUnit.lower() == "mph":
            if conversionUnit.lower() == "ft/s":
                return speedValue * 1.46667
            elif conversionUnit.lower() == "m/s":
                return speedValue * 0.44704
            elif conversionUnit.lower() == "km/h":
                return speedValue * 1.609344
            else:
                raise UnrecognisedConversionUnit
        else:
            raise UnrecognisedCurrentUnit

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
