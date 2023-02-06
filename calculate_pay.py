def calculate_pay(hours, wage):
    """
    Calculate weekly pay given the hours and wage an employee has worked.

    :param hours: must be any floating point number
    :param wage: must be any floating point number
    :precondition: hours and wage must be any floating point number
    :postcondition: calculates the expected weekly pay for the employee
    :return: expected weekly pay as a floating point number

    >>> calculate_pay(10, 10)
    100.0
    >>> calculate_pay(50, 10)
    600.0
    """
    weekly_pay = 0
    if hours < 0:
        return float(weekly_pay)
    elif hours <= 40:
        weekly_pay += (hours * wage)
        return float(weekly_pay)
    else:
        weekly_pay += (40 * wage)
        weekly_pay += (hours - 40) * (wage * 2)
        return float(weekly_pay)


def main():
    print("Here is our work Chris!")


if __name__ == "__main__":
    main()
