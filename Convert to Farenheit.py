def main():
    print("Enter the temperature in celcius:\t", end='')
    c=input()
    c=float(c)
    f=1.8*c+32
		k=c+273.15
    print(f"The temperature in farenheit is {f}F and in Kelvin is {k}K")
main()
