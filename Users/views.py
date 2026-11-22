import shutil
from django.shortcuts import render
from sklearn.model_selection import train_test_split

from AI_Powered_Plant_Disease_Detection.settings import MEDIA_ROOT, MEDIA_URL





from .models import userRegisteredTable
from django.core.exceptions import ValidationError
from django.contrib import messages


def userRegisterCheck(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("loginId")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        

        # Create an instance of the model
        user = userRegisteredTable(
            name=name,
            email=email,
            loginid=username,
            mobile=mobile,
            password=password,
            
        )

        try:
            # Validate using model field validators
            user.full_clean()
            
            # Save to DB
            user.save()
            messages.success(request,'registration Successfully done,please wait for admin APPROVAL')
            return render(request, "userRegisterForm.html")


        except ValidationError as ve:
            # Get a list of error messages to display
            error_messages = []
            for field, errors in ve.message_dict.items():
                for error in errors:
                    error_messages.append(f"{field.capitalize()}: {error}")
            return render(request, "userRegisterForm.html", {"messages": error_messages})

        except Exception as e:
            # Handle other exceptions (like unique constraint fails)
            return render(request, "userRegisterForm.html", {"messages": [str(e)]})

    return render(request, "userRegisterForm.html")


def userLoginCheck(request):
    if request.method=='POST':
        username=request.POST['userUsername']
        password=request.POST['userPassword']

        try:
            user=userRegisteredTable.objects.get(loginid=username,password=password)

            if user.status=='Active':
                request.session['id']=user.id
                request.session['name']=user.name
                request.session['email']=user.email
                
                return render(request,'users/userHome.html')
            else:
                messages.error(request,'Status not activated please wait for admin approval')
                return render(request,'userLoginForm.html')
        except:
            messages.error(request,'Invalid details please enter details carefully or Please Register')
            return render(request,'userLoginForm.html')
    return render(request,'userLoginForm.html')


def userHome(request):
    if not request.session.get('id'):
        return render(request,'userLoginForm.html')
    return render(request,'users/userHome.html')
def Ulog(request):
    request.session.flush()  # clears all session data
    return render(request,'userLoginForm.html')
# import os
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input
# from tensorflow.keras.applications import MobileNet
# from sklearn.metrics import classification_report, confusion_matrix
# import json
import pandas as pd
# import io
# import sys
# import warnings

# warnings.filterwarnings('ignore')

def training(request):
    
    if not request.session.get('id'):
        return render(request,'userLoginForm.html')
    # train = r"/content/new_plant_diseases_dataset/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train"
    # test= r"/content/new_plant_diseases_dataset/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/valid"
    # img_height, img_width = 128, 128
    # batch_size = 32
    # epochs = 15
    # model_save_path = "mudra_mobilenet_model.h5"
    # metrics_csv_path = "media/training_metrics.csv"

    # # Image generators
    # train_datagen = ImageDataGenerator(
    #     rescale=1./255,
    #     validation_split=0.2,
    #     rotation_range=20,
    #     zoom_range=0.2,
    #     horizontal_flip=True
    # )

    # train_generator = train_datagen.flow_from_directory(
    #     train,
    #     target_size=(img_height, img_width),
    #     batch_size=batch_size,
    #     class_mode='categorical',
    #     subset='training',
    #     shuffle=True
    # )

    # val_generator = train_datagen.flow_from_directory(
    #     test,
    #     target_size=(img_height, img_width),
    #     batch_size=batch_size,
    #     class_mode='categorical',
    #     subset='validation',
    #     shuffle=False
    # )

    # # Save class labels
    # class_labels = train_generator.class_indices
    # with open("class_labels.json", "w") as f:
    #     json.dump(class_labels, f)

    # # Model building
    # base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))
    # base_model.trainable = False

    # inputs = Input(shape=(img_height, img_width, 3))
    # x = base_model(inputs, training=False)
    # x = GlobalAveragePooling2D()(x)
    # x = Dense(128, activation='relu')(x)
    # x = Dropout(0.5)(x)
    # outputs = Dense(train_generator.num_classes, activation='softmax')(x)
    # model = Model(inputs, outputs)

    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # # Train model
    # history = model.fit(
    #     train_generator,
    #     epochs=epochs,
    #     validation_data=val_generator
    # )

    # # Save model
    # model.save(model_save_path)

    # # Evaluate
    # val_loss, val_accuracy = model.evaluate(val_generator)

    # # Predict
    # y_pred = model.predict(val_generator)
    # y_pred_classes = np.argmax(y_pred, axis=1)
    # y_true = val_generator.classes

    # # Classification report and confusion matrix
    # class_report = classification_report(y_true, y_pred_classes, target_names=val_generator.class_indices.keys(), output_dict=True)
    # cmatrix = confusion_matrix(y_true, y_pred_classes)

    # # Prepare metrics for CSV
    # metrics_data = {
    #     'Epoch': list(range(1, epochs + 1)),
    #     'Train_Accuracy': history.history['accuracy'],
    #     'Train_Loss': history.history['loss'],
    #     'Validation_Accuracy': history.history['val_accuracy'],
    #     'Validation_Loss': history.history['val_loss']
    # }

    # # Convert classification report to a flat dictionary for CSV
    # class_report_flat = {}
    # for label, metrics in class_report.items():
    #     if isinstance(metrics, dict):  # For each class
    #         for metric, value in metrics.items():
    #             class_report_flat[f"{label}_{metric}"] = value
    #     else:  # For overall metrics like accuracy
    #         class_report_flat[label] = metrics

    # # Add final validation metrics to class_report_flat
    # class_report_flat['Final_Validation_Accuracy'] = val_accuracy
    # class_report_flat['Final_Validation_Loss'] = val_loss

    # # Create DataFrame for metrics
    # metrics_df = pd.DataFrame(metrics_data)
    
    # # Add classification report metrics to DataFrame (as a single row)
    # class_report_df = pd.DataFrame([class_report_flat])
    
    # # Save confusion matrix to a separate CSV
    # cm_df = pd.DataFrame(cmatrix, index=val_generator.class_indices.keys(), columns=val_generator.class_indices.keys())
    # cm_df.to_csv("confusion_matrix.csv")

    # # Combine metrics and classification report
    # # Since metrics_df has multiple rows (per epoch) and class_report_df has one row, we'll save them separately
    # metrics_df.to_csv(metrics_csv_path, index=False)
    # class_report_df.to_csv("classification_report.csv", index=False)

    # context = {
    #     'train_accuracy': history.history['accuracy'][-1],
    #     'train_loss': history.history['loss'][-1],
    #     'val_accuracy': val_accuracy,
    #     'val_loss': val_loss,
    #     'classification_report': classification_report(y_true, y_pred_classes, target_names=val_generator.class_indices.keys()),
    #     'confusion_matrix': cmatrix.tolist()  # To safely render in template
    # }

    results1=pd.read_csv(r'media\training_metrics.csv')
    dff=results1.to_html()
    # Pass DataFrame to template (convert to dict for easier rendering)
    return render(request, 'users/training.html', {
         
        'results_df':dff  # Convert DataFrame to list of dictionaries
    })

from django.shortcuts import render
from django.core.files.uploadedfile import UploadedFile
from django.http import JsonResponse
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import json
import os
from django.conf import settings
import uuid
from google import genai

def prediction(request):
    if not request.session.get('id'):
        return render(request,'userLoginForm.html')
    if request.method == 'POST' and 'image' in request.FILES:
        model_path = os.path.join(settings.MEDIA_ROOT, "mudra_mobilenet_model.h5")
        class_labels_path = os.path.join(settings.MEDIA_ROOT, "class_labels.json")
        img_height, img_width = 128, 128

        # Load the saved model
        model = tf.keras.models.load_model(model_path)

        # Load class labels
        with open(class_labels_path, "r") as f:
            class_labels = json.load(f)
        # Reverse the class_labels dictionary to map indices to class names
        index_to_label = {v: k for k, v in class_labels.items()}

        # Get the uploaded image
        image_file = request.FILES['image']

        # Save the uploaded image temporarily
        unique_filename = f"uploads/{uuid.uuid4().hex}_{image_file.name}"
        image_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # Load and preprocess the image for prediction
        img = load_img(image_path, target_size=(img_height, img_width))
        img_array = img_to_array(img)
        img_array = img_array / 255.0  # Rescale to match training
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        predictions = model.predict(img_array)
        predicted_class_idx = np.argmax(predictions[0])
        predicted_class = index_to_label[predicted_class_idx]
        confidence = float(predictions[0][predicted_class_idx])

        # Generate the image URL for the template
        image_url = os.path.join(settings.MEDIA_URL, unique_filename)

        context = {
            'predicted_class': predicted_class,
            'confidence': confidence,
            'image_url': image_url,
            'error': None
        }
    else:
        context = {
            'predicted_class': None,
            'confidence': None,
            'image_url': None,
            'error': 'No image uploaded or invalid request method.'
        }

    return render(request, 'users/prediction.html', context)
    
def chatbot(request):
    if request.method == 'POST':
        try:
            import json
            from google import genai

            data = json.loads(request.body or "{}")
            user_message = data.get('message')
            predicted_class = data.get('predicted_class')

            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            client = genai.Client(api_key=settings.GEMINI_API_KEY)

            prompt = f"""You are an expert in plant pathology assisting users with plant disease queries. The user has uploaded an image predicted to have the plant disease: {predicted_class}. Answer the user's question: "{user_message}" Provide a concise, accurate response related to the disease, its symptoms, treatment, or prevention. Keep the tone friendly and professional."""

            models = ["gemini-2.5-flash", "gemini-flash-latest"]

            response = None
            for m in models:
                try:
                    response = client.models.generate_content(
                        model=m,
                        contents=prompt
                    )
                    if response and response.text:
                        break
                except Exception as e:
                    print(f"{m} failed:", e)

            if not response or not response.text:
                return JsonResponse({'error': 'AI service busy. Try again.'}, status=500)

            return JsonResponse({'response': response.text})

        except Exception as e:
            import traceback
            print("FULL ERROR:\n", traceback.format_exc())
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)