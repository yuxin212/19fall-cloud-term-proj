gcloud compute ssh --project 'cloud-infrs-proj' --zone 'us-central1-a' 'instance-1' --command 'wget https://raw.githubusercontent.com/yuxin212/19fall-cloud-term-proj/master/Part2/benchmark.sh' --quiet

gcloud compute ssh --project 'cloud-infrs-proj' --zone 'us-central1-a' 'instance-1' --command 'chmod +x ./benchmark.sh' --quiet

echo "Pause for 30 sec"

gcloud compute ssh --project 'cloud-infrs-proj' --zone 'us-central1-a' 'instance-1' --command 'sleep 30' --quiet

gcloud compute ssh --project 'cloud-infrs-proj' --zone 'us-central1-a' 'instance-1' --command './benchmark.sh' --quiet
