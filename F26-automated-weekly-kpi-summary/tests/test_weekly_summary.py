import csv, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_generator():
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([sys.executable,str(ROOT/'src/generate_weekly_summary.py'),'--input',str(ROOT/'sample-data/daily_channel_performance.csv'),'--week-ending','2026-08-02','--output-dir',d],check=True)
        rows=list(csv.DictReader(open(Path(d)/'weekly_kpis.csv')))
        assert len(rows)==7 and {r['status'] for r in rows}<={'On Track','Watch','Action'}
        assert (Path(d)/'management_summary.html').stat().st_size>1000
