:
BASE=/home/john/Gilt/GiltAlchemy
PYTHONPATH="${BASE}:$PYTHONPATH"
echo $PYTHONPATH
export PYTHONPATH
cd ${BASE}/test
python run_tests.py
