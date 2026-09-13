# Analysis and QA Guide

## Decision
Marketing and sales leaders need to decide where to allocate acquisition budget and which funnel or response-time issues deserve immediate intervention. The unit of analysis is one unique lead.

## Run
```bash
pip install -r requirements.txt
python src/analyze_leads.py --leads sample-data/website_leads.csv --spend sample-data/channel_spend.csv --output solution
python -m unittest tests/test_analysis.py -v
```

## Validation
Ten independent controls reconcile source rows, unique identifiers, stage order, revenue attribution, every main segmentation rollup, funnel monotonicity, and rate boundaries. Review `solution/validation_results.csv`; every result must be PASS. The follow-up queue is deliberately non-exclusive and should not be added to funnel totals.

## Limitations
This synthetic portfolio case demonstrates the workflow without exposing client data. It uses lead-source attribution rather than multi-touch attribution, revenue rather than profit, and observed association—not causal lift. Budget changes should be tested incrementally.
