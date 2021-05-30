# Resource Allocator

This package allows you to allocate instance based on user needs like
1. Alice would like to request for servers with minimum 135 CPUs for 24 hours.
2. Bob would like to request as many possible servers for $38 for 10 hours.
3. Charlie would like to request for minimum 180 CPUs and wouldn't want to pay for more than $65 for 6 hours.

## Usage

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
    
    obj = ResourceAllocator()
    obj.get_costs(instances=instancePrice, cpu=135, hours=24)
    obj.get_costs(instances=instancePrice, price=38, hours=10)
    obj.get_costs(instances=instancePrice,cpu=185, price=65, hours=6)
    
