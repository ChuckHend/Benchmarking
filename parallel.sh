nJobs=30
files='dir/*'

for f in $files; do
  while [ $(jobs | wc -l) -ge $nJobs ]; do
    echo 'waiting on job > > >'
    echo "Number Jobs Running: $(jobs | wc -l)"
    sleep 2
  done
    python py_proc.py $f &
done
