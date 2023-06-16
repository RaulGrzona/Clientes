from base_clients import Clients

client1 = Clients("Lucas", 2604845470, "Suipacha 236", 2)
client2 = Clients("Fernando", 214845470, "Peru 4236", 1)
client3 = Clients("Tomas", 261845470, "Av. San Martin 1236", 1)

print(" 1 : Clients Tax = Responsable")
print(" 2 : Client list ")
print(" 3 : Test option ")

input_number = input("Input Number: ")

if input_number == "1":
    client = [client1, client2, client3]
    for vclient in client:
        if vclient.tax == 1:
            print(f"{vclient.name}\t{vclient.phone}\t{vclient.tax}")
elif input_number == "2":
    client = [client1, client2, client3]
    for vclient in client:
        print(f"{vclient.name}\t{vclient.phone}\t{vclient.address}")

else:
    print("Invalid option")
