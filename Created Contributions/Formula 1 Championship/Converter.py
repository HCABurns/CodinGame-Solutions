# NOTE: Requires manual removal of sprint results.
while 1:
    driver = " ".join(input().strip().split(" ")[1:])
    driver = driver.replace("	"," ")
    driver = driver.replace("P","")
    driver = driver.replace("Ret","DNF")
    driver = driver.replace("DNS","DNF")
    driver = driver.replace("DSQ","DNF")
    driver = driver.replace("DNQ","DNF")
    driver = driver.replace("†","")
    print(" ".join(driver.split(" ")[:2]) + ":" + " ".join(driver.split(" ")[2:-1]).lstrip())
