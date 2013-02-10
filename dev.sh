ping -o foot

if [ $? -eq 0 ] ; then
  echo 'Direct connection'
  ssh foot 'tail -f ~/mixer-pre/db/dev.db' | python extract.py > data
else
  echo 'Connecting via Shell'
  ssh -t mnelimar@shell.hiit.fi ssh foot 'tail -f ~/mixer-pre/db/dev.db' | python extract.py > data
fi
