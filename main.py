from solution import ResourceAllocator

instancePrice = {
        "us-east": {
        "large": 0.12,
        "xlarge": 0.23,
        "2xlarge": 0.45,
        "4xlarge": 0.774,
        "8xlarge": 1.4,
        "10xlarge": 2.82
        },

        "us-west": {
        "large": 0.14,
        "2xlarge": 0.413,
        "4xlarge": 0.89,
        "8xlarge": 1.3,
        "10xlarge": 2.97
        },
}

a = ResourceAllocator()
b = a.get_costs(instances=instancePrice, cpus=135, hours=24)
c = a.get_costs(instances=instancePrice, price=38, hours=10)
d = a.get_costs(instances=instancePrice, cpus=180, price= 65, hours=6)
print(b)
print("\n",c)
print("\n",d)
