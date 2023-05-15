DeepMAT: Predicting Metabolic Pathways of Compounds using a Message Passing and Attention-Based Neural Networks
We collected data from the KEGG database on 12 different types of metabolic pathways, each containing several individual pathways.
 In total, we obtained 180 metabolic pathways and identified 2856 compounds associated with these pathways. Each compound was assigned
 to one or more pathways, with those belonging to a single pathway referred to as dataset samples.

However, some compounds belonged to multiple metabolic pathways, creating a multi-label classification problem. 
To address this, we used a binary classification approach based on similarity, as previously done in a related study.
 We paired each compound with its respective metabolic pathways and generated samples for binary classification.
 For example, compound "C02320" belonged to metabolic pathways "map00480 and map00983", so we paired it with each pathway
 separately to create two samples for binary classification.

To construct the binary classification problem, we created positive and negative samples. Positive samples were compounds
 that were associated with a particular metabolic pathway, and negative samples were compounds that were not associated with
 that pathway. We identified  4300 positive samples but did not find any negative samples in the KEGG database. Therefore, we
 randomly generated negative samples by pairing compounds with pathways they did not belong to. For instance, we paired the
 compound "acetyl phosphate" with the pyruvate metabolic pathway and labelled it as a positive sample. However, the same compound
 did not belong to the Propanoate pathway, so we paired it with that pathway and labelled it as a negative sample. We randomly
 generated 4300 negative samples in this manner for analysis.