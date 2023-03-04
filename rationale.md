# Rationale.md

The purpose of this file is to explain the validation of the container output files. The following tools have been used:

* **Python test:** These tests are used to verify the number of output files and also the final report file generated at the end of the execution.
  * These files search in the project structure for the "static" and "templates" folders, which is where the keyword images, the histograms containing the number of images per file and the final analysis report file are generated.
  * Additionally, they check the size of these files.
* **Manual test:** By manually viewing the PDF file, you can check that the output files are correct.
