from interface_pb2_grpc import HeySteimkeServerServicer, add_HeySteimkeServerServicer_to_server
from interface_pb2 import ItemResponse, Item
import grpc
from concurrent import futures

class HeySteimkeServer(HeySteimkeServerServicer):
    def __init__(self):
        pass
    def GetTodos(self, request, context):
        print(request)
        items = []
        for i in range(2):
            items.append(Item(i,f"Item no {i}"))
        return ItemResponse(items)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_HeySteimkeServerServicer_to_server(HeySteimkeServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()