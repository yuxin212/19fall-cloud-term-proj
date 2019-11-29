# gcloud auth login '@gmail.com' --quiet --no-launch-browser
gcloud auth activate-service-account '' --key-file './MyProject.json'
# gcloud init --console-only --account '@gmail.com' --quiet
# gcloud compute config-ssh --quiet
echo "Launching an instance..."
python ./Part2/launch.py 'cloud-infrs-proj' 'cloud-infrs-bucket'
gcloud compute config-ssh --quiet
echo "Listing instances..."
python ./Part2/list.py 'cloud-infrs-proj'
echo "Executing benchmark..."
chmod +x ./Part2/exec.sh
./Part2/exec.sh
echo "Deleting created instance..."
python ./Part2/delete.py 'cloud-infrs-proj' 
