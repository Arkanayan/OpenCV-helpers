## OpenCV Helpers

Collection of some commonly used functions written as individual scripts to run on batch of images.

### Don't forget to install the requirements
```pip install -r requirements.txt```
### sharpen.py

Sharpen the image/images in the input folder and write to the output folder. The amount of sharpness can be given via sigma.
#### Example
```python cropCircle.py -i image.jpg -dp 2.0 -md 3.0```

To get the details of the parameters, view the script.

### detectBlur.py
Detect the amount of blur in the image(s) and write the report to csv file. The threshold pass via command line determines if an image is blurred or not.

#### Example
```python detectBlur.py -imdir images -o output.csv -thresh 600 ```


### cropCircle.py
Detect circles in the given image. And crop them, then save the cropped images.

#### Example
```python sharpen.py -imdir input_folder -o ouput_folder -sigma 500```