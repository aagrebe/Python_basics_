from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('-p', '--product', type=int, default=1)
""" выработка в часах """
parser.add_argument('-r', '--rate', type=float, default=1)
""" ставка в час """
parser.add_argument('-b', '--bonus', type=float, default=0)
""" премия """
args = parser.parse_args()
if args.rate < 0 or args.product < 0:
    print(f"Product and rate can't be negative")
else:
    print(f"Salary {(args.product * args.rate) + args.bonus}")