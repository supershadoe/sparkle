# IoT Medical Data Encryption Project

Welcome to the IoT Medical Data Encryption project repository! This project aims to ensure secure communication and storage of medical data using lightweight cryptographic algorithms. The project utilizes Lightweight AES for encryption, Elliptic Curve Diffie-Hellman (ECDH) for key exchange, and employs an innovative approach of hiding encrypted data within image histograms for enhanced security.

## Overview

In the modern healthcare industry, ensuring the confidentiality and integrity of medical data is paramount. This IoT project addresses the need for secure transmission and storage of sensitive medical information by implementing robust encryption techniques tailored for resource-constrained environments.

## Features

- **Secure Encryption**: Utilizes Lightweight AES for efficient and secure encryption of medical data.
- **Key Exchange**: Implements Elliptic Curve Diffie-Hellman (ECDH) for secure key exchange between IoT devices and servers.
- **Random Key Generation**: Generates random keys for encryption to enhance security.
- **Image Histogram Concealment**: Conceals encrypted data within image histograms to provide an additional layer of security.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/sparkle.git
   ```

2. **Configuration**: Configure the IoT devices and server settings according to your requirements.

3. **Build and Deploy**: Build the project and deploy it to your IoT devices and server infrastructure.

4. **Testing**: Perform thorough testing to ensure the encryption and decryption processes function as expected.

## Usage

Once deployed, the IoT devices will securely encrypt medical data using Lightweight AES. The ECDH algorithm will facilitate secure key exchange between the devices and the server. The randomly generated keys for encryption will add an extra layer of security to the process. Finally, the encrypted data will be hidden within image histograms for enhanced security during transmission and storage.

## Contributing

Contributions to the project are welcome! If you'd like to contribute, please follow these guidelines:

- Fork the repository.
- Create your feature branch (`git checkout -b feature/new-feature`).
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/new-feature`).
- Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to express our gratitude to the open-source community for their invaluable contributions to cryptographic algorithms and security practices. Special thanks to the contributors and maintainers of Lightweight AES and ECDH implementations.

## Contact

For any inquiries or feedback, please contact [project@email.com](mailto:project@email.com).

Thank you for your interest in our IoT Medical Data Encryption project!





This repository has 2 pieces of code - `client.py` and `server.py` which
should be integrated on the respective devices.

### How to run
1. Get all the requirements using `pip install -r requirements.txt`
2. Run the `example.py` script.
