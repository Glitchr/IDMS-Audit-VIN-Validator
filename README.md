

# Audit IDMS Vin Validator

Audit IDMS Vin Validator is a Python script that checks VINs from a CSV file against the IDMS website and generates a report of it exists or not in the inventory.

## Installation

To install Audit IDMS Vin Validator, you need Python 3.6 or higher and the following packages:

- Selenium
- Pandas
- Decouple

You can install these packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use Audit IDMS Vin Validator, you need to have an `.env` file in the same directory as the script. The `.env` file should contain the following variables:

- `PASSWORD`: Your IDMS password
- `USER`: Your IDMS username
- `READ`: The name of the CSV file to read from (e.g. `input_data.csv`)
- `WRITE`: The name of the CSV file to write to (e.g. `output_data.csv`)
- `URL`: The URL of the IDMS website (e.g. `https://soleranab2b.b2clogin.com/soleranab2b.onmicrosoft.com/b2c_1a_hrdsignin_ns/oauth2/v2.0/authorize?client_id=`)

You also need to have a CSV file with whatever name you'd prefer, for example,  `input_data.csv`  in the same directory as the script. The CSV file should have the following columns:

- Dealer
- VIN
- Deal Date
- Issued/Finalized
- Total Fees
- State
- IDMS

The script will then read the CSV file and compare the VIN row with the inventory on the IDMS website. It will output a report of any mismatches as a CSV file with a name of your preference, for example,  `output_data.csv`  in the same directory as the script.

To run the script, you just need to execute it with Python:

```bash
python main.py
```

## License

Audit IDMS Scrapper is licensed under the MIT License. See  [LICENSE](https://github.com/Glitchr/audit_idms_vin_validator/blob/main/LICENSE) for more details.

## Contributing

Audit IDMS Scrapper is an open source project and contributions are welcome. If you want to contribute, please follow these steps:

1.  Fork this repository on GitHub.
2.  Clone your forked repository on your local machine.
3.  Create a new branch for your feature or bug fix.
4.  Make your changes and commit them with descriptive messages.
5.  Push your branch to your forked repository on GitHub.
6.  Create a pull request from your branch to this repository’s main branch.

Please make sure that your code follows the  [PEP 8](https://www.python.org/dev/peps/pep-0008/)  style guide and that you test it before submitting.
