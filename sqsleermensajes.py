import boto3

sqs = boto3.resource("sqs")
#RECUPERAMOS UNA COLA POR SU NOMBRE
#TIENE UN METODO PARA RECUPERAR LA COLA
#LLAMADO get_queue_by_name(NOMBRE)
#DEBEMOS INDICAR EL ATRIBUTO QueueName
queue = sqs.get_queue_by_name(QueueName="queue-estamos-en-jueves")
#DEBEMOS CREAR UN OBJETO QUE INDICARA UNA SERIE 
#DE ATRIBUTOS.  
#1) FILTRO DE MENSAJES
#2) MAXIMO NUMERO DE MENSAJES
#3) SEGUNDOS DE ESPERA PARA RECIBIR MENSAJES
mensajes = queue.receive_messages(
    MessageAttributeNames=["All"],
    MaxNumberOfMessages=10, 
    WaitTimeSeconds=15
)

#RECORREMOS TODOS LOS MENSAJES
for msj in mensajes:
    #DEBEMOS RECUPERAR EL CUERPO DEL MENSAJE
    #SI DESEAMOS VISUALIZARLO SIN CIFRAR
    print(msj.body)

print("Fin de programa")