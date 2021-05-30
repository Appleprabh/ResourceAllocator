
# This class allocates the resource
class ResourceAllocator:
    def __init__(self):
        self.instance_price = {}
        self.instance_cpus = {
            "large": 1,
            "xlarge": 2,
            "2xlarge": 4,
            "4xlarge": 8,
            "8xlarge": 16,
            "10xlarge": 32,
            }
        self.total_cost = 0
        self.server = []
        self.output = []
        self.instances = {}

    #This function is used to find the low cost server type
    def lowestPriceCalculator(self, instPrice):
        for i in list(instPrice.keys()):
            instPrice[i] = instPrice[i]/self.instance_cpus[i]
        instPricelist = sorted(instPrice.items(), key=lambda x: x[1])
        self.instance_price = dict(instPricelist)

    #This function is used to calculate the price for input cpus
    def calculateServerPrice(self, cpus, location, hours):
        for i in list(self.instance_price.keys()):
            cpuNeed = cpus // self.instance_cpus[i]
            if(cpuNeed != 0):
                if(i in self.instances[location]):
                    cpus -= cpuNeed * self.instance_cpus[i]
                    self.total_cost += ((self.instances[location]
                                         [i]) * hours) * cpuNeed
                    self.server.append((i, cpuNeed))
        self.outputFormatter(location)

    #This is setter for class
    def setters(self):
        self.instance_price = {}
        self.total_cost = 0
        self.server = []
    #This function helps to get the output to format
    def outputFormatter(self, location):
        op = {
            "region": location,
            "total_cost": float("%.2f" % self.total_cost),
            "server": self.server
        }
        self.output.append(op)

    #This function is used to calculate the number servers it can provide for given price
    def calculatePriceServer(self, price, hours, location):
        self.total_cost = 0
        for i in list(self.instance_price.keys()):
            cpuNeed = int(price // (self.instances[location][i] * hours))
            # print(self.instances[location][i] *hours, hours)
            if(cpuNeed != 0):
                self.total_cost += cpuNeed * \
                    (self.instances[location][i] * hours)
                self.server.append((i, cpuNeed))
                price -= cpuNeed * (self.instances[location][i] * hours)
        self.outputFormatter(location)

    #This function is used to calculate both cpus and price within the limit
    def server_price_hours(self, price, hours, cpus, location):
        self.total_cost = 0
        temp = 0
        tempCpu = cpus
        for i in list(self.instance_price.keys()):
            cpuNeed = tempCpu // self.instance_cpus[i]
            if(cpuNeed != 0):
                temp += cpuNeed * (self.instances[location][i] * hours)
                if(temp <= price):
                    self.server.append((i, cpuNeed))
                    tempCpu -= cpuNeed * self.instance_cpus[i]
                else:
                    temp -= cpuNeed * (self.instances[location][i] * hours)
        self.total_cost = temp
        if(len(self.server) == 0 or tempCpu != 0):
            return
        else:
            self.outputFormatter(location)


    #This helps to format the output with dollar sign
    def finalFormatter(self):
        for i in self.output:
            i["total_cost"] = "$"+str(i["total_cost"])

    #This function helps to sort the total cost
    def sorter(self):
        size = len(self.output)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if(self.output[min_index]["total_cost"] > self.output[j]["total_cost"]):
                    min_index = j
            self.output[i], self.output[min_index] = self.output[min_index], self.output[i]
        self.finalFormatter()

    #This function helps to redirect as per needs
    def get_costs(self,instances=None, hours=None, cpus=None, price=None):
        self.instances = instances.copy()
        self.output = []
        # print("here")
        if(cpus is not None and hours is not None and price is None):
            for i in list(instances.keys()):
                self.setters()
                self.lowestPriceCalculator(instances[i].copy())
                self.calculateServerPrice(cpus, i, hours)
        elif(price is not None and hours is not None and cpus is None):
            for i in list(instances.keys()):
                self.setters()
                self.lowestPriceCalculator(instances[i].copy())
                self.calculatePriceServer(price, hours, i)
        elif(cpus is not None and hours is not None and price is not None):
            for i in list(instances.keys()):
                self.setters()
                self.lowestPriceCalculator(instances[i].copy())
                # print(self.instance_price)
                self.server_price_hours(price, hours, cpus, i)
        self.sorter()
        return self.output



