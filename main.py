from flask import Flask, request, render_template
from backend_operation.process_CSV_File import processData
from backend_operation.apiCalls import createPersonalization
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def upload_file():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # Get the uploaded file from the request
        uploaded_file = request.files['file']
        
        information = await processData(uploaded_file)

        createPersonalization(information)
        
        return information
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
