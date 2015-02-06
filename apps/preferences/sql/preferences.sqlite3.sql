INSERT INTO Preferences 
VALUES  (1, 'PHONE', '000 000 000 00 00', 'Phone number', 'Contact phone number. It is visible on the top of site 
page.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), 
        (2, 'EMAIL', 'myemail@email.com', 'Email', 'Contact Email. It is visible on the top of site page as an image to 
protect from spambot.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), 
(3, 'SKYPE', 'myskype', 'Skype', 'Contact skype. It is visible on the top of site page.', CURRENT_TIMESTAMP, 
CURRENT_TIMESTAMP), 
(4, 'GOOGLE_ANALITYCS_CODE', '', 'Google Analytic code', 'Code uses to connect to Google Analytic service.', 
CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 'MAX_INNERLINK_HISTORY', '10', 'Max number of inner pages', 'Number of pages that can be shown under main menu when 
user follow links inside page. Generally inner pages used only as a link inside content.', CURRENT_TIMESTAMP, 
CURRENT_TIMESTAMP),
(6, 'REST_API', 'True', 'Turn on/off REST Api', 'Turn on/off alternative way of getting pages using REST api. Only a 
special marked pages can be available for api. For more information please look into page statuses list.', 
CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
