# Detect-And-Analyze-Faces---Machine-Learning

I used the Azure Face service to explore the detect and analyze capabilities by using a Jupyter notebook in Azure Machine Learning Studio to send images into the Face service, then I deployed it in my pc. 

First, I retrieved and set the key and endpoint values from my Azure Cognitive Services account, then I create a Face Client. 


Detect-faces.py

![image](https://user-images.githubusercontent.com/86535567/128427063-0348fa13-79ee-4323-b0e5-d8723561b402.png)

Then, with the custom python code "faces.py" I use the results to implement the Azure face service. 

First I just want to detect the faces, so show_id and show_attributes are set false. 

![Figure_1](https://user-images.githubusercontent.com/86535567/128427887-e6744263-8fa2-4c38-bcef-14c6d59383ca.png)


Each detected face is assigned a unique ID, allowing the application to identify each individual face that was detected, to showcase the Id, the show_id attribute is set True. 

![Figure_1](https://user-images.githubusercontent.com/86535567/128428210-ce9360e1-b512-4624-9c35-adaca7639c93.png)

To showcase the attributes such as gender, age and emotion, show_attributes is set True. 

![Figure_1](https://user-images.githubusercontent.com/86535567/128428735-d11824ed-3b62-486e-9b77-6bb71037c1f3.png)


When faces are detected using the Face service, each one is assigned a unique Face Id. Face Ids are used to individually identify face detections. I used these IDs to compare a detected face to previously detected faces and find faces with similar features.


![image](https://user-images.githubusercontent.com/86535567/128429035-54a0a0f5-e7bf-43fe-b915-ae2cd6960a90.png)


Results:

![Figure_1](https://user-images.githubusercontent.com/86535567/128429165-517f177d-f8ae-41c5-8c53-7336435df065.png)


Same code with different faces:


![Figure_1](https://user-images.githubusercontent.com/86535567/128429297-00f478bd-e3e7-4ae6-ae5f-548b980f7423.png)
