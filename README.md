# Smile-detector

With the advent of libraries like openCV and its consistent algorithms like Haar-Cascade, object detection no more requires training of hefty Neural Networks on bottomless datasets. This project serves as a basic example of the use of the Haar cascade algorithm by detecting whether a person is smiling or not. The project works on two different types of inputs which are a live feed from the users webcam or an image. Both can be fed to a function used to detect smile, which will also return relevant outputs on the console window.

Haar Cascade is an openCV algorithm which is used to detect an array of objects, smiles and eyes to mention a few alongside faces. In our code, we will be using it for face detection followed by smile detection over the region of interest comprising of our face. Haar cascade is the only external file other than the libraries of numpy and openCV our code would need. 

<h2><b> File setup </b></h2>

Instructions for setting up the Haar Cascade files:
1. Download the archived folder containing the Haar cascade files. It will be named as "haar-cascade-files-master.zip" in the resources folder.
2. In a terminal, type "pip install opencv-python" to donwload the opencv library. 
3. Navigate your way to where you have installed Python. Once in the folder, find the folder named "Lib", within Lib find "site-packages" which should contain a "cv2" folder. This is where you need to download and extract the Haar Cascade files. Follow: Python folder -> Lib -> site-packages -> cv2
4. Once the xml files are successfully extracted and placed in the shown directory, open the folder and move to the folder which shows all the xml files. This is the path you can copy to load your model in your python code

Note: The "cv2" folder in site-packages referred to in the second point will only be found if you have successfully installed openCV. 
