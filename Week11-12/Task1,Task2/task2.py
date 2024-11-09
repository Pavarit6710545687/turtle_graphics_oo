import csv, os


class CityTemperatureData:
    def __init__(self, cities_file, countries_file):
        self.cities = self.load_data(cities_file)
        self.countries = self.load_data(countries_file)

    def load_data(self, file_path):
        data = []
        with open(file_path) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data

    def get_city_temperatures(self, country_name):
        """Returns the list of temperatures for cities in the given country."""
        temps = []
        for city in self.cities:
            if city['country'] == country_name:
                temps.append(float(city['temperature']))
        return temps

    def temperature_stats(self, country_name):
        """Calculates and prints the average, min, and max temperatures for a given country."""
        temps = self.get_city_temperatures(country_name)

        if temps:
            avg_temp = sum(temps) / len(temps)
            min_temp = min(temps)
            max_temp = max(temps)
            print(f"The average temperature for all the cities in {country_name}: {avg_temp:.2f}")
            print(f"The min temperature for all the cities in {country_name}: {min_temp:.2f}")
            print(f"The max temperature for all the cities in {country_name}: {max_temp:.2f}")
        else:
            print(f"No cities found in {country_name}.")

    def get_all_city_temperatures(self):
        """Returns the list of temperatures for all cities."""
        return [float(city['temperature']) for city in self.cities]

    def print_all_city_temperature_stats(self):
        """Prints the average temperature of all cities."""
        temps = self.get_all_city_temperatures()
        avg_temp = sum(temps) / len(temps) if temps else 0
        print(f"The average temperature of all the cities: {avg_temp:.2f}")
        print()


def main():
    # Define file paths
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    cities_file = os.path.join(__location__, 'Cities.csv')
    countries_file = os.path.join(__location__, 'Countries.csv')

    # Initialize the CityTemperatureData object
    data = CityTemperatureData(cities_file, countries_file)

    # Print the average temperature for all cities
    data.print_all_city_temperature_stats()

    # Print the average, min, and max temperatures for Italy
    data.temperature_stats('Italy')
    print()

    # Print the average, min, and max temperatures for Sweden
    data.temperature_stats('Sweden')


if __name__ == "__main__":
    main()
