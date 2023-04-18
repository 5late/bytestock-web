"""Libraries"""
import calculations # importing the calculations module to use its functions
import data # importing the data module to use its functions
import subprocess


def main(stock, days)->None: # creating the main() functions
    """Main Function"""
    """
    while True: # infinite loop
        try: # ensuring that the user enters a valid number
            user_input = input("Enter a stock: ") # asking the user to enter a stock
            days = int(input("Enter preferred days: ")) # asking the user for the number of days
            if days >0: # break if the number of days is greater than 0
                break
        except ValueError: # asking the user to enter a valid number of days
            print("Enter a valid amount of days")
    """

    open_days, daily_open, daily_close, daily_adj_close, daily_high, daily_low = data.getOCHLData(days, stock) #Not close data, rather, open; we need Adj Close
    with open("close-data.txt", "w") as f:
        for val in daily_adj_close:
            f.write(str(val)+"\n")
        f.close()

    #calculations.mathematics(daily_adj_close)
    args = ("./bytestock-core-public/calc")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.readlines()
    with open('output.txt', 'w') as f:
        for output_line in output:
            output_line = str(output_line)
            period = output_line.split(' ')[1].split(' ')[0]
            probability = output_line.split(' ')[3].split(' ')[0]

            newline = f'Period:{period}:Probability:{probability}\n'
            f.write(newline)

