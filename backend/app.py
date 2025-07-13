import os
from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
import torch
from torch.autograd import Variable
from torchvision.utils import save_image
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Your custom imports
from model import TransformerNet  # assuming you have this file
from utils import test_transform, denormalize  # assuming your preprocessing is here

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
CHECKPOINT_FOLDER = 'checkpoints'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def test_image(image_path, checkpoint_model, output_path):
    transform = test_transform()
    transformer = TransformerNet().to(device)
    transformer.load_state_dict(torch.load(checkpoint_model, map_location=device))
    transformer.eval()

    image_tensor = Variable(transform(Image.open(image_path).convert("RGB"))).to(device)
    image_tensor = image_tensor.unsqueeze(0)

    with torch.no_grad():
        stylized_image = denormalize(transformer(image_tensor)).cpu()

    save_image(stylized_image, output_path)
    return output_path


@app.route('/style-transfer', methods=['POST'])
def style_transfer():
    if 'image' not in request.files or 'style' not in request.form:
        return jsonify({"error": "Missing image or style parameter"}), 400

    image = request.files['image']
    print(image)
    style = "Picasso_Selfportrait_5000"

    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    checkpoint_path = "./models/2nd_style_last_checkpoint.pth"
    if not os.path.exists(checkpoint_path):
        return jsonify({"error": "Checkpoint model not found"}), 404

    output_filename = f"{os.path.splitext(filename)[0]}_{style}.jpg"
    output_path = os.path.join(RESULT_FOLDER, output_filename)

    test_image(image_path, checkpoint_path, output_path)

    return send_file(output_path, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
