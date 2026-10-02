#			AI Moblie storege
name=input("Enter your Name:")
budget=int(input("Seclect your Budget:\n1:10k - 20k \n2:20k - 50k \n3:50k - 100k \n4:100k onwards \n"))
if budget==1:
    ram=int(input("select any one \n1:2/32gb \n2:4/64gb \n"))
    cam=int(input("select any one \n1:8-10 MP \n2:10-15 MP \n"))
    bat=int(input("select any one \n1:2500-300 MAH \n2:3000-3500 MAH \n"))
    if ram==1 and cam==1 and bat==1:
        print("=================================================================================")    
        print("Best Recommendation for you! \n ITEL - with below specs \nRAM=2GB \nStorage =32GB \n10MP camera with 2800 MAH Battery  \nTotal price is Rs:15000/-")
    elif ram==2 and cam==2 and bat==2:
        print("=================================================================================")
        print("Best Recommendation for you! \n Techno - with below specs \nRAM=4GB \nStorage =64GB \15MP camera with 3500 MAH Battery  \nTotal price is Rs:20000/-")
elif budget==2:
    ram = int(input("Select any one \n1: 4/64GB \n2: 6/128GB\n"))
    cam = int(input("Select any one \n1: 13-20 MP \n2: 20-50 MP\n"))
    bat = int(input("Select any one \n1: 4000-4500 MAH \n2: 4500-5000 MAH\n"))
    if ram == 1 and cam == 1 and bat == 1:
        print("=================================================================================")
        print("Best Recommendation for you!\n SAMSUNG - with below specs \n RAM = 4GB \nStorage = 64GB \n 20MP Camera with 4500 MAH Battery \n Total Price is Rs: 30000/-")
    elif ram == 2 and cam == 2 and bat == 2:
        print("=================================================================================")
        print("Best Recommendation for you! \n REDMI - with below specs \n RAM = 6GB \n Storage = 128GB \n 50MP Camera with 5000 MAH Battery \n Total Price is Rs: 45000/-")
elif budget == 3:
    ram = int(input("Select any one \n1: 8/128GB \n2: 8/256GB\n"))
    cam = int(input("Select any one \n1: 50MP \n2: 108MP\n"))
    bat = int(input("Select any one \n1: 4500-5000 MAH \n2: 5000-5500 MAH\n"))
    if ram == 1 and cam == 1 and bat == 1:
        print("=================================================================================")
        print("Best Recommendation for you! \n SAMSUNG - with below specs \nRAM = 8GB \nStorage = 128GB \n50MP Camera with 5000 MAH Battery \nTotal Price is Rs: 60000/-")
    elif ram == 2 and cam == 2 and bat == 2:
        print("=================================================================================")
        print("Best Recommendation for you! \n ONEPLUS - with below specs \nRAM = 8GB \nStorage = 256GB \n108MP Camera with 5500 MAH Battery \nTotal Price is Rs: 90000/-")
elif budget == 4:
    ram = int(input("Select any one \n1: 8/256GB \n2: 12/512GB\n"))
    cam = int(input("Select any one \n1: 50MP \n2: 200MP\n"))
    bat = int(input("Select any one \n1: 5000 MAH \n2: 5500 MAH\n"))
    if ram == 1 and cam == 1 and bat == 1:
        print("=================================================================================")
        print("Best Recommendation for you!")
        print("SAMSUNG - with below specs \nRAM = 8GB \nStorage = 256GB \n50MP Camera with 5000 MAH Battery \nTotal Price is Rs: 120000/-")
    elif ram == 2 and cam == 2 and bat == 2:
        print("=================================================================================")
        print("Best Recommendation for you! \n IPHONE - with below specs \nStorage = 512GB \n200MP Camera with 5500 MAH Battery \nTotal Price is Rs: 180000/-")
else:
    print("Invalid Budget Selection")             