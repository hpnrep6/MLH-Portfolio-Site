#!/bin/bash

echo "Creating random post and sending it to API"
echo " "
POSTANS=$(curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=Charlie&email=charlie@gmail.com&content=This post was made with my bash script')
echo ""
echo "Done! printing response..."
echo $POSTANS
echo ""
ID=$(echo $POSTANS | jq '.id')


echo "Fetching all data..."
GETANS=$(curl --request GET http://127.0.0.1:5000/api/timeline_post)
echo ""
echo "Done! printing response..."
echo $GETANS
echo ""

echo "Executing Cleanup and deleting test post..."
echo ""
DELETEANS=$(curl --request DELETE http://127.0.0.1:5000/api/timeline_post -d "id=$ID")
echo ""
echo "Done! printing..."
echo $DELETEANS

echo ""
echo "Fetching all data..."
GETANS=$(curl --request GET http://127.0.0.1:5000/api/timeline_post)
echo ""
echo "Done! printing response..."
echo $GETANS
echo ""