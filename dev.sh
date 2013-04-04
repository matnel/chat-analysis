ping -c 1 foot 2> /dev/null 1> /dev/null

if [ $? -eq 0 ] ; then
  echo 'direct'
  ssh mnelimar@foot 'tail -f ~/mixer-pre/db/dev.db' | python extract.py
else
  echo 'via Shell'
  ssh -t mnelimar@shell.hiit.fi ssh foot 'tail -f ~/open/db/dev.db' | python extract.py
fi
