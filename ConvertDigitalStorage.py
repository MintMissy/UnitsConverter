# TODO Gigabytes, Megabytes  Megabits etc

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


def digitalStorage(digitalValue, currentUnit="MB", conversionUnit="GB"):
    """
    This function convert digital storage to another unit

    :param digitalValue: Digital storage variable (For example 4)
    :param currentUnit: Current unit [bit, byte, KB, MB, GB, TB, PB]
    :param conversionUnit: Convert to unit [bit, byte, KB, MB, GB, TB, PB]
    :return: Digital storage converted to another unit
    """
    try:
        # Check for errors in code
        if currentUnit == conversionUnit:
            raise SameUnitsError

        # Convert current unit to bits
        if currentUnit == "byte":
            digitalValue *= 8
        elif currentUnit == "Kb":
            digitalValue *= 1024
        elif currentUnit == "Mb":
            digitalValue *= 1024 ** 2
        elif currentUnit == "Gb":
            digitalValue *= 1024 ** 3
        elif currentUnit == "Tb":
            digitalValue *= 1024 ** 4
        elif currentUnit == "Pb":
            digitalValue *= 1024 ** 5
        elif currentUnit == "byte":
            digitalValue *= 8
        elif currentUnit == "KB":
            digitalValue *= 8 * 1024
        elif currentUnit == "MB":
            digitalValue *= 8 * 1024 ** 2
        elif currentUnit == "GB":
            digitalValue *= 8 * 1024 ** 3
        elif currentUnit == "TB":
            digitalValue *= 8 * 1024 ** 4
        elif currentUnit == "PB":
            digitalValue *= 8 * 1024 ** 5
        else:
            raise UnrecognisedConversionUnit

        # Convert bits to another unit
        if conversionUnit == "bit":
            return digitalValue
        elif conversionUnit == "Kb":
            return digitalValue / 1024
        elif conversionUnit == "Mb":
            return digitalValue / 1024 ** 2
        elif conversionUnit == "Gb":
            return digitalValue / 1024 ** 3
        elif conversionUnit == "Tb":
            return digitalValue / 1024 ** 4
        elif conversionUnit == "Pb":
            return digitalValue / 1024 ** 5
        elif conversionUnit == "byte":
            return digitalValue / 8
        elif conversionUnit == "KB":
            return digitalValue / 8 / 1024
        elif conversionUnit == "MB":
            return digitalValue / 8 / 1024 ** 2
        elif conversionUnit == "GB":
            return digitalValue / 8 / 1024 ** 3
        elif conversionUnit == "TB":
            return digitalValue / 8 / 1024 ** 4
        elif conversionUnit == "PB":
            return digitalValue / 8 / 1024 ** 5
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
