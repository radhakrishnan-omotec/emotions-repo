#include <WiFi.h>

// Wi-Fi credentials
const char* ssid = "OMOTECH_2.4GHz";       // Replace with your Wi-Fi SSID
const char* password = "Omotech@23"; // Replace with your Wi-Fi Password

// Wi-Fi server
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to Wi-Fi...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }

  Serial.println("Connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  
  server.begin(); // Start the server
}

void loop() {
  WiFiClient client = server.available(); // Check if a client has connected
  if (client) {
    Serial.println("New Client Connected!");
    while (client.connected()) {
      int gsrValue = analogRead(34); // Read GSR sensor
      String data = String(gsrValue);
      client.println(data); // Send data to the client
      delay(1000); // Adjust the frequency as needed
    }
    client.stop();
    Serial.println("Client Disconnected!");
  }
}
