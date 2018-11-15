#!/usr/bin/python

# Import the otb applications package
import otbApplication

# The following line creates an instance of the ExtractROI application
ExtractROI = otbApplication.Registry.CreateApplication("ExtractROI")
url = "/home/nguyen/dumasl//Pleiades_Primary_Product_Pan-sharpened/FCGC600031034/IMG_PHR1A_PMS-N_001/IMG_PHR1A_PMS-N_201202250025599_SEN_PRG_FC_5844-001_R1C1.JP2"
# The following lines set all the application parameters:
ExtractROI.SetParameterString("in", url)

ExtractROI.SetParameterString("mode","extent")
ExtractROI.SetParameterString("mode.extent.unit","pxl")

ExtractROI.SetParameterFloat("mode.extent.ulx", 150)

ExtractROI.SetParameterFloat("mode.extent.uly", 150)

ExtractROI.SetParameterFloat("mode.extent.lrx", 649)

ExtractROI.SetParameterFloat("mode.extent.lry", 649)

ExtractROI.SetParameterString("out", "./data/PMS_reference.tif")

# The following line execute the application
ExtractROI.ExecuteAndWriteOutput()
