from flask import Flask, request, render_template
from graph import generate_plot, image_to_base64
app = Flask(__name__)

@app.route('/add_data', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        file = request.files['file']  
        x = int(request.form['x']) 
        y = int(request.form['y'])  
        image_path = './uploads/' + file.filename
        file.save(image_path)  
        image = image_to_base64(image_path)  
        radii = radii.append(x)
        percentages = percentages.append(y)
        images = images.append(image)
        script, div = generate_plot(radii, percentages, images)
        return render_template('./templates/search_data.html', script=script, div=div)
    else:
        # 当用户首次访问页面时
        radii = [3, 3,5]
        percentages = [39.4, 28, 38.8]
        images = [
            
            './templates/image4.png',
            'DFLT  WEB code/templates/image5.png',
            'DFLT  WEB code/templates/image6.png'
        ]
        encoded_images = [image_to_base64(image_path) for image_path in images]
        script, div = generate_plot( percentages,radii, encoded_images)
        return render_template('./templates/add_data.html', script=script, div=div)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
