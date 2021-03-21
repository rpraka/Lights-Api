<!-- Logo -->
<br />
<p align="center">
  <a href="https://github.com/rpraka/lightsapi">
    <img src="./readme_assets/images/cover_robot.jpg" width=100% alt="Logo">
  </a>

  <h3 align="center">An extensible API for custom IoT light systems.</h3>

  <p align="center">
    <a href="https://github.com/rpraka/lightsapi">View Demo</a>
    ·
    <a href="https://github.com/rpraka/lightsapi/issues">Report Bug</a>
    ·
    <a href="https://github.com/rpraka/lightsapi/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a simple REST API server and multiple REST client implementations for IoT light system control. Such an architecture uniquely allows a huge diversity for the type of clients allowed. The endpoints can be manipulated via Siri shortcuts, Google Home, Alexa, Chrome extensions and command line, among others.

---------ADD DIAGRAM HERE---------

### Built With

* **PostgreSQL** - backend database
* **Python/Flask** - RESTful handler
* **IFTTT** - Intermediate webhook handler for Google Home and Alexa clients
* **NodeMCU ESP8266 WiFi SoC** - hardware implementation for servo control
* **C++** - ESP8266 client implementation
* **Javascript** - Chrome extension client implementation


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites
The hardware implementation requires a servo motor with least 2.5 kg-cm torque and a NodeMCU ESP8266 development board or similar (any WiFi-capable board should suffice but will require alteration to pinouts and WiFi connection code)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rpraka/lightsapi.git
   ```
2. Reserve a Heroku dyno or any other VPS instance. Deployment is easiest with Heroku as all required files have been provided. Attach a postgreSQL instance to the instance and deploy the repo.


<!-- USAGE EXAMPLES -->
## Usage




<!-- ROADMAP -->
## Roadmap
### Upgrades
* Integrate a photoresistor into the hardware implementation to allow toggling via a single endpoint.
* Could add more advanced auth features, but is likely just uneccessary overhead in this case.
* Considered websocket rather than REST, but probably is overkill.
* 
<!-- CONTRIBUTING -->
## Contributing

Any contributions are greatly appreciated.

1. Fork the Project
2. Create a Feature Branch (`git checkout -b feature/example_feature`)
3. Commit your Changes (`git commit -m 'Added example_feature'`)
4. Push to the Branch (`git push origin feature/example_feature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

Rahul Prakash - [@rpraka](https://twitter.com/rpraka)

Project Link: [https://github.com/rpraka/lightsapi](https://github.com/rpraka/lightsapi)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* See in-line comments



