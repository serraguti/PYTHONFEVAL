import boto3

sqs = boto3.resource("sqs")
#PARA ENVIAR MENSAJES, DEBEMOS INDICAR SOBRE QUE
#QUEUE DESEAMOS HACERLO
#RECUPERAMOS UNA COLA POR SU NOMBRE
cola = sqs.get_queue_by_name(QueueName="queue-estamos-en-jueves")
#PEDIMOS AL USUARIO EL CONTENIDO DEL MENSAJE
print("Introduzca mensaje para SQS")
texto = input()
#TENEMOS UN METODO DENTRO DE QUEUE/COLA LLAMADO
#send_message() DONDE ENVIAMOS EL MENSAJE QUE DESEEMOS
#MEDIANTE EL ATTRIBUTO MessageBody
#PODEMOS CAPTURAR LA RESPUESTA DEL ENVIO Y VISUALIZAR EL ID DEL MENSAJE
response = cola.send_message(MessageBody=texto)
print("Mensaje enviado")
print(response)

print("Fin de programa")

