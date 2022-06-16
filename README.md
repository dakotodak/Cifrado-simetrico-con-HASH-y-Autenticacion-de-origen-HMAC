Cifrado simétrico con HASH y Autenticación de origen HMAC.

Este código simula el funcionamiento del cifrado simétrico en mensajes que son enviados a traves de la redes de telecomunicaciones.
Los algoritmos de cifrado utilizados en este código son SHA256 y SHA512. Ademas, se realiza un código de autenticación de origen HMAC permitiendo una mayor integridad en los datos. 

El objetivo de este código es demostrar la efectividad de esta autenticación de origen cuando la información se ve modificada por un intruso. Esto se hace realizando una comparación del hash del mensaje recibido y el mensaje original.
