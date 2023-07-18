### CloneSHAPInterpreter


This GitHub repo contains the source code, data, and results from our research study on explaining the predictions of the CodeBERT model for semantic code clone detection.

Data files include 115 clone pair samples of Java and 120 clone pair samples of Python which we filter from the SemanticCloneBench dataset of semantic clones. The human labels for clone pairs and statements are also uploaded as data.

Results include spreadsheets and files containing results of correlation analysis, statement types analysis.

Code includes the code for SHAP interpretation. We have also uploaded the code that performs the human-machine interpretation correlation analysis and statement types analysis. Some helper code to aid the analysis is also uploaded.

The Java folder contains all data, code, and results for the Java clone pairs. For further instructions on how to replicate please refer to README inside the Java/Code/SHAP Interpreter folder.
The Python f[model.py](..%2F..%2FcodeBERT%2FcodeBERTReview%2FShap%2Fmodel.py)older contains all data, code, and results for the Python clone pairs. For further instructions on how to replicate please refer to README inside the Python folder.
