class TempratureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

if __name__ == "__main__":
    print("Celsius to Fahrenheit" , TempratureConverter.celsius_to_fahrenheit(30))