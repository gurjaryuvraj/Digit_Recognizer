import io
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model

def ml_model(img):
    model = load_model("../trained_model/number_identify1_1.keras")

    st.text(img.shape)
    # st.text("dimension {}".format(img.shape))
    

    prediction = model.predict(img.reshape(1,28*28))
    prediction_p = tf.nn.softmax(prediction)
    yhat = np.argmax(prediction_p)
    st.text(f" predicting : \n{prediction}")
    return yhat









def open_draw():

    st.title("Digit Recognizer")
    st.header("Draw a digit")

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color=None,  
        stroke_width=25,
        stroke_color="#FFFFFF",
        background_color="#000000",
        background_image= None,
        update_streamlit=True,
        height = 400,
        width = 400,
        drawing_mode="freedraw",
        point_display_radius= 0,
        key="canvas",
        display_toolbar = True,
    )
    



   

    if(st.button("Predict the Digit")):
        

        image_data = canvas_result.image_data.astype(np.uint8)

        # Resize the image to 28x28 pixels
        resized_image = cv2.resize(image_data, (28, 28), interpolation=cv2.INTER_AREA)

        # Display the resized image
        # st.write("28x28 Resized Output:")
        # st.image(resized_image, width=140, caption="Resized 28x28 Canvas")
        # st.text(resized_image.shape)





        # st.text(img)
        rgb_image = resized_image[:, :, :3]
        
        # Convert to grayscale using luminosity method
        photo = np.dot(rgb_image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        # st.text(photo.shape)
        


        # Load the model
        prediction = ml_model(photo)
        st.title("The Prediction is")
        st.title(prediction)





        
        # download csv of the digit
        with io.BytesIO() as buffer:
             
            np.savetxt(buffer, photo, delimiter=",")
            st.download_button(
                label = "Download csv of Digit",
                data = buffer,
                file_name = "photo.csv",
                mime = "text/csv"
            )        








if __name__ == '__main__':
    open_draw()


