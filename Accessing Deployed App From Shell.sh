curl -X 'POST' \
'http://ec2-16-171-47-137.eu-north-1.compute.amazonaws.com:8080/predict'
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "gender": "Male",
  "age": 60,
  "hypertension": true,
  "heart": true,
  "work": "Private Job",
  "glucose": 250,
  "bmi": 60
}'
