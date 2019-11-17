# be careful which shebang statement to set to make sure source is found...
# this script is used to boot a Docker container
source /opt/envs/olse/bin/activate
# sleep 20
# flask run
exec gunicorn -b :19033 --access-logfile - --error-logfile - fromflask:app &
