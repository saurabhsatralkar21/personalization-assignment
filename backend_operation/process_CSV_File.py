

async def processData(uploaded_file):

    # Read the CSV file and store the information in an array
    data = []
    information = []
    n = 0
    if uploaded_file:

        # Assuming the CSV file has a single column
        for line in uploaded_file.readlines():
            data.append(line.decode().strip())
    
    keys = data[0].split(',')

    print(len(keys))
    print(len(data))

    for row in data[1:]:
        item = row.split(',')

    

        information.append({
            f"{keys[0]}": item[0],
            f"{keys[1]}": item[1],
            f"{keys[2]}": item[2],
            f"{keys[3]}": item[3],
        })



        # item = item.split(',')
        # for i in range(0, len(item)):
        #     information.append({
        #         keys[n]: item[i]
        #     })
        #     n = n + 1
    

    # Print the data on the console
    # for item in data:
    #     information.append(item.split(",")) 
    
    return information