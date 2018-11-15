# Import the otb applications package
import otbApplication

# The following line creates an instance of the ComputeImagesStatistics application
ComputeImagesStatistics = otbApplication.Registry.CreateApplication("ComputeImagesStatistics")

# The following lines set all the application parameters:
ComputeImagesStatistics.SetParameterStringList("il", ['PMS_reference.tif'])

ComputeImagesStatistics.SetParameterString("out", "EstimateImageStatistics_PMS.xml")

# The following line execute the application
ComputeImagesStatistics.ExecuteAndWriteOutput()
