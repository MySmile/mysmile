
INSERT INTO Page (slug, color, photo, sortorder, status, ptype, created_at, updated_at) 
          VALUES ('index', '#fda132', 'images/photo.png', 10, 'published', 'menu page', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Page_translation (page_id, lang, menu, name, col_central, youtube, col_right, col_bottom_1, col_bottom_2, col_bottom_3, meta_title, meta_description, meta_keywords, photo_alt, photo_description, created_at, updated_at) 
                      VALUES (1, 'en', 'Home', 'Home page', 'Welcome to MySmile!', '', 'Lorem ipsum', 'Lorem ipsum', 'Lorem ipsum', 'Lorem ipsum', 'Home', 'description', 'keywords', 'alt photo', 'photo description', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_PHONE', '000 000 000 00 00', 'Phone number', 'Contact phone number. It is visible on the top of site page.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_EMAIL', 'myemail@email.com', 'Email', 'Contact Email. It is visible on the top of site page as an image to protect from spam bot.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_SKYPE', 'myskype', 'Skype', 'Contact skype. It is visible on the top of site page.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_GOOGLE_ANALITYCS_CODE', '', 'Google Analytic code', 'Code uses to connect to Google Analytic service.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_MAX_INNERLINK_HISTORY', '4', 'Max number of inner pages', 'Number of pages that can be shown under main menu when user follow links inside page. Generally inner pages used only as a link inside content.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO Settings (key, value, name, description, created_at, updated_at) VALUES ('KEY_REST_API', 'True', 'Turn on/off REST Api', 'Turn on/off alternative way of getting pages using REST api. Only a special marked pages can be available for api. For more information please look into page statuses list.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

