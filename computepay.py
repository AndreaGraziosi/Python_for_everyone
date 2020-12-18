 # sh = input("enter hours!")
# sr = input("enter rate")
#
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print("error, please enter numeric input")
#     quit()
#
# if fh > 40:
#     reg = fr* fh
#     otp = (fh - 40) * (fr * .5)
#     xp = reg + otp
# else:
#     xp = fh* fr
# print('pay:', xp)

# hrs = input("Enter Hour")
# h = float(hrs)
# rt = input("Enter rate")
# r = float(rt)
# p = computepay(h,r)
# print(p)
#
# def computepay(h,r):
#
#     if h <= 40:
#         pay = h*r
#         return pay
#     else:
#         h > 40
#         return ( (40* r)+ ((r * 1.5) * (h-40))
def computepay(h,r):
    if h <= 40:
        pay= h * r
        return pay
    else:
        pay=40 * r+((h-40) * (1.5 * r))
        return pay

hrs = input('Enter Hours:')
h=float(hrs)
rate = input('Enter Rate:')
r=float(rate)

worker1=computepay(h,r)
print(worker1)
