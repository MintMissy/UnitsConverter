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

        # Convert second
        if currentUnit.lower() == "second":
            if conversionUnit.lower() == "minute":
                return timeValue / 60
            elif conversionUnit.lower() == "hour":
                return timeValue / 3600
            elif conversionUnit.lower() == "day":
                return timeValue / 86400
            elif conversionUnit.lower() == "week":
                return timeValue / 604800
            else:
                raise UnrecognisedConversionUnit

        # Convert minute
        if currentUnit.lower() == "minute":
            if conversionUnit.lower() == "second":
                return timeValue * 60
            elif conversionUnit.lower() == "hour":
                return timeValue / 60
            elif conversionUnit.lower() == "day":
                return timeValue / 1440
            elif conversionUnit.lower() == "week":
                return timeValue / 10080
            else:
                raise UnrecognisedConversionUnit

        # Convert hour
        if currentUnit.lower() == "hour":
            if conversionUnit.lower() == "second":
                return timeValue * 3600
            elif conversionUnit.lower() == "minute":
                return timeValue * 60
            elif conversionUnit.lower() == "day":
                return timeValue / 24
            elif conversionUnit.lower() == "week":
                return timeValue / 168
            else:
                raise UnrecognisedConversionUnit

        # Convert day
        if currentUnit.lower() == "day":
            if conversionUnit.lower() == "second":
                return timeValue * 86400
            elif conversionUnit.lower() == "minute":
                return timeValue * 1440
            elif conversionUnit.lower() == "hour":
                return timeValue * 24
            elif conversionUnit.lower() == "week":
                return timeValue / 7
            else:
                raise UnrecognisedConversionUnit

        # Convert week
        if currentUnit.lower() == "week":
            if conversionUnit.lower() == "second":
                return timeValue * 604800
            elif conversionUnit.lower() == "minute":
                return timeValue * 10080
            elif conversionUnit.lower() == "hour":
                return timeValue * 168
            elif conversionUnit.lower() == "day":
                return timeValue * 7
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

