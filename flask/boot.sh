gunicorn -b 0.0.0.0:6060 --access-logfile - --error-logfile - run:app

#!/bin/sh
#source venv/bin/activate
#
#while true; do
#    flask deploy
#    if [[ "$?" == "0" ]]; then
#        break
#    fi
#    echo Deploy command failed, retrying in 5 secs...
#    sleep 5
#done
#
#exec gunicorn -b :5000 --access-logfile - --error-logfile - flasky:app

