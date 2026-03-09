from xmlrpc.server import SimpleXMLRPCServer

# fungsiyang akan di ekspos ke klien

def add_numbers(a, b):
    return a + b

def substract_numbers(a, b):
    return a - b

# membuat xmlrpc server pada alamat tertentu
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# mengekspos fungsi ke server
server.register_function(add_numbers, "add_numbers")
server.register_function(substract_numbers, "substract_numbers")

# mengeksekusi server
server.serve_forever()