import paho.mqtt.client as mqtt
import json


URL_HTTP = 'https://micro-service.nvjhsv3tvm96u.us-east-1.cs.amazonlightsail.com'

HEADER = {
    'Authorization': 'Token fe3faddabc883462a30caf316d35ce046c532e9a'
}


def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker: " + str(rc))
    client.subscribe("smartGreenHouse")


def ascii(message):
    return bytes.fromhex(message).decode('ascii')


# def message_filter(key, position, message, content, userdata):
#     if key in ascii(message['data']):
#         teste = ascii(message['data']).split(';')
#         for data in teste:
#             value = data.split(':')
#             value[1] = value[1].replace("\x00", "")
#             content[f'{value[0]}'] = float(value[1])
#             print(data)
#         print('-----------------------------------')
#         print(position)
#         print(userdata)
#         userdata[position] = content


def on_message(client, userdata, msg):
    print(msg.payload.decode())
    #     if msg.topic == "Contentor":
    # message = json.loads(msg.payload)
    # content = {}
    # message_filter('lat', 'first', message, content, userdata)
    # message_filter('tmp', 'second', message, content, userdata)
    # if 'first' in userdata and 'second' in userdata:
    #     send_to_ip(userdata['first'], userdata['second'],
    #                message['devaddr'], message['datetime'])
    #     del userdata['first']
    #     del userdata['second']


# def send_to_ip(first, second, devaddr, datetime):
#     print(first, second, devaddr, datetime)
#     data = {
#         'device_serial': devaddr,
#         'girospio_eixo_x': round(second['Ex'], 2),
#         'girospio_eixo_y': round(second['Ey'], 2),
#         'temperatura': second['tmp'],
#         'distancia': second['V'],
#         'latitude': first['lat'],
#         'longitude': first['lon'],
#     }

#     try:
#         contentor = Contentor.objects.get(serial=devaddr)
#         try:
#             medida = Medida.objects.create(
#                 contentor=contentor,
#                 girospio_eixo_x=data['girospio_eixo_x'],
#                 girospio_eixo_y=data['girospio_eixo_y'],
#                 temperatura=data['temperatura'],
#                 distancia=data['distancia'],
#                 latitude=data['latitude'],
#                 longitude=data['longitude'],
#             )
#             print('Medida criada com sucesso')
#             print(medida)
#         except Exception as error:
#             print(f'Erro ao criar medida: {error}')
#     except Contentor.DoesNotExist:
#         print('Contentor não existe')
