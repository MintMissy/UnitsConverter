# TODO
# second (sec)
# minute (min)
# hour (hr)

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


def time(timeValue, currentUnit="second", conversionUnit="minute"):
    """
    This function convert time to another unit

    :param timeValue: Time variable (For example 4)
    :param currentUnit: Current unit [second, minute, hour, day, week]
    :param conversionUnit: Convert to unit [second, minute, hour, day, week]
    :return: Time converted to another unit
    """
    try:
        # Check for errors in code
        if currentUnit.lower() == conversionUnit.lower():
            raise SameUnitsError

        # Convert time value to seconds
        if currentUnit.lower() == "minute":
            timeValue *= 60
        elif currentUnit.lower() == "hour":
            timeValue *= 3600
        elif currentUnit.lower() == "day":
            timeValue *= 86400
        elif currentUnit.lower() == "week":
            timeValue *= 604800
        else:
            raise UnrecognisedConversionUnit

        # Convert second to conversion unit
        if conversionUnit == "second":
            return timeValue
        elif conversionUnit.lower() == "minute":
            return timeValue / 60
        elif conversionUnit.lower() == "hour":
            return timeValue / 3600
        elif conversionUnit.lower() == "day":
            return timeValue / 86400
        elif conversionUnit.lower() == "week":
            return timeValue / 604800
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
