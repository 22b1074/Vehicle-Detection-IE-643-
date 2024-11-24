SelfVision_IE643.ipynb is haing major part of data processing and training yolov5 model on normal weather dataset.

Foggy_Data_Collection_IE643_Final.ipynb have foggy dataset collection and experiment of foggy weather fine-tuning(here i collected dataset to g-drive foggy_IE643, whose link is https://drive.google.com/drive/folders/1aJcsVnMLVjDJpJ88hMqqDShbzlmcz12F?usp=sharing 
and from this i removed few images to get few-shot dataset for foggy weather target domain whose code is in Rainy_Foggy_FEWSHOT.ipynb and the final foggy few-shot dataset of train and val is in g-drive https://drive.google.com/drive/folders/165N-V-lw5HNbUrm9rC8T6ud8bgv06GD1?usp=sharing 

Rainy_Foggy_FEWSHOT.ipynb have code for rainy few-shot dataset preparation and also how i got final foggy few shot dataset from my starting foggy dataset

FEWSHOT_FINETUNING.ipynb have the experiment of fine-tuning for few-shot setup . I fine-tuned the trained yolov5m model by freezing earlier few layers(i tried 7,10,15,17,20) on combined few-shot weather datasets of foggy and rainy(Rainy, foggy_fewshot_IE643)

Following drive link https://drive.google.com/drive/folders/1A7b-ezDsDHRELrFOECYtqzdprmnVY2uW?usp=sharing, has results of combined_finetuning using few_shot approach (for which file is of how many freezing layers check file name to which they are saved in the code file i.e FEWSHOT_FINETUNING.ipynb)

Following drive link https://drive.google.com/drive/folders/18LfDBKv1bwvnfU3ULAfKrKZzjkfJbkfw?usp=sharing has results of training (100 epochs in total) yolov5m model using NormalWeather_IE643 dataset which is in the link https://drive.google.com/drive/folders/1KrHhutEgjWwE9I6V2zqCY-OgcL91Auw_?usp=sharing.

Following drive link has results of seperate fine-tuning using(180 images in rainy and foggy weather) where i performed sequential fine-tuning by shifting b/w rainy and foggy every 30-40 epochs 
  i)https://drive.google.com/drive/folders/1e3ufnN0qF2T3An5jg3A0Qr4SdhGtKWcs?usp=sharing (foggy finetuning link)
  ii)https://drive.google.com/drive/folders/13ICRc_tCAIZfIpBf3BfheImIzF6Nn8Ar?usp=sharing(rainy finetuning link)
  iii)https://colab.research.google.com/drive/1ciKesSppxcQMjCkWqk-_YKLilmLmlMLZ?usp=sharing (g-colab notebook link , sequential finetuning code)
  iv)https://colab.research.google.com/drive/1A5rKDKYcY6X249iNdjRAVm1aIFvyenB_?usp=sharing(first 30 epocs of foggy finetuning)

Following drive link has combined fintuning(180 images) of rainy and foggy weather datsets https://colab.research.google.com/drive/1WLPZjI191nBM2-FjS2BMTpPd1_omLrng?usp=sharing

Following drive links has few-shot datsets:-
  i)https://drive.google.com/drive/folders/165N-V-lw5HNbUrm9rC8T6ud8bgv06GD1?usp=sharing (foggy_fewshot_IE643 link)
  ii)https://drive.google.com/drive/folders/1ApGbcB5fzjijbN1sQPcVKEJaUEBUiwYM?usp=sharing (rainy fewshot link)

Following g-colab links have the training of normal weather dataset(100 epochs):
  i)https://colab.research.google.com/drive/1sD_q6eq4wLPl-TRAzvF-pF69r1wTeO7I?usp=sharing(40-47 epochs)
  ii)https://colab.research.google.com/drive/1ivxTbHkS0LDl3tsPhaDH5npAagL11meX?usp=sharing (19-35 epochs)
  iii)https://colab.research.google.com/drive/1A5rKDKYcY6X249iNdjRAVm1aIFvyenB_?usp=sharing (35-40 epochs, 90-100 epochs)
  iv)https://colab.research.google.com/drive/1WLPZjI191nBM2-FjS2BMTpPd1_omLrng?usp=sharing (60-75 epochs)
  v)https://colab.research.google.com/drive/1Y3DZMC8vJtjMgh6jO_wOCxiB_VVVGqXc?usp=sharing (47-60 epochs , 75-90 epochs)
  vi)https://colab.research.google.com/drive/1gdA8RSENH_6mPDz7d0I3IirDe15AUN4h?usp=sharing (1-19 epochs)
