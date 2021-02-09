# Errors
class Error(Exception):
    """Base class for other exceptions"""
    pass


class SameUnitsError(Exception):
    """Current unit and unit to convert are the same"""
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
        if currentUnit == conversionUnit:
            raise SameUnitsError

        # Convert second
        if currentUnit.lower() == "second":
            if conversionUnit.lower() == "minute":
                return timeValue / 60
            if conversionUnit.lower() == "hour":
                return timeValue / 3600
            if conversionUnit.lower() == "day":
                return timeValue / 86400
            if conversionUnit.lower() == "week":
                return timeValue / 604800

        # Convert minute
        if currentUnit.lower() == "minute":
            if conversionUnit.lower() == "second":
                return timeValue * 60
            if conversionUnit.lower() == "hour":
                return timeValue / 60
            if conversionUnit.lower() == "day":
                return timeValue / 1440
            if conversionUnit.lower() == "week":
                return timeValue / 10080

        # Convert hour
        if currentUnit.lower() == "hour":
            if conversionUnit.lower() == "second":
                return timeValue * 3600
            if conversionUnit.lower() == "minute":
                return timeValue * 60
            if conversionUnit.lower() == "day":
                return timeValue / 24
            if conversionUnit.lower() == "week":
                return timeValue / 168

        # Convert day
        if currentUnit.lower() == "day":
            if conversionUnit.lower() == "second":
                return timeValue * 86400
            if conversionUnit.lower() == "minute":
                return timeValue * 1440
            if conversionUnit.lower() == "hour":
                return timeValue * 24
            if conversionUnit.lower() == "week":
                return timeValue / 7

        # Convert week
        if currentUnit.lower() == "week":
            if conversionUnit.lower() == "second":
                return timeValue * 604800
            if conversionUnit.lower() == "minute":
                return timeValue * 10080
            if conversionUnit.lower() == "hour":
                return timeValue * 168
            if conversionUnit.lower() == "day":
                return timeValue * 7

    # Check for raised errors
    except SameUnitsError:
        print("==================== ERROR ====================\n"
              "Current unit and unit to convert are the same\n"
              "===============================================")
        return "ERROR"
