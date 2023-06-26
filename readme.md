# Laravel Server

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Laravel](https://img.shields.io/badge/Laravel-5.x%20%7C%206.x%20%7C%207.x%20%7C%208.x-orange.svg)

Laravel Server is a Python application that allows you to easily run a Laravel project using the `php artisan serve` command. It takes the Laravel folder path as input, executes the necessary commands, and provides the IP address where the application is running.

## Features

- Automatically runs Laravel applications using the `php artisan serve` command.
- Provides the IP address and port number where the Laravel application is being served.
- Simple and easy-to-use interface.

## Prerequisites

- Python 3.6 or higher installed on your system.
- Laravel 5.x, 6.x, 7.x, or 8.x installed in the target folder.
- Composer installed on your system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/snyype/LaravelServer.git
   ```

2. Change into the cloned directory:

   ```bash
   cd laravel-server
   ```

3. Install the required dependencies:

   ```bash
   pip install pyinstaller
   ```

## Usage

1. Open a terminal or command prompt and navigate to the cloned repository's directory.

2. Run the following command to start the application:

   ```bash
   python larvelserve.py
   ```

3. You will be prompted to enter the path to your Laravel project folder. Provide the absolute path to the folder and press Enter.

4. The application will execute the necessary commands to start the Laravel development server using `php artisan serve`.

5. Once the server is up and running, you will see the IP address and port number where the Laravel application is being served.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## Support

For any questions or concerns, please open an issue on the [GitHub repository](https://github.com/snyype/LaravelServer).

## Acknowledgements

This project was inspired by the need to quickly run Laravel applications during development without the need for manual commands.

## Disclaimer

This application is provided as-is, without any warranty or guarantee. Use it at your own risk.

**Note:** Make sure to run this application only in development environments and not in production environments.

## Author

- [SnYpe](https://github.com/snyype)
