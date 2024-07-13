rand=$(openssl rand -base64 12)
response=$(curl -X POST -s http://localhost:5000/api/timeline_post -d "name=${rand}&email=wei.he@mlh.io&content=${rand}")
result=$(curl "http://localhost:5000/api/timeline_post" > jq -s -e "contains(${response})$")
status=$?
if [ $status -eq "0" ]; then
	echo "Test passed."
	exit 0
else
	echo "Test failed"
	exit 1
fi
