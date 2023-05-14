import decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000 # Set the precision to handle larger numbers
        decimal_num = decimal.Decimal(decimal_num)
        binary = ""
        while decimal_num > 0:
            binary = str(decimal_num % 2) + binary
            decimal_num = decimal_num // 2
        return binary

# Function to convert binary to decimal
def binary_to_decimal(binary_num):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000 # Set the precision to handle larger numbers
        binary_num = str(binary_num)
        decimal_num = decimal.Decimal(0)
        for i in range(len(binary_num)):
            decimal_num += int(binary_num[i]) * 2**(len(binary_num)-i-1)
        return decimal_num
