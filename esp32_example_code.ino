void setup() {

  Serial.begin(9600);
}

void loop() {
  // Verificar se há dados disponíveis na porta serial
  if (Serial.available() > 0) {
    // Ler o comando recebido
    String comando = Serial.readStringUntil('\n');

    // Verificar se o comando recebido é para enviar dados
    if (comando == "GET_DATA") {
      // Simular a leitura de dados dos sensores
      float temperatura = 25.5;
      float umidade = 60.0;

      // Enviar os dados dos sensores pela porta serial
      Serial.print("Temperatura: ");
      Serial.print(temperatura);
      Serial.print(" Umidade: ");
      Serial.println(umidade);
    }
  }
}
