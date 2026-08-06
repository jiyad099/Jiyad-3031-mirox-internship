from transformers import pipeline

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

def classify_image(image):

    try:

        result = classifier(image)

        prediction = result[0]

        label = prediction["label"]

        confidence = prediction["score"] * 100

        return f"{label}, confidence: {confidence:.2f}%"

    except Exception:

        return "Model timeout - try again."
