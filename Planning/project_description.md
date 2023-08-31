# This webapp is part of a cluster of modules that are used to improve the data acquistion, quality and analysis of the AirTec company.

This Webapp is produced within the research project of Jonas Lülsdorf

## Project Description

The project is part of the research project of Jonas Lülsdorf. The project is about the digitization of the data acquisition process of the AirTec company.

### Problem Description

The company AirTec creates customized revisory mask for individual patients of all ages.
To create a customized revisory mask the company needs to create a 3D scan of the patient, which is already done through a well working process. However, since other factors like the velocity of the skin, the weight of the patient, etc. can not be measured with the 3D scan, the company needs to acquire this data.
Currently the data acquisition process is semi manual, where employees fill out pdf files on tablets to document personal and sensitive information like age, weight, height, etc. of the customer.
To improve the data acquisition process, the company wants to digitize the data acquisition process.
This will allow the company to improve the data quality, since the data is directly stored in a database and can be used for further analysis.
Since the data is sensitive, the data acquisition process has to be secure and the data has to be encrypted.

### Research Question
How to digitalize the data acquisition process of small sized company, responsible for handling sensitive patient data, protected through german and european data protection laws, through a webapp? 
-> Augenmerk auf datenaquisition, datenqualität, datenanalyse (Welche Features eignen sich gut zum Machine Learning)
S
## Use Cases


### Use Case 1: Transform written files in cloud files
-> Eher nice to have (wenn es die Zeit zulässt, wenn von Firma gewünscht)
#### Description
Within earlier stages of the companies data acquisition the files were written on paper. To improve the data quality and to make the data more accessible, the company wants to transform the written files into cloud files.
Therefore the webapp should be able to transform the written files into cloud files, or at least allow the user to enter the data through a form within the webapp and archive a picture of the original file.

### Use Case 2: Transform digital files in cloud files
-> 
#### Description
The user should be able to import the pdf file within the webapp, which then prefills a form with the data. The user then can edit the data and save it to the database.

### Use Case 3: Create cloud files

#### Description
To allow the user to create new files within the webapp, they should be able to access a form which allows them to enter the data manually.

### Use Case 4: Edit cloud files

#### Description
Sometimes patients loose a lot of weight within a certain time period or other other factors change.
To allow to adjust those changes the user should be able to edit files within the webapp, they should be able to access a form which allows them to edit the data manually.


### Use Case 5: Cloud file deletion

#### Description
Since the DSGVO requires a company to delete all data of a patient, if the patient requests it, the company needs to be able to delete the data of a patient.

### Use Case 6: Cloud file export

#### Description
To allow the company to export the data of a patient, the company needs to be able to export the data of a patient. The export transform the file in a pdf file, which can be send to the patient.

## Other Requirements

### Data Security

Since certain Norms have to be fulfilled, when working with patient data, the webapp has to encrypt the data before sending it to a secure database.

Furthermore the webapp should only be accessible through a logged in user.


## Open Question

How is the data stored in the database?
How is the software deployed?
How is the budget for the hosting of the webapp per year?

Wann wird ein User angelegt?
(Sobald der Außendienstmitarbeiter einen Termin hat)

Sollen Identifikationsdaten und Metadaten getrennt gespeichert werden? (Über zwei Datenbank)

Wie sieht das Form aus? 
(Falls es ein Freifeld gibt) Gibt es die Möglichkeit, daraus das Form zu erweitern? Im Sinne der Wissenserhaltung.
(Z.b. 30% der Formulare haben im Freifeld das Wort Asthma stehen-> Das Wort Asthma sollte im Form aufgenommen werden)