const int NUM_SAMPLES = 10;

void setup() {
  // Setup code, only runs once.
  Serial.begin(9600);
}

void loop() {
  // Loop code, runs repeatedly.
  long total = 0;
  for (int i = 0; i < NUM_SAMPLES; i++) {
    total += analogRead(A0);
    delay(2);
  }

  int sensorValue = total / NUM_SAMPLES;
  float voltage = sensorValue * (5.0 / 1023.0);

  float pressurePSI = 1946.10512 * voltage + 17.3707;
  float pressureBAR = pressurePSI / 14.5037738;

  Serial.print("Pressure_PSI:");
  Serial.print(pressurePSI);
  Serial.print(",");
  Serial.print("Pressure_BAR:");
  Serial.println(pressureBAR);

  delay(1000);
}