#include <WiFi.h>

const char* ssid = "OMOTECH_2.4GHz";       // Replace with your Wi-Fi SSID
const char* password = "Omotech@23"; // Replace with your Wi-Fi Password
const char* serverIP = "192.168.0.105";   // Replace with your server's IP
const int serverPort = 12345;           // Server port number

const int GSR_PIN = 34; // Analog pin connected to GSR sensor

WiFiClient client;

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wi-Fi...");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  int gsrValue = analogRead(GSR_PIN);
  Serial.println("GSR Value: " + String(gsrValue));

  // Connect to server and send data
  if (client.connect(serverIP, serverPort)) {
    client.println(String(gsrValue));
    //client.stop();
  } else {
    Serial.println("Failed to connect to server");
  }

  delay(1000); // Send data every second
}
