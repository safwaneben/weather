heroku auth:login
cd apicaller
sudo heroku container:login
heroku create apicallersaf
sudo heroku container:push web -a apicallersaf
heroku container:release web -a apicallersaf
heroku open -a apicallersaf
cd ../dataparser
sudo heroku container:login
heroku create dataparsersaf
sudo heroku container:push web -a dataparsersaf
heroku container:release web -a dataparsersaf
heroku open -a dataparsersaf
cd ../predictionservice
sudo heroku container:login
heroku create predictionsaf
sudo heroku container:push web -a predictionsaf
heroku container:release web -a predictionsaf
heroku open -a predictionsaf
cd ../visualizerservice
sudo heroku container:login
heroku create visualizersaf
sudo heroku container:push web -a visualizersaf
heroku container:release web -a visualizersaf
heroku open -a visualizersaf