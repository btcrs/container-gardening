from ph import Ph
from pumps import Pumps

def main():
    lower_bound = 7.6
    upper_bound = 6.5

    pumps = Pumps(lower_bound, upper_bound)
    ph = Ph()

    while True:
        current_ph = ph.poll()
        pumps.regulate(current_ph)
        time.sleep(1)

if __name__ == '__main__':
    main()
