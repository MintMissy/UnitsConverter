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
    :param currentUnit: Current unit [bit, byte, KB, Kb, MB, Mb, GB, Gb, TB, Tb, PB, Pb]
    :param conversionUnit: Convert to unit [bit, byte, KB, Kb, MB, Mb, GB, Gb, TB, Tb, PB, Pb]
    :return: Digital storage converted to another unit
    """
    try:
        # Check for errors in code
        if currentUnit == conversionUnit:
            raise SameUnitsError

        # Convert current unit to bits
        if currentUnit == "bit" or currentUnit == "b":
            pass
        elif currentUnit == "Kb" or currentUnit == "Kilobit":
            digitalValue *= 1024
        elif currentUnit == "Mb" or currentUnit == "Megabit":
            digitalValue *= 1024 ** 2
        elif currentUnit == "Gb" or currentUnit == "Gigabit":
            digitalValue *= 1024 ** 3
        elif currentUnit == "Tb" or currentUnit == "Terabit":
            digitalValue *= 1024 ** 4
        elif currentUnit == "Pb" or currentUnit == "Petabit":
            digitalValue *= 1024 ** 5
        elif currentUnit == "byte" or currentUnit == "B":
            digitalValue *= 8
        elif currentUnit == "KB" or currentUnit == "Kilobyte":
            digitalValue *= 8 * 1024
        elif currentUnit == "MB" or currentUnit == "Megabyte":
            digitalValue *= 8 * 1024 ** 2
        elif currentUnit == "GB" or currentUnit == "Gigabyte":
            digitalValue *= 8 * 1024 ** 3
        elif currentUnit == "TB" or currentUnit == "Terabyte":
            digitalValue *= 8 * 1024 ** 4
        elif currentUnit == "PB" or currentUnit == "Petabyte":
            digitalValue *= 8 * 1024 ** 5
        else:
            raise UnrecognisedConversionUnit

        # Convert bits to another unit
        if conversionUnit == "bit" or currentUnit == "b":
            return digitalValue
        elif conversionUnit == "Kb" or currentUnit == "Kilobit":
            return digitalValue / 1024
        elif conversionUnit == "Mb" or currentUnit == "Megabit":
            return digitalValue / 1024 ** 2
        elif conversionUnit == "Gb" or currentUnit == "Gigabit":
            return digitalValue / 1024 ** 3
        elif conversionUnit == "Tb" or currentUnit == "Terabit":
            return digitalValue / 1024 ** 4
        elif conversionUnit == "Pb" or currentUnit == "Petabit":
            return digitalValue / 1024 ** 5
        elif conversionUnit == "byte" or currentUnit == "B":
            return digitalValue / 8
        elif conversionUnit == "KB" or currentUnit == "Kilobyte":
            return digitalValue / 8 / 1024
        elif conversionUnit == "MB" or currentUnit == "Megabyte":
            return digitalValue / 8 / 1024 ** 2
        elif conversionUnit == "GB" or currentUnit == "Gigabyte":
            return digitalValue / 8 / 1024 ** 3
        elif conversionUnit == "TB" or currentUnit == "Terabyte":
            return digitalValue / 8 / 1024 ** 4
        elif conversionUnit == "PB" or currentUnit == "Petabyte":
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
