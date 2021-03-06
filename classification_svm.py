# Import the otb applications package
import otbApplication

# The following line creates an instance of the ImageClassifier application
ImageClassifier = otbApplication.Registry.CreateApplication("ImageClassifier")

# The following lines set all the application parameters:
ImageClassifier.SetParameterString("in", "./data/PMS_reference.tif")

ImageClassifier.SetParameterString("imstat", "EstimateImageStatistics_PMS.xml")

ImageClassifier.SetParameterString("model", "clsvmModelQB1.svm")

ImageClassifier.SetParameterString("out", "./data/clLabeledImage_SVM.tif")

# The following line execute the application
ImageClassifier.ExecuteAndWriteOutput()